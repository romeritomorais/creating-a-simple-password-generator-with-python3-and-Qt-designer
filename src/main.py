# -*- coding: utf-8 -*-
# Developed by Romerito Morais using QtDesigner + Python3.10
# To work it is necessary to have installed the following libs:

import random
import string
import sys
from pathlib import Path

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

root = Path.cwd()
local = f"{root.parent}"


class Ui_MainPassGenerator(object):
    def setupUi (self, MainPassGenerator):
        MainPassGenerator.setObjectName("MainPassGenerator")
        MainPassGenerator.resize(432, 424)
        MainPassGenerator.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainPassGenerator)
        self.centralwidget.setObjectName("centralwidget")
        self.lineSeparator = QtWidgets.QFrame(self.centralwidget)
        self.lineSeparator.setGeometry(QtCore.QRect(10, 130, 411, 16))
        self.lineSeparator.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineSeparator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineSeparator.setObjectName("lineSeparator")
        self.labelIcon = QtWidgets.QLabel(self.centralwidget)
        self.labelIcon.setGeometry(QtCore.QRect(140, 0, 150, 131))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelIcon.setFont(font)
        self.labelIcon.setAutoFillBackground(False)
        self.labelIcon.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelIcon.setText("")
        self.labelIcon.setTextFormat(QtCore.Qt.AutoText)
        self.labelIcon.setPixmap(QtGui.QPixmap(f"{local}/src/img/logo.jpg"))
        self.labelIcon.setScaledContents(True)
        self.labelIcon.setAlignment(QtCore.Qt.AlignCenter)
        self.labelIcon.setWordWrap(False)
        self.labelIcon.setObjectName("labelIcon")
        self.btnGenerator = QtWidgets.QPushButton(self.centralwidget)
        self.btnGenerator.setGeometry(QtCore.QRect(210, 170, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnGenerator.setFont(font)
        self.btnGenerator.setAutoFillBackground(False)
        self.btnGenerator.setStyleSheet("")
        self.btnGenerator.setInputMethodHints(QtCore.Qt.ImhNone)
        self.btnGenerator.setAutoDefault(False)
        self.btnGenerator.setDefault(False)
        self.btnGenerator.setFlat(False)
        self.btnGenerator.setObjectName("btnGenerator")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 150, 50, 18))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(10, 170, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox.setFont(font)
        self.spinBox.setMinimum(25)
        self.spinBox.setMaximum(999)
        self.spinBox.setObjectName("spinBox")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 210, 411, 151))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.editGenerated = QtWidgets.QPlainTextEdit(self.groupBox)
        self.editGenerated.setGeometry(QtCore.QRect(10, 30, 391, 101))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(15)
        self.editGenerated.setFont(font)
        self.editGenerated.setAutoFillBackground(False)
        self.editGenerated.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.editGenerated.setFrameShadow(QtWidgets.QFrame.Plain)
        self.editGenerated.setReadOnly(True)
        self.editGenerated.setPlainText("")
        self.editGenerated.setBackgroundVisible(False)
        self.editGenerated.setObjectName("editGenerated")
        self.btnClipboard = QtWidgets.QPushButton(self.centralwidget)
        self.btnClipboard.setGeometry(QtCore.QRect(320, 170, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnClipboard.setFont(font)
        self.btnClipboard.setObjectName("btnClipboard")
        self.lblInfo = QtWidgets.QLabel(self.centralwidget)
        self.lblInfo.setGeometry(QtCore.QRect(10, 370, 410, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblInfo.setFont(font)
        self.lblInfo.setText("")
        self.lblInfo.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lblInfo.setObjectName("lblInfo")
        MainPassGenerator.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainPassGenerator)
        self.toolBar.setObjectName("toolBar")
        MainPassGenerator.addToolBar(QtCore.Qt.BottomToolBarArea, self.toolBar)
        self.btnGenerator.clicked.connect(self.generate)
        self.btnClipboard.clicked.connect(self.copyToClipboard)

        self.retranslateUi(MainPassGenerator)
        QtCore.QMetaObject.connectSlotsByName(MainPassGenerator)

    def generate (self):
        response = self.passwordGenerator(len_pass=self.spinBox.text())
        self.lblInfo.clear()
        self.editGenerated.setPlainText(f"{response}")

    # código original de: https://github.com/iuryrosal/projetos-python/tree/main/level-a/05
    def passwordGenerator (self, len_pass):
        ascii_options = string.ascii_letters
        number_options = string.digits
        punt_options = string.punctuation
        options = ascii_options + number_options + punt_options

        password_user = ""

        for i in range(0, int(self.spinBox.text())):
            digit = random.choice(options)
            password_user = password_user + digit

        return password_user

    def copyToClipboard (self):
        if self.editGenerated.toPlainText() == "":
            self.lblInfo.setText('generate the password before copying it to the clipboard')
            self.lblInfo.setStyleSheet("color: rgb(237, 51, 59);")
        else:
            clip = QApplication.clipboard()
            clip.clear(mode=clip.Clipboard)
            clip.setText(self.editGenerated.toPlainText(), mode=clip.Clipboard)
            self.lblInfo.setStyleSheet("color: rgb(36, 146, 52);")
            self.lblInfo.setText(f"password | {self.editGenerated.toPlainText()} | copied to clipboard!")

    def retranslateUi (self, MainPassGenerator):
        _translate = QtCore.QCoreApplication.translate
        MainPassGenerator.setWindowTitle(_translate("MainPassGenerator", "Simple Password v1.0"))
        self.btnGenerator.setText(_translate("MainPassGenerator", "generate"))
        self.label.setText(_translate("MainPassGenerator", "length"))
        self.btnClipboard.setText(_translate("MainPassGenerator", "clipboard"))
        self.toolBar.setWindowTitle(_translate("MainPassGenerator", "toolBar"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QMainWindow()
    ui = Ui_MainPassGenerator()
    ui.setupUi(Principal)
    Principal.show()
    sys.exit(app.exec_())
