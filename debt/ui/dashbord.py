#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: Fad

from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import Qt

from database import *

from common import DebtWidget, DebtPageTitle, DebtTableWidget
from operationview import OperationViewWidget


class DashbordViewWidget(DebtWidget):
    def __init__(self, parent=0, *args, **kwargs):
        super(DashbordViewWidget, self).__init__(parent=parent,
                                                        *args, **kwargs)
        self.title = DebtPageTitle(u"Dashbord")
        self.table_debts = DebtsTableWidget(parent=self)
        self.table_alert = AlertTableWidget(parent=self)

        self.vbox = QtGui.QVBoxLayout(self)

        #Calandar
        self.cal = QtGui.QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.connect(self.cal, QtCore.SIGNAL('selectionChanged()'), self.showDate)
        self.label = QtGui.QLabel(self)
        date = self.cal.selectedDate()
        #--------------------

        topleft = QtGui.QFrame(self)
        topleft.setFrameShape(QtGui.QFrame.StyledPanel)

        topright = QtGui.QFrame(self)
        topright.setFrameShape(QtGui.QFrame.StyledPanel)

        splitter_left = QtGui.QSplitter(QtCore.Qt.Horizontal)
        splitter_left.addWidget(self.cal)
        splitter_left.resize(10, 50)
        splitter_left.addWidget(self.table_debts)


        splitter_down = QtGui.QSplitter(QtCore.Qt.Vertical)
        splitter_down.addWidget(self.table_alert)
        splitter_down.resize(900, 650)

        splitter = QtGui.QSplitter(QtCore.Qt.Vertical)
        splitter.addWidget(splitter_left)
        splitter.addWidget(splitter_down)

        self.vbox.addWidget(self.title)
        self.vbox.addWidget(splitter)
        self.setLayout(self.vbox)

        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))

    def showDate(self):
        date = self.cal.selectedDate()
        self.label.setText(str(date.toPyDate()))
        self.label.move(180, 25)
        #~ print str(date.toPyDate()),"date"


class DebtsTableWidget(DebtTableWidget):

    def __init__(self, parent, *args, **kwargs):

        DebtTableWidget.__init__(self, parent=parent, *args, **kwargs)
        self.header = [(u"first_name"), (u"Designation"), \
                        (u"Amount"), (u"End date"), \
                        (u"Go")]
        self.set_data_for()
        self.refresh(True)


    def set_data_for(self):
        debts = session.query(Debt).all()
        if len(debts) > 0:
            self.data = [(db.creditor.first_name, db.designation,\
                            db.amount_debt, db.start_date, db.end_date) for db in debts]

    def _item_for_data(self, row, column, data, context=None):
        if column == self.data[0].__len__() - 1:
            return QtGui.QTableWidgetItem(QtGui.QIcon("icons/go-next.png"), \
                                          (u"Operations"))

        return super(DebtsTableWidget, self)\
                                    ._item_for_data(row, column, data, context)

    def click_item(self, row, column, *args):
        last_column = self.header.__len__() - 1
        if column != last_column:
            return
        try:
            self.parent.change_main_context(OperationViewWidget, \
                                        debt=self.data[row][last_column])
        except IndexError:
            pass

class AlertTableWidget(DebtTableWidget):

    def __init__(self, parent, *args, **kwargs):

        DebtTableWidget.__init__(self, parent=parent, *args, **kwargs)
        self.header = [(u"last_name"), (u"first_name"), \
                        (u"Amount paid")]
        self._title = [("fad")]
        self.set_data_for()
        self.refresh(True)

    def set_data_for(self):
        self.data = [(op.debt.creditor.last_name, \
        op.debt.creditor.first_name, op.amount_paid)
            for op in session.query(Operation).all()]
