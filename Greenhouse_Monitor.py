# -*- coding: utf-8 -*-
"""
Various methods of drawing scrolling plots.
"""
#import initExample ## Add path to library (just for examples; you do not need this)
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QAction
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot
from pyqtgraph.Qt import QtCore, QtGui
import os
import sys
import numpy as np
from random import randint

from datetime import datetime


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self._createActions()
        self._createMenuBar()
        self._connectActions()
        self.graphWidget = pg.PlotWidget()
        #main window
        self.setCentralWidget(self.graphWidget)
        #toolbar
        
        self.GH_days = list(range(100))
        self.GH_temperature = [randint(0,100) for _ in range (100)]


        styles = {'color':'r', 'font-size':'20px'}
        self.graphWidget.setLabel('left', 'Temperature (°C)', **styles)
        self.graphWidget.setLabel('bottom', 'Hour (H)', **styles)
        self.graphWidget.setBackground(QtGui.QColor(220,220,220,185))#light grey
        # plot data: x, y values
        pen = pg.mkPen(color=(200,100,100),width=10)
        
        self.data_line = self.graphWidget.plot(self.GH_days, self.GH_temperature,pen=pen, symbol='o', symbolSize=15, symbolBrush=(200,100,100))
        
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()
    
    def _createActions(self):
        self.newAction = QAction(self)
        self.newAction.setText("&New")
        # Creating actions using the second constructor
        self.openAction = QAction("&Open...", self)
        self.saveAction = QAction("&Save", self)
        self.exitAction = QAction("&Exit", self)
        self.copyAction = QAction("&Copy", self)
        self.pasteAction = QAction("&Paste", self)
        self.cutAction = QAction("C&ut", self)
        self.helpContentAction = QAction("&Help Content", self)
        self.aboutAction = QAction("&About", self)
    
    def _createMenuBar(self):
        menubar = self.menuBar()
        fileMenu = QtWidgets.QMenu("&File",self)
        menubar.addMenu(fileMenu)
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAction)
        editMenu = menubar.addMenu("Edit")
        editMenu.addAction(self.copyAction)
        editMenu.addAction(self.pasteAction)
        editMenu.addAction(self.cutAction)
    def _connectActions(self):
        # Connect File actions
        self.newAction.triggered.connect(self.newFile)
        self.openAction.triggered.connect(self.openFile)
        self.saveAction.triggered.connect(self.saveFile)
        self.exitAction.triggered.connect(self.close)
        # Connect Edit actions
        self.copyAction.triggered.connect(self.copyContent)
        self.pasteAction.triggered.connect(self.pasteContent)
        self.cutAction.triggered.connect(self.cutContent)

    def newFile(self):
        # Logic for creating a new file goes here...
        self.centralWidget.setText("<b>File > New</b> clicked")

    def openFile(self):
        # Logic for opening an existing file goes here...
        #find the saved file and then popluate widgets
        self.centralWidget.setText("<b>File > Open...</b> clicked")

    def saveFile(self):
        # Logic for saving a file goes here...
        self.centralWidget.setText("<b>File > Save</b> clicked")

    def copyContent(self):
        # Logic for copying content goes here...
        self.centralWidget.setText("<b>Edit > Copy</b> clicked")

    def pasteContent(self):
        # Logic for pasting content goes here...
        self.centralWidget.setText("<b>Edit > Paste</b> clicked")

    def cutContent(self):
        # Logic for cutting content goes here...
        self.centralWidget.setText("<b>Edit > Cut</b> clicked")

    
    def update_plot_data(self):

        self.GH_days = self.GH_days[1:]  # Remove the first y element.
        self.GH_days.append(self.GH_days[-1] + 1)  # Add a new value 1 higher than the last.

        self.GH_temperature = self.GH_temperature[1:]  # Remove the first 
        self.GH_temperature.append( randint(0,100))  # Add a new random value.

        self.data_line.setData(self.GH_days, self.GH_temperature)  # Update the data.
        
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
    



if __name__ == '__main__':
    main()