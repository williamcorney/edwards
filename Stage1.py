from bs4 import BeautifulSoup
import os, requests
import time
count = 0
########################################################################################################################
########################################################################################################################
#First phase where we grab the top level table of contents of all volumes, the hyperlink TO each file and the name of the file
########################################################################################################################
########################################################################################################################


# 1 If the 'final' index exists remove it - this is so can re-run script if make changes
if os.path.isfile('./temp/index.html') is True: os.remove('./temp/index.html')
# 2 If working cache index  doesnt exist then create it
if os.path.isfile('./temp/cache') is False:
    print ('main index cache file doesnt exist so grabbing it')
    page = (requests.get('http://edwards.yale.edu/research/browse'))
    soup = BeautifulSoup(page.text, "html.parser")
    with open("./temp/cache", "w") as myfile:
        myfile.write(str(soup))
# 3 Otherwise if it does exist lets process it through soup
else:
    print ('main index cache file was found so using' )
    with open('./temp/cache', 'r') as f:
        contents = f.read()
    soup = BeautifulSoup(contents, "html.parser")
# 4 Obtain all the A HREF links from the index and populate filename /dirname

for links in soup.findAll('a'):

    filename = os.path.basename(links.get('href'))
    pathname = os.path.dirname(links.get('href'))
#5  Figure out the base url,  update index links to append html and strip base url.
    #this also filters out the urls we dont want from all the hyperlinks found on page
    if "archive" in pathname:
        basepath = pathname
        count = count + 1
        print ('Renaming link ' + str(count))
        links['href'] = links['href'].replace(filename, filename + ".html")
        links['href'] = links['href'].replace(pathname + '/', '')

#6  Remove the 'final' index file if it exists before outputing soup to index
if os.path.isfile('./temp/index.html') is True:
    os.remove('./temp/index.html')

##
result = soup.select('style, #center ul ')
for items in result:
    with open("./temp/index.html", "a") as myfile: myfile.write(str(items))

print ('Finished creating index.html file')

#7  Determine all the urls, filenames  for next part of downloading and output to a dictionary called secondphaselinksandfilenames
   # The select statement homes in on the elements we want from the raw html

secondphaselinksandfilenames = {}
selectquery1 = soup.select('#center ul ')
count = 0
for link in selectquery1:

    raw = link.select('a')
    for item in raw:


        fullfilename =  (item.get('href'))
        nameoffile = fullfilename
        nameoffile = nameoffile.replace('.html', '')
        fullurl = 'http://edwards.yale.edu' + basepath + '/' + nameoffile

        #print (fullfilename)
        #print (fullurl)


        secondphaselinksandfilenames[fullurl] = fullfilename


for key,val in secondphaselinksandfilenames.items():
    print (key)
    print (val)

import csv


with open('stage1.csv', 'w') as f:
    for key in secondphaselinksandfilenames.keys():
        f.write("%s,%s\n" % (key, secondphaselinksandfilenames[key]))
