from PyQt5.QtWidgets import *
import sys
from Functions import *

soup = SoupFILEimport('/Users/williamcorney/PycharmProjects/pythonProject/source/Yy4wOjI6NS53amVv.html')



class Window(QWidget):
    global soup


    def __init__(self):
        global soup
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setWindowTitle('BeautifulSoup')
        self.setLayout(layout)
        self.setMinimumSize(1000,200)

        self.listwidget = QListWidget()
        self.listwidget.clicked.connect(self.listclicked)

        tags = SoupALLtags(soup)
        for items in tags: self.listwidget.insertItem(0,str(items))
        tags = ['']
        self.textedit = QTextEdit()
        self.textedit.setText(str(soup))
        self.label = QLabel()
        self.label.text()
        self.label.setText('Tags found:')
        self.button1 = QPushButton()
        self.button1.setText('Purge Tag')
        self.button1.clicked.connect(self.button1clicked)
        self.button2 = QPushButton()
        self.button2.setText('Reset')



        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.label)
        layout.addWidget(self.listwidget)
        layout.addWidget(self.textedit)

    def listclicked(self, qmodelindex):
        global item
        global soup
        print (soup)


        item = self.listwidget.currentItem()
        filter = SoupSPECIFICtag(soup,item.text())
        print(type(soup))
        self.textedit.setPlainText((str(filter)))






    def button1clicked(self, qmodelindex):
        global soup

        search = (item.text())
        print(type(soup))
        soup = SoupDECOMPOSEtag(soup,search)
        tags = SoupALLtags(soup)
        print(type(soup))
        print (tags)
        self.listwidget.clear()
        for items in tags: self.listwidget.insertItem(0, str(items))
        self.textedit.setPlainText(str(soup))

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())