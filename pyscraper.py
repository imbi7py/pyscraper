import requests
from bs4 import BeautifulSoup
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5 import QtCore,QtGui

#backend





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
save_label = QLabel("Save Loc")

url = QLineEdit()
search = QLineEdit()
btn = QLineEdit()
save = QLineEdit()
submit = QPushButton("Submit")


layout.addWidget(url_label)
layout.addWidget(url)
layout.addWidget(search_label)
layout.addWidget(search)
layout.addWidget(btn_label)
layout.addWidget(btn)
layout.addWidget(save_label)
layout.addWidget(save)
layout.addWidget(submit)


#app initialization
window.setLayout(layout)
window.setFixedSize(500,500)
window.show()
sys.exit(app.exec_())
