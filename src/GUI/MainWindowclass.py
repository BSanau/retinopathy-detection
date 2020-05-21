from PyQt5 import QtCore
from PyQt5.Qt import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QPushButton, QLabel, QFileDialog

from src.loadmodel import *
from src.createPDF import createpdf


class MainWindow (QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.title = "Vision"
        self.x, self.y = 350, 150
        self.width, self.height = 700, 400
        self.setStyleSheet(
            "color: white;" # letters color
            #"background-image: url(INPUT/bck2.jpg);"
            "background-color: rgb(4, 23, 34);" # background color
            "selection-color: white;" # letters color when the mouse is on??
            "selection-background-color: rgb(27, 128, 73);") 
        
        self.initUI()
        

    def initUI(self):
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowTitle(self.title) # Window title
        self.setWindowIcon(QIcon('images/icon.png')) # icon of my app
        self.setWindowOpacity(1.0) # opacity ranges from 0.0 to 1.0 (by default)
        #self.statusBar().showMessage('Ready')

        # MENU
        newAct = QAction(QIcon('images/newfile.png'), 'New case', self)
        newAct.setShortcut('Ctrl+N')
        #newAct.setStatusTip('Diagnose new case')
        newAct.triggered.connect(self.selectFileDialog)

        saveAct = QAction(QIcon('images/save.png'), 'Save PDF', self)
        saveAct.setShortcut('Ctrl+S')
        #saveAct.setStatusTip('Save current case')
        saveAct.triggered.connect(self.saveFile)

        exitAct = QAction(QIcon('images/exit.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        #exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        treatAct = QAction('See treatment', self)
        treatAct.triggered.connect(self.seeTreatements)

        menubar = self.menuBar() # menu bar on top of the window
        menubar.setStyleSheet("""
        QMenuBar {
            background-color: rgb(49,49,49);
            color: rgb(255,255,255); 
            border: 1px solid #000;
        }""") 

        fileMenu = menubar.addMenu('File') # name of the submenu
        fileMenu.addAction(newAct)
        fileMenu.addAction(saveAct)
        fileMenu.addAction(exitAct)
        treatment = menubar.addMenu('Treatments')
        treatment.addAction(treatAct)


        # SELECT BUTTON
        self.select_button = QPushButton('Select file', self) #create the widget and the text in the button
        self.select_button.setToolTip('Select an image') # message when the user points the mouse on the button
        self.select_button.move(50,50)
        self.select_button.clicked.connect(self.selectFileDialog)

 
        # IMAGE
        self.original_label = QLabel(self)
        pixmap_sel = QPixmap("images/noimage.png")
        self.original_label.setPixmap(pixmap_sel)
        self.original_label.move(50, 100)
        self.original_label.resize(224, 224)


        # DIAGNOSE BUTTON
        self.diagnose_button = QPushButton('Diagnose', self)
        self.diagnose_button.move(380,50)
        self.diagnose_button.clicked.connect(self.makeDiagnose)
        self.diagnose_button.setEnabled(False)


        # DIAGNOSE RESULT
        self.label_CNV = QLabel(self)
        self.label_CNV.setText("Choroidal Neovascularization")
        self.label_CNV.adjustSize()
        self.label_CNV.move(380, 100)
        self.label_CNV_prob = QLabel(self)
        self.label_CNV_prob.setText("0.0 %")
        self.label_CNV_prob.move(610, 95)

        self.label_DME = QLabel(self)
        self.label_DME.setText("Diabetic Macular Edema")
        self.label_DME.adjustSize()
        self.label_DME.move(380, 150)
        self.label_DME_prob = QLabel(self)
        self.label_DME_prob.setText("0.0 %")
        self.label_DME_prob.move(610, 145)

        self.label_DRUSEN = QLabel(self)
        self.label_DRUSEN.setText("Drusen")
        self.label_DRUSEN.move(380, 200)
        self.label_DRUSEN_prob = QLabel(self)
        self.label_DRUSEN_prob.setText("0.0 %")
        self.label_DRUSEN_prob.move(610, 200)

        self.label_NORMAL = QLabel(self)
        self.label_NORMAL.setText("Normal")
        self.label_NORMAL.move(380, 250)
        self.label_NORMAL_prob = QLabel(self)
        self.label_NORMAL_prob.setText("0.0 %")
        self.label_NORMAL_prob.move(610, 250)
        

    def selectFileDialog(self):
        filename = QFileDialog.getOpenFileName(self, 
            "Open file", # titulo de la ventana que se abre
            "", # se abre en la carpeta en la que se encuentra el main
            "Image Files (*.png *.jpg *.jpeg)") 

        if filename[0]:
            self.path = filename[0]
            pixmap_sel = QPixmap(filename[0])
            pixmap_sel2 = pixmap_sel.scaled(224, 224, aspectRatioMode = Qt.IgnoreAspectRatio)
            self.original_label.setPixmap(pixmap_sel2)
            self.original_label.move(50, 100)
            self.original_label.resize(224, 224)
            self.diagnose_button.setEnabled(True)


    def makeDiagnose(self):
        if self.path:
            print (self.path)
            self.main_window_button = QPushButton("Start")

            path_image = self.path
            self.y_pred = predictClass(path_image)

            self.label_CNV_prob.setText(f"{str(round(self.y_pred[0]*100,2))} %")
            self.label_DME_prob.setText(f"{str(round(self.y_pred[1]*100,2))} %")
            self.label_DRUSEN_prob.setText(f"{str(round(self.y_pred[2]*100,2))} %")
            self.label_NORMAL_prob.setText(f"{str(round(self.y_pred[3]*100,2))} %")
            

    def saveFile(self):
        pathfile = QFileDialog.getSaveFileName(self, "Save File")
        createpdf(self.path, pathfile[0], self.y_pred)


    def seeTreatements(self):
        self.switch_window.emit()
