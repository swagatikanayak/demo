import re

import requests as requests

url = input("Enter the URL: ")

html = requests.get(url).text

links = re.findall('"(https?://.*?)"', html)

for link in links:
    print(link)