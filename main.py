import sys
from PyQt5.QtWidgets import QApplication
#from src.userinterface_v2 import UserInterface
from src.userinterface import *

def main():
    app = QApplication(sys.argv)
    #GUI = UserInterface()
    #GUI.show()
    controller = Controller()
    controller.show_login()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()