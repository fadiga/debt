#!/usr/bin/env python
# -*- coding: utf-8 -*-
#maintainer :fad

from PyQt4 import QtGui, QtCore

class MenuBar(QtGui.QMenuBar):
    
    def __init__(self, parent=None, *args, **kwargs):
        QtGui.QMenuBar.__init__(self, parent, *args, **kwargs)
        
        exit = QtGui.QAction(QtGui.QIcon('icons/exit.png'), 'Exit', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit application')
        self.connect(exit, QtCore.SIGNAL("triggered()"), \
                                         self.parentWidget(), \
                                         QtCore.SLOT("close()"))
        #~ self.statusBar()
        file = self.addMenu('&File')
        file.addAction(exit)
