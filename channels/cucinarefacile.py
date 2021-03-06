# -*- coding: utf-8 -*-
#------------------------------------------------------------
# streamondemand.- XBMC Plugin
# Canal para cucinarefacile
# http://blog.tvalacarta.info/plugin-xbmc/streamondemand.
#------------------------------------------------------------
import urlparse,urllib2,urllib,re
import os, sys

from core import logger
from core import config
from core import scrapertools
from core.item import Item
from servers import servertools

__channel__ = "cucinarefacile"
__category__ = "D"
__type__ = "generic"
__title__ = "cucinarefacile (IT)"
__language__ = "IT"


DEBUG = config.get_setting("debug")

def isGeneric():
    return True

def mainlist(item):
    logger.info("streamondemand.cucinarefacile mainlist")
    itemlist = []
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Videoricette[/COLOR]", action="peliculas", url="http://www.cucinarefacile.com/tipo-ricetta/video-ricette/", thumbnail="http://orig03.deviantart.net/6889/f/2014/079/7/b/movies_and_popcorn_folder_icon_by_matheusgrilo-d7ay4tw.png"))

    
    return itemlist

def peliculas(item):
    logger.info("streamondemand.cucinarefacile peliculas")
    itemlist = []

    # Descarga la pagina
    data = scrapertools.cache_page(item.url)

    # Extrae las entradas (carpetas)
    patron  = '<div class="post-thumb single-img-box">\s*'
    patron  += '<a href="(.*?)"><img[^=]+=[^=]+=[^=]+="(.*?)"[^>]+></a>\s*'
    patron  += '</div>\s*'
    patron  += '<div[^>]+>\s*'
    patron  += '<h2>[^>]+>(.*?)</a>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedurl,scrapedthumbnail,scrapedtitle in matches:
        scrapedtitle = scrapertools.decodeHtmlentities(scrapedtitle)
        scrapedplot = ""
        if (DEBUG): logger.info("title=["+scrapedtitle+"], url=["+scrapedurl+"], thumbnail=["+scrapedthumbnail+"]")
        itemlist.append( Item(channel=__channel__, action="findvideos", fulltitle=scrapedtitle, show=scrapedtitle, title=scrapedtitle, url=scrapedurl , thumbnail=scrapedthumbnail , plot=scrapedplot , folder=True) )

    # Extrae el paginador
    patronvideos  = 'a class="nextpostslink" rel="next" href="(.*?)">&raquo;'
    matches = re.compile(patronvideos,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    if len(matches)>0:
        scrapedurl = urlparse.urljoin(item.url,matches[0])
        itemlist.append( Item(channel="channelselector" , action="channeltypes", title="[COLOR yellow]Torna Home[/COLOR]" , folder=True) )
        itemlist.append( Item(channel=__channel__, action="peliculas", title="[COLOR orange]Avanti >>[/COLOR]" , url=scrapedurl , folder=True) )

    return itemlist

