from html.parser import HTMLParser
from bs4 import BeautifulSoup
from html.entities import name2codepoint
from colorama import Fore, Back, Style
import time
with open('cache', 'r') as f: contents = f.read()
soup = BeautifulSoup(contents, "html.parser")

import docx

document = docx.Document()

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        self.flag = '0'

        #attribute = str(attrs[class])

        try:
            test = str(attrs[0])
        except:
            test = ''

        print(Fore.BLACK + Back.GREEN + "Start tag:", tag.upper() + ' ' + str(test))

        print (Fore.WHITE + Back.BLACK)
        for attr in attrs:

            if 'fnote' in attr:
                self.flag = 'fnote'
            if 'head' in attr:
                self.flag = 'head'
            if '1' in attr:
                self.flag = '1'
        if len(tag) < 2 :
            self.flag = 'p'
            self.tag = ''

    def handle_endtag(self, tag):
        print(Fore.RED + "End tag:", tag.upper())

    def handle_data(self, data):

        length = len (data)
        if length > 2:
            print(Fore.LIGHTGREEN_EX + "Data     :", data)
            print (self.flag)
        #if 'head' in self.flag:
         #   print ('blablablablablablablablablablablablablablablablablablablablablablablablablablablablablablablablablablablablablablabla')
         #   document.add_heading(data, 0)
        if 'p' in self.flag:
            print(Fore.LIGHTYELLOW_EX + " Flag was P")
            p = document.add_paragraph(data)
        if 'head' in self.flag:
            document.add_heading(data, 0)

for tag in soup.find_all(attrs={'style': True}):
    del tag['style']

with open("cache", "w") as myfile: myfile.write(str(soup))




with open('cache', 'r') as f: contents = f.read()
soup = BeautifulSoup(contents, "html.parser")
parser = MyHTMLParser()

div_tags = soup.find_all('date')
for item in div_tags: item.unwrap()
div_tags = soup.find_all('daterange')
for item in div_tags: item.unwrap()
div_tags = soup.find_all('quote')
for item in div_tags: item.unwrap()
div_tags = soup.find_all('div')
for item in div_tags: item.unwrap()



div_tags = soup.find_all('span')

for items in div_tags:
    if 'class' not in str(items):
        items.unwrap()


mydivs = soup.find_all("span", {"class": "bibl"})

for items in mydivs:
    items.unwrap()

mydivs = soup.find_all("span", {"class": "reg"})

for items in mydivs:
    items.unwrap()

#print (soup)

#soup = soup.prettify()

parser.feed(str(soup))

with open("test.html", "w") as myfile: myfile.write(str(soup))

#soup = soup.select('.span , .bibl')

document.save('testing.docx')
