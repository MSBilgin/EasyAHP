# -*- coding: utf-8 -*-
"""
/***************************************************************************
 easyAHP
                                 A QGIS plugin

Easy AHP provides Analytic Hierarchy Process (AHP) and Weighted Linear Combination (WLC) analysis in QGIS.
Target audience is decision makers that work on suitability analysis for land use, agriculture, disaster management, environmental resources etc.
The user-friendly interface makes analysis easier by dividing operations to different steps

                             -------------------
        begin                : 2014-10-20
        version              : 0.8
        copyright            : (C) 2014 by Mehmet Selim BILGIN
        email                : mselimbilgin@yahoo.com
        web                  : cbsuygulama.wordpress.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
from PyQt4 import QtGui, uic

mainFormClass, notImportant = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'main.ui'))
step1FormClass, notImportant = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'step1.ui'))
step2FormClass, notImportant = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'step2.ui'))
step3FormClass, notImportant = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'step3.ui'))

class mainDialog(QtGui.QDialog, mainFormClass):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)

class step1Dialog(QtGui.QDialog, step1FormClass):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)

class step2Dialog(QtGui.QDialog, step2FormClass):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)

class step3Dialog(QtGui.QDialog, step3FormClass):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)


