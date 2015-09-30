# -*- coding: utf-8 -*-
#------------------------------------------------------------
# streamondemand.- XBMC Plugin
# Canal para foxycinema
# http://blog.tvalacarta.info/plugin-xbmc/streamondemand.
#------------------------------------------------------------
import urlparse,urllib2,urllib,re
import os, sys

from core import logger
from core import config
from core import scrapertools
from core.item import Item
from servers import servertools

__channel__ = "foxycinema"
__category__ = "F"
__type__ = "generic"
__title__ = "Foxycinema (IT)"
__language__ = "IT"

sito="http://www.foxycinema.org/"

DEBUG = config.get_setting("debug")

def isGeneric():
    return True

def mainlist(item):
    logger.info("streamondemand.foxycinema mainlist")
    itemlist = []
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Ultimi Film Inseriti[/COLOR]", action="peliculas", url="http://www.foxycinema.org/film.html", thumbnail="http://orig03.deviantart.net/6889/f/2014/079/7/b/movies_and_popcorn_folder_icon_by_matheusgrilo-d7ay4tw.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film Per Categoria[/COLOR]", action="categorias", url="http://www.foxycinema.org/film-per-genere.html", thumbnail="http://xbmc-repo-ackbarr.googlecode.com/svn/trunk/dev/skin.cirrus%20extended%20v2/extras/moviegenres/All%20Movies%20by%20Genre.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film Per Anno[/COLOR]", action="byyear", url="http://www.foxycinema.org/film-per-anno.html", thumbnail="http://xbmc-repo-ackbarr.googlecode.com/svn/trunk/dev/skin.cirrus%20extended%20v2/extras/moviegenres/All%20Movies%20by%20Genre.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR yellow]Cerca...[/COLOR]", action="search", thumbnail="http://dc467.4shared.com/img/fEbJqOum/s7/13feaf0c8c0/Search"))
    
    return itemlist


def categorias(item):
    logger.info("streamondemand.foxycinema categorias")
    itemlist = []

    # Descarga la pagina
    data = scrapertools.cache_page(item.url)
    bloque = scrapertools.get_match(data,'<select style="width: 100%; color: #2d252c; border-color: #dddddd;" name="generi" onchange="location.href=cerca.generi.value;">(.*?)</select>')
    
    # Extrae las entradas (carpetas)
    patron  = '<option value="(.*?)">(.*?)</option>'
    matches = re.compile(patron,re.DOTALL).findall(bloque)
    scrapertools.printMatches(matches)

    for scrapedurl,scrapedtitle in matches:
        scrapedplot = ""
        scrapedthumbnail = ""
        scrapedurl=scrapertools.decodeHtmlentities(scrapedurl.replace("..",""))
        scrapedurl=scrapertools.decodeHtmlentities(scrapedurl.replace("#",""))
        scrapedtitle=scrapertools.decodeHtmlentities(scrapedtitle.replace("|- Cerca per Genere -|",""))
        if (DEBUG): logger.info("title=["+scrapedtitle+"], url=["+scrapedurl+"]")
        itemlist.append( Item(channel=__channel__, action="peliculas", title="[COLOR azure]"+scrapedtitle+"[/COLOR]" , url=sito+scrapedurl , thumbnail="http://xbmc-repo-ackbarr.googlecode.com/svn/trunk/dev/skin.cirrus%20extended%20v2/extras/moviegenres/All%20Movies%20by%20Genre.png", folder=True) )

    return itemlist

def byyear(item):
    logger.info("streamondemand.foxycinema byyear")
    itemlist = []

    # Descarga la pagina
    data = scrapertools.cache_page(item.url)
    bloque = scrapertools.get_match(data,'<select style="width: 100%; color: #2d252c; border-color: #dddddd;" name="anno" onchange="location.href=cerca02.anno.value;">(.*?)</select>')
    
    # Extrae las entradas (carpetas)
    patron  = '<option value="(.*?)">(.*?)</option>'
    matches = re.compile(patron,re.DOTALL).findall(bloque)
    scrapertools.printMatches(matches)

    for scrapedurl,scrapedtitle in matches:
        scrapedplot = ""
        scrapedthumbnail = ""
        scrapedurl=scrapertools.decodeHtmlentities(scrapedurl.replace("..",""))
        scrapedurl=scrapertools.decodeHtmlentities(scrapedurl.replace("#",""))
        scrapedtitle=scrapertools.decodeHtmlentities(scrapedtitle.replace("|- Cerca per Anno -|",""))
        if (DEBUG): logger.info("title=["+scrapedtitle+"], url=["+scrapedurl+"]")
        itemlist.append( Item(channel=__channel__, action="peliculas", title="[COLOR azure]"+scrapedtitle+"[/COLOR]" , url=sito+scrapedurl , thumbnail="http://xbmc-repo-ackbarr.googlecode.com/svn/trunk/dev/skin.cirrus%20extended%20v2/extras/moviegenres/All%20Movies%20by%20Genre.png", folder=True) )

    return itemlist


def search(item,texto):
    logger.info("[foxycinema.py] "+item.url+" search "+texto)
    item.url = "http://www.foxycinema.org/search?q="+texto+"&Search="
    try:
        return peliculasearch(item)
    # Se captura la excepción, para no interrumpir al buscador global si un canal falla
    except:
        import sys
        for line in sys.exc_info():
            logger.error( "%s" % line )
        return []


def peliculas(item):
    logger.info("streamondemand.foxycinema peliculas")
    itemlist = []

    # Descarga la pagina
    data = scrapertools.cache_page(item.url)

    # Extrae las entradas (carpetas)
    patron = '</script>\s*'
    patron += '<a href="(.*?)"[^>]+><img src="(.*?)" title="(.*?)"[^>]+></a>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedurl,scrapedthumbnail,scrapedtitle in matches:
        #response = urllib2.urlopen(scrapedurl)
        #html = response.read()
        #start = html.find("<div class=\"pos-description\">")
        #end = html.find("</p></div>", start)
        #scrapedplot = html[start:end]
        #scrapedplot = re.sub(r'<[^>]*>', '', scrapedplot)
        #scrapedplot = scrapertools.decodeHtmlentities(scrapedplot)
        scrapedtitle = scrapertools.decodeHtmlentities(scrapedtitle)
        scrapedplot = ""
        if (DEBUG): logger.info("title=["+scrapedtitle+"], url=["+scrapedurl+"], thumbnail=["+scrapedthumbnail+"]")
        itemlist.append( Item(channel=__channel__, action="findvideos", fulltitle=scrapedtitle, show=scrapedtitle, title="[COLOR azure]"+scrapedtitle+"[/COLOR]" , url=sito+scrapedurl , thumbnail=scrapedthumbnail , plot=scrapedplot , folder=True) )

    # Extrae el paginador
    patronvideos  = '<a class="next" href="(.*?)">&gt;&nbsp;'
    matches = re.compile(patronvideos,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    if len(matches)>0:
        scrapedurl = urlparse.urljoin(item.url,matches[0])
        itemlist.append( Item(channel=__channel__, action="peliculas", title="[COLOR orange]Successivo>>[/COLOR]" , url=scrapedurl , thumbnail="http://2.bp.blogspot.com/-fE9tzwmjaeQ/UcM2apxDtjI/AAAAAAAAeeg/WKSGM2TADLM/s1600/pager+old.png", folder=True) )

    return itemlist

def peliculasearch(item):
    logger.info("streamondemand.foxycinema peliculas")
    itemlist = []

    # Descarga la pagina
    data = scrapertools.cache_page(item.url)

    # Extrae las entradas (carpetas)
    patron = '<h1 class="uk-article-title">\s*'
    patron += '<a href="(.*?)" title=".*?">(.*?)</a>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedurl,scrapedtitle in matches:
        scrapedtitle = scrapertools.decodeHtmlentities(scrapedtitle)
        if (DEBUG): logger.info("title=["+scrapedtitle+"], url=["+scrapedurl+"]")
        itemlist.append( Item(channel=__channel__, action="findvideos", fulltitle=scrapedtitle, show=scrapedtitle, title=scrapedtitle, url=sito+scrapedurl , folder=True) )

    # Extrae el paginador
    patronvideos  = '<li><a class="next" href="(.*?)" title="Avanti"><i class="uk-icon-angle-right"></i></a></li>'
    matches = re.compile(patronvideos,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    if len(matches)>0:
        scrapedurl = urlparse.urljoin(item.url,matches[0])
        itemlist.append( Item(channel=__channel__, action="peliculas", title="[COLOR orange]Successivo>>[/COLOR]" , url=scrapedurl , thumbnail="http://2.bp.blogspot.com/-fE9tzwmjaeQ/UcM2apxDtjI/AAAAAAAAeeg/WKSGM2TADLM/s1600/pager+old.png", folder=True) )

    return itemlist
