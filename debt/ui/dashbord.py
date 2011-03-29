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
        
        vbox = QtGui.QVBoxLayout()
        
        vbox_cal = QtGui.QHBoxLayout(self.initUI())

        vbox_table = QtGui.QHBoxLayout()
        vbox_table.addWidget(self.table)
        
        vbox.addLayout(vbox_cal)
        vbox.addLayout(vbox_table)
        self.setLayout(vbox)
    
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
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.title)
        self.setLayout(vbox)

class DashbordTableWidget(DebtTableWidget):

    def __init__(self, parent, *args, **kwargs):

        DebtTableWidget.__init__(self, parent=parent, *args, **kwargs)
        self.header = [_(u"Date"), _(u"Type"), \
                        _(u"Valeur")]
        self.set_data_for()
        self.refresh(True)

    def set_data_for(self):
        self.data = [(op.first_name, op.last_name, op.phone)
            for op in session.query(Creditor).all()]
