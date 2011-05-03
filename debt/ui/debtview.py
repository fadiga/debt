#!usr/bin/env python
# -*- coding: utf-8 -*-
#maintainer: Fad


from datetime import datetime

from PyQt4 import QtGui, QtCore
from sqlalchemy import desc

from database import *
from utils import raise_success, raise_error
from dashbord import DashbordViewWidget
from common import DebtWidget, DebtPageTitle


class DebtViewWidget(QtGui.QDialog, DebtWidget):

    def __init__(self, parent, credit, *args, **kwargs):
        QtGui.QDialog.__init__(self, parent, *args, **kwargs)
        self.setWindowTitle((u"Add debt"))

        self.title = DebtPageTitle(u"Debt")

        # Edit
        self.des = QtGui.QLineEdit()
        self.startdate = QtGui.QDateTimeEdit(QtCore.QDate.currentDate())
        self.startdate.setDisplayFormat("dd-MM-yyyy")
        self.starttime = QtGui.QDateTimeEdit(QtCore.QTime.currentTime())
        self.starttime.setDisplayFormat("hh:mm")
        self.enddate = QtGui.QDateTimeEdit(QtCore.QDate.currentDate())
        self.enddate.setDisplayFormat("dd-MM-yyyy")
        self.endtime = QtGui.QDateTimeEdit(QtCore.QTime.currentTime())
        self.endtime.setDisplayFormat("hh:mm")
        self.amount = QtGui.QLineEdit()
        self.amount.setValidator(QtGui.QIntValidator())
        #Combobox widget
        self.box_creditor = QtGui.QComboBox()
        self.data_creditor = session.query(Creditor).order_by(desc(Creditor.id)).all()

        for index in xrange(0, len(self.data_creditor)):
            creditor = self.data_creditor[index]
            self.box_creditor.\
                addItem((u'%(last_name)s %(first_name)s tel : %(phone)s') %\
                            {'last_name': creditor.last_name,\
                             "first_name":creditor.first_name,\
                             "phone":creditor.phone})
        if credit is not None:
            self.box_creditor.setCurrentIndex(credit -1)

        desbox = QtGui.QFormLayout()
        desbox.addRow("Designation", self.des)

        formboxleft = QtGui.QFormLayout()
        formboxleft.addRow("Creditor", self.box_creditor)
        formboxleft.addRow("Amount", self.amount)
        formboxright = QtGui.QFormLayout()
        formboxright.addRow("Start date", self.startdate)
        formboxright.addRow("End date", self.enddate)
        formbox = QtGui.QFormLayout()
        formbox.addRow("Time", self.starttime)
        formbox.addRow("Time", self.endtime)

        button_hbox = QtGui.QHBoxLayout()
        butt = QtGui.QPushButton((u"Add"))
        butt.clicked.connect(self.add_debt)
        cancel_but = QtGui.QPushButton((u"Cancel"))
        cancel_but.clicked.connect(self.cancel)
        button_hbox.addWidget(butt)
        button_hbox.addWidget(cancel_but)

        hbox = QtGui.QHBoxLayout()
        hbox.addLayout(formboxleft)
        hbox.addLayout(formboxright)
        hbox.addLayout(formbox)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.title)
        vbox.addLayout(desbox)
        vbox.addLayout(hbox)
        vbox.addLayout(button_hbox)
        self.setLayout(vbox)

    def cancel(self):
        self.close()

    def add_debt(self):
        ''' add operation '''
        day, month, year = self.startdate.text().split('-')
        hour, minute = self.starttime.text().split(':')
        start_datetime = datetime(int(year), int(month),\
                                  int(day), int(hour), int(minute))
        day, month, year = self.enddate.text().split('-')
        hour, minute = self.endtime.text().split(':')
        end_datetime = datetime(int(year), int(month),\
                                int(day), int(hour), int(minute))
        if self.des and self.starttime and self.startdate\
                        and self.box_creditor and self.enddate\
                        and self.endtime and self.amount:
            debt = Debt(unicode(self.des.text()), unicode(self.amount.text()),\
                                            start_datetime, end_datetime)
            debt.creditor = self.data_creditor[self.box_creditor.currentIndex()]
            session.add(debt)
            session.commit()
            self.des.clear()
            self.amount.clear()
            self.change_main_context(DashbordViewWidget)
            self.close()
            raise_success((u'Confirmation'), (u'Registered opération'))
