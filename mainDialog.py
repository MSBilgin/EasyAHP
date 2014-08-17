# -*- coding: utf-8 -*-
"""
/***************************************************************************
 easyAHP
                                 A QGIS plugin

Easy AHP provides Analytic Hierarchy Process (AHP) and Weighted Linear Combination (WLC) analysis in QGIS.
Target audience is decision makers that work on suitability analysis for land use, agriculture, disaster management, environmetal resources etc.
The user-friendly interface makes analysis easier by dividing operations to different steps

                             -------------------
        begin                : 2014-07-20
        version              : 0.7
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

from PyQt4 import QtGui

from main import Ui_main


class mainDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_main()
        self.ui.setupUi(self)