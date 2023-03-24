from bs4 import BeautifulSoup
import os
import requests
import csv
import time

#page = (requests.get('http://edwards.yale.edu/archive?path=aHR0cDovL2Vkd2FyZHMueWFsZS5lZHUvY2dpLWJpbi9uZXdwaGlsby9nZXRvYmplY3QucGw/Yy4xODo3LndqZW8='))
#soup = BeautifulSoup(page.text, "html.parser")
#soup = soup.select ('#content #text')
#if os.path.isfile('test3') is True: os.remove('test3')
#for items in soup:
 #   with open('test3', "a") as myfile:
  #      myfile.write(str(items))

with open('test3', 'r') as f:
    contents = f.read()
soup = BeautifulSoup(contents, "html.parser")

if os.path.isfile('test4.html') is True: os.remove('test4.html')
for items in soup:
    with open('test4.html', "a") as myfile: myfile.write(str(items))

for unwanted in soup("center"):
    unwanted.decompose()
for unwanted in soup("a"):
    unwanted.decompose()
for unwanted in soup("hr"):
        unwanted.decompose()
if os.path.isfile('test4.html') is True: os.remove('test4.html')
soup= str(soup)

with open('stylefinal', 'r') as f: style = f.read()
with open('test4.html', "w") as myfile: myfile.write(str(style))


for line in soup.splitlines():

        if '</p><p></p>'  in line:
            data =  line.replace('</p><p></p><p>','')
            with open('test4.html', "a") as myfile: myfile.write(str(data))

        if '</p><p></p><p>' not in line:
            data = (line)
            with open('test4.html', "a") as myfile: myfile.write(str(data))

import webbrowser
webbrowser.open('file:///Users/williamcorney/Edwards/test4.html', new=2)
