from bs4 import BeautifulSoup
import os
import requests
import csv
import time
with open('Stage1.csv', mode='r') as infile:
    reader = csv.reader(infile)
    mydict = {rows[0]:rows[1] for rows in reader}

#

secondphaselinksandfilenames = {}
for url,filename in mydict.items():

    if os.path.isfile(filename) is False:

        page = (requests.get(url))
        soup = BeautifulSoup(page.text, "html.parser")

        with open(filename, "w") as myfile:
            myfile.write(str(soup))
    with open(filename,'r') as f:
        contents = f.read()

    soup = BeautifulSoup(contents, "html.parser")
    for unwanted in soup("input"):
        unwanted.decompose()
    soup = soup.select('.navlevel1, .navlevel2')
    if os.path.isfile(filename) is False:
        os.remove(filename)
        for items in soup:
            with open(filename, "a") as myfile: myfile.write(str(items))

    for links in soup:
        test =  (links.find('a').attrs)
        filename = (os.path.basename(test.get('href')))
        path = ((os.path.dirname(test.get('href'))))
        fullurl = 'http://edwards.yale.edu/archive' + path + '/' + filename
        fullfilename = filename + '.html'
        secondphaselinksandfilenames[fullurl] = fullfilename

for key,val in secondphaselinksandfilenames.items():
    print (key)
    print (val)

import csv


with open('stage2.csv', 'w') as f:
    for key in secondphaselinksandfilenames.keys():
        f.write("%s,%s\n" % (key, secondphaselinksandfilenames[key]))




