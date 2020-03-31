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
import time
import traceback


class kiminime(object):
    def __init__(self):
        super(kiminime, self)
        self.url = 'https://kiminime.com/'
        self.session = requests.session()
        debug(session_proxy = self.session.proxies)
        self.monitor_run = False
    
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
    
    
    
    def makeList(self, alist, ncols, vertically=True, file=None):
        debug()
        from distutils.version import StrictVersion # pep 386
        import prettytable as ptt # pip install prettytable
        assert StrictVersion(ptt.__version__) >= StrictVersion('0.7') # for PrettyTable.vrules property
        L = alist
        nrows = - ((-len(L)) // ncols)
        ncols = - ((-len(L)) // nrows)
        t = ptt.PrettyTable([str(x) for x in range(ncols)])
        t.header = False
        t.align = 'l'
        t.hrules = ptt.NONE
        t.vrules = ptt.NONE
        r = nrows if vertically else ncols
        chunks = [L[i:i+r] for i in range(0, len(L), r)]
        chunks[-1].extend('' for i in range(r - len(chunks[-1])))
        if vertically:
            chunks = list(zip(*chunks))
        for c in chunks:
            t.add_row(c)
        print(t)
     
    def home(self, last = 1, url = None):
        if not url:
            url = self.url
        if url.split('/')[-1].isdigit():
            last = int(url.split('/')[-1])        
        if url.split('/')[-2].isdigit():
            last = int(url.split('/')[-2])
        while 1:
            try:
                a1 = self.session.get(url, timeout = 3)
                break
            except:
                if not self.monitor_run:
                    sys.stdout.write(".")
        while 1:
            try:
                a2 = self.session.get(url + 'page/%d/' % (last + 1), timeout = 3)
                break
            except:
                if not self.monitor_run:
                    sys.stdout.write(".")
        while 1:
            try:
                a3 = self.session.get(url + 'page/%d/' % (last + 2), timeout = 3)
                break
            except:
                if not self.monitor_run:
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
        
    def search(self, query):
        params = {'s': query,}
        url = self.url
        while 1:
            try:
                a = self.session.get(url, timeout = 3, params = params)
                break
            except:
                if not self.monitor_run:
                    sys.stdout.write(".")
        debug(proxy_set = a.connection.proxy_manager)

        print("\n")
        b = bs(a.content, 'lxml')
        class_putih = b.find('div', {'class': 'dev',}).find('div', {'class': 'putih',})
        #print('class_putih_updateanime =', class_putih_updateanime)
        debug(class_putih = class_putih)
        div_bs = class_putih.find_all('div', {'class': 'bs',})
        debug(div_bs = div_bs)
        
        data = {}
        n = 1
        for i in div_bs:
            pre_link = i.find('a', {'class': 'tip',})
            link = pre_link.get('href')
            debug(link = link)
            thumb = pre_link.find('div', {'class': 'limit'}).find('img').get('src')
            debug(thumb = thumb)
            title = pre_link.find('div', {'class': 'bigor',}).find('div', {'class': 'tt',}).text
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
        page = {}
        div_pagination = b.find('div', {'class': 'pagination',})
        if div_pagination:
            page_a = div_pagination.find_all('a')        
            for i in page_a:
                if i.text.isdigit():
                    page.update({int(str(i.text).strip()): i.get('href'),})
                else:
                    page.update({str(i.text).strip(): i.get('href'),})
        debug(page = page)
        
        return data, page
    
    
    def get_anime_detail(self, url):
        debug("cls")
        data = {}
        a = self.session.get(url)
        b = bs(a.content, 'lxml')
        backdrop = b.find('div', {'class': 'ime',}).find('img').get('src')
        debug(backdrop = backdrop)
        thumb = b.find('div', {'class': 'thumbss',}).find('img').get('src')
        debug(thumb = thumb)
        title = b.find('div', {'class': 'infox',}).find('h1', {'class': 'entry-title',})
        if title:
            title = re.split("Subtitle|Indonesia", title.text)[0].strip()
        else:
            title = ''
        data.update({'title': title,})
        div_spe = b.find("div", {"class": "spe",})
        all_span = div_spe.find_all('span')
        for i in all_span:
            key = i.find('b')
            debug(key = key)
            key = re.split(" :", key.text)[0]
            debug(key = key)
            if i.find_all('a'):
                value = {}
                for j in i.find_all('a'):
                    value.update({j.text : j.get('href')})
                    debug(value0 = value)
            else:
                value = re.split(": ", i.text)[1].strip()
                debug(value1 = value)
            data.update({key: value,})
        debug(data = data)
        
        description = ""
        div_desc = b.find('div', {'class': 'desc',})
        debug(div_desc = div_desc)
        if div_desc:
            description = div_desc.find('div', {'class': 'entry-content entry-content-single',}).find_all('p')
            if len(description[0].text) > 100:
                description = description[0].text
            else:
                description = description[1].text
        data.update({'desc': description,})
        debug(data = data)
        episodes = {}
        div_episode = b.find('div', {'class': 'episodelist',})
        all_li_episode = div_episode.find('ul').find_all('li')
        for i in all_li_episode:
            a_pre = i.find('a')
            title = a_pre.text
            link = a_pre.get('href')
            key = re.split("Episode ", title, re.I)[1]
            debug(key = key)
            key = int(key)
            episodes.update({
                key: {
                    'title': title,
                    'link': link,
                },
            })
        debug(episodes = episodes)
        
        #data.update({'episodes': episodes,})
        return data, episodes     
    
    def get_download_links(self, url, download_path = os.getcwd(), saveas = None, confirm = False, print_list = True):
        #choice = ['lightgreen', 'lightblue', 'lightmagenta', 'lightred', 'lightcyan']
        while 1:
            try:
                a = self.session.get(url, timeout = 3)
                break
            except:
                if not self.monitor_run:
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
        
        if print_list:
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
        return all_data
    
    def get_root_link(self, url):
        #choice = ['lightgreen', 'lightblue', 'lightmagenta', 'lightred', 'lightcyan']
        while 1:
            try:
                a = self.session.get(url, timeout = 3)
                break
            except:
                if not self.monitor_run:
                    sys.stdout.write(".")
        b = bs(a.content, 'lxml')
        data = b.find('div', {'class': 'dtl',}).find('a').get('href')
        debug(data = data)
        return data
    
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
    
    def navigator(self, download_path = os.getcwd(), saveas = None, confirm = False, search = False, query = None, word_insert = "", q = None, show_episode = True, show_home = True):
        choice = ['lightgreen', 'lightblue', 'lightmagenta', 'lightred']
        if search:
            debug(query = query)
            if not query:
                words = make_colors("No Search query !", 'lightwhite', 'lightred', ['blink'])
                return self.navigator(download_path, saveas, confirm, word_insert = words)
            else:
                data, page = self.search(query)
                debug(data_search = data)
        else:
            data, page, last = self.home()
        n = 0
        m = ''
        if show_home:
            for i in data:
                if len(str(n)) == 1 and not n + 1 == 10:
                    m = '0' + str(n + 1)
                else:
                    m = str(n + 1)
                print(m + ". " + make_colors(data.get(i).get('title').encode('utf-8'), 'lightwhite', random.choice(choice)))
                n += 1
        if word_insert:
            print(word_insert)
            word_insert = ""
        note = make_colors('Select Number to Download: ', 'lightred', 'lightwhite') + "[" + make_colors("enter = refresh and continue", 'lightwhite', 'lightmagenta') + "," + make_colors("x|q = exit", 'lightwhite', 'lightred') + "," + make_colors("[n]i = info of number selected", 'lightwhite', 'green')  + "," + make_colors("[n]e|e = '[n]e' for direct show episode, 'e' for show episode after show detail info", 'lightwhite', 'lightmagenta')+ "]: "
        
        warn_1 = make_colors("Please insert a valid number !", 'lightred', 'lightyellow', ['blink']) + "[" + make_colors("enter = refresh and continue", 'lightwhite', 'lightmagenta') + "," + make_colors("x|q = exit", 'lightwhite', 'lightred') + "]: "
        
        if not q:
            q = raw_input(note)        
        if q:
            if str(q).isdigit():
                link = data.get(int(q)).get('link')
                if show_episode:
                    self.get_download_links(link, download_path, saveas, confirm, True)
                    return self.navigator(download_path, saveas, confirm)
            elif q == 'x' or q == 'q':
                print(make_colors("EXIT ! (bye bye)", 'lightwhite', 'lightred', ['blink']))
                sys.exit()
            elif len(q) > 1 and q[-1] == 'd':
                word_insert = make_colors("[ERROR] Invalid Number !", 'lightwhite', 'lightred')
                if not q[:-1].isdigit():
                    return self.navigator(download_path, saveas, confirm, search, query, word_insert)                                
                link = data.get(int(q[:-1])).get('link')
                self.get_download_links(link, download_path, saveas, confirm, True)
                return self.navigator(download_path, saveas, confirm)                
            elif len(q) > 1 and q[-1] == 'i':
                word_insert = make_colors("[ERROR] Invalid Number !", 'lightwhite', 'lightred')
                if not q[:-1].isdigit():
                    return self.navigator(download_path, saveas, confirm, search, query, word_insert)                                
                info = ''
                link = data.get(int(q[:-1])).get('link')
                if 'episode' in link:
                    link = self.get_root_link(link)
                data_details, episodes = self.get_anime_detail(link)
                for i in data_details:
                    if isinstance(data_details.get(i), dict):
                        info = ", ".join(data_details.get(i).keys())
                    else:
                        info = data_details.get(i)
                    print(make_colors(i, 'lightcyan') + " " * (12 - len(i)) + ": " + info)
                q1 = raw_input(note)
                if q1 == 'e':
                    return self.navigator(download_path, saveas, confirm, search, query, word_insert, q=q[:-1]+'e')
            
            elif len(q) > 1 and q[-1] == 'e':
                word_insert = make_colors("[ERROR] Invalid Number !", 'lightwhite', 'lightred')
                if not q[:-1].isdigit():
                    return self.navigator(download_path, saveas, confirm, search, query, word_insert)                
                link = data.get(int(q[:-1])).get('link')
                if 'episode' in link:
                    link = self.get_root_link(link)
                data_details, episodes = self.get_anime_detail(link)                
                ne = 1
                nl = (len(episodes) / 12) / 2
                if nl == 0:
                    nl = 1
                episodes_keys = episodes.keys()
                debug(episodes_keys = episodes_keys)
                print(make_colors(data_details.get('title'), 'black', 'lightyellow') + ": ")

                for j in episodes_keys:
                    if len(str(ne)) == 1:
                        if len(episodes) >= 100:
                            j2 = "00" + str(ne) + ". Episode 0" + str(j)
                        else:
                            j2 = "0" + str(ne) + ". Episode 0" + str(j)
                    else:
                        if len(str(ne)) == 2 and len(episodes) >= 100:
                            j2 = "0" + str(ne) + ". Episode 0" + str(j)
                        else:
                            j2 = str(ne) + ". Episode " + str(j)
                    ne += 1
                    index = episodes_keys.index(j)
                    episodes_keys.remove(j)
                    episodes_keys.insert(index, j2)
                #if show_episode:
                self.makeList(episodes_keys, nl)
                string_note_download_all = "download all or separated can with other option. for example you can download with specific vtype, quality and provider code by type: 'a[all] mp4 720 zs', it will download all episode with vtype mp4, quality 720p and provider from zippyshare,  '1,3,5,4 mp4 720 zs', '1-3 mp4 720 zs' or it will ask for vtype,quality,provider automaticly"
                note_download_all = make_colors(string_note_download_all, 'lightwhite', 'lightblue')
                print(note_download_all)
                q2 = raw_input(make_colors("Select number to download", 'lightred', 'lightwhite') + "[" + make_colors("a[ll] = download all", 'black', 'lightyellow') + ", " + make_colors(" x|q = exit", 'lightwhite', 'lightred') + ", " + make_colors("enter = refresh and continue", 'lightwhite', 'lightblue') + "]: ")
                q_vtype = ""
                q_quality = ""
                q_provider = ""                
                if q2 and q2.isdigit() and int(q2) <= len(episodes):
                    print(make_colors(episodes.get(int(q2)).get('title'), 'lightwhite', 'blue'))
                    self.get_download_links(episodes.get(int(q2)).get('link'), download_path, saveas, confirm, True)
                    return self.navigator(download_path, saveas, confirm, search, query, word_insert)
                elif q2 == 'x' or q2 == 'q':
                    print(make_colors("Bye bye ...", 'lightred'))
                    sys.exit()
                elif "," in q2 or "-":
                    episodes_temp = {}
                    data_split = re.split(" ", str(q2).strip())
                    if "," in q2:
                        data_split_number = re.split(",", data_split[0])
                    elif "-" in q2:
                        data_split_number_0 = re.split("-", data_split[0])
                        data_split_number = []
                        for r in range(int(data_split_number_0[0]), int(data_split_number_0[1]) + 1):
                            data_split_number.append(r)
                    debug(data_split_number = data_split_number)
                    for e in data_split_number:
                        episodes_temp.update({int(e): episodes.get(int(e))})
                    
                    episodes = episodes_temp
                    episodes_keys = episodes.keys()
                    debug(episodes_keys = episodes_keys)
                    
                    try:
                        q_vtype = data_split[1]
                    except:
                        pass
                    try:
                        q_quality = data_split[2]
                    except:
                        pass
                    try:
                        q_provider = data_split[3]
                    except:
                        pass
                    
                elif str(q2).strip() == 'a' or str(q2).strip() == 'all':
                    q_vtype = raw_input(make_colors("Video Type [mp4]: ", 'lightgreen'))
                    q_quality = raw_input(make_colors("Quality [720]: ", 'lightcyan'))
                    q_provider = raw_input(make_colors("Provider [ZS]: ", 'lightyellow'))
                    
                elif "a" in str(q2).strip() or "all" in str(q2).strip():
                    data_split = re.split(" ", str(q2).strip())
                    try:
                        q_vtype = data_split[1]
                    except:
                        pass
                    try:
                        q_quality = data_split[2]
                    except:
                        pass
                    try:
                        q_provider = data_split[3]
                    except:
                        pass
                if not q_vtype:
                    q_vtype = 'mp4'
                if not q_provider:
                    q_provider = 'zs'
                if not q_quality:
                    q_quality = '720'
                for z in episodes_keys:
                    debug(episodes = episodes)
                    debug(episodes_keys = episodes_keys)
                    all_download_link = []
                    all_download_link = self.get_download_links(episodes.get(int(z)).get('link'), download_path, saveas, confirm, False)
                    debug(all_download_link = all_download_link)
                    #'quality': v_quality,
                    #'provider': j.text,
                    #'link': j.get('href'),
                    #'vtype': v_type,
                    
                    download_link = ''
                    q_provider = str(q_provider).upper()
                    if not str(q_quality).lower()[-1] == 'p':
                        q_quality = str(q_quality) + "p"                    
                    debug(q_vtype = q_vtype)
                    debug(q_provider = q_provider)
                    debug(q_quality = q_quality)
                    for d in all_download_link:
                        if all_download_link.get(d).get('vtype') == q_vtype and all_download_link.get(d).get('provider') == q_provider and all_download_link.get(d).get('quality') == q_quality:
                            download_link = all_download_link.get(d).get('link')
                            debug(download_link = download_link)
                            print(make_colors('download', 'lightwhite', 'lightcyan') + ' ' + make_colors(episodes.get(int(z)).get('title'), 'lightwhite', 'blue'))
                            self.download(download_link, confirm, download_path, saveas)
                    if not download_link:
                        print(make_colors('download [ERROR] (no vtype/provider/quality found)', 'lightwhite', 'lightred') + ' ' + make_colors(episodes.get(int(z)).get('title'), 'lightwhite', 'blue'))
                
                if "a" in str(q2).strip() or "all" in str(q2).strip():
                    return self.navigator(download_path, saveas, confirm, False, query, word_insert)
                elif str(q2).strip() == 'a' or str(q2).strip() == 'all':
                    return self.navigator(download_path, saveas, confirm, False, query, word_insert)
                else:
                    return self.navigator(download_path, saveas, confirm, False, query, word_insert, q, False, False)
            elif len(q) > 1 and q[-1] == 't':
                word_insert = make_colors("[ERROR] Invalid Number !", 'lightwhite', 'lightred')
                if not q[:-1].isdigit():
                    return self.navigator(download_path, saveas, confirm, search, query, word_insert)                
                info = ''
                link = data.get(int(q[:-1])).get('link')
                if 'episode' in link:
                    link = self.get_root_link(link)
                data_details, episodes = self.get_anime_detail(link)
                for i in data_details:
                    if isinstance(data_details.get(i), dict):
                        info = ", ".join(data_details.get(i).keys())
                    else:
                        info = data_details.get(i)
                    print(make_colors(i, 'lightcyan') + " " * (12 - len(i)) + ": " + info)
                                
                import tkimage
                from pywget import wget
                #import download
                from multiprocessing import Process
                
                thumb_url = data.get(int(q[:-1])).get('thumb')
                title = data.get(int(q[:-1])).get('title')
                img_download_path = os.path.join(os.getenv('temp'), os.path.split(thumb_url)[1])
                #download.download_img(thumb_url, os.path.split(thumb_url)[1], os.getenv('temp'))
                wget.download(thumb_url, img_download_path)
                if os.path.isfile(img_download_path):
                    #tkimage.showImages(title, img_download_path)
                    tx = Process(target=tkimage.showImages, args=(title, img_download_path, ))
                    tx.start()                                    
                else:
                    print(make_colors("No Image Found !", 'lightwhite', 'lightred', ['blink']))
                return self.navigator(download_path, saveas, confirm, search, query, word_insert)
        else:
            return self.navigator(download_path, saveas, confirm)
    
    def usage(self):
        parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)
        parser.add_argument('-p', '--download-path', action = 'store', help = 'Download Directory/Save to')
        parser.add_argument('-o', '--saveas', action = 'store', help = 'Save as name')
        parser.add_argument('-s', '--search', action = 'store', help = 'Search')
        parser.add_argument('-c', '--confirm', action = 'store_true', help = 'Confirm before download (IDM Only)')
        parser.add_argument('-m', '--monitor', action = 'store_true', help = 'Service monitor for update')
        parser.add_argument('-ms', '--monitor-sleep', action = 'store', help = 'Service monitor for update timer', type = int, default = 900)
        parser.add_argument('-x', '--proxy', help="Via Proxy, example: https://192.168.0.1:3128 https://192.168.0.1:3128 ftp://127.0.0.1:33 or {'http':'127.0.0.1:8080', 'https': '10.5.6.7:5656'}", action='store', nargs='*')
        if len(sys.argv) == 1:
            parser.print_help()
            #self.navigator()
        #else:
        args = parser.parse_args()
        if args.proxy:
            args.proxy = self.set_proxy(args.proxy)
        debug(args_proxy = args.proxy)
        self.session.proxies = args.proxy
        if args.search:
            self.navigator(args.download_path, args.saveas, args.confirm, True, args.search)
        elif args.monitor:
            self.monitor(args.monitor_sleep)
        else:
            self.navigator(args.download_path, args.saveas, args.confirm)
            
    def monitor(self, sleep = 900):
        self.monitor_run = True
        import notify
        notif = notify.notify(active_pushbullet = False)
        data0, page, last = self.home()
        time.sleep(sleep)
        diff = {}
        n = 1
        try:
            while 1:
                data, page, last = self.home()
                if data0 == data:
                    time.sleep(900)
                else:
                    for i in data.values():
                        if not i in data0.values():
                            diff.update({n: {i},})
                    data0 = data
                    if diff:
                        for i in diff:
                            title = diff.get(i).get('title')
                            notif.nmd("New Update Anime", title)
                    diff = {}           
        except:
            traceback.format_exc()
        
            
    
if __name__ == '__main__':
    c = kiminime()
    c.usage()
    #c.get_root_link("https://kiminime.com/pet-episode-12/")
    #c.get_anime_detail("https://kiminime.com/anime/boruto-naruto-next-generations/")
    #c.home()
    #c.get_download_links("https://kiminime.com/rezero-kara-hajimeru-isekai-seikatsu-shin-henshuu-ban-episode-5/")
    #c.navigator()
    