#Reddit Video Viewer

import requests, json, os
'''
url = input("Enter the multi url: ")
sort = input("What sort method do you want to use? Enter 1 for hot, 2 for new, 3 for rising, 4 for top, and 5 for gilded: ")

if sort == 1:
    sortMethod = ""
elif sort == 2:
    sortMethod = "new"
elif sort == 3:
    sortMethod = "rising"
elif sort == 4:
    sortMethod = "top"
else:
    sortMethod = "gilded"
'''
'''if url.endswith('/'):
    url = url
else:
    url = url + ".json?sort=top&t=month"'''
url = "https://reddit.com/r/videos+gifs/top.json?sort=top&t=month&limit=100"
data = requests.get(url, headers = {'User-agent': 'Reddit Viewer  Thing'}).json()
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
