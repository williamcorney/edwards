from html.parser import HTMLParser
import time
import colorama
from colorama import Fore, Back, Style
import csv
from bs4 import BeautifulSoup
from Functions import *
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for items in attrs:

            if items[0] == 'class':
                self.flag = tag + Fore.MAGENTA + ' (' + items[0].upper() + ')' + ' (' + items[1] + ')' + colorama.Style.RESET_ALL
            if items[0] == 'style':
                self.flag = tag + Fore.RED + ' (' + items[0].upper() + ')' + ' (' + items[1] + ')' + colorama.Style.RESET_ALL
        if len(attrs) > 1:
          print(Fore.GREEN + tag + ":", attrs)
    def handle_data(self, data):
        if self.lasttag != '???':
            print (Fore.GREEN + self.flag)
          #  print (Fore.GREEN + self.lasttag.upper())
        if len(data) > 1:
            print(colorama.Style.RESET_ALL  + Fore.BLUE + "DATA:", data.upper())
parser = MyHTMLParser()

with open('allfile-filelist.csv', mode='r') as infile:
    reader = csv.reader(infile)
    mydict = {rows[0]:rows[1] for rows in reader}

path2 = '/Users/williamcorney/PycharmProjects/pythonProject/source/'
tagdict = []
secondphaselinksandfilenames = {}


decomposelist = ['img','table','div-img']
unwraplist = ['div']
classunwraplist =['font-style:italic']
for url,filename in mydict.items():
    # STAGE 0 ---LOAD UP SOUP FILE

    with open(path2 + filename, 'r') as f: contents = f.read()
    soup = BeautifulSoup(contents, "lxml")
    soup = soup.select('#text')
    DecomposeLIST(decomposelist,soup)
    UnwrapLIST(unwraplist,soup)
    SpanCLASSunwrap(classunwraplist,soup)

    parser.feed(str(soup))
    print (soup)

    quit()



