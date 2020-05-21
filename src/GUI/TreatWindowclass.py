from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QRadioButton, 
     QGridLayout, QVBoxLayout, QHBoxLayout, QButtonGroup) 

from src.recommentreat import recommend

class TreatWindow(QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Treatements')
        self.x, self.y = 400, 200
        self.width, self.height = 700, 300
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('images/icon.png'))

        self.setStyleSheet(
            "color: white;" # letters color
            "background-color: rgb(4, 23, 34);" # background color
            "selection-color: white;" # letters color when the mouse is on??
            "selection-background-color: rgb(27, 128, 73);") 
        self.initTreat()

    def initTreat(self):

        # Buttons
        self.lbl_sex = QLabel('Sex')
        self.sex0 = QRadioButton('Male')
        self.sex1 = QRadioButton('Female')
        sex_group = QButtonGroup(self)
        sex_group.addButton(self.sex0)
        sex_group.addButton(self.sex1)       

        self.lbl_diab = QLabel('Diabetes')
        self.diab0 = QRadioButton('No')
        self.diab1 = QRadioButton('Type 1')
        self.diab2 = QRadioButton('Type 2')
        diab_group = QButtonGroup(self)
        diab_group.addButton(self.diab0)
        diab_group.addButton(self.diab1)
        diab_group.addButton(self.diab2)

        self.lbl_age = QLabel('Age')
        self.age0 = QRadioButton('<30')
        self.age1 = QRadioButton('30-40')
        self.age2 = QRadioButton('40-50')
        self.age3 = QRadioButton('50-60')
        self.age4 = QRadioButton('>60')
        age_group = QButtonGroup(self)
        age_group.addButton(self.age0)
        age_group.addButton(self.age1)
        age_group.addButton(self.age2)
        age_group.addButton(self.age3)
        age_group.addButton(self.age4)

        self.lbl_trauma = QLabel('Eye trauma')
        self.trauma0 = QRadioButton('No')
        self.trauma1 = QRadioButton('Yes')
        trauma_group = QButtonGroup(self)
        trauma_group.addButton(self.trauma0)
        trauma_group.addButton(self.trauma1)       

        self.lbl_myopia = QLabel('Myopia')
        self.myopia0 = QRadioButton('No')
        self.myopia1 = QRadioButton('Light')
        self.myopia2 = QRadioButton('Severe')
        myopia_group = QButtonGroup(self)
        myopia_group.addButton(self.myopia0)
        myopia_group.addButton(self.myopia1)
        myopia_group.addButton(self.myopia2)

        self.lbl_col = QLabel('Cholesterol')
        self.col0 = QRadioButton('No')
        self.col1 = QRadioButton('Yes')
        col_group = QButtonGroup(self)
        col_group.addButton(self.col0)
        col_group.addButton(self.col1)

        self.lbl_diag = QLabel('Diagnostic')
        self.CNV = QRadioButton('CNV')
        self.DME = QRadioButton('DME')
        self.Drunes = QRadioButton('Drunes')
        diag_group = QButtonGroup(self)
        diag_group.addButton(self.CNV)
        diag_group.addButton(self.DME)
        diag_group.addButton(self.Drunes)
       
        self.btn = QPushButton('Select')
        self.btn.clicked.connect(self.onClicked)

        # Buttons positioning
        layout1 = QVBoxLayout()
        
        layout1.addWidget(self.lbl_sex)
        layout1.addWidget(self.sex0)
        layout1.addWidget(self.sex1)
        
        layout2 = QVBoxLayout()
        layout2.addWidget(self.lbl_diab)
        layout2.addWidget(self.diab0)
        layout2.addWidget(self.diab1)
        layout2.addWidget(self.diab2)

        layout3 = QVBoxLayout()
        layout3.addWidget(self.lbl_age)
        layout3.addWidget(self.age0)
        layout3.addWidget(self.age1)
        layout3.addWidget(self.age2)
        layout3.addWidget(self.age3)
        layout3.addWidget(self.age4)

        layout4 = QVBoxLayout()
        layout4.addWidget(self.lbl_trauma)
        layout4.addWidget(self.trauma0)
        layout4.addWidget(self.trauma1)

        layout5 = QVBoxLayout()
        layout5.addWidget(self.lbl_myopia)
        layout5.addWidget(self.myopia0)
        layout5.addWidget(self.myopia1)
        layout5.addWidget(self.myopia2)

        layout6 = QVBoxLayout()
        layout6.addWidget(self.lbl_col)
        layout6.addWidget(self.col0)
        layout6.addWidget(self.col1)

        layout7 = QVBoxLayout()
        layout7.addWidget(self.lbl_diag)
        layout7.addWidget(self.CNV)
        layout7.addWidget(self.DME)
        layout7.addWidget(self.Drunes)

        layout8 = QHBoxLayout()
        layout8.addLayout(layout1)
        layout8.addLayout(layout2)
        layout8.addLayout(layout3)
        layout8.addLayout(layout4)

        layout9 = QHBoxLayout()
        layout9.addLayout(layout5)
        layout9.addLayout(layout6)
        layout9.addLayout(layout7)
        layout9.addWidget(self.btn)

        layout10 = QVBoxLayout()
        layout10.addLayout(layout8)
        layout10.addLayout(layout9)
        empty = QLabel('')
        layout10.addWidget(empty)
        self.treat1 = QLabel(self)
        self.treat1.setText(" ")
        layout10.addWidget(self.treat1)
        self.treat2 = QLabel(self)
        self.treat2.setText(" ")
        layout10.addWidget(self.treat2)
        self.treat3 = QLabel(self)
        self.treat2.setText(" ")
        layout10.addWidget(self.treat3)
              
        self.setLayout(layout10)


    def onClicked(self):
        if self.sex0.isChecked(): sex = 0
        else: sex = 1

        if self.diab0.isChecked(): diab = 0
        elif self.diab1.isChecked(): diab = 1
        else: diab = 2

        if self.age0.isChecked(): age = 0
        elif self.age1.isChecked(): age = 1
        elif self.age2.isChecked(): age = 2
        elif self.age3.isChecked(): age = 3
        else: age = 4

        if self.trauma0.isChecked(): trauma = 0
        else: trauma = 1

        if self.myopia0.isChecked(): myopia = 0
        elif self.myopia1.isChecked(): myopia = 1
        else: myopia = 2

        if self.col0.isChecked(): col = 0
        else: col = 1

        if self.CNV.isChecked(): diag = "CNV"
        elif self.DME.isChecked(): diag = "DME"
        else: diag = "DRUNES"

        result = recommend(sex, diab, age, trauma, myopia, col, diag)
        result.reset_index(inplace=True)
        
        self.treat1.setText(f'Treatment 1 : {result["Treatment"][0]}')
        self.treat2.setText(f'Treatment 2 : {result["Treatment"][1]}')
        self.treat3.setText(f'Treatment 3 : {result["Treatment"][2]}')