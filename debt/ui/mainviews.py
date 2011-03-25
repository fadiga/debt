#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer : Fad

import sys
from PyQt4 import QtCore, QtGui
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
        self.initUI()

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def initUI(self):
        self.cal = QtGui.QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.cal.move(20, 30)
        self.cal.setGeometry(5, 30, 300, 200)
        self.connect(self.cal, QtCore.SIGNAL('selectionChanged()'), self.showDate)

        self.label = QtGui.QLabel(self)
        date = self.cal.selectedDate()
        self.label.setText(str(date.toPyDate()))
        self.label.move(130, 260)

    def showDate(self):
        date = self.cal.selectedDate()
        self.label.setText(str(date.toPyDate()))
        self.title = setWindowTitle("Account's Summary.")
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.title)
        self.setLayout(vbox)
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    qb = MainWindows()
    qb.show()
    sys.exit(app.exec_())
