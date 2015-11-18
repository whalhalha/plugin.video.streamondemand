# -*- coding: utf-8 -*-
#------------------------------------------------------------
# streamondemand.- XBMC Plugin
# Canal para hdstreamingit
# http://blog.tvalacarta.info/plugin-xbmc/streamondemand.
#------------------------------------------------------------
import urlparse,urllib2,urllib,re
import os, sys
import base64

from core import logger
from core import config
from core import scrapertools
from core.item import Item
from servers import servertools

__channel__ = "hdstreamingit"
__category__ = "F"
__type__ = "generic"
__title__ = "hd-streaming.it (IT)"
__language__ = "IT"

DEBUG = config.get_setting("debug")

site = "http://www.hd-streaming.it/"
param = "&format=JSON&js=false&_apikey="
key = base64.urlsafe_b64decode('ZTViNTA5OGJhMWU1NDNlNGFiMGNjNThiNWYzYjE5NTg4MzE3YmQ3NjczMjliZGNiODk0ZDg5YjU2MGU1NTJjMDY4ZjFmOWI5NTc5Zjc0NjQ4MmU2YzEyNGViNzQzYmFlY2MyZmVkZTIyNDk5YzA2NGNiMjZjYTQ1ZDlmM2Y1ODFkMmRjZWM4YjdmNmY0ZmI5YmJhMTgyZmQ4Nzc2NzQyYg==')


headers = [
    ['User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:38.0) Gecko/20100101 Firefox/38.0'],
    ['Accept-Encoding', 'gzip, deflate'],
    ['Connection', 'keep-alive'],
    ['Host', 'adfoc.us'],
    ['Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'],
    ['Pragma', 'no-cache'],
    ['Referer', 'http://www.hd-streaming.it/event_categories/film/']
]

def isGeneric():
    return True

def mainlist(item):
    logger.info("streamondemand.hdstreamingit mainlist")
    itemlist = []
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Ultimi Film Inseriti[/COLOR]", action="peliculas", url="http://www.hd-streaming.it/event_categories/film/", thumbnail="http://orig03.deviantart.net/6889/f/2014/079/7/b/movies_and_popcorn_folder_icon_by_matheusgrilo-d7ay4tw.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film Per Categoria[/COLOR]", action="categorias", url="http://www.hd-streaming.it/event_categories/film/", thumbnail="http://xbmc-repo-ackbarr.googlecode.com/svn/trunk/dev/skin.cirrus%20extended%20v2/extras/moviegenres/All%20Movies%20by%20Genre.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR yellow]Cerca...[/COLOR]", action="search", thumbnail="http://dc467.4shared.com/img/fEbJqOum/s7/13feaf0c8c0/Search"))

    
    return itemlist

def search(item,texto):
    logger.info("[hdstreamingit.py] "+item.url+" search "+texto)
    item.url = "http://www.hd-streaming.it/?s=" +texto+ "&search=Cerca"
    try:
        return peliculas(item)
    # Se captura la excepción, para no interrumpir al buscador global si un canal falla
    except:
        import sys
        for line in sys.exc_info():
            logger.error( "%s" % line )
        return []

def categorias(item):
    itemlist = []
    
    # Descarga la pagina
    data = scrapertools.cache_page(item.url)
    bloque = scrapertools.get_match(data,'<ul class="sub-menu">(.*?)</ul>')
    
    # Extrae las entradas (carpetas)
    patron  = '<a href="(.*?)">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(bloque)
    scrapertools.printMatches(matches)

    for scrapedurl,scrapedtitle in matches:
        scrapedplot = ""
        scrapedthumbnail = ""
        if (DEBUG): logger.info("title=["+scrapedtitle+"], url=["+scrapedurl+"]")
        itemlist.append( Item(channel=__channel__, action="peliculas", title="[COLOR azure]"+scrapedtitle+"[/COLOR]" , url=site+scrapedurl , thumbnail="http://xbmc-repo-ackbarr.googlecode.com/svn/trunk/dev/skin.cirrus%20extended%20v2/extras/moviegenres/All%20Movies%20by%20Genre.png", folder=True) )

    return itemlist

def peliculas(item):
    logger.info("streamondemand.hdstreamingit peliculas")
    itemlist = []

    # Descarga la pagina
    data = scrapertools.cache_page(item.url)

    # Extrae las entradas (carpetas)
    patron = '<div class="button_red"><a href="(.*?)"[^>]+>[^>]+>[^>]+>\s*<div class="button_yellow"><a target="_blank" href="(.*?)"'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle, scrapedurl in matches:
        scrapedplot = ""
        #html = scrapertools.cache_page(scrapedtitle)
        #start = html.find("<h1>TRAMA</h1>")
        #end = html.find("</p>", start)
        #scrapedplot = html[start:end]
        #scrapedplot = re.sub(r'<[^>]*>', '', scrapedplot)
        #scrapedplot = scrapertools.decodeHtmlentities(scrapedplot)
        scrapedtitle = scrapertools.decodeHtmlentities(scrapedtitle.replace("http://www.hd-streaming.it/movies/"," "))
        scrapedtitle = scrapertools.decodeHtmlentities(scrapedtitle.replace("/"," "))
        scrapedtitle = scrapertools.decodeHtmlentities(scrapedtitle.replace("-"," "))
        scrapedtitle = ' '.join(word[0].upper() + word[1:] for word in scrapedtitle.split())
        scrapedthumbnail = ""
        if (DEBUG): logger.info("title=["+scrapedtitle+"], url=["+scrapedurl+"], thumbnail=["+scrapedthumbnail+"]")
        itemlist.append( Item(channel=__channel__, action="findvideos", fulltitle=scrapedtitle, show=scrapedtitle, title="[COLOR azure]"+scrapedtitle+"[/COLOR]" , url="https://api.import.io/store/connector/_magic?url="+scrapedurl+param+key, thumbnail=scrapedthumbnail , plot=scrapedplot , folder=True) )

    # Extrae el paginador
    #patronvideos  = '</a><span class="current">.*<a href="(.*?)" class="page"[^>]+>'
    patronvideos  = '<link rel=\'next\' href=\'(.*?)\' />'
    matches = re.compile(patronvideos,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    if len(matches)>0:
        scrapedurl = urlparse.urljoin(item.url,matches[0])
        itemlist.append( Item(channel=__channel__, action="peliculas", title="[COLOR orange]Successivo>>[/COLOR]" , url=scrapedurl , thumbnail="http://2.bp.blogspot.com/-fE9tzwmjaeQ/UcM2apxDtjI/AAAAAAAAeeg/WKSGM2TADLM/s1600/pager+old.png", folder=True) )

    return itemlist

def findvideos(item):
    logger.info("streamondemand.hdstreamingit findvideos")

    # Descarga la página
    data = scrapertools.cache_page(item.url, headers=headers)

    # Skip adfoc.us
    #import time
    #time.sleep(12)

    itemlist = servertools.find_video_items(data=data)
    for videoitem in itemlist:
        videoitem.title = item.title + videoitem.title
        videoitem.fulltitle = item.fulltitle
        videoitem.thumbnail = item.thumbnail
        videoitem.show = item.show
        videoitem.plot = item.plot
        videoitem.channel = __channel__

    # Extrae las entradas
    patron = r'<span id="showSkip" style="display: none;"><a href="(.*?)" class="(.*?)">'
    matches = re.compile(patron, re.DOTALL).findall(data)
    for scrapedurl, scrapedtitle in matches:
        title = scrapedtitle
        itemlist.append(
            Item(channel=__channel__,
                 action="play",
                 title=title,
                 url=scrapedurl,
                 thumbnail=item.thumbnail,
                 fulltitle=item.fulltitle,
                 show=item.show,
                 folder=False))

    return itemlist


def play(item):
    logger.info("[hdstreamingit.py] play")

    ## Sólo es necesario la url
    data = item.url

    itemlist = servertools.find_video_items(data=data)

    for videoitem in itemlist:
        videoitem.title = item.show
        videoitem.fulltitle = item.fulltitle
        videoitem.thumbnail = item.thumbnail
        videoitem.channel = __channel__

    return itemlist


