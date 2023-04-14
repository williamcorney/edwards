from PyQt5.QtWidgets import *
import sys
from Functions import *

soup = SoupFILEimport('/Users/williamcorney/PycharmProjects/pythonProject/source/Yy4wOjI6NS53amVv.html')


#.
class Window(QWidget):
    global soup


    def __init__(self):
        global soup
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setWindowTitle('BeautifulSoup')
        self.setLayout(layout)
        self.setMinimumSize(100,200)

        self.listwidget = QListWidget()
        self.listwidget.itemSelectionChanged.connect(self.listchanged)
        self.listwidget.clicked.connect(self.listclicked)
        self.listwidget.setMaximumWidth(100)

        tags = SoupALLtags(soup)
        for items in tags: self.listwidget.insertItem(0,str(items))
        tags = ['']
        self.textedit = QTextEdit()
        self.textedit.setText(str(soup))
        self.textedit
        self.label = QLabel()
        self.label.text()
        self.label.setText('Tags found:')
        self.button1 = QPushButton()
        self.button1.setText('Purge Tag')
        self.button1.setMaximumWidth(100)
        self.button1.clicked.connect(self.button1clicked)
        self.button2 = QPushButton()
        self.button2.setText('Unwrap Tag')
        self.button2.setMaximumWidth(100)
        self.button2.clicked.connect(self.button2clicked)
        self.button3 = QPushButton()
        self.button3.setText('Next')
        self.button3.setMaximumWidth(100)
        self.button3.clicked.connect(self.button3clicked)
        self.button4 = QPushButton()
        self.button4.setText('.')
        self.button4.setMaximumWidth(100)
        self.button4.clicked.connect(self.button4clicked)


        layout.addWidget(self.button1,0,0)
        layout.addWidget(self.button2,0,1)
        layout.addWidget(self.button3,0,2)
        layout.addWidget(self.button4,0,3)
        layout.addWidget(self.label,1,0)
        layout.addWidget(self.listwidget,2,0)
        layout.addWidget(self.textedit,2,1,1,3)


    def listclicked(self, qmodelindex):
        global item
        global soup
        print (soup)


        item = self.listwidget.currentItem()
        #filter = SoupSPECIFICtag(soup,item.text())
        print (type(filter))
        #for x in filter:
         #   self.textedit.insertPlainText(str(x))
        #self.textedit.setPlainText((str(filter)))

    def listchanged (self,):
        global item
        global soup
        item = self.listwidget.currentItem()
        filter = SoupSPECIFICtag(soup, item.text())
        print(type(soup))
        #self.listwidget.clear()
        self.textedit.clear()
        for x in filter:
            self.textedit.insertPlainText(str(x))


    def button1clicked(self, qmodelindex):
        global soup

        search = (item.text())
        print(type(soup))
        soup = SoupDECOMPOSEtag(soup,search)
        tags = SoupALLtags(soup)
        print(type(soup))
        print (tags)
        self.listwidget.clear()
        self.textedit.clear()
        for items in tags: self.listwidget.insertItem(0, str(items))
        self.textedit.setPlainText(str(soup))

    def button2clicked(self, qmodelindex):
        global soup

        search = (item.text())
        soup = SoupUNWRAP(soup, search)
        tags = SoupALLtags(soup)
        print(type(soup))
        print(tags)
        self.listwidget.clear()
        self.textedit.clear()
        for items in tags: self.listwidget.insertItem(0, str(items))
        self.textedit.setPlainText(str(soup))
    def button3clicked(self, qmodelindex):

        print ('Button 3 was clicked')



    def button4clicked(self, qmodelindex):
        global soup

        print ('Button 4 was clicked')

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())