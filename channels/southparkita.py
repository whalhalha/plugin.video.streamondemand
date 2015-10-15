# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# streamondemand.- XBMC Plugin
# Canal para cineblog01
# http://blog.tvalacarta.info/plugin-xbmc/streamondemand.
# ------------------------------------------------------------
import re
import sys
import time
import urllib2
import urlparse

from core import config
from core import logger
from core import scrapertools
from core.item import Item
from servers import servertools

__channel__ = "southparkita"
__category__ = "F,S,A"
__type__ = "generic"
__title__ = "SouthParkITA Streaming"
__language__ = "IT"

sito = "http://southparkstreaming.altervista.org/"

headers = [
    ['User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:38.0) Gecko/20100101 Firefox/38.0'],
    ['Accept-Encoding', 'gzip, deflate'],
    ['Referer', 'http://southparkstreaming.altervista.org/'],
    ['Connection', 'keep-alive']
]

sitofilm = "http://thesimpsonstreaming.altervista.org/i-simpson-il-film-streaming/"

DEBUG = config.get_setting("debug")


def isGeneric():
    return True


def mainlist(item):
    logger.info("[cineblog01.py] mainlist")

    # Descarga la página
    data = scrapertools.cachePage(sitofilm)
    logger.info(data)

    # Extrae las entradas (carpetas)
    patronvideos = '<a href="([^"]+)" target="_blank"><strong>'
    matches = re.compile(patronvideos, re.DOTALL).finditer(data)

    # Main options
    itemlist = [Item(channel=__channel__,
                     action="listseasons",
                     title="[COLOR yellow]Tutte le Stagioni[/COLOR]",
                     url=sito,
                     thumbnail="https://upload.wikimedia.org/wikipedia/en/0/0d/Simpsons_FamilyPicture.png")]
                


    for match in matches:
        scrapedurl = match.group(1)
        if (DEBUG): logger.info(
            "url=[" + scrapedurl + "]")

        # Añade al listado de XBMC
        itemlist.append(
            Item(channel=__channel__,
                     action="play",
                     title="[COLOR red]Il Film[/COLOR]",
                     url=scrapedurl,
                     thumbnail="http://images.movieplayer.it/images/2007/09/13/la-locandina-di-the-simpsons-movie-47408.jpg"))

    return itemlist


def listseasons(item):
    logger.info("[simpsonita.py] mainlist")
    itemlist = []

    # Descarga la página
    data = scrapertools.cachePage(item.url)
    logger.info(data)

    # Extrae las entradas (carpetas)
    
        

    return itemlist


def listepisodes(item):
    logger.info("[simpsonita.py] episodeslist")
    itemlist = []

    # Descarga la página
    data = scrapertools.cachePage(item.url)
    logger.info(data)

    # Extrae las entradas (carpetas)
    patronvideos = '<a href="([^"]+)" target="_blank">\d&#215;([^<]+)'
    matches = re.compile(patronvideos, re.DOTALL).finditer(data)

    for match in matches:
        scrapedtitle = scrapertools.unescape(match.group(2))
        scrapedurl = match.group(1)
        if (DEBUG): logger.info(
            "title=[" + scrapedtitle + "], url=[" + scrapedurl + "]")

        # Añade al listado de XBMC
        itemlist.append(
            Item(channel=__channel__,
                 action="play",
                 fulltitle=scrapedtitle,
                 show=scrapedtitle,
                 title="[COLOR azure]"+ scrapedtitle + "[/COLOR]",
                 url=scrapedurl))

    return itemlist

def play(item):
    logger.info("[cineblog01.py] play")

    data = item.url

    itemlist = servertools.find_video_items(data=data)

    for videoitem in itemlist:
        videoitem.title = item.show
        videoitem.fulltitle = item.fulltitle
        videoitem.show = item.show
        videoitem.thumbnail = item.thumbnail
        videoitem.channel = __channel__

    return itemlist