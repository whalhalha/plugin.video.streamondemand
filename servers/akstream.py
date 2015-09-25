# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# pelisalacarta - XBMC Plugin
# Conector for akstream.net
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
# by be4t5
# ------------------------------------------------------------

import re

from core import scrapertools
from core import logger
from lib import mechanize


def get_video_url(page_url, premium=False, user="", password="", video_password=""):
    logger.info("[akstream.py] url=" + page_url)
    video_urls = []

    br = mechanize.Browser()
    br.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:38.0) Gecko/20100101 Firefox/38.0')]
    br.set_handle_robots(False)

    r = br.open(page_url)
    vid = scrapertools.find_single_match(r.read(), """http://akstream.video/stream/([^"']+)""")

    r = br.open("http://akstream.video/stream/%s" % vid)

    url = "../viewvideo.php"
    req = br.click_link(url=url)
    data = br.open(req)
    data = data.read()

    # URL
    url = scrapertools.find_single_match(data, '<source src="([^"]+)" type="video/mp4"')
    logger.info("url=" + url)

    # URL del vídeo
    video_urls.append([".mp4" + " [Akstream]", url])

    for video_url in video_urls:
        logger.info("[akstream.py] %s - %s" % (video_url[0], video_url[1]))

    return video_urls


# Encuentra vídeos del servidor en el texto pasado
def find_videos(text):
    encontrados = set()
    devuelve = []

    # http://akstream.net/v/iwbe6genso37
    patronvideos = 'http://akstream.(?:net|video)/(?:v|videos)/([a-z0-9]+)'
    logger.info("[akstream.py] find_videos #" + patronvideos + "#")
    matches = re.compile(patronvideos, re.DOTALL).findall(text)

    for match in matches:
        titulo = "[Akstream]"
        url = "http://akstream.video/videos/" + match
        if url not in encontrados:
            logger.info("  url=" + url)
            devuelve.append([titulo, url, 'akstream'])
            encontrados.add(url)
        else:
            logger.info("  url duplicada=" + url)


    # http://vcrypt.net/sak/0a8hqibleus5
    # Filmpertutti.eu
    br = mechanize.Browser()
    br.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:38.0) Gecko/20100101 Firefox/38.0'),
                     ('Accept-Encoding', 'gzip, deflate'),
                     ('Connection', 'keep-alive')]
    br.set_handle_robots(False)
    patronvideos = 'http://vcrypt.net/sak/([^"]+)'
    matches = re.compile(patronvideos, re.DOTALL).findall(text)
    page = scrapertools.find_single_match(text, 'rel="canonical" href="([^"]+)"')

    for match in matches:
        titulo = "[Akstream]"
        url = "http://vcrypt.net/sak/" + match
        r = br.open(url)
        data = r.read()
        vid = scrapertools.find_single_match(data, 'akstream.(?:net|video)/(?:v|videos)/([^"]+)"')
        url = "http://akstream.video/videos/" + vid
        if url not in encontrados and vid != "":
            logger.info("  url=" + url)
            devuelve.append([titulo, url, 'akstream'])
            encontrados.add(url)
        else:
            logger.info("  url duplicada=" + url)

    return devuelve


def test():
    video_urls = get_video_url("http://akstream.net/v/8513acv2alss")

    return len(video_urls) > 0
