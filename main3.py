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




print ('There are ' + str(len(downloadlist)) + ' Volumes')
count = 0
for item,val in downloadlist.items():


    downloadparent =  (val + "/" + item)

    fileparent =  item + ".html"

    if  os.path.isfile(fileparent) is False:
        count = count + 1
        print(count)
        print (fileparent + "does not exist")
        #print ('there are ' + str(len(fileparent)) + " in this list")

        page = requests.get(downloadparent)
        soup = BeautifulSoup(page.text, "html.parser")
        with open(fileparent, "w") as myfile: myfile.write(str(soup))

    with open(fileparent, 'r') as f: contents = f.read()
  
    soup = BeautifulSoup(contents, "html.parser")


    for unwanted in soup ("input"):
        unwanted.decompose()
  
    result = soup.select('style , .navlevel1 , .navlevel2')
    style = soup.select('style')



    #print (result)
    count = 0
    for items in result:
        count = count + 1
        #print (str(items) + 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz' + str(count))
        with open('zzz' + fileparent, "a") as myfile: myfile.write(str(items))

    with open('zzz' + fileparent, 'r') as f: contents = f.read()
    soup = BeautifulSoup(contents, "html.parser")
    print(soup)
        #print (soup)

    os.remove('zzz' + fileparent)

    for links in soup.findAll('a'):


        #print (links)

        filename = os.path.basename(links.get('href'))
        dirname = os.path.dirname(links.get('href'))
        url = dirname
        links['href'] = links['href'].replace(filename, filename + '.html')
        links['href'] = links['href'].replace(dirname + '/', '')

    for items in style:
        with open('zzz' + fileparent, "a") as myfile: myfile.write(str(items))

    for items in soup:



        with open('zzz' + fileparent, "a") as myfile: myfile.write(str(items))
        """
    downloadlist = {}
    result2 = soup
    for links in result2:
        raw = links.select('a')
        for items in raw:
              key = items.get('href')
              val = 'http://edwards.yale.edu/archive' + url
              key = key.replace('.html', '')
              downloadlist[key] = val
  
    for item,val in downloadlist.items():
        downloadurl =  (val + "/" + item)
        filename =  item + ".html"
"""