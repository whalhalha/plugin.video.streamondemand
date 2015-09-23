# -*- coding: utf-8 -*-
#------------------------------------------------------------
# streamondemand - XBMC Plugin
# Ricerca "Biblioteca"
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
#------------------------------------------------------------
import urlparse,urllib2,urllib,re
import os, sys

from core import logger
from core import config
from core import scrapertools
from core.item import Item
from servers import servertools

__channel__ = "biblioteca"
__category__ = "F"
__type__ = "generic"
__title__ = "Biblioteca"
__language__ = "IT"

host = "http://www.darkstream.tv"

DEBUG = config.get_setting("debug")

def isGeneric():
    return True

def mainlist(item):
    logger.info("streamondemand.darkstream mainlist")
    itemlist = []
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Registi[/COLOR]", action="cat_registi", url="http://www.darkstream.tv/elenco-registi/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Attori[/COLOR]", action="cat_attori", url="http://www.darkstream.tv/elenco-attori/", thumbnail="http://repository-butchabay.googlecode.com/svn/branches/eden/skin.cirrus.extended.v2/extras/moviegenres/All%20Movies%20by%20Actor.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Attrici[/COLOR]", action="cat_attrici", url="http://www.darkstream.tv/elenco-attrici/", thumbnail="http://i.imgur.com/oRIjIiE.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Elenco Film [A-Z][/COLOR]", action="categorias", url="http://www.darkstream.tv/", thumbnail="http://repository-butchabay.googlecode.com/svn/branches/eden/skin.cirrus.extended.v2/extras/moviegenres/Movies%20A-Z.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR yellow]Cerca...[/COLOR]", action="search", thumbnail="http://dc467.4shared.com/img/fEbJqOum/s7/13feaf0c8c0/Search"))

    
    return itemlist

def cat_registi(item):
    logger.info("streamondemand.darkstream cat_registi")
    itemlist = []

    # Descarga la pagina
    data = scrapertools.cache_page(item.url)
    
    # Extrae las entradas (carpetas)
    patron  = '<a href=".*?">(.*?)</a>[^<]+<em>[^>]+>[^<]+<'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )
        
    return itemlist

def cat_attori(item):
    logger.info("streamondemand.darkstream cat_attori")
    itemlist = []

    # Descarga la pagina
    data = scrapertools.cache_page(item.url)
    
    # Extrae las entradas (carpetas)
    patron  = '<a href=".*?">(.*?)</a>.*?<span'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_attrici(item):
    logger.info("streamondemand.darkstream cat_attrici")
    itemlist = []

    # Descarga la pagina
    data = scrapertools.cache_page(item.url)
    
    # Extrae las entradas (carpetas)
    patron  = '<a href=".*?">(.*?)</a>.*?<span'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def categorias(item):
    logger.info("streamondemand.darkstream categorias")
    itemlist = []

    # Descarga la pagina
    data = scrapertools.cache_page(item.url)
    
    # Extrae las entradas (carpetas)
    patron  = '<li class="menu-item-3[^>]+><a[^=]+=[^=]+="(.*?)">(.*?)</a>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedurl,scrapedtitle in matches:
        scrapedplot = ""
        scrapedthumbnail = ""
        scrapedtitle=scrapertools.decodeHtmlentities(scrapedtitle.replace("Home",""))
        scrapedtitle=scrapertools.decodeHtmlentities(scrapedtitle.replace("http://www.darkstream.tv/",""))
        if (DEBUG): logger.info("title=["+scrapedtitle+"], url=["+scrapedurl+"]")
        itemlist.append( Item(channel=__channel__, action="cat_elenco", title="[COLOR azure]"+scrapedtitle+"[/COLOR]" , url=scrapedurl , thumbnail="http://xbmc-repo-ackbarr.googlecode.com/svn/trunk/dev/skin.cirrus%20extended%20v2/extras/moviegenres/All%20Movies%20by%20Genre.png", folder=True) )

    return itemlist

def cat_elenco(item):
    logger.info("streamondemand.darkstream cat_elenco")
    itemlist = []

    # Descarga la pagina
    data = scrapertools.cache_page(item.url)
    
    # Extrae las entradas (carpetas)
    patron  = '<a href="(.*?)">(.*?)</a>[^<]+<span style='
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedurl,scrapedtitle in matches:
        #response = urllib2.urlopen(scrapedurl)
        #html = response.read()
        #start = html.find("<span style=\"color: #5f5f5f;\">")
        #end = html.find("</p>", start)
        #scrapedplot = html[start:end]
        #scrapedplot = re.sub(r'<[^>]*>', '', scrapedplot)
        #scrapedplot = scrapertools.decodeHtmlentities(scrapedplot)
        scrapedplot = ""
        scrapedthumbnail = ""
        scrapedtitle = scrapertools.decodeHtmlentities(scrapedtitle)
        if (DEBUG): logger.info("title=["+scrapedtitle+"], url=["+scrapedurl+"]")
        itemlist.append( Item(channel=__channel__, action="findvideos", title="[COLOR azure]"+scrapedtitle+"[/COLOR]" , url=scrapedurl , thumbnail="http://xbmc-repo-ackbarr.googlecode.com/svn/trunk/dev/skin.cirrus%20extended%20v2/extras/moviegenres/All%20Movies%20by%20Genre.png", folder=True) )

    return itemlist

def search(item,texto):
    logger.info("[darkstream.py] "+item.url+" search "+texto)
    item.url = "http://www.darkstream.tv/?s="+texto
    try:
        return peliculas(item)
    # Se captura la excepción, para no interrumpir al buscador global si un canal falla
    except:
        import sys
        for line in sys.exc_info():
            logger.error( "%s" % line )
        return []

def peliculas(item):
    logger.info("streamondemand.darkstream peliculas")
    itemlist = []

    # Descarga la pagina
    data = scrapertools.cache_page(item.url)

    # Extrae las entradas (carpetas)
    patron = '<h2 class="art-postheader"><a href=".*?"[^>]+>(.*?)</a></h2>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    # Extrae el paginador
    patronvideos  = '<a class="next page-numbers" href="(.*?)">Successivo &raquo;</a>/div>'
    matches = re.compile(patronvideos,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    if len(matches)>0:
        scrapedurl = urlparse.urljoin(item.url,matches[0])
        itemlist.append( Item(channel=__channel__, action="peliculas", title="[COLOR orange]Successivo>>[/COLOR]" , url=scrapedurl , thumbnail="http://2.bp.blogspot.com/-fE9tzwmjaeQ/UcM2apxDtjI/AAAAAAAAeeg/WKSGM2TADLM/s1600/pager+old.png", folder=True) )

    return itemlist

def do_search(item):
    logger.info("streamondemand.channels.biblioteca do_search")

    tecleado = item.extra
    mostra = tecleado.replace("+"," ")

    itemlist = []

    import os
    import glob
    import imp

    master_exclude_data_file = os.path.join( config.get_runtime_path() , "resources", "biblioteca.txt")
    logger.info("streamondemand.channels.buscador master_exclude_data_file="+master_exclude_data_file)

    exclude_data_file = os.path.join( config.get_data_path() , "biblioteca.txt")
    logger.info("streamondemand.channels.buscador exclude_data_file="+exclude_data_file)

    channels_path = os.path.join( config.get_runtime_path() , "channels" , '*.py' )
    logger.info("streamondemand.channels.buscador channels_path="+channels_path)

    excluir=""

    if os.path.exists(master_exclude_data_file):
        logger.info("streamondemand.channels.buscador Encontrado fichero exclusiones")

        fileexclude = open(master_exclude_data_file,"r")
        excluir= fileexclude.read()
        fileexclude.close()
    else:
        logger.info("streamondemand.channels.buscador No encontrado fichero exclusiones")
        excluir = "seriesly\nbuscador\ntengourl\n__init__"

    if config.is_xbmc():
        show_dialog = True

    try:
        import xbmcgui
        progreso = xbmcgui.DialogProgressBG()
        progreso.create("Ricerca di "+ mostra.title())
    except:
        show_dialog = False

    channel_files = glob.glob(channels_path)
    number_of_channels = len(channel_files)

    for index, infile in enumerate(channel_files):
        percentage = index*100/number_of_channels

        basename = os.path.basename(infile)
        basename_without_extension = basename[:-3]
        
        if basename_without_extension not in excluir:

            if show_dialog:
                progreso.update(percentage, ' Sto cercando "' + mostra+ '"')

            logger.info("streamondemand.channels.buscador Tentativo di ricerca su " + basename_without_extension + " per "+ mostra)
            try:

                # http://docs.python.org/library/imp.html?highlight=imp#module-imp
                obj = imp.load_source(basename_without_extension, infile)
                logger.info("streamondemand.channels.buscador cargado " + basename_without_extension + " de "+ infile)
                channel_result_itemlist = obj.search( Item() , tecleado)
                for item in channel_result_itemlist:
                    item.title = scrapertools.decodeHtmlentities( item.title )
                    item.title = item.title + " [COLOR orange]su[/COLOR] [COLOR green]" + basename_without_extension + "[/COLOR]"
                    item.viewmode = "list"

                itemlist.extend( channel_result_itemlist )
            except:
                import traceback
                logger.error( traceback.format_exc() )

        else:
            logger.info("streamondemand.channels.buscador do_search_results, Escluso il server " + basename_without_extension)

    itemlist = sorted(itemlist, key=lambda Item: Item.title) 

    if show_dialog:
        progreso.close()

    return itemlist


