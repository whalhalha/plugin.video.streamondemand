# -*- coding: utf-8 -*-
#------------------------------------------------------------
# streamondemand.- XBMC Plugin
# Canal para effettolunatico
# http://blog.tvalacarta.info/plugin-xbmc/streamondemand.
#------------------------------------------------------------
import urlparse,urllib2,urllib,re
import os, sys

from core import logger
from core import config
from core import scrapertools
from core.item import Item
from servers import servertools
from platformcode import captcha

__channel__ = "effettolunatico"
__category__ = "F"
__type__ = "generic"
__title__ = "Effetto Lunatico"
__language__ = "IT"

DEBUG = config.get_setting("debug")


def isGeneric():
    return True

def mainlist(item):
    logger.info("streamondemand.effettolunatico mainlist")
    itemlist = []
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Ultimi Film Inseriti[/COLOR]", action="peliculas", url="http://effettolunatico.altervista.org/forum/vbtube.php?do=cat&id=2&o=0&page=0", thumbnail="http://orig03.deviantart.net/6889/f/2014/079/7/b/movies_and_popcorn_folder_icon_by_matheusgrilo-d7ay4tw.png"))
    #itemlist.append( Item(channel=__channel__, title="[COLOR yellow]Cerca...[/COLOR]", action="search", thumbnail="http://dc467.4shared.com/img/fEbJqOum/s7/13feaf0c8c0/Search"))

    
    return itemlist

def search(item,texto):
    logger.info("[effettolunatico.py] "+item.url+" search "+texto)
    item.url = "http://effettolunatico.altervista.org/forum/vbtube.php?do=search&"+texto
    try:
        return peliculas(item)
    # Se captura la excepción, para no interrumpir al buscador global si un canal falla
    except:
        import sys
        for line in sys.exc_info():
            logger.error( "%s" % line )
        return []

def peliculas(item):
    logger.info("streamondemand.effettolunatico peliculas")
    itemlist = []

    # Descarga la pagina
    data = scrapertools.cache_page(item.url)

    # Extrae las entradas (carpetas)
    patron = '<td[^>]+><a href="(.*?)"><img src="(.*?)"[^>]+>[^>]+>[^>]+>\s*[^>]+>[^>]+>\s*[^>]+>[^>]+><b>(.*?)</b>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedurl,scrapedthumbnail,scrapedtitle in matches:
        scrapedtitle = scrapertools.decodeHtmlentities(scrapedtitle)
        scrapedtitle = scrapertools.decodeHtmlentities(scrapedtitle.replace("]...","]"))
        html = scrapertools.cache_page(scrapedurl)
        start = html.find("Trama del film")
        end = html.find("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=ISO-8859-1\" />", start)
        scrapedplot = html[start:end]
        scrapedplot = re.sub(r'<[^>]*>', '', scrapedplot)
#        scrapedplot = ""
        if (DEBUG): logger.info("title=["+scrapedtitle+"], url=["+scrapedurl+"], thumbnail=["+scrapedthumbnail+"]")
        itemlist.append( Item(channel=__channel__, action="findvideos", fulltitle=scrapedtitle, show=scrapedtitle, title="[COLOR azure]"+scrapedtitle+"[/COLOR]" , url=scrapedurl , thumbnail=scrapedthumbnail , plot=scrapedplot , folder=True) )

    # Extrae el paginador
    patronvideos  = '<span class="prev_next"><a rel="next" href="(.*?)" title="Pagina successiva[^>]+>'
    matches = re.compile(patronvideos,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    if len(matches)>0:
        scrapedurl = urlparse.urljoin(item.url,matches[0])
        scrapedurl = scrapertools.decodeHtmlentities(scrapedurl.replace(" ","%20"))
        scrapedurl = scrapertools.decodeHtmlentities(scrapedurl.replace("&amp;","&"))
        itemlist.append( Item(channel=__channel__, action="peliculas", title="[COLOR orange]Successivo>>[/COLOR]" , url=scrapedurl , thumbnail="http://2.bp.blogspot.com/-fE9tzwmjaeQ/UcM2apxDtjI/AAAAAAAAeeg/WKSGM2TADLM/s1600/pager+old.png", folder=True) )

    return itemlist

