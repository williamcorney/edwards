from bs4 import BeautifulSoup
from html.parser import HTMLParser
import docx, os



# STAGE 0 ---LOAD UP SOUP FILE
with open('sermon.html', 'r') as f: contents = f.read()
soup = BeautifulSoup(contents, "lxml")
# STAGE 0 ---CLASS SECTION

from colorama import Fore, Back, Style
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if len (attrs) == 0 :
           #print(Fore.LIGHTGREEN_EX + 'start of ' + tag)
            self.flag = tag
        else:
            for item in attrs:
                #print (Fore.LIGHTGREEN_EX + tag + ' (' + item[1] + ')')
                self.flag = tag + '-' + item[1]

        #for item in attrs:
            #print ( tag  + item[1] + 'ZZZZZZ' )
        tag = ''

        #for item in attrs:
           # if item[1]

    #def handle_endtag(self, tag):
        #print (Fore.RED + 'end of ' + tag )
    def handle_data(self, data):
        print (Fore.LIGHTGREEN_EX + self.flag)
        print (Fore.LIGHTBLUE_EX + data )

# ******** TRANSFORMATIONS********

# STAGE 1 ---ENTIRELY REMOVE A TAG

decomposetags= ['img','table']
if decomposetags != '':
    for tags in decomposetags:
        NumberofOcurrences = len(soup.find_all(tags))
        if NumberofOcurrences == 1: soup.find(tags).decompose()
        if NumberofOcurrences > 1:
            for items in soup.find_all(tags):
                items.decompose()


# STAGE 2 --- UNWRAP TAGS BY TAG

tagunwrap = ['cit','seg','figure','div']

if len (tagunwrap) == 1 :
    for span_tag in soup.findAll(tagunwrap): span_tag.unwrap()
if len (tagunwrap) > 1 :
    for items in tagunwrap:
        for span_tag in soup.findAll(items): span_tag.unwrap()

# STAGE 3 ---UNWRAP SPAN TAGS BY CLASS

classnames = ['reg']
if len (classnames) == 1 :
    for span_tag in soup.findAll('span', {'class': classnames}): span_tag.unwrap()
if len (classnames) > 1 :
    for items in classnames:
        for span_tag in soup.findAll('span', {'class': items}): span_tag.unwrap()


# STAGE 4 - REMOVE ATTRIBUTES FROM CLASS TAG BY NAME OF CLASS TAG AND ATTRIBUTE NAME

thenameofclass ='.fnote'
attrofclass = 'id'

for items in soup.select(thenameofclass):
    if attrofclass in (items.attrs): items.attrs.pop(attrofclass)


#print (soup.prettify())

# STAGE 5 - SEARCH FOR TAGS BY TAG NAME
taglist = [tag.name for tag in soup.find_all()]
list = []
for items in taglist:
    if items not in list:
        list.append(items)
print (list)

#STAGE 6 - SEARCH FOR SPAN TAGS BY  CLASSNAME

searchterm = ['']

searchresponse= (soup.findAll('span', {'class':searchterm}))

for items in searchresponse: print (items)

#STAGE 7 - SEARCH FOR SPECIFIC TAG

tagquery=['']
for items in soup.find_all(tagquery): print (items)
#searchterm = 'span'
#for items in soup.find_all(searchterm): print (items)

# STAGE 8 ---CREATE DOCX OBJECT
if os.path.isfile('testing.docx') is True: os.remove('testing.docx')
document = docx.Document()
MyHTMLParser().feed(str(soup))
document.save('testing.docx')


if os.path.isfile('test.html') is True: os.remove('test.html')
for items in soup:
            with open('test.html', "a") as myfile: myfile.write(str(items))
















"""
# ---UNWRAP TAGS


unwantedtags=['body','html','daterange','date','div','figure']
for tags in unwantedtags:
    target = soup.find_all(tags)
    
    
    for items in target: items.unwrap()

for span_tag in soup.findAll('seg', {'type':'tei wrapper'}): span_tag.unwrap()
for span_tag in soup.findAll('span', {'class':'reg'}): span_tag.unwrap()
for tag in soup.findAll('span', {'class':''}): tag.unwrap()
for items in soup.select('.fnote'):
    if 'id' in (items.attrs): items.attrs.pop('id')



# STAGE 2---REMOVE TAGS - VERSION 2 created accidently

decomposelist= ''
if len (decomposelist) == 1 :
    for tag in decomposelist: soup.find(tag).decompose()
if len (decomposelist) > 1 :
    for tags in decomposelist:
        items = soup.find_all(tags)
        for item in items: item.decompose()



"""

print (soup)
