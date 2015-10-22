# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# streamondemand.- XBMC Plugin
# Canal para southparkita.altervista.org
# http://blog.tvalacarta.info/plugin-xbmc/streamondemand.
# ------------------------------------------------------------
import re
import os
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
__category__ = "S,A"
__type__ = "generic"
__title__ = "SouthParkITA Streaming"
__language__ = "IT"

sito = "http://southparkita.altervista.org/south-park-ita-streaming/"

headers = [
    ['User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:38.0) Gecko/20100101 Firefox/38.0'],
    ['Accept-Encoding', 'gzip, deflate'],
    ['Referer', 'http://southparkita.altervista.org/south-park-ita-streaming/'],
    ['Connection', 'keep-alive']
]

DEBUG = config.get_setting("debug")


def isGeneric():
    return True


def mainlist(item):
    logger.info("[southparkita.py] mainlist")
    itemlist = []

    # Descarga la página
    data = scrapertools.cachePage(sito)
    logger.info(data)


    itemlist.append(
        Item(channel=__channel__,
                action="mainlist",
                title="[COLOR green]Ricarica...[/COLOR]"))


    # Extrae las entradas (carpetas)
    patronvideos = '<li id="menu-item-\d{4}.*?\d{4}"><a href="([^"]+)">([^<]+)<\/a><\/li>'
    matches = re.compile(patronvideos, re.DOTALL).finditer(data)
    for match in matches:
        scrapedtitle = scrapertools.unescape(match.group(2))
        scrapedurl = match.group(1)
        if (DEBUG): logger.info(
            "title=[" + scrapedtitle + "], url=[" + scrapedurl + "]")

        # Añade al listado de XBMC
        itemlist.append(
            Item(channel=__channel__,
                 action="listepisodes",
                 fulltitle=scrapedtitle,
                 show=scrapedtitle,
                 title="[COLOR azure]" + scrapedtitle + "[/COLOR]",
                 url=scrapedurl))

    

    return itemlist


def listepisodes(item):
    logger.info("[southparkita.py] episodeslist")
    logger.info(item.url)
    itemlist = []

    # Descarga la página
    data = scrapertools.cachePage(item.url)

    cicla = True
    cnt = 2
    while cicla:
        data = data + scrapertools.cachePage(item.url + 'page/' + str(cnt) + '/')
        logger.info(item.url + 'page/' + str(cnt) + '/')
        patronvideos = '<title>Pagina non trovata.*?<\/title>'
        matches = re.compile(patronvideos, re.DOTALL).finditer(data)
        cnt += 1
        logger.info(str(cnt))
        if matches :cicla = False
    

    logger.info(data)

    # Extrae las entradas (carpetas)
    patronvideos = '<h1 class="entry-title noMarginTop"><a href="([^"]+)".*?>([^<]+)<\/a><\/h1>'
    matches = re.compile(patronvideos, re.DOTALL).finditer(data)

    for match in matches:
        scrapedtitle = scrapertools.unescape(match.group(2)).strip()
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

    data = scrapertools.cachePage(item.url)

    itemlist = servertools.find_video_items(data=data)

    for videoitem in itemlist:
        videoitem.title = item.show
        videoitem.fulltitle = item.fulltitle
        videoitem.show = item.show
        videoitem.thumbnail = item.thumbnail
        videoitem.channel = __channel__

    return itemlist
