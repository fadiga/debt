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
        self.table = DebtsTableWidget(parent=self)
        self.table1 = OperationTableWidget(parent=self)
        self.table3 = AlertTableWidget(parent=self)

        #Calandar
        self.vbox = QtGui.QVBoxLayout(self)

        self.cal = QtGui.QCalendarWidget(self)
        self.cal.setGridVisible(True)
        #~ self.cal.move(20, 30)
        #~ self.cal.setGeometry(0, 0, 10, 10)
        self.connect(self.cal, QtCore.SIGNAL('selectionChanged()'), self.showDate)
        self.label = QtGui.QLabel(self)
        date = self.cal.selectedDate()
        self.label.setText(str(date.toPyDate()))
        self.label.move(130, 560)
        #--------------------

        topleft = QtGui.QFrame(self)
        topleft.setFrameShape(QtGui.QFrame.StyledPanel)

        topright = QtGui.QFrame(self)
        topright.setFrameShape(QtGui.QFrame.StyledPanel)

        splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)
        splitter.addWidget(self.title)
        splitter.addWidget(self.cal)
        splitter.addWidget(self.table)
        splitter.addWidget(self.table1)

        splitter1 = QtGui.QSplitter(QtCore.Qt.Vertical)
        splitter1.addWidget(self.table3)

        splitter2 = QtGui.QSplitter(QtCore.Qt.Vertical)
        splitter2.addWidget(self.title)
        splitter2.addWidget(splitter)
        splitter2.addWidget(splitter1)

        self.vbox.addWidget(splitter2)
        self.setLayout(self.vbox)

        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))

    def showDate(self):
        date = self.cal.selectedDate()
        self.label.setText(str(date.toPyDate()))
        self.setLayout(self.vbox)

class DebtsTableWidget(DebtTableWidget):

    def __init__(self, parent, *args, **kwargs):

        DebtTableWidget.__init__(self, parent=parent, *args, **kwargs)
        self.header = [_(u"first_name"), _(u"Designation"), \
                        _(u"Amount"), _(u"End date")]
        self.set_data_for()
        self.refresh(True)


    def set_data_for(self):
        debts = session.query(Debt).all()
        if len(debts) > 0:
            self.data = [(db.creditor.first_name, db.designation,\
                            db.amount_debt, db.end_date) for db in \
                            session.query(Debt).all()]


class OperationTableWidget(DebtTableWidget):

    def __init__(self, parent, *args, **kwargs):

        DebtTableWidget.__init__(self, parent=parent, *args, **kwargs)
        self.header = [_(u"last_name"), _(u"first_name"), \
                        _(u"Amount paid")]
        self.set_data_for()
        self.refresh(True)


    def set_data_for(self):
        operations = session.query(Operation).all()
        if len(operations) > 0:
            self.data = [(op.debt.creditor.last_name, \
            op.debt.creditor.first_name, op.amount_paid)
                for op in operations]

class AlertTableWidget(DebtTableWidget):

    def __init__(self, parent, *args, **kwargs):

        DebtTableWidget.__init__(self, parent=parent, *args, **kwargs)
        self.header = [_(u"last_name"), _(u"first_name"), \
                        _(u"Amount paid")]
        self.set_data_for()
        self.refresh(True)

    def set_data_for(self):
        #~ self.data = [(op.debt.creditor.last_name, \
        #~ op.debt.creditor.first_name, op.amount_paid)
            #~ for op in session.query(Operation).all()]
        pass
