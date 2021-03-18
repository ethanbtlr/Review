# Reddit Video Viewer

from __future__ import unicode_literals
import requests, json, os
from bs4 import BeautifulSoup
import youtube_dl
data = requests.get(url, headers = {'User-agent': 'Reddit Viewer'}).json()
file = open('list.m3u', 'w')
file.write('#EXTM3U\n')
pageLength = len(data['data']['children'])
dir_path = os.path.dirname(os.path.realpath(__file__))

for i in range(0,100):
    print(i)
    pageUrl = data['data']['children'][i]['data']['url']
    if (pageUrl.endswith('mp4')):
        file.write(pageUrl + "\n")
        print("mp4: " + pageUrl)
    elif (pageUrl.endswith('gif')):
        file.write(pageUrl + "\n")
        print("gif: " + pageUrl)
    elif (pageUrl.endswith('gifv')):
        file.write(pageUrl + "\n")
        print("gifv: " + pageUrl)
    elif (pageUrl.endswith('jpg')):
        file.write(pageUrl + "\n")
        print("jpg: " + pageUrl)
    elif (pageUrl.endswith('jpeg')):
        file.write(pageUrl + "\n")
        print("jpeg: " + pageUrl)
    elif (pageUrl.endswith('png')):
        file.write(pageUrl + "\n")
        print("png: " + pageUrl)
    elif ("deliverynetwork" in pageUrl):
        try: 
            page = requests.get(pageUrl)
            soup = BeautifulSoup(page.content, 'html.parser')
            sourceURL = soup.find(id="webmSource")['src']
            print("gfycat: " + sourceURL)

            file.write(sourceURL + "\n")
        except:
            print(pageUrl)
            print("This gfycat was deleted. Sorry about that.")
    elif ("gfycat" in pageUrl):
        try: 
            page = requests.get(pageUrl)
            soup = BeautifulSoup(page.content, 'html.parser')
            sourceURL = soup.find(type="video/webm")['src']
            print("gfycat: " + sourceURL)

            file.write(sourceURL + "\n")
        except:
            print(pageUrl)
            print("This gfycat was deleted. Sorry about that.")
    elif ("v.redd.it" in pageUrl):
        try:
            ydl_opts = {"skip_download": True , no-check-certifcate: True}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                redditUrl = info_dict = ydl.extract_info(pageUrl)['url']   
                print(redditUrl)
                
                file.write(redditUrl + "\n")
        except:
            print(pageUrl)
            print("Error parsing the reddit video")
    else:
        print("missed control flow" + pageUrl)

file.close()                    
