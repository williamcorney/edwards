from bs4 import BeautifulSoup
import os
import requests
import csv
import time

with open('Stage2.csv', mode='r') as infile:
    reader = csv.reader(infile)
    mydict = {rows[0]: rows[1] for rows in reader}

secondphaselinksandfilenames = {}
for url, filename in mydict.items():
    print(url)
    page = (requests.get(url))
    soup = BeautifulSoup(page.text, "html.parser")
    soup = soup.select ('#content #text')
    if os.path.isfile(filename) is True: os.remove(filename)
    for items in soup:
        with open(filename, "a") as myfile: myfile.write(str(items))
    with open(filename, 'r') as f: contents = f.read()
    soup = BeautifulSoup(contents, "html.parser")
    if os.path.isfile(filename) is True: os.remove(filename)
    for items in soup:
        with open(filename, "a") as myfile: myfile.write(str(items))

    for unwanted in soup("center"):
        unwanted.decompose()
    for unwanted in soup("a"):
        unwanted.decompose()
    for unwanted in soup("hr"):
        unwanted.decompose()
    if os.path.isfile(filename) is True: os.remove(filename)
    soup = str(soup)

    with open('stylefinal', 'r') as f: style = f.read()
    with open(filename, "w") as myfile: myfile.write(str(style))

    for line in soup.splitlines():

        if '</p><p></p>' in line:
            data = line.replace('</p><p></p><p>', '')
            with open(filename, "a") as myfile: myfile.write(str(data))
        if '</p><p></p><p>' not in line:
            data = (line)
            with open(filename, "a") as myfile: myfile.write(str(data))

time.sleep(15)

import webbrowser

webbrowser.open('file:///Users/williamcorney/Edwards/' + filename, new=2)
