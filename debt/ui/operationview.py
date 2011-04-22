#!usr/bin/env python
# -*- coding: utf-8 -*-
#maintainer: Fad


from datetime import datetime

from PyQt4 import QtGui, QtCore

from database import *
from dashbord import DashbordViewWidget
from common import DebtWidget, DebtPageTitle, DebtTableWidget


class OperationViewWidget(DebtWidget):

    def __init__(self, parent=0, *args, **kwargs):
        super(OperationViewWidget, self).__init__(parent=parent, *args, **kwargs)
        self.setWindowTitle((u"Add operation"))

        self.title = DebtPageTitle(u"Operation")
        self.table_op = OperationTableWidget(parent=self)

        self.date_ = QtGui.QDateTimeEdit(QtCore.QDate.currentDate())
        self.date_.setDisplayFormat("dd-MM-yyyy")
        self.time = QtGui.QDateTimeEdit(QtCore.QTime.currentTime())
        self.time.setDisplayFormat("hh:mm")
        self.value_ = QtGui.QLineEdit()
        self.value_.setValidator(QtGui.QIntValidator())
        #Combobox widget
        self.box_type = QtGui.QComboBox()
        self.data_debt = session.query(Debt).all()
        for index in xrange(0, len(self.data_debt)):
            debt = self.data_debt[index]
            self.box_type.\
            addItem((u'%(last_name)s %(first_name)s pour%(amount)s le %(date)s')\
                        % {'last_name': debt.creditor.last_name,\
                             "first_name":debt.creditor.first_name,\
                             "amount":debt.amount_debt,\
                             "date":debt.start_date})

        formbox = QtGui.QFormLayout()
        formbox.addRow("Date", self.date_)
        formbox.addRow("time", self.time)
        formbox.addRow("Debt", self.box_type)
        formbox.addRow("Montant", self.value_)
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.table_op)
        butt = QtGui.QPushButton((u"Add"))
        butt.clicked.connect(self.add_operation)
        formbox.addWidget(butt)
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.title)

        vbox.addLayout(formbox)
        #~ vbox.addLayout(editbox)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def add_operation(self):
        ''' add operation '''
        day, month, year = self.date_.text().split('-')
        hour, minute = self.time.text().split(':')
        datetime_ = datetime(int(year), int(month),\
                                int(day), int(hour),\
                                        int(minute))

        if self.date_ and self.time and self.type_ and self.value_:
            operation = Operation(unicode(self.value_.text()), \
                            datetime_,\
                            self.data_debt[self.box_type.currentIndex()])
            session.add(operation)
            session.commit()
            self.value_.clear()
            self.change_main_context(OperationViewWidget)


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
