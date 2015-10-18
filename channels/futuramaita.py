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

__channel__ = "futuramaita"
__category__ = "F,S,A"
__type__ = "generic"
__title__ = "FuturamaITA Streaming"
__language__ = "IT"

sito = "http://futuramastreamingita.altervista.org/"

headers = [
    ['User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:38.0) Gecko/20100101 Firefox/38.0'],
    ['Accept-Encoding', 'gzip, deflate'],
    ['Referer', 'http://futuramastreamingita.altervista.org/'],
    ['Connection', 'keep-alive']
]

sitofilm = "http://thesimpsonstreaming.altervista.org/i-simpson-il-film-streaming/"

DEBUG = config.get_setting("debug")


def isGeneric():
    return True


def mainlist(item):
    logger.info("[simpsonita.py] mainlist")
    itemlist = []

    # Descarga la página
    data = scrapertools.cachePage(sito)
    logger.info(data)


    itemlist.append(
        Item(channel=__channel__,
                action="mainlist",
                title="[COLOR green]Ricarica...[/COLOR]"))


    patronvideos = '<div class="random-article random-k2-article  ">\s*<div class="title">\s*<h4>\s*<a href="([^"]+)">([^<]+)<\/a>'
    matches = re.compile(patronvideos, re.DOTALL).finditer(data)
    for match in matches:
        scrapedtitle = scrapertools.unescape(match.group(2))
        scrapedurl = sito + match.group(1)
        if (DEBUG): logger.info(
            "title=[" + scrapedtitle + "], url=[" + scrapedurl + "]")

        itemlist.append(
            Item(channel=__channel__,
                 action="play",
                 fulltitle=scrapedtitle,
                 show=scrapedtitle,
                 title="[COLOR green]Puntata Random - " + scrapedtitle + "[/COLOR]",
                 url=scrapedurl))



    # Extrae las entradas (carpetas)
    patronvideos = '<li><a href="([^"]+)"><span class="catTitle">([^<]+)<\/span>'
    matches = re.compile(patronvideos, re.DOTALL).finditer(data)
    for match in matches:
        scrapedtitle = scrapertools.unescape(match.group(2))
        scrapedurl = sito + match.group(1)
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
    logger.info("[simpsonita.py] episodeslist")
    itemlist = []

    # Descarga la página
    data = scrapertools.cachePage(item.url)
    logger.info(data)

    # Extrae las entradas (carpetas)
    patronvideos = '<h3 class="catItemTitle">\s*<a href="([^"]+)">([^<]+)<\/a>'
    matches = re.compile(patronvideos, re.DOTALL).finditer(data)

    for match in matches:
        scrapedtitle = scrapertools.unescape(match.group(2)).strip()
        scrapedurl = sito + match.group(1)
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
