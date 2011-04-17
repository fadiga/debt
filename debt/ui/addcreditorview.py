#!usr/bin/env python
# -*- coding: utf-8 -*-
#maintainer: Fad


from datetime import datetime

from PyQt4 import QtGui, QtCore

from database import *
from dashbord import DashbordViewWidget
from common import DebtWidget, DebtPageTitle
from debtview import DebtViewWidget


class CreditorViewWidget(QtGui.QDialog, DebtWidget):

    def __init__(self, parent=0, *args, **kwargs):
        QtGui.QDialog.__init__(self, parent, *args, **kwargs)
        self.title = DebtPageTitle(u"Creditor")

        formbox = QtGui.QFormLayout()

        self.first_name = QtGui.QLineEdit()
        self.last_name = QtGui.QLineEdit()
        self.adress = QtGui.QLineEdit()
        self.phone = QtGui.QLineEdit()

        formbox.addRow("first_name", self.first_name)
        formbox.addRow("last_name", self.last_name)
        formbox.addRow("adresse", self.adress)
        formbox.addRow("phone", self.phone)

        button_hbox = QtGui.QHBoxLayout()
        butt = QtGui.QPushButton((u"Next"))
        butt.clicked.connect(self.add_creditor)
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

    def add_creditor(self):
        ''' add creditor '''
        if self.first_name and self.last_name and self.adress and self.phone:
            creditor = Creditor(unicode(self.first_name.text()),\
                                    unicode(self.last_name.text()),\
                                    unicode(self.adress.text()), \
                                    unicode(self.phone.text()), \
                                    )
            session.add(creditor)
            session.commit()
            self.first_name.clear()
            self.last_name.clear()
            self.adress.clear()
            self.phone.clear()
            self.change_main_context(DashbordViewWidget)
            self.close()
            self.open_dialog(DebtViewWidget, modal=True, credit = None)
