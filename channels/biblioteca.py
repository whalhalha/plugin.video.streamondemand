# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# streamondemand - XBMC Plugin
# Ricerca "Biblioteca"
# http://www.mimediacenter.info/foro/viewforum.php?f=36
# ------------------------------------------------------------
import re

from core import logger
from core import config
from core import scrapertools
from core.item import Item

__channel__ = "biblioteca"
__category__ = "F"
__type__ = "generic"
__title__ = "biblioteca"
__language__ = "IT"

host = "http://www.ibs.it"

DEBUG = config.get_setting("debug")


def isGeneric():
    return True


def mainlist(item):
    logger.info("streamondemand.biblioteca mainlist")
    itemlist = []
    itemlist.append(
        Item(channel=__channel__,
             title="[COLOR azure]Indice Registi [A-Z][/COLOR]",
             action="cat_lettera_registi",
             url="http://www.ibs.it/dvd/lista+registi.html",
             thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append(
        Item(channel=__channel__,
             title="[COLOR azure]Indice Attori/Attrici [A-Z][/COLOR]",
             action="cat_lettera_attori",
             url="http://www.ibs.it/dvd-film/lista-attori.html",
             thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    # itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Attori/Attrici[/COLOR]", action="cat_attori", url="http://altadefinizione.co/attori/", thumbnail="http://repository-butchabay.googlecode.com/svn/branches/eden/skin.cirrus.extended.v2/extras/moviegenres/All%20Movies%20by%20Actor.png"))
    # itemlist.append(
    #     Item(channel=__channel__,
    #          title="[COLOR azure]Elenco Film [A-Z][/COLOR]",
    #          action="categorias",
    #          url="http://www.darkstream.tv/",
    #          thumbnail="http://repository-butchabay.googlecode.com/svn/branches/eden/skin.cirrus.extended.v2/extras/moviegenres/Movies%20A-Z.png"))
    # itemlist.append( Item(channel=__channel__, title="[COLOR yellow]Cerca...[/COLOR]", action="search", thumbnail="http://dc467.4shared.com/img/fEbJqOum/s7/13feaf0c8c0/Search"))

    return itemlist


def cat_lettera_registi(item):
    logger.info("streamondemand.biblioteca cat_registi")
    itemlist = []

    matches = [("A", "/dvd/ser/serreg.asp?q=A"),
               ('B', '/dvd/ser/serreg.asp?q=B'),
               ('C', '/dvd/ser/serreg.asp?q=C'),
               ('D', '/dvd/ser/serreg.asp?q=D'),
               ('E', '/dvd/ser/serreg.asp?q=E'),
               ('F', '/dvd/ser/serreg.asp?q=F'),
               ('G', '/dvd/ser/serreg.asp?q=G'),
               ('H', '/dvd/ser/serreg.asp?q=H'),
               ('I', '/dvd/ser/serreg.asp?q=I'),
               ('J', '/dvd/ser/serreg.asp?q=J'),
               ('K', '/dvd/ser/serreg.asp?q=K'),
               ('L', '/dvd/ser/serreg.asp?q=L'),
               ('M', '/dvd/ser/serreg.asp?q=M'),
               ('N', '/dvd/ser/serreg.asp?q=N'),
               ('O', '/dvd/ser/serreg.asp?q=O'),
               ('P', '/dvd/ser/serreg.asp?q=P'),
               ('Q', '/dvd/ser/serreg.asp?q=Q'),
               ('R', '/dvd/ser/serreg.asp?q=R'),
               ('S', '/dvd/ser/serreg.asp?q=S'),
               ('T', '/dvd/ser/serreg.asp?q=T'),
               ('U', '/dvd/ser/serreg.asp?q=U'),
               ('V', '/dvd/ser/serreg.asp?q=V'),
               ('W', '/dvd/ser/serreg.asp?q=W'),
               ('X', '/dvd/ser/serreg.asp?q=X'),
               ('Y', '/dvd/ser/serreg.asp?q=Y'),
               ('Z', '/dvd/ser/serreg.asp?q=Z')]

    for scrapedtitle, scrapedurl in matches:
        url = host + scrapedurl
        itemlist.append(Item(channel=__channel__, action="cat_ruolo", title=scrapedtitle, url=url, folder=True))

    return itemlist


def cat_lettera_attori(item):
    logger.info("streamondemand.biblioteca cat_attori")
    itemlist = []

    matches = [('A', '/dvd/ser/seratt.asp?q=A'),
               ('B', '/dvd/ser/seratt.asp?q=B'),
               ('C', '/dvd/ser/seratt.asp?q=C'),
               ('D', '/dvd/ser/seratt.asp?q=D'),
               ('E', '/dvd/ser/seratt.asp?q=E'),
               ('F', '/dvd/ser/seratt.asp?q=F'),
               ('G', '/dvd/ser/seratt.asp?q=G'),
               ('H', '/dvd/ser/seratt.asp?q=H'),
               ('I', '/dvd/ser/seratt.asp?q=I'),
               ('J', '/dvd/ser/seratt.asp?q=J'),
               ('K', '/dvd/ser/seratt.asp?q=K'),
               ('L', '/dvd/ser/seratt.asp?q=L'),
               ('M', '/dvd/ser/seratt.asp?q=M'),
               ('N', '/dvd/ser/seratt.asp?q=N'),
               ('O', '/dvd/ser/seratt.asp?q=O'),
               ('P', '/dvd/ser/seratt.asp?q=P'),
               ('Q', '/dvd/ser/seratt.asp?q=Q'),
               ('R', '/dvd/ser/seratt.asp?q=R'),
               ('S', '/dvd/ser/seratt.asp?q=S'),
               ('T', '/dvd/ser/seratt.asp?q=T'),
               ('U', '/dvd/ser/seratt.asp?q=U'),
               ('V', '/dvd/ser/seratt.asp?q=V'),
               ('W', '/dvd/ser/seratt.asp?q=W'),
               ('X', '/dvd/ser/seratt.asp?q=X'),
               ('Y', '/dvd/ser/seratt.asp?q=Y'),
               ('Z', '/dvd/ser/seratt.asp?q=Z')]

    for scrapedtitle, scrapedurl in matches:
        url = host + scrapedurl
        itemlist.append(Item(channel=__channel__, action="cat_ruolo", title=scrapedtitle, url=url, folder=True))

    return itemlist


def cat_ruolo(item):
    logger.info("streamondemand.biblioteca cat_registi")
    itemlist = []

    data = scrapertools.cache_page(item.url)
    logger.info(data)

    # Narrow search by selecting only the combo
    patron = r'<td bgColor=#ffffff width="33%"><table width="100%"><tr><td bgcolor="eeeee4">(.*?)</font></td></tr></table></td>'
    bloques = re.compile(patron, re.DOTALL).findall(data)

    patron = r'<a\s*(?:rel="nofollow")?\s*href="([^"]+)">([^<]+)</a>'
    for bloque in bloques:
        # Extrae las entradas (carpetas)
        matches = re.compile(patron, re.DOTALL).findall(bloque)

        for scrapedurl, scrapedtitle in matches:
            url = host + scrapedurl
            itemlist.append(
                Item(channel=__channel__, action="cat_filmografia", title=scrapedtitle, url=url, folder=True))

    return itemlist


def cat_filmografia(item):
    logger.info("streamondemand.biblioteca cat_registi")
    itemlist = []

    data = scrapertools.cache_page(item.url)
    logger.info(data)

    # Extrae las entradas (carpetas)
    patron = r'<td width="90" valign="middle" height="120"><a href="[^"]+"><img alt="([^"]+)" border="0" src="([^"]+)"></a></td>'
    matches = re.compile(patron, re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle, scrapedthumbnail in matches:
        titolo = scrapedtitle.replace(" ", "+")
        itemlist.append(
            Item(channel=__channel__, action="do_search", extra=titolo, title=scrapedtitle, thumbnail=scrapedthumbnail,
                 folder=True))

    return itemlist


def do_search(item):
    logger.info("streamondemand.channels.biblioteca do_search")

    tecleado = item.extra
    mostra = tecleado.replace("+", " ")

    itemlist = []

    import os
    import glob
    import imp
    from lib.fuzzywuzzy import fuzz

    master_exclude_data_file = os.path.join(config.get_runtime_path(), "resources", "biblioteca.txt")
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
        progreso.create("Ricerca di " + mostra)
    except:
        show_dialog = False

    channel_files = glob.glob(channels_path)
    number_of_channels = len(channel_files)

    for index, infile in enumerate(channel_files):
        percentage = index * 100 / number_of_channels

        basename = os.path.basename(infile)
        basename_without_extension = basename[:-3]

        if basename_without_extension not in excluir:

            if show_dialog:
                progreso.update(percentage, ' Sto cercando "' + mostra + '"')

            logger.info("streamondemand.channels.buscador Tentativo di ricerca su " + basename_without_extension + " per " + mostra)
            try:

                # http://docs.python.org/library/imp.html?highlight=imp#module-imp
                obj = imp.load_source(basename_without_extension, infile)
                logger.info("streamondemand.channels.buscador cargado " + basename_without_extension + " de " + infile)
                channel_result_itemlist = obj.search(Item(), tecleado)
                for new_item in channel_result_itemlist:
                    new_item.title = scrapertools.decodeHtmlentities(new_item.title)
                    new_item.title = new_item.title + " [COLOR orange]su[/COLOR] [COLOR green]" + basename_without_extension + "[/COLOR]"
                    new_item.viewmode = "list"

                itemlist.extend(channel_result_itemlist)
            except:
                import traceback
                logger.error(traceback.format_exc())

        else:
            logger.info(
                "streamondemand.channels.buscador do_search_results, Escluso il server " + basename_without_extension)

    new_itemlist = []
    for new_item in itemlist:
        ratio = fuzz.WRatio(item.title, new_item.fulltitle)
        # print str(ratio) + "\t" + new_item.fulltitle + "\t" + new_item.title
        if ratio > 85:
            new_itemlist.append(new_item)

    itemlist = sorted(new_itemlist, key=lambda Item: Item.title)

    if show_dialog:
        progreso.close()

    return itemlist

