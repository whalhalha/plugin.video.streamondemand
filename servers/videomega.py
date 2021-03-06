# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# pelisalacarta - XBMC Plugin
# Conector para videomega
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
# ------------------------------------------------------------

import re

from core import logger
from core import scrapertools

headers = [
    ['User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:38.0) Gecko/20100101 Firefox/38.0'],
    ['Accept-Encoding', 'gzip, deflate'],
    ['Accept', "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"]
]


def get_video_url(page_url, premium=False, user="", password="", video_password=""):
    logger.info("streamondemand.videomega get_video_url(page_url='%s')" % page_url)

    headers.append(['Referer', page_url.replace('view.php', '')])
    data = scrapertools.downloadpage(page_url, follow_redirects=False, headers=headers)
    video_urls = []

    location = scrapertools.find_single_match(data, '<source src="([^"]+)"')
    logger.info("streamondemand.videomega location=" + location)

    video_urls.append([scrapertools.get_filename_from_url(location)[-4:] + " [videomega]", location])

    for video_url in video_urls:
        logger.info("streamondemand.videomega %s - %s" % (video_url[0], video_url[1]))

    return video_urls


# Encuentra vídeos del servidor en el texto pasado
def find_videos(data):
    encontrados = set()
    devuelve = []

    pattern = r"//(?:www\.)?videomega\.tv/(?:(?:iframe|cdn|validatehash|view)\.php)?\?(?:ref|hashkey)=([a-zA-Z0-9]+)"

    logger.info("[videomega.py] find_videos #" + pattern + "#")
    matches = re.compile(pattern, re.DOTALL).findall(data)

    for match in matches:
        titulo = "[videomega]"
        url = "http://videomega.tv/view.php?ref=" + match + "&width=100%&height=400"
        if url not in encontrados:
            logger.info("  url=" + url)
            devuelve.append([titulo, url, 'videomega'])
            encontrados.add(url)
        else:
            logger.info("  url duplicada=" + url)

    return devuelve
