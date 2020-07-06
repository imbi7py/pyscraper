import requests
from bs4 import BeautifulSoup
import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pdfkit
from PyQt5 import QtCore,QtGui

config = pdfkit.configuration(wkhtmltopdf='wkhtmltopdf.exe')
#trial
pdfkit.from_url("https://www.google.co.in/","demo.pdf",configuration=config)
#call venv/scripts/activate.bat  #call this before running the file
#backend
class pyscraper(object):
    def __init__(self):
        #initialization
        self.url = None
        self.search = None
        self.btn = None
        self.file_loc = "./saved/"
        self.file_name = "def"

    def print_it(self):
        print(self.url)
        print(self.search)



if __name__ == "__main__":
    obj = pyscraper()

    def data_transfer():
        obj.url = url.text()
        obj.search = search.text()
        obj.btn = btn.text()
        obj.print_it()

#frontend
app = QApplication(sys.argv)
window = QWidget()

title = 'PyScraper'
window.setWindowTitle(title)
window.setWindowIcon(QtGui.QIcon("logo.png"))
style = """
QWidget{
background : #262D37;
}
QLabel{
color: #fff;
}
QPushButton{
color:#fff;
background:#1b03a3;
width:100px;
}

QLineEdit{
color:#fff;
width: 300px;
border: 1px solid #fff;
border-radius: 8px;
padding: 5px;
}
"""
app.setStyleSheet(style)
layout = QVBoxLayout()

# url = QLabel(window)
# url.setText("URL")
# label.move(50,50)

url_label = QLabel("Base URL")
search_label = QLabel("Search by")
btn_label = QLabel("Next Button Text")
file_loc_label = QLabel("File Loc")
file_name_label = QLabel("File Name")

url = QLineEdit()
search = QLineEdit()
btn = QLineEdit()
file_loc = QLineEdit() #file location
file_name = QLineEdit()
submit = QPushButton("Submit")
submit.clicked.connect(data_transfer)


layout.addWidget(url_label)
layout.addWidget(url)
layout.addWidget(search_label)
layout.addWidget(search)
layout.addWidget(btn_label)
layout.addWidget(btn)
layout.addWidget(file_loc_label)
layout.addWidget(file_loc)
layout.addWidget(file_name_label)
layout.addWidget(file_name)
layout.addWidget(submit)


#app initialization
window.setLayout(layout)
window.setFixedSize(500,500)
window.show()
sys.exit(app.exec_())
