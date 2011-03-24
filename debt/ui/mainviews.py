#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer : Fad

import sys
from PyQt4 import QtGui
from menubar import MenuBar


class MainWindows(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(900, 650)
        #~ self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Principale')
        self.setWindowIcon(QtGui.QIcon('icons/fad.png'))
        
        self.menubar = MenuBar(self)
        self.setMenuBar(self.menubar)
        
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


