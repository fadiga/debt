#!usr/bin/env python
# -*- coding: utf-8 -*-
#maintainer: Fad

from PyQt4 import QtGui, QtCore
from sqlalchemy import desc

from database import *
from dashbord import DashbordViewWidget
from common import DebtWidget, DebtPageTitle
from debtview import DebtViewWidget
from addcreditorview import CreditorViewWidget


class addViewWidget(QtGui.QDialog, DebtWidget):

    def __init__(self, parent=0, *args, **kwargs):
        QtGui.QDialog.__init__(self, parent, *args, **kwargs)
        self.title = DebtPageTitle(u"Choose")

        formbox = QtGui.QFormLayout()

        #Combobox widget
        self.box_type = QtGui.QComboBox()
        self.data_creditor = session.query(Creditor).order_by(desc(Creditor.id)).all()
        self.box_type.addItem(u"Nouveau")
        for index in xrange(0, len(self.data_creditor)):
            creditor = self.data_creditor[index]
            self.box_type.addItem((u"%(last_name)s %(first_name)s pour%(phone)s") %\
                            {'last_name': creditor.last_name,\
                             "first_name": creditor.first_name,\
                             "phone":creditor.phone})

        formbox.addRow("Creator", self.box_type)

        button_hbox = QtGui.QHBoxLayout()
        butt = QtGui.QPushButton((u"Next"))
        butt.clicked.connect(self.goto_next)
        cancel_but = QtGui.QPushButton((u"Cancel"))
        cancel_but.clicked.connect(self.cancel)
        button_hbox.addWidget(butt)
        button_hbox.addWidget(cancel_but)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.title)

        vbox.addLayout(formbox)
        vbox.addLayout(button_hbox)
        self.setLayout(vbox)

    def cancel(self):
        self.close()
    def goto_next(self):
        if self.box_type.currentIndex() == 0:
            self.open_dialog(CreditorViewWidget, modal=True)
        else:
            self.open_dialog(DebtViewWidget, modal=True)
