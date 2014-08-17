# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'step3.ui'
#
# Created: Sat Aug 16 13:36:05 2014
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

class Ui_step3(object):
    def setupUi(self, step3):
        step3.setObjectName(_fromUtf8("step3"))
        step3.resize(610, 475)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(step3.sizePolicy().hasHeightForWidth())
        step3.setSizePolicy(sizePolicy)
        self.runBTN = QtGui.QPushButton(step3)
        self.runBTN.setGeometry(QtCore.QRect(350, 440, 75, 23))
        self.runBTN.setObjectName(_fromUtf8("runBTN"))
        self.exitBTN = QtGui.QPushButton(step3)
        self.exitBTN.setGeometry(QtCore.QRect(480, 440, 75, 23))
        self.exitBTN.setObjectName(_fromUtf8("exitBTN"))
        self.line = QtGui.QFrame(step3)
        self.line.setGeometry(QtCore.QRect(0, 410, 631, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_3 = QtGui.QLabel(step3)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(step3)
        self.label_4.setGeometry(QtCore.QRect(120, 33, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.backBTN = QtGui.QPushButton(step3)
        self.backBTN.setGeometry(QtCore.QRect(250, 440, 75, 23))
        self.backBTN.setObjectName(_fromUtf8("backBTN"))
        self.groupBox = QtGui.QGroupBox(step3)
        self.groupBox.setGeometry(QtCore.QRect(20, 110, 561, 51))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 451, 23))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.browseBTN = QtGui.QPushButton(self.groupBox)
        self.browseBTN.setGeometry(QtCore.QRect(480, 20, 75, 23))
        self.browseBTN.setObjectName(_fromUtf8("browseBTN"))
        self.groupBox_2 = QtGui.QGroupBox(step3)
        self.groupBox_2.setGeometry(QtCore.QRect(130, 210, 351, 171))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.tableWidget = QtGui.QTableWidget(self.groupBox_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 331, 141))
        self.tableWidget.setStyleSheet(_fromUtf8(""))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)

        self.retranslateUi(step3)
        QtCore.QMetaObject.connectSlotsByName(step3)

    def retranslateUi(self, step3):
        step3.setWindowTitle(_translate("step3", "Easy AHP", None))
        self.runBTN.setText(_translate("step3", "Run", None))
        self.exitBTN.setText(_translate("step3", "Exit", None))
        self.label_3.setText(_translate("step3", "STEP 3: ", None))
        self.label_4.setText(_translate("step3", "Weighted Linear Combination (WLC)", None))
        self.backBTN.setText(_translate("step3", "Back", None))
        self.groupBox.setTitle(_translate("step3", "Output", None))
        self.browseBTN.setText(_translate("step3", "Browse...", None))
        self.groupBox_2.setTitle(_translate("step3", "Layer Weights", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("step3", "Layer Name", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("step3", "Weight", None))

