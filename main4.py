from bs4 import BeautifulSoup
import os, requests
import pandas as pd
from tabulate import tabulate
from urllib.parse import urlparse
import time


if os.path.isfile('index.html') is True: os.remove('index.html')
if os.path.isfile('cache') is False:
    page = (requests.get('http://edwards.yale.edu/research/browse'))
    soup = BeautifulSoup(page.text, "html.parser")
    with open("cache", "w") as myfile:
        myfile.write(str(soup))
else:
    with open('cache', 'r') as f:
        contents = f.read()
    soup = BeautifulSoup(contents, "html.parser")

for links in soup.findAll('a'):

    filename = os.path.basename(links.get('href'))
    dirname = os.path.dirname(links.get('href'))
    if "archive" in dirname:
        url = dirname
        links['href'] = links['href'].replace(filename, filename + '.html')
        links['href'] = links['href'].replace(dirname + '/', '')

result = soup.select('style, #center ul ')
for items in result:
    with open("index.html", "a") as myfile: myfile.write(str(items))

downloadlist = {}

result2 = soup.select('#center ul ')
for links in result2:
    raw = links.select('a')
    for items in raw:
        nameoffile = items.get('href')
        urloffile = 'http://edwards.yale.edu' + url
        nameoffile = nameoffile.replace('.html', '')
        downloadlist[nameoffile] = urloffile

print (str(len(raw)) + ' links were processed ')
print (str(len(downloadlist)) + ' links added to downloadlist dictionary')





for nameoffile, urloffile in downloadlist.items():

    fulllinkurl = (urloffile + "/" + nameoffile)
    fullfilename = nameoffile + ".html"
    if os.path.isfile(fullfilename) is False:
        page = requests.get(fulllinkurl)
        soup = BeautifulSoup(page.text, "html.parser")
        with open(fullfilename, "w") as myfile: myfile.write(str(soup))

for nameoffile, urloffile in downloadlist.items():
    fulllinkurl = (urloffile + "/" + nameoffile)
    fullfilename = nameoffile + ".html"
    with open(fullfilename, 'r') as f:
        contents = f.read()

    soup = BeautifulSoup(contents, "html.parser")
    for unwanted in soup("input"):
        unwanted.decompose()

    result = soup.select(' .navlevel1 , .navlevel2')
    if os.path.isfile(fullfilename + '.tmp') is False:
        for items in result:
            with open(fullfilename + '.tmp', "a") as myfile: myfile.write(str(items))



    with open(fullfilename + '.tmp', 'r') as f:
        contents = f.read()
    soup = BeautifulSoup(contents, "html.parser")

    for links in soup.findAll('a'):

        filename = os.path.basename(links.get('href'))
        dirname = os.path.dirname(links.get('href'))

        url = dirname
        links['href'] = links['href'].replace(filename, filename + '.html')
        links['href'] = links['href'].replace(dirname + '/', '')




        with open('stylefile', 'r') as f:
            contents = f.read()
            #print (contents)
        print ('arrived')
        os.remove(fullfilename)
        if os.path.isfile(fullfilename + '.tmp') is True:
            os.remove(fullfilename + '.tmp')
        with open(fullfilename, "w") as myfile:
            myfile.write(str(contents))

        for items in soup:
            with open(fullfilename, "a") as myfile: myfile.write(str(items))


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