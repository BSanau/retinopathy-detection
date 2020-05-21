from PyQt5 import QtCore, QtWidgets
from PyQt5.Qt import Qt
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtWidgets import (QMainWindow, QGridLayout, QPushButton, QWidget, QFileDialog, 
    QLabel, QLineEdit, QAction, qApp, QProgressBar)

#from src.loadmodel import *
from src.GUI.Loginclass import Login
from src.GUI.MainWindowclass import MainWindow
from src.GUI.TreatWindowclass import TreatWindow

class Controller:

    def __init__(self):
        pass

    def show_login(self):
        self.login = Login()
        self.login.switch_window.connect(self.show_main)
        self.login.show()

    def show_main(self):
        self.window = MainWindow()
        self.window.switch_window.connect(self.show_riskfactors)
        self.login.close()
        self.window.show()

    def show_riskfactors(self):
        self.treatwindow = TreatWindow()
        self.treatwindow.show()
               

 
