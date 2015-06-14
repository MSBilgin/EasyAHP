# -*- coding: utf-8 -*-
"""
/***************************************************************************
 easyAHP
                                 A QGIS plugin

Easy AHP provides Analytic Hierarchy Process (AHP) and Weighted Linear Combination (WLC) analysis in QGIS.
Target audience is decision makers that work on suitability analysis for land use, agriculture, disaster management, environmental resources etc.
The user-friendly interface makes analysis easier by dividing operations to different steps

                             -------------------
        begin                : 2015-06-14
        version              : 0.9
        copyright            : (C) 2015 by Mehmet Selim BILGIN
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
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import qgis
import processing

import resources_rc
from dialogs import *

import sys
import csv

class easyAHP:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'easyAHP_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)


        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Easy AHP')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'easyAHP')
        self.toolbar.setObjectName(u'easyAHP')

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('easyAHP', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the InaSAFE toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/easyAHP/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Easy AHP'),
            callback=self.run,
            parent=self.iface.mainWindow())


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Easy AHP'),
                action)
            self.iface.removeToolBarIcon(action)

    def uiSettings(self):
        #initializing settings for some UI elements.
        self.dlgMain.setFixedSize(610, 475)
        self.dlgStep1.setFixedSize(610, 475)
        self.dlgStep2.setFixedSize(610, 475)
        self.dlgStep3.setFixedSize(610, 475)
        self.dlgStep2.label_8.hide()
        self.dlgStep3.tableWidget.horizontalHeader().setStretchLastSection(True)

    def nextStep1(self):
        self.dlgMain.reject()
        self.dlgStep1.show()

    def backStep1(self):
        self.dlgStep1.reject()
        self.dlgMain.show()

    def tableColumnList(self):
        columnCount = self.dlgStep2.tableWidget.columnCount()
        columnList = list()
        for i in range(columnCount):
            columnList.append(self.dlgStep2.tableWidget.horizontalHeaderItem(i).text())
        if columnCount==0:
            return [] #returns blank list.
        else:
            return columnList

    def tableMaker(self):
        #preparing the pairwise table.
        self.dlgStep2.tableWidget.setRowCount(len(self.paramList))
        self.dlgStep2.tableWidget.setColumnCount(len(self.paramList))

        row = col = self.dlgStep1.inputList.count() -1
        while row > -1:
            while col > -1:
                if col == row:
                    cellItem = QtGui.QTableWidgetItem()
                    brush = QtGui.QBrush(QtGui.QColor(209, 209, 209))
                    brush.setStyle(Qt.SolidPattern)
                    cellItem.setBackground(brush)
                    cellItem.setText('1')
                    cellItem.setFlags(Qt.ItemIsEnabled)
                    cellItem.setTextAlignment(Qt.AlignCenter)
                    self.dlgStep2.tableWidget.setItem(col,row,cellItem)

                col-=1
            row-=1
            col=row

    def nextStep2(self):
        if self.dlgStep1.inputList.count() > 15:
            QMessageBox.information(None, 'Easy AHP', 'The number of layers can not be more than 15.')

        elif self.dlgStep1.inputList.count() > 2:

            #If input layers changed it affect to the pairwise table and clears it.
            self.paramList = list()
            for i in range(self.dlgStep1.inputList.count()):
                self.paramList.append(self.dlgStep1.inputList.item(i).text())

            if self.tableColumnList() == []:
                #the table's initial generate.
                self.tableMaker()
                self.dlgStep2.tableWidget.setHorizontalHeaderLabels(self.paramList)
                self.dlgStep2.tableWidget.setVerticalHeaderLabels(self.paramList)
                self.dlgStep2.tableWidget.resizeColumnsToContents()


            elif self.paramList != self.tableColumnList():
                #The table is generated but after layers are changed so it clears it.
                self.dlgStep2.tableWidget.clear()
                self.tableMaker()
                self.dlgStep2.tableWidget.setHorizontalHeaderLabels(self.paramList)
                self.dlgStep2.tableWidget.setVerticalHeaderLabels(self.paramList)
                self.dlgStep2.tableWidget.resizeColumnsToContents()

            else:
                #do nothing if input layers are not changed.
                pass


            #resizing column widht.
            for i in range(len(self.paramList)):
                self.dlgStep2.tableWidget.setColumnWidth(i,60)

            self.dlgStep1.reject()
            self.dlgStep2.show()

        else:
            QMessageBox.information(None, 'Easy AHP', 'You must select at least 3 layers.')

    def backStep2(self):
        self.dlgStep2.reject()
        self.dlgStep1.show()

    def nextStep3(self):
        if not self.istableEdited:
            self.dlgStep3.tableWidget.setRowCount(len(self.paramList))

            for i in range(len(self.paramList)):
                itemLayerName = QTableWidgetItem()
                itemLayerName.setTextAlignment(Qt.AlignCenter)
                itemLayerName.setText(self.paramList[i])
                itemLayerName.setFlags(Qt.ItemIsEnabled)
                self.dlgStep3.tableWidget.setItem(i,0, itemLayerName)

                itemWeight= QTableWidgetItem()
                itemWeight.setTextAlignment(Qt.AlignCenter)
                itemWeight.setText(str(self.LAYER_WEIGHT_LIST[i]))
                itemWeight.setFlags(Qt.ItemIsEnabled)
                self.dlgStep3.tableWidget.setItem(i,1, itemWeight)

            for i in range(len(self.paramList)):
                self.dlgStep2.tableWidget.setColumnWidth(i,60)

            self.dlgStep2.reject()
            self.dlgStep3.show()
        else:
            QMessageBox.information(None, 'Easy AHP', 'You must calculate AHP Indicators before passing the next step.')

    def backStep3(self):
        self.dlgStep3.reject()
        self.dlgStep2.show()

    def cancel(self):
        quit_msg = "Are you sure you want to exit?"
        reply = QMessageBox.question(None, 'Easy AHP', quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            try:
                self.dlgMain.reject()
                self.dlgStep1.reject()
                self.dlgStep2.reject()
                self.dlgStep3.reject()
            except:
                pass
        else:
            pass


    def addLayer(self):
        try:
            currItem = self.dlgStep1.qgisLayerList.currentItem()
            self.dlgStep1.qgisLayerList.takeItem(self.dlgStep1.qgisLayerList.currentRow())
            self.dlgStep1.inputList.addItem(currItem.text())
        except:
            pass

    def removeLayer(self):
        try:
            currItem = self.dlgStep1.inputList.currentItem()
            self.dlgStep1.inputList.takeItem(self.dlgStep1.inputList.currentRow())
            self.dlgStep1.qgisLayerList.addItem(currItem.text())
        except:
            pass

    def check(self):
        self.istableEdited = True #this attibute is used for passing NEXT STEP. If it is True the user must re-calculate indicators.
        #Everything about the pairwise table (tableWidget) is handling in here.

        try:
            self.dlgStep2.tableWidget.currentItem().setTextAlignment(Qt.AlignCenter) #text alignment for pairwise table.
            self.dlgStep2.tableWidget.currentItem().setText(self.dlgStep2.tableWidget.currentItem().text().replace(',' , '.')) #handling precise char (comma -> point)
        except:
            pass

        if self.dlgStep2.tableWidget.currentItem() == None:
            #clears the cross cell
            pass

        elif self.dlgStep2.tableWidget.currentItem().text()== '':
            #clears the cross cell
            self.dlgStep2.tableWidget.setItem(self.dlgStep2.tableWidget.currentItem().column(), self.dlgStep2.tableWidget.currentItem().row(), QtGui.QTableWidgetItem(''))

        else:
            if self.isNumeric(self.dlgStep2.tableWidget.currentItem().text()): #checking the cell is numeric or not

                if float(self.dlgStep2.tableWidget.currentItem().text()) > 9 or float(self.dlgStep2.tableWidget.currentItem().text()) < 0.111:
                    QtGui.QMessageBox.information(None,'Easy AHP', 'Your value cannot be greater than 9 and less than 0.1111')
                    self.dlgStep2.tableWidget.currentItem().setText('')
                    #clears the cross cell
                    self.dlgStep2.tableWidget.setItem(self.dlgStep2.tableWidget.currentItem().column(), self.dlgStep2.tableWidget.currentItem().row(), QtGui.QTableWidgetItem(''))

                else:
                    #numeric values is rounding in here.
                    numericvalue = str(round(float(self.dlgStep2.tableWidget.currentItem().text()),3))
                    self.dlgStep2.tableWidget.currentItem().setText(numericvalue)
                    self.crossFill()

            else:
                QtGui.QMessageBox.information(None,'Easy AHP', 'Please enter a numeric value.')
                self.dlgStep2.tableWidget.currentItem().setText('')
                self.dlgStep2.tableWidget.setItem(self.dlgStep2.tableWidget.currentItem().column(), self.dlgStep2.tableWidget.currentItem().row(), QtGui.QTableWidgetItem(''))

    def isNumeric(self,inputListValue):
        #checking for cell input value is numeric or not.
        try:
            float(inputListValue)
        except:
            return False
        return True

    def crossFill(self):
        self.dlgStep2.tableWidget.blockSignals(True) #disabling signals before updating table.
        #Filling cross cell
        normalValue = float(self.dlgStep2.tableWidget.currentItem().text())
        reverseValue = round((1/normalValue),3)

        if reverseValue > 9: #1/9 = 0.11111111 but 1/0.11111111 > 9 so this problem is handling in here.
            reverseValue = 9

        reverveItem = QtGui.QTableWidgetItem()
        reverveItem.setTextAlignment(Qt.AlignCenter)
        reverveItem.setText(str(reverseValue))
        self.dlgStep2.tableWidget.setItem(self.dlgStep2.tableWidget.currentItem().column(), self.dlgStep2.tableWidget.currentItem().row(), reverveItem)
        self.dlgStep2.tableWidget.blockSignals(False) #enabling signals.

    def isTableCompleted(self):
        #checking the table for containing any blank cell.
        row = col = 0
        control = 0
        tableSize = self.dlgStep2.tableWidget.columnCount()
        while row < tableSize:
            while col < tableSize:
                try:
                    if not self.dlgStep2.tableWidget.item(row,col).text():
                        control+=1
                except:
                    control+=1
                col+=1
            row+=1
            col=0

        if control > 0:
            return False
        else:
            return True

    def parameterCalculator(self):
        if self.isTableCompleted():
            self.ahpCalculator()
        else:
            QMessageBox.information(None, 'Easy AHP','You must fill all the cells in the pairwise table.')

    def columnAddition(self):
        #Sums QtableWidget columns and inserting into columnSum list.
        columnCount = self.dlgStep2.tableWidget.columnCount()-1
        columnSum = list()

        while columnCount> -1:
            sum = float()
            counter = self.dlgStep2.tableWidget.columnCount()-1
            while counter > -1:
                sum+= float(self.dlgStep2.tableWidget.item(counter,columnCount).text())
                counter-=1
            columnSum.append(sum)
            columnCount-=1
        columnSum.reverse()
        return columnSum

    def matrixNormalizer(self, sumOfColumns):
        normalizedMatrix = list()
        columnCount = self.dlgStep2.tableWidget.columnCount()-1
        while columnCount> -1:
            numberList = list()
            counter = self.dlgStep2.tableWidget.columnCount()-1
            while counter > -1:
                divided = round(float(self.dlgStep2.tableWidget.item(counter,columnCount).text()) / sumOfColumns[columnCount],3)
                numberList.append(divided)
                counter-=1
            normalizedMatrix.extend([numberList])
            columnCount-=1
        return normalizedMatrix

    def weightCalculator(self, normalMatrix):
        #layers weight calculations.
        listlen = len(normalMatrix) -1
        layerWeights = list()
        while listlen > -1:
            sum = float()
            for i in normalMatrix:
                sum+= i[listlen]
            sumAverage = round(sum / len(normalMatrix),3)
            layerWeights.append(sumAverage)
            listlen-=1
        return layerWeights

    def lambdaParameter(self, layerWeightList):
        #lambda value calculations.
        listLen = len(layerWeightList)
        row = col = 0
        lambdaValue = lambdaSum = float()
        while row < listLen:
            sum = float()
            while col < listLen:
                sum += round(float(self.dlgStep2.tableWidget.item(row,col).text()) * layerWeightList[col] , 3)
                col += 1
            lambdaSum += round(sum / layerWeightList[row] , 3)
            row += 1
            col = 0
        lambdaValue = round(lambdaSum / listLen , 3)
        self.dlgStep2.label_5.setText(str(lambdaValue))
        return lambdaValue

    def conIndex(self, lambdaValue, layerWeightList):
        #consistency index calculations.
        criteriaNumber = len(layerWeightList)
        ci = round((lambdaValue - criteriaNumber) / (criteriaNumber-1) , 3)
        self.dlgStep2.label_6.setText(str(ci))
        return ci

    def conRatio(self,consistencyIndex, numberOfLayers):
        randomConsIndex = {1:0.0 , 2:0.0 , 3:0.58 , 4:0.9 , 5:1.12 , 6:1.24 , 7:1.32 ,
                            8:1.41 , 9:1.45 , 10:1.49 , 11:1.51 , 12:1.48 , 13:1.56 , 14:1.57 , 15:1.59}

        cr = round(consistencyIndex / randomConsIndex[numberOfLayers] , 3)
        self.dlgStep2.label_7.setText(str(cr))
        if cr >= 0.1:
            self.dlgStep2.label_8.show()
        else:
            self.dlgStep2.label_8.hide()
        return cr

    def ahpCalculator(self):
        self.istableEdited = False #user calculates parameter and makes this attr. FALSE
        self.LAYER_WEIGHT_LIST = self.weightCalculator(self.matrixNormalizer(self.columnAddition()))
        LAMBDA_PARAMETER = self.lambdaParameter(self.LAYER_WEIGHT_LIST)
        CONSISTENCY_INDEX = self.conIndex(LAMBDA_PARAMETER, self.LAYER_WEIGHT_LIST)
        CONSISTENCY_RATIO = self.conRatio(CONSISTENCY_INDEX, len(self.LAYER_WEIGHT_LIST))

    def browse(self):
        fileLocation = QFileDialog.getSaveFileName(None, "Save Output File", self.dlgStep3.lineEdit.text(), "GeoTIFF file (*.tif)")
        if fileLocation:
            #If the output file has no extension it considered as TIFF file.
            if not os.path.splitext(fileLocation)[1]:
                outputFile =  os.path.splitext(fileLocation)[0] + '.tif'

            elif os.path.splitext(fileLocation)[1] != '.tif':
                outputFile =  os.path.splitext(fileLocation)[0] + '.tif'

            else:
                outputFile = fileLocation

            self.dlgStep3.lineEdit.setText(outputFile)

    def wlcProcessing(self):
        if self.dlgStep3.lineEdit.text() == '':
            QMessageBox.information(None, 'Easy AHP', 'You must specify the output folder.')
        else:
            expression = list() #the expression for SAGA Raster Calculator.
            files = list() #files for SAGA Raster Calculator.
            itemAlpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o'] #This letter list is necessary for SAGA Raster Calculator.

            #formulating the expression.
            for i in range(len(self.paramList)):
                expression.append(itemAlpha[i] + '*' + str(self.LAYER_WEIGHT_LIST[i]))
                for j in self.allMapLayers:
                    if self.paramList[i] == j[1].name():
                        files.append(j[1].source())


            savePath = self.dlgStep3.lineEdit.text().encode('utf-8')


            output = processing.runalg("saga:rastercalculator", files[0], ';'.join(files[1:]), '+'.join(expression), savePath)

            #Checking if SAGA is installed.
            if output:
                qgis.utils.iface.addRasterLayer(self.dlgStep3.lineEdit.text(), os.path.splitext(os.path.basename(savePath))[0]) #adding the result to QGIS canvas.
                QMessageBox.information(None, 'Easy AHP', 'Calculation succesfully completed and the result was added into QGIS Canvas.')
            else:
                QMessageBox.information(None, 'Easy AHP', "An error occured during the calculation. Please make sure that Processing Toolbox's SAGA provider is installed.")

    def saveTable(self):
        #Saving the pairwise table.
        if not self.istableEdited:
            saveDlg = QFileDialog.getSaveFileName(None, 'Save Table', '.', 'CSV file (*.csv)')

            if saveDlg:
                if not os.path.splitext(saveDlg)[1]:
                    saveDlg += '.csv'

                tableSize = self.dlgStep2.tableWidget.columnCount()

                try:
                    csvOutput = open(saveDlg, 'w')
                    writer = csv.writer(csvOutput, delimiter=';')

                    for i in range(int(tableSize)):
                        tempList = list()
                        for j in range(int(tableSize)):
                            tempList.append(self.dlgStep2.tableWidget.item(i,j).text())
                        writer.writerow(tempList)
                    csvOutput.close()
                    QMessageBox.information(None, 'Easy AHP', 'The pairwise table has been successfully saved.')

                except Exception as saveError:
                    QMessageBox.critical(None, 'EasyAHP', str(saveError))

        else:
            QMessageBox.information(None, 'Easy AHP', 'You must calculate AHP Indicators to save the table.')


    def loadTable(self):
        #Loading the pairwise table.
        loadDlg = QFileDialog.getOpenFileName(None, 'Load Table', '.', 'CSV file (*.csv)')

        if loadDlg:
            self.dlgStep2.tableWidget.blockSignals(True)
            try:

                with open(loadDlg, 'r') as csvFile:
                	reader  =csv.reader(csvFile, delimiter=';')
                	csvList = list()
                	for i in reader:
                		csvList.append(i)

                if self.dlgStep2.tableWidget.rowCount() == len(csvList):
                    for i in range(len(csvList)):
                        for j in range(len(csvList)):
                            cellItem = QtGui.QTableWidgetItem()
                            cellItem.setText(csvList[i][j])
                            self.dlgStep2.tableWidget.setItem(i,j,cellItem)
                    self.tableMaker() #preparing the table structure.

                else:
                    QMessageBox.critical(None, 'Easy AHP', 'The pairwise table size and the loaded table size are not compatible.')

            except Exception as loadError:
                    QMessageBox.critical(None, 'EasyAHP', str(loadError))

            self.dlgStep2.tableWidget.blockSignals(False)



    def run(self):
        self.dlgStep1 = step1Dialog()
        self.dlgStep2 = step2Dialog()
        self.dlgStep3 = step3Dialog()
        self.dlgMain = mainDialog()

        self.uiSettings()

        #QGIS raster layers adding into QLayerWidget (availables)
        self.allMapLayers = qgis.core.QgsMapLayerRegistry.instance().mapLayers().items()
        self.dlgStep1.qgisLayerList.clear()

        #I used try-except block for vector layers. Beacuse they have no method named "rasterType".
        for (notImportantForNow, layerObj) in self.allMapLayers:
            try:
    			if layerObj.rasterType() == 0:
    				self.dlgStep1.qgisLayerList.addItem(layerObj.name())
            except:
                pass

        #Main dialog connections
        self.dlgMain.nextBTN.clicked.connect(self.nextStep1)
        self.dlgMain.cancelBTN.clicked.connect(self.cancel)

        #Step1 dialog connections
        self.dlgStep1.backBTN.clicked.connect(self.backStep1)
        self.dlgStep1.cancelBTN.clicked.connect(self.cancel)
        self.dlgStep1.addLayerBTN.clicked.connect(self.addLayer)
        self.dlgStep1.removeLayerBTN.clicked.connect(self.removeLayer)
        self.dlgStep1.nextBTN.clicked.connect(self.nextStep2)

        #Step2 dialog connections
        self.dlgStep2.backBTN.clicked.connect(self.backStep2)
        self.dlgStep2.tableWidget.itemChanged.connect(self.check)
        self.dlgStep2.calcBTN.clicked.connect(self.parameterCalculator)
        self.dlgStep2.nextBTN.clicked.connect(self.nextStep3)
        self.dlgStep2.cancelBTN.clicked.connect(self.cancel)
        self.dlgStep2.saveBTN.clicked.connect(self.saveTable)
        self.dlgStep2.loadBTN.clicked.connect(self.loadTable)

        #Step3 dialog connections
        self.dlgStep3.backBTN.clicked.connect(self.backStep3)
        self.dlgStep3.exitBTN.clicked.connect(self.cancel)
        self.dlgStep3.browseBTN.clicked.connect(self.browse)
        self.dlgStep3.runBTN.clicked.connect(self.wlcProcessing)

        self.dlgMain.show()