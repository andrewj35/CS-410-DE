# need these
import json

import requests
import time

url = 'http://rbi.ddns.net/getBreadCrumbData'
response = requests.get(url)

with open('bcfullsample.json', 'w') as fw:
    fw.write(response.text)

i = 0 
with open('bcfullsample.json') as f:
    with open('bcsample.json', 'w') as fw:
        for line in f:
            if i <= 16000:
                fw.write(line)
                i = i + 1
            else:
                break
        fw.write('}')

