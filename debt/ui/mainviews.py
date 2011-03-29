#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer : Fad

import sys
from PyQt4 import QtCore, QtGui
from menubar import MenuBar
from dashbord import DashbordViewWidget

class MainWindows(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(900, 650)
        #~ self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Principale')
        self.setWindowIcon(QtGui.QIcon('icons/fad.png'))

        self.menubar = MenuBar(self)
        self.setMenuBar(self.menubar)
        
        self.change_context(DashbordViewWidget)
    # pour changer les pages
    def change_context(self, context_widget, *args, **kwargs):

        # instanciate context
        self.view_widget = context_widget(parent=self, *args, **kwargs)

        # refresh menubar
        self.menubar.refresh()

        # attach context to window
        self.setCentralWidget(self.view_widget)

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    qb = MainWindows()
    qb.show()
    sys.exit(app.exec_())
