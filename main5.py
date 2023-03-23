from bs4 import BeautifulSoup
import os, requests
import pandas as pd
from tabulate import tabulate
from urllib.parse import urlparse
import time
# START OF LEVEL 1

if os.path.isfile('./temp/index.html') is True: os.remove('./temp/index.html')
if os.path.isfile('./temp/cache') is False:
    page = (requests.get('http://edwards.yale.edu/research/browse'))
    soup = BeautifulSoup(page.text, "html.parser")
    with open("./temp/cache", "w") as myfile:
        myfile.write(str(soup))
else:
    with open('./temp/cache', 'r') as f:
        contents = f.read()
    soup = BeautifulSoup(contents, "html.parser")


# LEVEL 1 - FIXING LINKS IN INDEX FILE
for links in soup.findAll('a'):

    filename = os.path.basename(links.get('href'))
    dirname = os.path.dirname(links.get('href'))
    if "archive" in dirname:
        url = dirname
        links['href'] = links['href'].replace(filename, filename + '.html')
        links['href'] = links['href'].replace(dirname + '/', '')

result = soup.select('style, #center ul ')
for items in result:
    with open("./temp/index.html", "a") as myfile: myfile.write(str(items))

downloadlist = {}

result2 = soup.select('#center ul ')

for links in result2:

    raw = links.select('a')
    for items in raw:
        nameoffile = items.get('href')
        urloffile = 'http://edwards.yale.edu' + url
        nameoffile = nameoffile.replace('.html', '')
        downloadlist[nameoffile] = urloffile







for nameoffile, urloffile in downloadlist.items():

    fulllinkurl = (urloffile + "/" + nameoffile)
    fullfilename = nameoffile + ".html"
    if os.path.isfile('./temp/' + fullfilename) is False:
        page = requests.get(fulllinkurl)
        soup = BeautifulSoup(page.text, "html.parser")
        with open('./temp/' + fullfilename, "w") as myfile: myfile.write(str(soup))

for nameoffile, urloffile in downloadlist.items():

    fulllinkurl = (urloffile + "/" + nameoffile)
    fullfilename = nameoffile + ".html"
    with open('./temp/' + fullfilename, 'r') as f:
        contents = f.read()

    soup = BeautifulSoup(contents, "html.parser")
    for unwanted in soup("input"):
        unwanted.decompose()
    count = 0
    result = soup.select(' .navlevel1 , .navlevel2, .navlevel3')

    # this loop has been checked as appropriate  as its updating many items to the tmp file

    if os.path.isfile('./temp/' + fullfilename + '.tmp') is False:

        for items in result:

            with open('./temp/' + fullfilename + '.tmp', "a") as myfile: myfile.write(str(items))



    with open('./temp/' + fullfilename + '.tmp', 'r') as f:
        contents = f.read()
    soup = BeautifulSoup(contents, "html.parser")
    count =0
    for links in soup.findAll('a'):
        count = count + 1
        print('Loop number is ' + str(count))
        filename = os.path.basename(links.get('href'))
        dirname = os.path.dirname(links.get('href'))

        url = dirname

        if '.html' not in filename:
            links['href'] = links['href'].replace(filename, filename + '.html')
            links['href'] = links['href'].replace(dirname + '/', '')




    with open('./temp/stylefile', 'r') as f:
        contents = f.read()
            #print (contents)
        #print ('arrived')
    os.remove('./temp/' + fullfilename)
    if os.path.isfile('./temp/' + fullfilename + '.tmp') is True:
        os.remove('./temp/' + fullfilename + '.tmp')
    with open('./temp/' + fullfilename, "w") as myfile:
        myfile.write(str(contents))

    for items in soup:
        with open('./temp/' + fullfilename, "a") as myfile: myfile.write(str(items))


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