# -*- coding: utf-8 -*-
#------------------------------------------------------------
# streamondemand - XBMC Plugin
# Ricerca "Bibliotecaregisti"
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

__channel__ = "bibliotecaregisti"
__category__ = "F"
__type__ = "generic"
__title__ = "Bibliotecaregisti"
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
    logger.info("streamondemand.bibliotecaregisti mainlist")
    itemlist = []
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Registi [A][/COLOR]", action="cat_registi_A", url="http://altadefinizione.co/registi/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Registi [B C D][/COLOR]", action="cat_registi_B_C_D", url="http://altadefinizione.co/registi/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Registi [E F][/COLOR]", action="cat_registi_E_F", url="http://altadefinizione.co/registi/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Registi [G][/COLOR]", action="cat_registi_G", url="http://altadefinizione.co/registi/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Registi [H I][/COLOR]", action="cat_registi_H_I", url="http://altadefinizione.co/registi/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Registi [J][/COLOR]", action="cat_registi_J", url="http://altadefinizione.co/registi/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Registi [K L][/COLOR]", action="cat_registi_K_L", url="http://altadefinizione.co/registi/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Registi [M][/COLOR]", action="cat_registi_M", url="http://altadefinizione.co/registi/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Registi [N O P][/COLOR]", action="cat_registi_N_O_P", url="http://altadefinizione.co/registi/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Registi [Q R][/COLOR]", action="cat_registi_Q_R", url="http://altadefinizione.co/registi/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Registi [S][/COLOR]", action="cat_registi_S", url="http://altadefinizione.co/registi/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Registi [T U V][/COLOR]", action="cat_registi_T_U_V", url="http://altadefinizione.co/registi/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    itemlist.append( Item(channel=__channel__, title="[COLOR azure]Film per Registi [W X Y Z][/COLOR]", action="cat_registi_W_X_Y_Z", url="http://altadefinizione.co/registi/", thumbnail="http://cinema.clubefl.gr/wp-content/themes/director-theme/images/logo.png"))
    
    return itemlist


def cat_registi_A(item):
    logger.info("streamondemand.bibliotecaregisti cat_registi_A")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/regista/a.*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        scrapedtitle=scrapertools.decodeHtmlentities(scrapedtitle.replace("Aldo","Aldo Baglio"))
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_registi_B_C_D(item):
    logger.info("streamondemand.bibliotecaregisti cat_registi_B_C_D")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/regista/[bcd].*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_registi_E_F(item):
    logger.info("streamondemand.bibliotecaregisti cat_registi_E_F")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/regista/[ef].*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_registi_G(item):
    logger.info("streamondemand.bibliotecaregisti cat_registi_G")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/regista/g.*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        scrapedtitle=scrapertools.decodeHtmlentities(scrapedtitle.replace("Giacomo","Giacomo Poretti"))
        scrapedtitle=scrapertools.decodeHtmlentities(scrapedtitle.replace("Giovanni","Giovanni Storti"))
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_registi_H_I(item):
    logger.info("streamondemand.bibliotecaregisti cat_registi_H_I")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/regista/[hi].*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_registi_J(item):
    logger.info("streamondemand.bibliotecaregisti cat_registi_J")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/regista/[j].*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_registi_K_L(item):
    logger.info("streamondemand.bibliotecaregisti cat_registi_K_L")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/regista/[kl].*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_registi_M(item):
    logger.info("streamondemand.bibliotecaregisti cat_registi_M")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/regista/[m].*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_registi_N_O_P(item):
    logger.info("streamondemand.bibliotecaregisti cat_registi_N_O_P")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/regista/[nop].*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        scrapedtitle=scrapertools.decodeHtmlentities(scrapedtitle.replace("N/A",""))
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_registi_Q_R(item):
    logger.info("streamondemand.bibliotecaregisti cat_registi_Q_R")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/regista/[qr].*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_registi_S(item):
    logger.info("streamondemand.bibliotecaregisti cat_registi_S")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/regista/[s].*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def cat_registi_T_U_V(item):
    logger.info("streamondemand.bibliotecaregisti cat_registi_T_U_V")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/regista/[tuv].*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist


def cat_registi_W_X_Y_Z(item):
    logger.info("streamondemand.bibliotecaregisti cat_registi_W_X_Y_Z")
    itemlist = []

    # Descarga la pagina
    data = anti_cloudflare( item.url )
    
    # Extrae las entradas (carpetas)
    patron  = '<li><a href="http://altadefinizione.co/regista/[wxyz].*?" rel="tag">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedtitle in matches:
        titolo = scrapedtitle.replace(" ","+")
        itemlist.append( Item(channel=__channel__, action="do_search", extra=titolo, title= scrapedtitle , folder=True) )

    return itemlist

def do_search(item):
    logger.info("streamondemand.channels.bibliotecaregisti do_search")

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


