# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'step2.ui'
#
# Created: Fri Aug 15 01:02:00 2014
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

class Ui_step2(object):
    def setupUi(self, step2):
        step2.setObjectName(_fromUtf8("step2"))
        step2.resize(610, 475)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(step2.sizePolicy().hasHeightForWidth())
        step2.setSizePolicy(sizePolicy)
        self.nextBTN = QtGui.QPushButton(step2)
        self.nextBTN.setGeometry(QtCore.QRect(350, 440, 75, 23))
        self.nextBTN.setObjectName(_fromUtf8("nextBTN"))
        self.cancelBTN = QtGui.QPushButton(step2)
        self.cancelBTN.setGeometry(QtCore.QRect(480, 440, 75, 23))
        self.cancelBTN.setObjectName(_fromUtf8("cancelBTN"))
        self.line = QtGui.QFrame(step2)
        self.line.setGeometry(QtCore.QRect(0, 410, 631, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_3 = QtGui.QLabel(step2)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(step2)
        self.label_4.setGeometry(QtCore.QRect(120, 35, 311, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.backBTN = QtGui.QPushButton(step2)
        self.backBTN.setGeometry(QtCore.QRect(250, 440, 75, 23))
        self.backBTN.setObjectName(_fromUtf8("backBTN"))
        self.tableWidget = QtGui.QTableWidget(step2)
        self.tableWidget.setGeometry(QtCore.QRect(20, 80, 410, 310))
        self.tableWidget.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(30)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.groupBox = QtGui.QGroupBox(step2)
        self.groupBox.setGeometry(QtCore.QRect(450, 75, 141, 316))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.calcBTN = QtGui.QPushButton(self.groupBox)
        self.calcBTN.setGeometry(QtCore.QRect(35, 270, 71, 31))
        self.calcBTN.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.calcBTN.setAutoFillBackground(False)
        self.calcBTN.setFlat(False)
        self.calcBTN.setObjectName(_fromUtf8("calcBTN"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 50, 61, 181))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(55, 75, 46, 131))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(80, 85, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(80, 130, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(80, 175, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 200, 121, 61))
        self.label_8.setObjectName(_fromUtf8("label_8"))

        self.retranslateUi(step2)
        QtCore.QMetaObject.connectSlotsByName(step2)

    def retranslateUi(self, step2):
        step2.setWindowTitle(_translate("step2", "Easy AHP", None))
        self.nextBTN.setText(_translate("step2", "Next", None))
        self.cancelBTN.setText(_translate("step2", "Cancel", None))
        self.label_3.setText(_translate("step2", "STEP 2: ", None))
        self.label_4.setText(_translate("step2", "Fill The Pairwise Matrix", None))
        self.backBTN.setText(_translate("step2", "Back", None))
        self.groupBox.setTitle(_translate("step2", "AHP Parameters", None))
        self.calcBTN.setText(_translate("step2", "Calculate", None))
        self.label.setText(_translate("step2", "λ\n"
"\n"
"CI\n"
"\n"
"CR", None))
        self.label_2.setText(_translate("step2", "=\n"
"\n"
"=\n"
"\n"
"=", None))
        self.label_5.setText(_translate("step2", "NaN", None))
        self.label_6.setText(_translate("step2", "NaN", None))
        self.label_7.setText(_translate("step2", "NaN", None))
        self.label_8.setText(_translate("step2", "<html><head/><body><p><span style=\" color:#ff0000;\">CR ≥ 0.1 You should </span></p><p><span style=\" color:#ff0000;\"> revise the pairwise table.</span></p></body></html>", None))

