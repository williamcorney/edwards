from bs4 import BeautifulSoup
import os,requests
import pandas as pd
from tabulate import tabulate
from urllib.parse import urlparse

if  os.path.isfile('index.html') is True: os.remove('index.html')
if  os.path.isfile('cache') is False:
    page = (requests.get ('http://edwards.yale.edu/research/browse'))
    soup = BeautifulSoup(page.text, "html.parser")
    with open("cache", "w") as myfile:
        myfile.write(str(soup))
else:
    with open('cache', 'r') as f: contents = f.read()
    soup = BeautifulSoup(contents, "html.parser")

for links in soup.findAll('a'):

    filename = os.path.basename(links.get('href'))
    dirname   = os.path.dirname(links.get('href'))
    if "archive" in dirname:
        url = dirname
        links['href'] = links['href'].replace (filename, filename + '.html')
        links['href'] = links['href'].replace(dirname + '/', '')


result = soup.select('style, #center ul ')
for items in result:
    with open("index.html", "a") as myfile: myfile.write(str(items))

downloadlist = {}

result2 = soup.select('#center ul ')
for links in result2:
    raw = links.select('a')
    for items in raw:
        key = items.get('href')
        val = 'http://edwards.yale.edu' + url
        key = key.replace('.html', '')
        downloadlist[key] = val

for item,val in downloadlist.items():
    downloadurl =  (val + "/" + item)
    filename =  item + ".html"

    print (downloadurl)
    print (filename)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
df = pd.DataFrame(downloadlist.items())
print(tabulate(df, showindex=False, headers=df.columns))
print ( "There are " + str(len(df)) + " items in this list")

# Launch index page to browser
import webbrowser
webbrowser.open('file:///Users/williamcorney/Edwards/index.html', new=2)