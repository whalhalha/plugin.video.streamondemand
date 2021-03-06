# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# streamondemand.- XBMC Plugin
# http://blog.tvalacarta.info/plugin-xbmc/streamondemand.
# ------------------------------------------------------------
import os

from core import config
from core import logger
from core.item import Item

__channel__ = "buscador"

logger.info("streamondemand.channels.buscador init")

DEBUG = True


def isGeneric():
    return True


def mainlist(item, preferred_thumbnail="squares"):
    logger.info("streamondemand.channels.buscador mainlist")

    itemlist = [
        Item(channel=__channel__,
             action="search",
             title="[COLOR yellow]Nuova ricerca film...[/COLOR]"),
        Item(channel=__channel__,
             action="search",
             category="serie",
             title="[COLOR yellow]Nuova ricerca serie tv...[/COLOR]"),
    ]

    saved_searches_list = get_saved_searches(item.channel)

    for saved_search_text in saved_searches_list:
        itemlist.append(
            Item(channel=__channel__,
                 action="do_search",
                 title=' "' + saved_search_text + '"',
                 extra=saved_search_text))

    if len(saved_searches_list) > 0:
        itemlist.append(
            Item(channel=__channel__,
                 action="clear_saved_searches",
                 title="[COLOR red]Elimina cronologia ricerche[/COLOR]"))

    return itemlist


# Al llamar a esta función, el sistema pedirá primero el texto a buscar
# y lo pasará en el parámetro "tecleado"
def search(item, tecleado):
    logger.info("streamondemand.channels.buscador search")

    if tecleado != "":
        save_search(item.channel, tecleado)

    item.extra = tecleado
    return do_search(item)


# Esta es la función que realmente realiza la búsqueda
def do_search(item):
    logger.info("streamondemand.channels.buscador do_search")

    tecleado = item.extra
    mostra = tecleado.replace("+", " ")

    itemlist = []

    import os
    import glob
    import imp
    from lib.fuzzywuzzy import fuzz
    import threading
    import Queue

    master_exclude_data_file = os.path.join(config.get_runtime_path(), "resources", "global_search_exclusion.txt")
    logger.info("streamondemand.channels.buscador master_exclude_data_file=" + master_exclude_data_file)

    channels_path = os.path.join(config.get_runtime_path(), "channels", '*.py')
    logger.info("streamondemand.channels.buscador channels_path=" + channels_path)

    excluir = ""

    if os.path.exists(master_exclude_data_file):
        logger.info("streamondemand.channels.buscador Encontrado fichero exclusiones")

        fileexclude = open(master_exclude_data_file, "r")
        excluir = fileexclude.read()
        fileexclude.close()
    else:
        logger.info("streamondemand.channels.buscador No encontrado fichero exclusiones")
        excluir = "seriesly\nbuscador\ntengourl\n__init__"

    if config.is_xbmc():
        show_dialog = True

    try:
        import xbmcgui
        progreso = xbmcgui.DialogProgressBG()
        progreso.create("Ricerca di " + mostra.title())
    except:
        show_dialog = False

    def worker(infile, queue):
        channel_result_itemlist = []
        try:
            basename_without_extension = os.path.basename(infile)[:-3]
            # http://docs.python.org/library/imp.html?highlight=imp#module-imp
            obj = imp.load_source(basename_without_extension, infile)
            logger.info("streamondemand.channels.buscador cargado " + basename_without_extension + " de " + infile)
            channel_result_itemlist.extend(obj.search(Item(extra=item.category), tecleado))
            for local_item in channel_result_itemlist:
                local_item.title = " [COLOR azure] " + local_item.title + " [/COLOR] [COLOR orange]su[/COLOR] [COLOR green]" + basename_without_extension + "[/COLOR]"
                local_item.viewmode = "list"
        except:
            import traceback
            logger.error(traceback.format_exc())
        queue.put(channel_result_itemlist)

    channel_files = [infile for infile in glob.glob(channels_path) if os.path.basename(infile)[:-3] not in excluir]

    result = Queue.Queue()
    threads = [threading.Thread(target=worker, args=(infile, result)) for infile in channel_files]

    for t in threads:
        t.start()

    number_of_channels = len(channel_files)

    for index, t in enumerate(threads):
        percentage = index * 100 / number_of_channels
        if show_dialog:
            progreso.update(percentage, ' Sto cercando "' + mostra + '"')
        t.join()
        itemlist.extend(result.get())

    itemlist = sorted([item for item in itemlist if fuzz.WRatio(mostra, item.fulltitle) > 85],
                      key=lambda Item: Item.title)

    if show_dialog:
        progreso.close()

    return itemlist


def save_search(channel, text):
    saved_searches_limit = (10, 20, 30, 40,)[int(config.get_setting("saved_searches_limit"))]

    if os.path.exists(os.path.join(config.get_data_path(), "saved_searches.txt")):
        f = open(os.path.join(config.get_data_path(), "saved_searches.txt"), "r")
        saved_searches_list = f.readlines()
        f.close()
    else:
        saved_searches_list = []

    saved_searches_list.append(text)

    if len(saved_searches_list) >= saved_searches_limit:
        # Corta la lista por el principio, eliminando los más recientes
        saved_searches_list = saved_searches_list[-saved_searches_limit:]

    f = open(os.path.join(config.get_data_path(), "saved_searches.txt"), "w")
    for saved_search in saved_searches_list:
        f.write(saved_search + "\n")
    f.close()


def clear_saved_searches(item):
    f = open(os.path.join(config.get_data_path(), "saved_searches.txt"), "w")
    f.write("")
    f.close()


def get_saved_searches(channel):
    if os.path.exists(os.path.join(config.get_data_path(), "saved_searches.txt")):
        f = open(os.path.join(config.get_data_path(), "saved_searches.txt"), "r")
        saved_searches_list = f.readlines()
        f.close()
    else:
        saved_searches_list = []

    # Invierte la lista, para que el último buscado salga el primero
    saved_searches_list.reverse()

    trimmed = []
    for saved_search_text in saved_searches_list:
        trimmed.append(saved_search_text.strip())

    return trimmed
