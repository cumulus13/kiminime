#!c:/SDK/Anaconda2/python.exe
from __future__ import print_function
import requests
import sys, os
if sys.version_info.major == 3:
    from urllib.parse import urlparse
    raw_input = input
else:
    from urlparse import urlparse
from pydebugger.debug import debug
import json
from bs4 import BeautifulSoup as bs
import re

class anonfile(object):
    def __init__(self):
        super(anonfile, self)
        
    def info(self, url):
        debug(url = url)
        url_api = "https://api.anonfile.com/v2/file/{0}/info"
        file_id = urlparse(url).path.split("/")[1]
        if file_id:
            url_api = url_api.format(file_id)
            debug(url_api = url_api)
            a = requests.get(url_api)
            content = json.loads(a.content)
            debug(content = content)
            return content
        else:
            return False
        
    def upload(self, filepath):
        filepath = os.path.realpath(filepath)
        debug(filepath = filepath)
        data = {
            'file': filepath,
        }
        url = "https://api.anonfile.com/upload"
        debug(data = data)
        a = requests.post(url, data = data)
        content = a.content
        debug(content = content)
        if content:
            content = json.loads(content)
        debug(content = content)
        
    def generate(self, url):
        a = requests.get(url)
        b = bs(a.content, 'lxml')
        div_download_wrapper = b.find('div', {'id': 'download-wrapper',})
        div_download_url = div_download_wrapper.find_all('a', {'id': re.compile('download-'),})
        debug(div_download_wrapper = div_download_wrapper)
        debug(div_download_url = div_download_url)
        links = []
        for i in div_download_url:
            links.append(i.get('href'))
        debug(links = links)
        return links
        
if __name__ == '__main__':
    c = anonfile()
    #c.info("https://anonfile.com/NfIeC8Renf/_neonime_RZ_New_Edition_-_05-360p_mp4")
    #c.upload(sys.argv[1])
    c.generate("https://anonfile.com/NfIeC8Renf/_neonime_RZ_New_Edition_-_05-360p_mp4")