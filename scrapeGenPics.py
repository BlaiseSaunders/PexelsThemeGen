PEXELS_API_KEY = '563492ad6f91700001000001c28844238cb4477c888876d50d876565' # Generic API key from tutorial dont roast me fo this 1 i doing u a favor homie

import requests
import json
from pprint import pprint
from requests.structures import CaseInsensitiveDict
from operator import itemgetter
import os
import sys
import subprocess
import requests

query = sys.argv[1]

def getPage(url):
    print("Scraping: "+url)
    headers = CaseInsensitiveDict()
    headers["Authorization"] = PEXELS_API_KEY
    resp = requests.get(url, headers=headers)
    print("Status: "+str(resp.status_code))
    
    return json.loads(resp.text)

url = "https://api.pexels.com/v1/search?query="+query+"&per_page=128"
jason = getPage(url)

while jason['next_page']:
    for pic in jason['photos']:
        if float(pic['width']) > 1920 and float(pic['height']) > 1080:
            url = pic['src']['original']
            print("Getting: "+url)
            img_data = requests.get(url).content
            with open(str(pic['id'])+'.jpg', 'wb') as handler:
                handler.write(img_data)
    jason = getPage(jason['next_page'])
        

"""
stream = os.popen("./combine.sh "+query)
output = stream.read()
"""
