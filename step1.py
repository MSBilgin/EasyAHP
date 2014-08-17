# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'step1.ui'
#
# Created: Wed Jul 23 01:08:55 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_step1(object):
    def setupUi(self, step1):
        step1.setObjectName(_fromUtf8("step1"))
        step1.resize(610, 475)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(step1.sizePolicy().hasHeightForWidth())
        step1.setSizePolicy(sizePolicy)
        self.qgisLayerList = QtGui.QListWidget(step1)
        self.qgisLayerList.setGeometry(QtCore.QRect(20, 110, 241, 260))
        self.qgisLayerList.setObjectName(_fromUtf8("qgisLayerList"))
        self.inputList = QtGui.QListWidget(step1)
        self.inputList.setGeometry(QtCore.QRect(350, 110, 241, 260))
        self.inputList.setObjectName(_fromUtf8("inputList"))
        self.addLayerBTN = QtGui.QPushButton(step1)
        self.addLayerBTN.setGeometry(QtCore.QRect(280, 210, 51, 23))
        self.addLayerBTN.setObjectName(_fromUtf8("addLayerBTN"))
        self.removeLayerBTN = QtGui.QPushButton(step1)
        self.removeLayerBTN.setGeometry(QtCore.QRect(280, 250, 51, 23))
        self.removeLayerBTN.setObjectName(_fromUtf8("removeLayerBTN"))
        self.nextBTN = QtGui.QPushButton(step1)
        self.nextBTN.setGeometry(QtCore.QRect(350, 440, 75, 23))
        self.nextBTN.setObjectName(_fromUtf8("nextBTN"))
        self.cancelBTN = QtGui.QPushButton(step1)
        self.cancelBTN.setGeometry(QtCore.QRect(480, 440, 75, 23))
        self.cancelBTN.setObjectName(_fromUtf8("cancelBTN"))
        self.line = QtGui.QFrame(step1)
        self.line.setGeometry(QtCore.QRect(0, 410, 631, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label = QtGui.QLabel(step1)
        self.label.setGeometry(QtCore.QRect(80, 90, 121, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(step1)
        self.label_2.setGeometry(QtCore.QRect(450, 90, 71, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(step1)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(step1)
        self.label_4.setGeometry(QtCore.QRect(120, 35, 311, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.backBTN = QtGui.QPushButton(step1)
        self.backBTN.setGeometry(QtCore.QRect(250, 440, 75, 23))
        self.backBTN.setObjectName(_fromUtf8("backBTN"))

        self.retranslateUi(step1)
        QtCore.QMetaObject.connectSlotsByName(step1)

    def retranslateUi(self, step1):
        step1.setWindowTitle(_translate("step1", "Easy AHP", None))
        self.addLayerBTN.setText(_translate("step1", ">>>", None))
        self.removeLayerBTN.setText(_translate("step1", "<<<", None))
        self.nextBTN.setText(_translate("step1", "Next", None))
        self.cancelBTN.setText(_translate("step1", "Cancel", None))
        self.label.setText(_translate("step1", "Available Raster Layers", None))
        self.label_2.setText(_translate("step1", "Input Layers", None))
        self.label_3.setText(_translate("step1", "STEP 1: ", None))
        self.label_4.setText(_translate("step1", "Choose Input Layers (Parameters)", None))
        self.backBTN.setText(_translate("step1", "Back", None))

