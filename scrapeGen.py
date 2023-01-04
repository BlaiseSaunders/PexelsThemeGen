PEXELS_API_KEY = '563492ad6f91700001000001c28844238cb4477c888876d50d876565' # Generic API key from tutorial dont roast me fo this 1 i doing u a favor homie

import requests
import json
from pprint import pprint
from requests.structures import CaseInsensitiveDict
from operator import itemgetter
import os
import sys
import subprocess

query = sys.argv[1]


url = "https://api.pexels.com/videos/search?query="+query+"&per_page=60"
print("Scraping: "+url)

headers = CaseInsensitiveDict()
headers["Authorization"] = PEXELS_API_KEY


resp = requests.get(url, headers=headers)

#print(resp.text)


print("Status: "+str(resp.status_code))
jason = json.loads(resp.text)['videos']
for vid in jason:
    clean_vids = []
    for fi in vid['video_files']:
        if fi['width'] is not None:   
            aspect = float(fi['width'])/float(fi['height'])
            print("Aspect: "+str(aspect))
            if aspect > 1.7 and aspect < 1.8:
                clean_vids.append(fi)
    if len(clean_vids) == 0:
        continue 
    sortedv = sorted(clean_vids, key=itemgetter('width'))  
    vidurl = sortedv[-1]['link']
    print("Getting: "+vidurl)
    stream = os.popen("yt-dlp -c "+vidurl)
    output = stream.read()

stream = os.popen("./combine.sh "+query)
output = stream.read()                                                                                                                                                                                                                      
