from Functions import *
count=0
volume = '17'
soup = SoupFILEimport('./Volumes/' + volume + '.html')
decomposelist = ['figure','a','b','i','table','hr','front']
unwraplist = ['chapter','date','supplied','ins','del','abbr','u','sup','div','br','dateline']
for tags in decomposelist:
    for items in soup.find_all(tags): items.decompose()
for tags in unwraplist:
    for items in soup.find_all(tags): items.unwrap()
for items in soup.find_all('span','fnote'):
    if len(str(items)) < 40 : items.unwrap()
    for rows in items.find_all('i'): rows.unwrap()
    for rows in items.find_all('p'): rows.unwrap()
R2(soup, 'p', 'rend', 'font-style: italic;', 'i')
R2(soup, 'span', 'style', 'font-style: italic', 'i')
R2(soup, 'hi', 'rend', 'font-style:italic', 'i')
R2(soup, 'span', 'style', 'font-style:italic', 'i')
R2(soup, 'span', 'style', 'font-style: italic;', 'i')
R2(soup, 'span', 'class', 'fnote', 'fnote')
R2(soup, 'span', 'style', 'font-size: small;', 'h1')
R2(soup, 'span', 'style', 'font-size: x-small;', 'h1')
R2(soup, 'span', 'style', 'font-size: xx-small;', 'h1')
R2(soup, 'span', 'class', 'head', 'h1')
R2(soup, 'span', 'class', 'salute', 'p')
U2(soup ,'span', 'style', 'font-variant:small-caps')
U2(soup ,'span', 'style', 'font-variant:small caps')
U2(soup ,'span', 'class', 'item')
U2(soup ,'span', 'class', 'hi')
U2(soup ,'span', 'class', 'emph')
U2(soup ,'span', 'class', 'foreign')
U2(soup ,'span', 'class', 'opener')
U2(soup ,'span', 'class', 'closer')
U2(soup ,'span', 'class', 'reg')
U2(soup ,'span', 'class', 'bibl')
U2(soup ,'span', 'style', 'font-style: normal;')
U2(soup ,'p', 'rend', 'font-style: normal;')

U2(soup ,'span', 'class', 'signed')
U2(soup ,'span', 'style', 'font-weight:bold;')
U2(soup ,'span', 'style', 'text-align:right')
U2(soup ,'span', 'style', 'text-align:left')
U2(soup ,'span', 'style', 'color: #000000;')
U2(soup ,'name', 'type', 'place')
R1(soup,'quote','p')
soup = str(soup).replace('</fnote><fnote>' , '')
soup = str(soup).replace('&lt;/div' , '')

if os.path.isfile('./Volumes/' + volume + '-01.html') is True: os.remove('./Volumes/' + volume + '-01.html')
with open('./Volumes/' + volume + '-01.html', "a") as myfile: myfile.write(str(soup))


# soup = SoupFILEimport('./Volumes/' + volume + '-01' + '.html')
#
# result =  (soup.find_all('fnote'))
# for items in result:
#     count +=1
#     list.append(str(items))
#     list.sort()
#
#
# def sortmylist (list):
#     sortedlist= sorted(list,key=len)
#     return sortedlist
#
# theresult= (sortmylist(list))
#
# for items in theresult:
#     print (items)


