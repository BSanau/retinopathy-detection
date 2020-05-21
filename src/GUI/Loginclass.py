from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QGridLayout, QPushButton

class Login(QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Login')
        self.x, self.y = 500, 150
        self.width, self.height = 300, 500#200
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('images/icon.png'))

        self.setStyleSheet(
            "color: white;" # letters color
            #"background-image: url(inkscape/login.png);"
            "background-color: rgb(4, 23, 34);" # background color
            "selection-background-color: rgb(27, 128, 73);")

        layout = QGridLayout()

        self.original_label = QLabel(self)
        pixmap_sel = QPixmap("images/logo.png")
        self.original_label.setPixmap(pixmap_sel)
        self.original_label.resize(300, 200)

        # Mask the pwd
        self.text_pwd = QLineEdit()
        #self.text_pwd.setObjectName("txt_pwd")
        self.text_pwd.setEchoMode(QLineEdit.Password)
        self.text_pwd.move(50,550)
        layout.addWidget(self.text_pwd)

        self.button = QPushButton('Login')
        self.button.clicked.connect(self.login)

        layout.addWidget(self.button)

        self.setLayout(layout)

    def login(self):
        self.switch_window.emit()