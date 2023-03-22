from bs4 import BeautifulSoup
import requests,os

if  os.path.isfile('index2.html') is True: os.remove('index2.html')
if  os.path.isfile('cache2') is False:
  url = 'http://edwards.yale.edu/archive?path=aHR0cDovL2Vkd2FyZHMueWFsZS5lZHUvY2dpLWJpbi9uZXdwaGlsby9zZWxlY3QucGw/d2plby4w'
  page = requests.get(url)
  soup = BeautifulSoup(page.text, "html.parser")
  with open("cache2", "w") as myfile: myfile.write(str(soup))

with open('cache2', 'r') as f:
    contents = f.read()




  #  filename = os.path.basename(links.get('href'))

    #if "path" in links:
   # print (links)

    #filename = os.path.basename(links.get('href'))
    #dirname   = os.path.dirname(links.get('href'))
    #if "archive" in dirname:
     #   url = dirname
      #  links['href'] = links['href'].replace (filename, filename + '.html')
       # links['href'] = links['href'].replace(dirname + '/', '')

soup = BeautifulSoup(contents, "html.parser")
for unwanted in soup ("input"):
  unwanted.decompose()


result = soup.select('style .navlevel1 , .navlevel2, .navlevel3 ')
for items in result:
    with open("index2.html", "a") as myfile: myfile.write(str(items))

with open('index2.html', 'r') as f: contents = f.read()
soup = BeautifulSoup(contents, "html.parser")




for links in soup.findAll('a'):
    filename = os.path.basename(links.get('href'))
    dirname = os.path.dirname(links.get('href'))
    print (dirname)

    #links['href'] = links['href'].replace(filename, filename + '.html')
    #links['href'] = links['href'].replace(dirname + '/', '')




#import webbrowser
#webbrowser.open('file:///Users/williamcorney/Edwards/index2.html', new=2)

"""


import pandas as pd
from tabulate import tabulate
from urllib.parse import urlparse

#   GRAB URL TO SOUP
#url = 'http://edwards.yale.edu/archive?path=aHR0cDovL2Vkd2FyZHMueWFsZS5lZHUvY2dpLWJpbi9uZXdwaGlsby9zZWxlY3QucGw/d2plby4w'
#page = requests.get(url)
#soup = BeautifulSoup(page.text, "html.parser")
#   WRITE SOUP TO FILE
#with open("/Users/williamcorney/Edwards/Volumes/d2plby4w.html", "w") as file:
#  file.write(str(soup))
#   READ SOUP FROM FILE
with open('/Users/williamcorney/Edwards/Volumes/d2plby45.html', 'r') as f:
  contents = f.read()
  soup = BeautifulSoup(contents, 'html.parser')
  query = soup.select('#content .navlevel1 [href]')
  #print(query)
sectiondict ={}

for items in query:
  item1 = items.get("href")
  item2 = items.contents

  # CODE TO GET FILENAME
  item3 = os.path.basename(item1)
  print (item3)

  sectiondict[item1]=item2


#print (type (item1))

pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
df = pd.DataFrame(sectiondict.items())


#print(tabulate(df, showindex=False, headers=df.columns))
#print ( "There are " + str(len(df)) + " items in this list")




#print (type(sectiondict))


#print (sectiondict)


query = soup.select('#content','.navlevel2','[href]')
#print(len(dict))


for key, val in sectiondict.items():
  print (key)
   # print (str(len (key))+ " " + key )
  #  print (val)
 #   #print (val)
    #print (len(val))
    #result = requests.get(val)
    #soup = BeautifulSoup(result.text, "html.parser")
    #with open("/Users/williamcorney/Edwards/1-Freedom of the Will (WJE Online Vol. 1)/" + key + ".html", "w") as file:
     #3   file.write(str(soup))
   # print (os.path.basename(val)) # CODE TO GET FILENAME

"""