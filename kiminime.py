#!c:/SDK/Anaconda2/python.exe
from __future__ import print_function
import os, sys
import requests
from bs4 import BeautifulSoup as bs
import argparse
from pydebugger.debug import debug
from make_colors import make_colors
import random
from idm import IDMan
from pywget import wget
if sys.version_info.major == 3:
    raw_input = input
    from urllib.parse import urlparse
else:
    from urlparse import urlparse
import clipboard
from zippyshare_generator import zippyshare
from anonfile import anonfile
from pprint import pprint
import re
import ast

class kiminime(object):
    def __init__(self):
        super(kiminime, self)
        self.url = 'https://kiminime.com/'
    
    def set_proxy(self, proxy):
        proxy_list = {}
        if isinstance(proxy, list):
            for i in proxy:
                if "{" in i[0]:
                    n = ast.literal_eval(i)
                    if isinstance(n, dict):
                        proxy_list.update(n)
                else:
                    j = urlparse(i)
                    scheme = j.scheme
                    netloc = j.netloc
                    if "www." in netloc:
                        netloc = netloc.split('www.')[1]
                    #if ":" in netloc:
                        #netloc = netloc.split(":")[0]
                    proxy_list.update({scheme:scheme + "://" + netloc})
            return proxy_list
        return False
    
    
    def home(self, last = 1, url = None):
        if not url:
            url = self.url
        if url.split('/')[-1].isdigit():
            last = int(url.split('/')[-1])        
        if url.split('/')[-2].isdigit():
            last = int(url.split('/')[-2])
        while 1:
            try:
                a1 = requests.get(url, timeout = 3)
                break
            except:
                sys.stdout.write(".")
        while 1:
            try:
                a2 = requests.get(url + 'page/%d/' % (last + 1), timeout = 3)
                break
            except:
                sys.stdout.write(".")
        while 1:
            try:
                a3 = requests.get(url + 'page/%d/' % (last + 2), timeout = 3)
                break
            except:
                sys.stdout.write(".")
        print("\n")
        b1 = bs(a1.content, 'lxml')
        b2 = bs(a2.content, 'lxml')
        b3 = bs(a3.content, 'lxml')
        class_putih_updateanime1 = b1.find('div', {'class': 'dev',}).find('div', {'class': 'putih updateanime',})
        class_putih_updateanime2 = b2.find('div', {'class': 'dev',}).find('div', {'class': 'putih updateanime',})
        class_putih_updateanime3 = b3.find('div', {'class': 'dev',}).find('div', {'class': 'putih updateanime',})
        #print('class_putih_updateanime =', class_putih_updateanime)
        debug(class_putih_updateanime1 = class_putih_updateanime1)
        all_li1 = class_putih_updateanime1.find('ul').find_all('li')
        all_li2 = class_putih_updateanime2.find('ul').find_all('li')
        all_li3 = class_putih_updateanime3.find('ul').find_all('li')
        all_li = all_li1 + all_li2 + all_li3
        debug(all_li = all_li)
        #print('all_li =', all_li)
        data = {}
        n = 1
        for i in all_li:
            pre_link = i.find('a')
            link = pre_link.get('href')
            debug(link = link)
            thumb = pre_link.find('img').get('src')
            debug(thumb = thumb)
            title = pre_link.find('img').get('title')
            debug(title = title)
            data.update({
                n:{
                    'link': link,
                    'title': title,
                    'thumb': thumb,
                }
            })
            n += 1
        debug(data = data)
        div_pagination = b3.find('div', {'class': 'pagination',})
        page_a = div_pagination.find_all('a')
        page = {}
        for i in page_a:
            if i.text.isdigit():
                page.update({int(str(i.text).strip()): i.get('href'),})
            else:
                page.update({str(i.text).strip(): i.get('href'),})
        debug(page = page)
        
        return data, page, last
        
    def get_download_links(self, url, download_path = os.getcwd(), saveas = None, confirm = False):
        choice = ['lightgreen', 'lightblue', 'lightmagenta', 'lightred', 'lightcyan']
        while 1:
            try:
                a = requests.get(url, timeout = 3)
                break
            except:
                sys.stdout.write(".")
        b = bs(a.content, 'lxml')
        div_download = b.find('div', {'class': 'download',})
        all_div = div_download.find_all('div')
        debug(all_div = all_div)
        v_type = ''
        v_quality = ''
        data = {}
        all_data = {}
        n = 0
        x = 1
        for i in all_div:
            debug(i = i)
            debug(i_text = i.text)
            if not "|" in i.text:
                #print(make_colors("* " + i.text.strip(), random.choice(choice)))
                v_type = re.split("video", i.text.strip().lower(), re.I)[1].strip()
                debug(v_type = v_type)
            else:
                debug(i = i)
                all_a = i.find_all('a')
                quality = i.find('span').text
                debug(quality = quality)
                m = 1
                if quality:
                    v_quality = quality
                    data.update({n: {quality: {}}})
                    for j in all_a:
                        data.get(n).get(quality).update({m: {j.text: j.get('href')}})
                        all_data.update({
                            x: {
                                'quality': v_quality,
                                'provider': j.text,
                                'link': j.get('href'),
                                'vtype': v_type,
                            },
                        })                        
                        #mx = ''
                        #if len(str(m)) == 1 and not m == 10:
                            #mx = '0' + str(m)
                        #else:
                            #mx = str(m)
                        m += 1
                        x += 1
                n += 1
        debug(data = data)
        debug(all_data = all_data)
        #pprint(data)
        z = 1
        zx = ''
        for i in all_data:
            if len(str(z)) == 1:
                zx = "0" + str(z)
            else:
                zx = str(z)
            print(make_colors(str(zx) + ". ", 'lightcyan') + "[" + make_colors(all_data.get(i).get('provider'), 'lightmagenta') + "] (" + make_colors(all_data.get(i).get('quality'), 'lightyellow') + ":" + all_data.get(i).get('vtype') + ") " + make_colors(all_data.get(i).get('link'), 'lightcyan'))
            z += 1
        q = raw_input(make_colors('Select Number to Download: ', 'lightwhite', 'lightblue'))
        
        warn_1 = make_colors("Please insert a valid number !", 'lightred', 'lightyellow', ['blink']) + "[" + make_colors("enter = refresh", 'lightwhite', 'lightmagenta') + "," + make_colors("x|q = exit", 'lightwhite', 'lightred') + "]: "
        
        if q:
            if str(q).isdigit():
                if len(all_a) <= int(q):
                    link = all_data.get(int(q)).get('link')
                    debug(link = link)
                    self.download(link, confirm, download_path, saveas)
            else:
                q = raw_input(warn_1)
        else:
            print(make_colors("EXIT ! (bye bye)", 'lightwhite', 'lightred', ['blink']))
                
    def download(self, url, confirm = False, download_path = os.getcwd(), saveas = None):
        debug(url = url)
        if 'zippyshare' in urlparse(url).netloc:
            z = zippyshare.zippyshare()
            url_download = z.generate(url)
            debug(url_download = url_download)
            d = IDMan()
            d.download(url_download, download_path, saveas, confirm = confirm)
            
        elif 'anonfile' in urlparse(url).netloc:
            a = anonfile.anonfile()
            url_download = a.generate(url)
            debug(url_download = url_download)
            d = IDMan()
            d.download(url_download, download_path, saveas, confirm = confirm)            
        else:
            clipboard.copy(url)
    
    def print_list(self):
        pass
    
    def navigator(self, download_path = os.getcwd(), saveas = None, confirm = False):
        choice = ['lightgreen', 'lightblue', 'lightmagenta', 'lightred']
        
        data, page, last = self.home()
        n = 0
        m = ''
        for i in data:
            if len(str(n)) == 1 and not n + 1 == 10:
                m = '0' + str(n + 1)
            else:
                m = str(n + 1)
            print(m + ". " + make_colors(data.get(i).get('title').encode('utf-8'), 'lightwhite', random.choice(choice)))
            n += 1
            
        q = raw_input(make_colors('Select Number to Download: ', 'lightred', 'lightwhite'))
        
        warn_1 = make_colors("Please insert a valid number !", 'lightred', 'lightyellow', ['blink']) + "[" + make_colors("enter = refresh", 'lightwhite', 'lightmagenta') + "," + make_colors("x|q = exit", 'lightwhite', 'lightred') + "]: "
        
        if q:
            if str(q).isdigit():
                link = data.get(int(q)).get('link')
                self.get_download_links(link, download_path, saveas, confirm)
            elif q == 'x' or q == 'q':
                print(make_colors("EXIT ! (bye bye)", 'lightwhite', 'lightred', ['blink']))
                sys.exit()
            else:
                q = raw_input(warn_1)
        else:
            return self.navigator(download_path, saveas, confirm)
    
    def usage(self):
        parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)
        parser.add_argument('-p', '--download-path', action = 'store', help = 'Download Directory/Save to')
        parser.add_argument('-s', '--saveas', action = 'store', help = 'Save as name')
        parser.add_argument('-c', '--confirm', action = 'store_true', help = 'Confirm before download (IDM Only)')
        if len(sys.argv) == 1:
            parser.print_help()
            #self.navigator()
        #else:
        args = parser.parse_args()
        self.navigator(args.download_path, args.saveas, args.confirm)
    
if __name__ == '__main__':
    c = kiminime()
    c.usage()
    #c.home()
    #c.get_download_links("https://kiminime.com/rezero-kara-hajimeru-isekai-seikatsu-shin-henshuu-ban-episode-5/")
    #c.navigator()
    