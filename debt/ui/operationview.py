#!usr/bin/env python
# -*- coding: utf-8 -*-
#maintainer: Fad


from datetime import datetime

from PyQt4 import QtGui, QtCore

from database import *
from dashbord import DashbordViewWidget
from common import DebtWidget, DebtPageTitle


class OperationViewWidget(QtGui.QDialog, DebtWidget):

    def __init__(self, parent=0, *args, **kwargs):
        QtGui.QDialog.__init__(self, parent, *args, **kwargs)
        self.setWindowTitle((u"Add operation"))

        self.title = DebtPageTitle(u"Operation")

        formbox = QtGui.QFormLayout()
        self.date_ = QtGui.QDateTimeEdit(QtCore.QDate.currentDate())
        self.date_.setDisplayFormat("dd-MM-yyyy")
        self.time = QtGui.QDateTimeEdit(QtCore.QTime.currentTime())
        self.time.setDisplayFormat("hh:mm")
        self.type_ = QtGui.QLineEdit()
        self.value_ = QtGui.QLineEdit()
        self.value_.setValidator(QtGui.QIntValidator())

        #~ self.label.move(130, 100)
        titelebox = QtGui.QHBoxLayout()
        titelebox.addWidget(QtGui.QLabel((u'Date')))
        titelebox.addWidget(QtGui.QLabel((u'time')))
        titelebox.addWidget(QtGui.QLabel((u'Debt')))
        titelebox.addWidget(QtGui.QLabel((u'Montant')))

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

        editbox = QtGui.QHBoxLayout()
        editbox.addWidget(self.date_)
        editbox.addWidget(self.time)
        editbox.addWidget(self.box_type)
        editbox.addWidget(self.value_)

        button_hbox = QtGui.QHBoxLayout()
        butt = QtGui.QPushButton((u"Add"))
        butt.clicked.connect(self.add_operation)
        cancel_but = QtGui.QPushButton((u"Cancel"))
        cancel_but.clicked.connect(self.cancel)
        button_hbox.addWidget(butt)
        button_hbox.addWidget(cancel_but)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.title)

        vbox.addLayout(titelebox)
        vbox.addLayout(formbox)
        vbox.addLayout(editbox)
        vbox.addLayout(button_hbox)
        self.setLayout(vbox)

    def cancel(self):
        self.close()

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
            self.change_main_context(DashbordViewWidget)
