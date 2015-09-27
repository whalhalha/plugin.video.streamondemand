# -*- coding: utf-8 -*-
#------------------------------------------------------------
# streamondemand - XBMC Plugin
# Ricerca "Bibliotecaattori"
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
#------------------------------------------------------------
import urlparse,urllib2,urllib,re
import os, sys
import time

from core import logger
from core import config
from core import scrapertools
from core.item import Item
from servers import servertools

__channel__ = "bibliotecaattori"
__category__ = "F"
__type__ = "generic"
__title__ = "Bibliotecaattori"
__language__ = "IT"

host = "http://altadefinizione.co"

headers = [
    ['User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:38.0) Gecko/20100101 Firefox/38.0'],
    ['Accept-Encoding', 'gzip, deflate'],
    ['Referer', 'http://altadefinizione.co/'],
    ['Connection', 'keep-alive']
]

DEBUG = config.get_setting("debug")

def isGeneric():
    return True

def mainlist(item):
    logger.info("streamondemand.bibliotecaattori mainlist")
    itemlist = []
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Attori-Attrici [A][/COLOR]", action="cat_attori_A", url="http://altadefinizione.co/attori/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Attori-Attrici [B][/COLOR]", action="cat_attori_B", url="http://altadefinizione.co/attori/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Attori-Attrici [C][/COLOR]", action="cat_attori_C", url="http://altadefinizione.co/attori/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Attori-Attrici [D][/COLOR]", action="cat_attori_D", url="http://altadefinizione.co/attori/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Attori-Attrici [E][/COLOR]", action="cat_attori_E", url="http://altadefinizione.co/attori/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Attori-Attrici [F][/COLOR]", action="cat_attori_F", url="http://altadefinizione.co/attori/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Attori-Attrici [G][/COLOR]", action="cat_attori_G", url="http://altadefinizione.co/attori/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Attori-Attrici [H][/COLOR]", action="cat_attori_H", url="http://altadefinizione.co/attori/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Attori-Attrici [I][/COLOR]", action="cat_attori_I", url="http://altadefinizione.co/attori/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Attori-Attrici [J][/COLOR]", action="cat_attori_J", url="http://altadefinizione.co/attori/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Attori-Attrici [K][/COLOR]", action="cat_attori_K", url="http://altadefinizione.co/attori/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Attori-Attrici [L][/COLOR]", action="cat_attori_L", url="http://altadefinizione.co/attori/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Attori-Attrici [M][/COLOR]", action="cat_attori_M", url="http://altadefinizione.co/attori/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Attori-Attrici [N][/COLOR]", action="cat_attori_N", url="http://altadefinizione.co/attori/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Attori-Attrici [O][/COLOR]", action="cat_attori_O", url="http://altadefinizione.co/attori/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Attori-Attrici [P][/COLOR]", action="cat_attori_P", url="http://altadefinizione.co/attori/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Attori-Attrici [Q][/COLOR]", action="cat_attori_Q", url="http://altadefinizione.co/attori/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Attori-Attrici [R][/COLOR]", action="cat_attori_R", url="http://altadefinizione.co/attori/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Attori-Attrici [S][/COLOR]", action="cat_attori_S", url="http://altadefinizione.co/attori/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Attori-Attrici [T][/COLOR]", action="cat_attori_T", url="http://altadefinizione.co/attori/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Attori-Attrici [U][/COLOR]", action="cat_attori_U", url="http://altadefinizione.co/attori/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Attori-Attrici [W][/COLOR]", action="cat_attori_W", url="http://altadefinizione.co/attori/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Attori-Attrici [X][/COLOR]", action="cat_attori_X", url="http://altadefinizione.co/attori/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Attori-Attrici [Y][/COLOR]", action="cat_attori_Y", url="http://altadefinizione.co/attori/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Attori-Attrici [Z][/COLOR]", action="cat_attori_Z", url="http://altadefinizione.co/attori/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))

    return itemlist


def cat_attori_A(item):
    logger.info("streamondemand.bibliotecaattori cat_attori_A")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/attori/a.*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_attori_B(item):
    logger.info("streamondemand.bibliotecaattori cat_attori_B")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/attori/b.*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_attori_C(item):
    logger.info("streamondemand.bibliotecaattori cat_attori_C")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/attori/c.*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_attori_D(item):
    logger.info("streamondemand.bibliotecaattori cat_attori_D")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/attori/d.*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_attori_E(item):
    logger.info("streamondemand.bibliotecaattori cat_attori_E")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/attori/e.*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_attori_F(item):
    logger.info("streamondemand.bibliotecaattori cat_attori_F")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/attori/f.*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_attori_G(item):
    logger.info("streamondemand.bibliotecaattori cat_attori_G")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/attori/g.*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_attori_H(item):
    logger.info("streamondemand.bibliotecaattori cat_attori_H")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/attori/h.*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_attori_I(item):
    logger.info("streamondemand.bibliotecaattori cat_attori_I")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/attori/i.*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_attori_J(item):
    logger.info("streamondemand.bibliotecaattori cat_attori_J")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/attori/j.*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_attori_L(item):
    logger.info("streamondemand.bibliotecaattori cat_attori_L")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/attori/l.*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_attori_M(item):
    logger.info("streamondemand.bibliotecaattori cat_attori_M")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/attori/m.*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_attori_N(item):
    logger.info("streamondemand.bibliotecaattori cat_attori_N")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/attori/n.*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_attori_O(item):
    logger.info("streamondemand.bibliotecaattori cat_attori_O")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/attori/o.*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_attori_P(item):
    logger.info("streamondemand.bibliotecaattori cat_attori_P")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/attori/p.*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_attori_Q(item):
    logger.info("streamondemand.bibliotecaattori cat_attori_Q")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/attori/q.*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_attori_R(item):
    logger.info("streamondemand.bibliotecaattori cat_attori_R")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/attori/r.*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_attori_S(item):
    logger.info("streamondemand.bibliotecaattori cat_attori_S")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/attori/s.*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_attori_T(item):
    logger.info("streamondemand.bibliotecaattori cat_attori_T")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/attori/t.*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_attori_U(item):
    logger.info("streamondemand.bibliotecaattori cat_attori_U")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/attori/u.*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_attori_V(item):
    logger.info("streamondemand.bibliotecaattori cat_attori_V")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/attori/v.*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_attori_W(item):
    logger.info("streamondemand.bibliotecaattori cat_attori_W")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/attori/w.*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_attori_X(item):
    logger.info("streamondemand.bibliotecaattori cat_attori_X")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/attori/x.*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_attori_Y(item):
    logger.info("streamondemand.bibliotecaattori cat_attori_Y")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/attori/y.*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_attori_Z(item):
    logger.info("streamondemand.bibliotecaattori cat_attori_Z")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/attori/z.*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def do_search(item):
    logger.info("streamondemand.channels.bibliotecaattori do_search")

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

def anti_cloudflare(url):
    # global headers

    try:
        resp_headers = scrapertools.get_headers_from_response(url, headers=headers)
        resp_headers = dict(resp_headers)
    except urllib2.HTTPError, e:
        resp_headers = e.headers

    if 'refresh' in resp_headers:
        time.sleep(int(resp_headers['refresh'][:1]))
        
        scrapertools.get_headers_from_response(host + "/" + resp_headers['refresh'][7:], headers=headers)

    return scrapertools.cache_page(url, headers=headers)


