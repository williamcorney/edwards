from bs4 import BeautifulSoup
import os,requests

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
    dirname  = os.path.dirname(links.get('href'))
    links['href'] = links['href'].replace (filename, filename + '.html')
    links['href'] = links['href'].replace(dirname + '/', '')

result = soup.select('style, #center ul ')
for items in result:
    with open("index.html", "a") as myfile: myfile.write(str(items))