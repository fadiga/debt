#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: alou

from PyQt4 import QtGui, QtCore
from database import *
from common import DebtWidget, DebtPageTitle, DebtTableWidget
from gettext import gettext as _


class DashbordViewWidget(DebtWidget):
    def __init__(self, parent=0, *args, **kwargs):
        super(DashbordViewWidget, self).__init__(parent=parent,
                                                        *args, **kwargs)
        self.title = DebtPageTitle(u"Dashbord")        
        self.table = DashbordTableWidget(parent=self)
        
        #Calandar
        hbox = QtGui.QHBoxLayout(self)

        self.cal = QtGui.QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.cal.move(20, 30)
        self.cal.setGeometry(0, 0, 10, 10)
        self.connect(self.cal, QtCore.SIGNAL('selectionChanged()'), self.showDate)
        self.label = QtGui.QLabel(self)
        date = self.cal.selectedDate()
        self.label.setText(str(date.toPyDate()))
        self.label.move(130, 260)
        #--------------------
 
        topright = QtGui.QFrame(self)
        topright.setFrameShape(QtGui.QFrame.StyledPanel)

        bottom = QtGui.QFrame(self)
        bottom.setFrameShape(QtGui.QFrame.StyledPanel)

        splitter = QtGui.QSplitter(QtCore.Qt.Vertical)
        splitter.addWidget(topright)
        
        splitter1 = QtGui.QSplitter(QtCore.Qt.Horizontal)
        splitter1.addWidget(self.cal)
        splitter1.addWidget(self.table)
        #~ splitter1.addWidget(topright)

        splitter2 = QtGui.QSplitter(QtCore.Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        hbox.addWidget(splitter2)
        self.setLayout(hbox)
        
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))

    def showDate(self):
        date = self.cal.selectedDate()
        self.label.setText(str(date.toPyDate()))
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.title)
        self.setLayout(vbox)

class DashbordTableWidget(DebtTableWidget):

    def __init__(self, parent, *args, **kwargs):

        DebtTableWidget.__init__(self, parent=parent, *args, **kwargs)
        self.header = [_(u"last_name"), _(u"first_name"), \
                        _(u"phone")]
        self.set_data_for()
        self.refresh(True)

    def set_data_for(self):
        self.data = [(op.first_name, op.last_name, op.phone)
            for op in session.query(Creditor).all()]
