# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sun Aug 17 15:44:02 2014
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

class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName(_fromUtf8("main"))
        main.resize(610, 475)
        main.setStyleSheet(_fromUtf8("WindowTitleHint"))
        self.label = QtGui.QLabel(main)
        self.label.setGeometry(QtCore.QRect(220, 30, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.textBrowser = QtGui.QTextBrowser(main)
        self.textBrowser.setGeometry(QtCore.QRect(50, 130, 521, 241))
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.label_2 = QtGui.QLabel(main)
        self.label_2.setGeometry(QtCore.QRect(190, 80, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.line = QtGui.QFrame(main)
        self.line.setGeometry(QtCore.QRect(0, 410, 631, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.nextBTN = QtGui.QPushButton(main)
        self.nextBTN.setGeometry(QtCore.QRect(350, 440, 75, 23))
        self.nextBTN.setObjectName(_fromUtf8("nextBTN"))
        self.cancelBTN = QtGui.QPushButton(main)
        self.cancelBTN.setGeometry(QtCore.QRect(480, 440, 75, 23))
        self.cancelBTN.setObjectName(_fromUtf8("cancelBTN"))
        self.label_3 = QtGui.QLabel(main)
        self.label_3.setGeometry(QtCore.QRect(50, 445, 46, 13))
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(main)
        self.label_4.setGeometry(QtCore.QRect(500, 370, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        main.setWindowTitle(_translate("main", "Easy AHP", None))
        self.label.setText(_translate("main", "EASY AHP", None))
        self.textBrowser.setHtml(_translate("main", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">General Terms</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Easy AHP provides Analytic Hierarchy Process (AHP) and Weighted Linear Combination (WLC) analysis in QGIS. </li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Target audience is decision makers that work on suitability analysis for land use, agriculture, disaster management, environmetal resources etc. </li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The user-friendly interface makes analysis easier by dividing operations to different steps.</li></ul>\n"
"<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Before Run</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">It is strongly recommended that all the input layers of the analysis are to be in same CRS. </li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Easy AHP uses Processing Toolbox\'s SAGA provider for WLC analysis. So it has to be installed before run.</li></ul>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.label_2.setText(_translate("main", "Analytic Hierarchy Process Tool for QGIS", None))
        self.nextBTN.setText(_translate("main", "Next", None))
        self.cancelBTN.setText(_translate("main", "Cancel", None))
        self.label_3.setText(_translate("main", "<html><head/><body><p><a href=\"https://cbsuygulama.wordpress.com/2014/08/17/vulnerability-mapping-using-easy-ahp/\"><span style=\" text-decoration: underline; color:#0000ff;\">Help</span></a></p></body></html>", None))
        self.label_4.setText(_translate("main", "(C) by MSBilgin", None))

