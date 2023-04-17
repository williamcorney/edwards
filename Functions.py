
from bs4 import BeautifulSoup
import requests,os
import time,csv
import mysql.connector

list = []

#   Function 1
def SoupFILEimport(filename):

    with open(filename, 'r') as f: contents = f.read()
    soup = BeautifulSoup(contents, "lxml")
    return soup
#   Function 2
def SoupALLtags(soup):
    taglist1 = []
    taglist2 = []
    taglist1 = [tag.name for tag in soup.find_all()]
    for tags in taglist1:
       if tags not in taglist2:
           taglist2.append(tags)
    taglist2.reverse()
    return taglist2
#   Function 3
def SoupSPECIFICtag(soup,tag):
    searchresponse = soup.find_all(tag)

    return searchresponse
#   Function 4
def SoupSPANclassTAG(classname):
    searchresponse = (soup.findAll('span', {'class': classname}))
    return searchresponse
#   Function 5
def SoupTAGATTRVAL (soup, tag,attrib,value):
    searchresponse = (soup.findAll(tag, {attrib: value}))
    return searchresponse
#   Function 6
def SoupSelect(soup,tag):
    soup =soup.select(tag)
    return soup
#   Function 7
def DataType(object):

    return
#   Function 8
def SoupFILEnames(soup):
    filename = []
    for items in soup:
      items = items.find('a')
      items = os.path.basename(items.get('href'))
      filename.append(items)
    return filename
#   Function 9
def SoupFILEnameTITLEdict (soup):
    filenametitledict = {}
    for items in soup:
        items = items.find('a')

        filename = os.path.basename(items.get('href'))
        description = items.text
        filenametitledict[filename]=description
    return filenametitledict
#   Function 10
def SoupDECOMPOSEtag (soup,tag):
    for items in soup.find_all(tag): items.decompose()
    return
#Function 11
def SoupDECOMPOSEadv (soup, tag,attrib,value):
    searchresponse = (soup.findAll(tag, {attrib: value}))
    for items in searchresponse:
        items.decompose()
    return soup
def SoupSTRIPattribute (soup,att):
    tag = soup.find(attrs={att: True})
    del tag[att]
    print('Successfully removed ' +  str(att).upper())
    print(str(att) + ' not found in document ')
    return soup
#   Function 12
def SoupUNWRAP ( soup, tag):

    for span_tag in soup.findAll(tag): span_tag.unwrap()
    return soup
def CSVimport (filename):
    filenamelist= []
    with open(filename, mode='r') as infile:
        reader = csv.reader(infile)
        mydict = {rows[0]: rows[1] for rows in reader}
    for key,val in mydict.items():
        filenamelist.append(val)
    return filenamelist


def DecomposeLIST(decomposelist,soup):
    for items in soup:
        for decomps in decomposelist:
            for result in items.findAll(str(decomps)):
                result.decompose()
    return
def UnwrapLIST(unwraplist,soup):
    for items in soup:
        for unwraps in unwraplist:
            for result in items.findAll(str(unwraps)):
                result.unwrap()
    return


# Retired functions
"""

def SoupURLimport(url,usecache):

    if 'http://' not in url:
        if 'https://' not in url:
            url = 'http://' + url
    if usecache =='cached=NO':
        if os.path.isfile('cache') is True:
            os.remove('cache')
        try:
            page = (requests.get(url))
            soup = BeautifulSoup(page.text, "lxml")
            with open("cache", "w") as myfile:
                myfile.write(str(soup))
            return soup
        except:
            print('URL not provided ')
    if usecache =='cached=YES':
        with open('cache', 'r') as f:
            contents = f.read()
        soup = BeautifulSoup(contents, "html.parser")
        return soup
    else:
        print ('You must provide the value cached:yes or cached:no')
    return

"""
