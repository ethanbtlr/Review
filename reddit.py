# Reddit Video Viewer

import requests, json, os

url = "https://reddit.com/r/videos+gifs/top.json?sort=top&t=month&limit=100"
data = requests.get(url, headers = {'User-agent': 'Reddit Viewer'}).json()
file = open('list.m3u', 'w')
file.write('#EXTM3U\n')
pageLength = len(data['data']['children'])
dir_path = os.path.dirname(os.path.realpath(__file__))

for i in range(0,80):
    print(i)
    pageUrl = data['data']['children'][i]['data']['url']
    print(pageUrl)
    if (pageUrl.endswith('mp4')):
        file.write(pageUrl + "\n")
    elif (pageUrl.endswith('gif')):
            file.write(pageUrl.replace("gif", "mp4") + "\n")
    elif (pageUrl.endswith('gifv')):
            file.write(pageUrl.replace("gifv", "mp4") + "\n")
    elif ("gfycat.com" in pageUrl):
        gfyId = pageUrl.rsplit('/', 1)[-1]
        gfycatUrl = "https://gfycat.com/cajax/get/" + gfyId
        try: 
            gfyData = requests.get(gfycatUrl, headers = {'User-agent': 'Link Scraper'}).json()
            mp4Link = gfyData['gfyItem']['mp4Url']
            file.write(mp4Link + "\n")
        except:
            print("This gfycat was deleted. Sorry about that.")
    

file.close()                
