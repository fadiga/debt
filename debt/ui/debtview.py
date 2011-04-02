#!usr/bin/env python
# -*- coding: utf-8 -*-
#maintainer: Fad


from datetime import datetime

from PyQt4 import QtGui, QtCore

from database import *
from dashbord import DashbordViewWidget
from common import DebtWidget, DebtPageTitle


class DebtViewWidget(QtGui.QDialog, DebtWidget):

    def __init__(self, parent=0, *args, **kwargs):
        QtGui.QDialog.__init__(self, parent, *args, **kwargs)
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

        #~ self.label.move(130, 100)
        #Combobox widget
        self.box_type = QtGui.QComboBox()
        self.data_creditor = session.query(Creditor).all()

        for index in xrange(0, len(self.data_creditor)):
            creditor = self.data_creditor[index]
            self.box_type.addItem((u'%(last_name)s %(first_name)s tel : %(phone)s') %\
                            {'last_name': creditor.last_name,\
                             "first_name":creditor.first_name,\
                             "phone":creditor.phone})
        formboxleft = QtGui.QFormLayout()
        formboxleft.addRow("Creditor", self.box_type)
        formboxleft.addRow("Designation", self.des)
        formboxleft.addRow("Amount", self.amount)
        formboxright = QtGui.QFormLayout()
        formboxright.addRow("Start date", self.startdate)
        formboxright.addRow("Start time", self.starttime)
        formboxright.addRow("End date", self.enddate)
        formboxright.addRow("End time", self.endtime)

        button_hbox = QtGui.QHBoxLayout()
        butt = QtGui.QPushButton((u"Add"))
        butt.clicked.connect(self.add_operation)
        cancel_but = QtGui.QPushButton((u"Cancel"))
        cancel_but.clicked.connect(self.cancel)
        button_hbox.addWidget(butt)
        button_hbox.addWidget(cancel_but)
        cancel_but.move(30, 10)
        hbox = QtGui.QHBoxLayout()
        hbox.addLayout(formboxleft)
        hbox.addLayout(formboxright)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.title)
        vbox.addLayout(hbox)
        vbox.addLayout(button_hbox)

        self.setLayout(vbox)

    def cancel(self):
        self.close()

    def add_operation(self):
        ''' add operation '''
        pass
