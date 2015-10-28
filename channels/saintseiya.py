# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# streamondemand.- XBMC Plugin
# Canale per I Cavalieri Dello Zodiaco
# http://blog.tvalacarta.info/plugin-xbmc/streamondemand.
# ------------------------------------------------------------
import urllib2
import re
import sys
import time
import binascii

from core import logger
from core import config
from core import scrapertools
from core.item import Item
from servers import servertools

__channel__ = "saintseiya"
__category__ = "A"
__type__ = "generic"
__title__ = "Saint Seiya"
__language__ = "IT"

headers = [
    ['User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0'],
    ['Accept-Encoding', 'gzip, deflate']
]

DEBUG = config.get_setting("debug")

def isGeneric():
    return True

def mainlist(item):
    logger.info("[saintseiya.py] mainlist")

    itemlist = [Item( channel=__channel__,
                      title="[COLOR azure]Saint Seiya - Saga I - VIII[/COLOR]",
                      action="episodi",
                      url="http://archive.forumcommunity.net/?t=47797121",
                      thumbnail="http://www.sentieriselvaggi.it/wp-content/uploads/public/articoli/14593/Images/200604250765114593.jpg",
                      fanart="http://wfiles.brothersoft.com/s/saint-seiya-wallpaper_153109-1280x720.jpg"),

                Item( channel=__channel__,
                      title="[COLOR azure]Saint Seiya - Hades[/COLOR]",
                      action="episodihades",
                      url="http://archive.forumcommunity.net/?t=39222201",
                      thumbnail="http://imagenes.asia-team.net/afiche/1800.jpg",
                      fanart="http://cartoonsimages.com/sites/default/files/field/image/Saint_Seiya_Hades_Elysion_by_Juni_Anker.jpg"),

                Item( channel=__channel__,
                      title="[COLOR azure]Saint Seiya - Soul Of Gold[/COLOR]",
                      action="episodisoul",
                      url="http://pastebin.com/XsdtYBhU",
                      thumbnail="http://i.imgur.com/0rYG1mV.jpg",
                      fanart="http://vignette4.wikia.nocookie.net/saintseiya/images/8/8e/Gold_Saints_%28No_Cloths%29.png/revision/latest?cb=20150413225923"),
                
                Item( channel=__channel__,
                      title="[COLOR azure]Saint Seiya - Omega[/COLOR]",
                      action="episodiomega",
                      url="http://archive.forumcommunity.net/?t=50446785",
                      thumbnail="http://41.media.tumblr.com/646ae07c78acbb7dd0b32dca6febc2b3/tumblr_mo1n061YrE1rvobogo1_500.jpg",
                      fanart="http://cartoonsimages.com/sites/default/files/field/image/Saint%2BSeiya%2BOmega.jpg"),
                
                Item( channel=__channel__,
                      title="[COLOR azure]Saint Seiya - The Lost Canvas[/COLOR]",
                      action="episodicanvas",
                      url="http://archive.forumcommunity.net/?t=53018304",
                      thumbnail="http://www.thetvking.com/images/tvShows/poster/Saint%20Seiya%20The%20Lost%20Canvas%20%E2%80%93%20Hades%20Mythology.jpg",
                      fanart="http://i.ytimg.com/vi/9QQX6Rtw1IU/maxresdefault.jpg")]


    return itemlist

def episodi( item ):
    logger.info( "saintseiya.py episodi" )

    itemlist = []

    ## Downloads page
    data = anti_cloudflare(item.url)
    ## Extracts the entries
    bloque = scrapertools.get_match(data, "Saga della Guerra Galattica</span></b><br>(.*?)<br></p><br><br><span class=")
    patron = '<br>(.*?)<a href="(.*?)" target="_blank">(.*?)</a>'
    matches = re.compile( patron, re.DOTALL ).findall( bloque )
    scrapertools.printMatches(matches)
   
    for tit1,scrapedurl,tit2 in matches:
        scrapedurl = scrapertools.decodeHtmlentities(scrapedurl)
        scrapedtitle = tit1 + tit2
        scrapedtitle = scrapertools.decodeHtmlentities(scrapedtitle)
        scrapedtitle = scrapertools.htmlclean(scrapedtitle).strip()
        scrapedtitle = scrapertools.decodeHtmlentities(scrapedtitle.replace("<b>", ""))
        itemlist.append( Item( channel=__channel__, action="findvid", title=scrapedtitle, url=scrapedurl, fanart="http://wfiles.brothersoft.com/s/saint-seiya-wallpaper_153109-1280x720.jpg", thumbnail="http://www.toei-animation.com/files/visuels/Saint_Seiya.jpg") )

    return itemlist

def episodihades( item ):
    logger.info( "saintseiya.py episodi" )

    itemlist = []

    ## Downloads page
    data = anti_cloudflare(item.url)
    ## Extracts the entries
    bloque = scrapertools.get_match(data, "<b>SANTUARIO:</b></span><br>(.*?)<br></p><br><br><span class=")
    patron = '<a href="(.*?)" target="_blank">(.*?)</a>'
    matches = re.compile( patron, re.DOTALL ).findall( bloque )
    scrapertools.printMatches(matches)
   
    for scrapedurl,scrapedtitle in matches:
        scrapedurl = scrapertools.decodeHtmlentities(scrapedurl)
        scrapedtitle = scrapertools.decodeHtmlentities(scrapedtitle)      
        itemlist.append( Item( channel=__channel__, action="findvid", title=scrapedtitle, url=scrapedurl, fanart="http://wfiles.brothersoft.com/s/saint-seiya-wallpaper_153109-1280x720.jpg", thumbnail="http://www.animeemanga.it/wp-content/uploads/2012/02/I-Cavalieri-dello-Zodicao-Hades-Chapter-Inferno-Pegasus-Sirio-Crystal-Andromeda-Phoenix-Hades-Pandora-Radamantis-Minosse-Eaco.jpg") )

    return itemlist

def episodiomega( item ):
    logger.info( "saintseiya.py episodi" )

    itemlist = []

    ## Downloads page
    data = anti_cloudflare(item.url)
    ## Extracts the entries
    bloque = scrapertools.get_match(data, "<i>Episodi Saint Seya Omega Streming </i></span></b></span><br><br>(.*?)<br><br><br><br><br>Si Ringrazia")
    patron = '<br>(.*?)<a href="(.*?)" target="_blank">(.*?)</a>'
    matches = re.compile( patron, re.DOTALL ).findall( bloque )
    scrapertools.printMatches(matches)
   
    for tit1,scrapedurl,tit2 in matches:
        scrapedurl = scrapertools.decodeHtmlentities(scrapedurl)
        scrapedtitle = tit1 + tit2
        scrapedtitle = scrapertools.decodeHtmlentities(scrapedtitle)      
        itemlist.append( Item( channel=__channel__, action="findvid", title=scrapedtitle, url=scrapedurl, fanart="http://wfiles.brothersoft.com/s/saint-seiya-wallpaper_153109-1280x720.jpg", thumbnail="http://www.toei-animation.com/files/visuels/Saint_Seiya.jpg") )

    return itemlist

def episodicanvas( item ):
    logger.info( "saintseiya.py episodi" )

    itemlist = []

    ## Downloads page
    data = anti_cloudflare(item.url)
    ## Extracts the entries
    bloque = scrapertools.get_match(data, ">Saint Seiya: The Lost Canvas Sub Ita Streaming</span></b></i></span><br>(.*?)Saint Seiya: The Lost Canvas Sub Ita Download")
    patron = '<br>(.*?)<a href="(.*?)" target="_blank">(.*?)</a>'
    matches = re.compile( patron, re.DOTALL ).findall( bloque )
    scrapertools.printMatches(matches)
   
    for tit1,scrapedurl,tit2 in matches:
        scrapedurl = scrapertools.decodeHtmlentities(scrapedurl)
        scrapedtitle = tit1 + tit2
        scrapedtitle = scrapertools.decodeHtmlentities(scrapedtitle)      
        itemlist.append( Item( channel=__channel__, action="findvid", title=scrapedtitle, url=scrapedurl, fanart="http://wfiles.brothersoft.com/s/saint-seiya-wallpaper_153109-1280x720.jpg", thumbnail="http://media.comicsblog.it/N/New/News5890.jpg") )

    return itemlist

def episodisoul( item ):
    logger.info( "saintseiya.py episodi" )

    itemlist = []

    ## Downloads page
    data = anti_cloudflare(item.url)
    ## Extracts the entries
    patron = '>&lt;br&gt;(.*?)&lt;a href=&quot;(.*?)&quot; target=&quot;_blank&quot;&gt;'
    matches = re.compile( patron, re.DOTALL ).findall( data )
    scrapertools.printMatches(matches)
   
    for scrapedtitle,scrapedurl in matches:
        scrapedurl = scrapertools.decodeHtmlentities(scrapedurl)
        scrapedtitle = scrapertools.decodeHtmlentities(scrapedtitle)      
        itemlist.append( Item( channel=__channel__, action="findvid", title=scrapedtitle, url=scrapedurl, fanart="http://ib3.huluim.com/show/22747?size=476x268&region=US", thumbnail="http://4.bp.blogspot.com/-3o0SH8YNW3k/VXNxuNfiXxI/AAAAAAAABYk/tjuOx7DdlxI/s1600/%255BHorribleSubs%255D%2BSaint%2BSeiya%2B-%2BSoul%2Bof%2BGold%2B-%2B05%2B%255B720p%255D.mkv_snapshot_17.26_%255B2015.06.06_23.09.44%255D.jpg") )

    return itemlist

def findvid(item):
    logger.info("[saintseiya.py] findvideos")

    ## Downloads page
    data = anti_cloudflare(item.url)

    itemlist = servertools.find_video_items(data=data)
    for videoitem in itemlist:
        videoitem.title = item.title + videoitem.title
        videoitem.fulltitle = item.fulltitle
        videoitem.thumbnail = item.thumbnail
        videoitem.channel = __channel__

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

def unescape(par1, par2, par3):
    var1 = par1
    for ii in xrange(0, len(par2)):
        var1 = re.sub(par2[ii], par3[ii], var1)

    var1 = re.sub("%26", "&", var1)
    var1 = re.sub("%3B", ";", var1)
    return var1.replace('<!--?--><?', '<!--?-->')
