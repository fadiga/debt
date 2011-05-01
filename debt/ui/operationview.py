#!usr/bin/env python
# -*- coding: utf-8 -*-
#maintainer: Fad


from datetime import datetime

from sqlalchemy import desc
from PyQt4 import QtGui, QtCore

from database import *
from common import DebtWidget, DebtPageTitle, DebtBoxTitle, DebtTableWidget


class OperationViewWidget(DebtWidget):

    def __init__(self, debt="", parent=0, *args, **kwargs):
        super(OperationViewWidget, self).__init__(parent=parent, *args, **kwargs)
        self.setWindowTitle((u"Add operation"))
        self.debt = debt
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(DebtPageTitle(u"Operation"))

        hbox = QtGui.QHBoxLayout()
        hbox1 = QtGui.QHBoxLayout()
        hbox2 = QtGui.QHBoxLayout()

        tablebox = QtGui.QVBoxLayout()
        tablebox.addWidget(DebtBoxTitle(u"Table opertion"))
        self.table_op = OperationTableWidget(parent=self)
        tablebox.addWidget(self.table_op)

        self.date_ = QtGui.QDateTimeEdit(QtCore.QDate.currentDate())
        self.date_.setDisplayFormat("dd-MM-yyyy")
        self.time = QtGui.QDateTimeEdit(QtCore.QTime.currentTime())
        self.time.setDisplayFormat("hh:mm")
        self.value_ = QtGui.QLineEdit()
        self.value_.setValidator(QtGui.QIntValidator())

        cretorbox = QtGui.QFormLayout()
        cretorbox.addWidget(DebtBoxTitle(u"Creditor info"))
        cretorbox.addRow("First nameane: ", QtGui.QLabel(self.debt.creditor.first_name))
        cretorbox.addRow("Last name: ", QtGui.QLabel(self.debt.creditor.last_name))
        cretorbox.addRow("Adress: ", QtGui.QLabel(self.debt.creditor.adress))
        cretorbox.addRow("Phone: ", QtGui.QLabel(self.debt.creditor.phone))

        formbox = QtGui.QFormLayout()
        formbox.addWidget(DebtBoxTitle(u"Add opertion"))
        formbox.addRow("Date", self.date_)
        formbox.addRow("time", self.time)
        formbox.addRow("Montant", self.value_)

        butt = QtGui.QPushButton((u"Add"))
        butt.clicked.connect(self.add_operation)
        formbox.addWidget(butt)
        hbox1.addLayout(formbox)
        hbox2.addLayout(cretorbox)
        hbox.addLayout(hbox1)
        hbox.addLayout(hbox2)
        vbox.addLayout(hbox)
        vbox.addLayout(tablebox)
        self.setLayout(vbox)

    def add_operation(self):
        ''' add operation '''
        debt = self.debt
        day, month, year = self.date_.text().split('-')
        hour, minute = self.time.text().split(':')
        datetime_ = datetime(int(year), int(month),\
                                int(day), int(hour),\
                                        int(minute))

        if self.date_ and self.time and self.value_:
            operation = Operation(unicode(self.value_.text()), \
                                        datetime_, debt)
            session.add(operation)
            session.commit()
            self.value_.clear()
            self.refresh()
            self.change_main_context(OperationViewWidget,debt)


class OperationTableWidget(DebtTableWidget):

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
