# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# streamondemand.- XBMC Plugin
# Canal para altadefinizione01
# http://www.mimediacenter.info/foro/viewforum.php?f=36
# ------------------------------------------------------------
import urlparse
import re
import sys
import urllib2
import time

from core import logger
from core import config
from core import scrapertools
from core.item import Item

__channel__ = "altadefinizione01"
__category__ = "F,S,A"
__type__ = "generic"
__title__ = "AltaDefinizione01"
__language__ = "IT"

sito = "http://www.altadefinizione01.com/"

headers = [
    ['User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:38.0) Gecko/20100101 Firefox/38.0'],
    ['Accept-Encoding', 'gzip, deflate'],
    ['Referer', 'http://www.altadefinizione01.com'],
    ['Connection', 'keep-alive']
]

DEBUG = config.get_setting("debug")


def isGeneric():
    return True


def mainlist(item):
    logger.info("streamondemand.altadefinizione01 mainlist")

    itemlist = [Item(channel=__channel__,
                     title="[COLOR azure]Ultimi film inseriti[/COLOR]",
                     action="peliculas",
                     url=sito,
                     thumbnail="http://orig03.deviantart.net/6889/f/2014/079/7/b/movies_and_popcorn_folder_icon_by_matheusgrilo-d7ay4tw.png"),
                Item(channel=__channel__,
                     title="[COLOR azure]Film Sub-Ita[/COLOR]",
                     action="peliculas",
                     url=sito + "genere/sub-ita/",
                     thumbnail="http://i.imgur.com/qUENzxl.png"),
                Item(channel=__channel__,
                     title="[COLOR azure]Categorie film[/COLOR]",
                     action="categorias",
                     url=sito,
                     thumbnail="http://xbmc-repo-ackbarr.googlecode.com/svn/trunk/dev/skin.cirrus%20extended%20v2/extras/moviegenres/All%20Movies%20by%20Genre.png"),
                Item(channel=__channel__,
                     title="[COLOR yellow]Cerca...[/COLOR]",
                     action="search",
                     thumbnail="http://dc467.4shared.com/img/fEbJqOum/s7/13feaf0c8c0/Search")]

    return itemlist


def peliculas(item):
    logger.info("streamondemand.altadefinizione01 peliculas")
    itemlist = []

    # Descarga la pagina
    # data = scrapertools.cache_page(item.url)

    data = anti_cloudflare(item.url)
    logger.info(data)

    ## ------------------------------------------------
    cookies = ""
    matches = re.compile('(.altadefinizione01.com.*?)\n', re.DOTALL).findall(config.get_cookie_data())
    for cookie in matches:
        name = cookie.split('\t')[5]
        value = cookie.split('\t')[6]
        cookies += name + "=" + value + ";"
    headers.append(['Cookie', cookies[:-1]])
    import urllib
    _headers = urllib.urlencode(dict(headers))
    ## ------------------------------------------------

    # Extrae las entradas (carpetas)
    patron = '<a\s+href="([^"]+)"\s+title="[^"]*">\s+<img\s+width="[^"]*"\s+height="[^"]*"\s+src="([^"]+)"\s+class="[^"]*"\s+alt="([^"]+)"'
    matches = re.compile(patron, re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    for scrapedurl, scrapedthumbnail, scrapedtitle in matches:
        html = scrapertools.cache_page(scrapedurl)
        start = html.find("<div class=\"aciklama\">")
        end = html.find("<div class=\'bMavi\'>Titolo originale:", start)
        scrapedplot = html[start:end]
        scrapedtitle = scrapertools.decodeHtmlentities(scrapedtitle.replace("Streaming", ""))
        scrapedplot = re.sub(r'<[^>]*>', '', scrapedplot)
        scrapedplot = scrapertools.decodeHtmlentities(scrapedplot)
        if DEBUG: logger.info(
            "title=[" + scrapedtitle + "], url=[" + scrapedurl + "], thumbnail=[" + scrapedthumbnail + "]")
        ## ------------------------------------------------
        scrapedthumbnail+= "|" + _headers
        ## ------------------------------------------------
        itemlist.append(
            Item(channel=__channel__,
                 action="findvid",
                 title="[COLOR azure]" + scrapedtitle + "[/COLOR]",
                 fulltitle=scrapedtitle,
                 show=scrapedtitle,
                 url=scrapedurl,
                 viewmode="movie_with_plot",
                 thumbnail=scrapedthumbnail,
                 plot=scrapedplot,
                 folder=True))

    # Extrae el paginador
    patronvideos = 'class="nextpostslink" rel="next" href="([^"]+)">&raquo;'
    matches = re.compile(patronvideos, re.DOTALL).findall(data)
    scrapertools.printMatches(matches)

    if len(matches) > 0:
        scrapedurl = urlparse.urljoin(item.url, matches[0])
        itemlist.append(
            Item(channel=__channel__,
                 action="peliculas",
                 title="[COLOR orange]Successivo >>[/COLOR]",
                 url=scrapedurl,
                 thumbnail="http://2.bp.blogspot.com/-fE9tzwmjaeQ/UcM2apxDtjI/AAAAAAAAeeg/WKSGM2TADLM/s1600/pager+old.png",
                 folder=True))

    return itemlist


def categorias(item):
    logger.info("streamondemand.altadefinizione01 categorias")
    itemlist = []

    # data = scrapertools.cache_page(item.url)
    data = anti_cloudflare(item.url)
    logger.info(data)

    # Narrow search by selecting only the combo
    bloque = scrapertools.get_match(data, '<ul class="kategori_list">(.*?)</ul>')

    # The categories are the options for the combo  
    patron = '<li><a href="([^"]+)">([^<]+)</a></li>'
    matches = re.compile(patron, re.DOTALL).findall(bloque)
    scrapertools.printMatches(matches)

    for url, titulo in matches:
        scrapedtitle = titulo
        scrapedurl = urlparse.urljoin(item.url, url)
        scrapedthumbnail = ""
        scrapedplot = ""
        if DEBUG: logger.info(
            "title=[" + scrapedtitle + "], url=[" + scrapedurl + "], thumbnail=[" + scrapedthumbnail + "]")
        itemlist.append(
            Item(channel=__channel__,
                 action="peliculas",
                 title="[COLOR azure]" + scrapedtitle + "[/COLOR]",
                 url=scrapedurl,
                 thumbnail=scrapedthumbnail,
                 plot=scrapedplot))

    return itemlist


def search(item, texto):
    logger.info("[altadefinizione01.py] " + item.url + " search " + texto)
    item.url = "%sindex.php/?s=%s" % (sito, texto)
    try:
        return peliculas(item)
    # Se captura la excepción, para no interrumpir al buscador global si un canal falla
    except:
        import sys
        for line in sys.exc_info():
            logger.error("%s" % line)
        return []


def findvid(item):
    logger.info("[altadefinizione01.py] findvideos")
    itemlist = []

    ## Descarga la página
    data = re.sub(
        r'\t|\n|\r',
        '',
        anti_cloudflare(item.url)
    )
    '''
    <a href="http://www.vid.gg/video/1926a2839ef78" rel="nofollow" target="_blank"><li class="part"><span class="a"><i class="fa fa-circle-o fa-lg"></i> Streaming</span><span class="b"><img src="http://www.vidgg.to/images/favicon.ico" alt="Vidgg" height="10"> Vidgg</span><span class="d">360p</span><span class="c"><ul class="link_rating rating" data="8"><li><i class="fa fa-star"></i></li><li><i class="fa fa-star"></i></li><li><i class="fa fa-star"></i></li><li><i class="fa fa-star"></i></li><li><i class="fa fa-star"></i></li></ul>
    '''
    patron = '<a href="([^"]+)"[^>]+><li class="part">'  # url
    patron += '<span class="a"><i[^>]+></i>([^<]+)</span>'  # type
    patron += '<span class="b"><img src="([^"]+)"[^>]+>([^<]+)</span>'  # thumbnail & title
    patron += '<span class="d">([^<]+)</span>'  # quality
    patron += '<span class="c"><ul class="link_rating rating" data="([^"]+)">'  # rating

    matches = re.compile(patron, re.DOTALL).findall(data)

    for url, type, thumbnail, scrapedtitle, quality, rating in matches:
        title = "[" + scrapedtitle.strip() + "] " + type + " (" + quality.strip() + ") (" + rating + ")"

        itemlist.append(
            Item(channel=__channel__,
                 action="findvideos",
                 title=title, url=url,
                 thumbnail=thumbnail,
                 fulltitle=item.fulltitle,
                 show=item.show,
                 plot=item.plot))

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

        scrapertools.get_headers_from_response(sito + resp_headers['refresh'][7:], headers=headers)

    return scrapertools.cache_page(url, headers=headers)

