#!/usr/bin/env python
# -*- coding: utf-8 -*-
#maintainer :fad

from PyQt4 import QtGui, QtCore
from gettext import gettext as _


from common import DebtWidget
from operationview import OperationViewWidget
from dashbord import DashbordViewWidget
from debtview import DebtViewWidget
from addcreditorview import CreditorViewWidget


class MenuBar(QtGui.QMenuBar, DebtWidget):

    def __init__(self, parent=None, *args, **kwargs):
        QtGui.QMenuBar.__init__(self, parent, *args, **kwargs)

        # change icon so that it appears in About box
        exit = QtGui.QAction(QtGui.QIcon('icons/exit.png'), 'Exit', self)
        #Menu File
        file = self.addMenu(_(u"&File"))
        # Delete
        self.delete = QtGui.QAction(_(u"Delete a statement"), self)
        self.connect(self.delete, QtCore.SIGNAL("triggered()"),\
                                            self.goto_delete_statement)
        self.delete.setEnabled(False)
        file.addAction(self.delete)

        # Print
        print_statement = QtGui.QAction(_(u"Print"), self)
        print_statement.setShortcut("Ctrl+P")
        self.connect(print_statement, QtCore.SIGNAL("triggered()"),\
                                            self.goto_print)
        file.addAction(print_statement)
        # Export
        export = file.addMenu(_(u"&Export data"))
        export.addAction(_(u"Backup Database"), self.goto_export_db)

        # Exit
        exit = QtGui.QAction(_(u"Exit"), self)
        exit.setShortcut("Ctrl+Q")
        exit.setToolTip(_("Exit application"))
        self.connect(exit, QtCore.SIGNAL("triggered()"), \
                                         self.parentWidget(), \
                                         QtCore.SLOT("close()"))
        file.addAction(exit)
        # Menu go to
        goto = self.addMenu(_(u"&Go to"))
        goto.addAction(_(u"Add Statement"),\
                                       self.goto_add_statement)
        goto.addAction(_(u"Add Debt"),\
                                       self.goto_add_debt)
        goto.addAction(_(u"Add creditor"),\
                                       self.goto_add_creditor)
        goto.addAction(_(u"Dashbord"),\
                                    self.goto_dashbord)

        #Menu help
        help = self.addMenu(_(u"Help"))
        help.addAction(_(u"About"), self.goto_about)

    #Print
    def goto_print(self):
        print u'print'

    def goto_add_statement(self):
        self.open_dialog(OperationViewWidget, modal=True)

    def goto_add_debt(self):
        self.open_dialog(DebtViewWidget, modal=True)

    def goto_add_creditor(self):
        self.open_dialog(CreditorViewWidget, modal=True)

    #Delete an operation.
    def goto_delete_statement(self):
        print u'delete'

    #Export the database.
    def goto_export_db(self):
        print 'export_database_as_file()'

    # dashbord
    def goto_dashbord(self):
        self.change_main_context(DashbordViewWidget)

    #About
    def goto_about(self):
        mbox = QtGui.QMessageBox.about(self, _(u"About Debt-M"), \
                          _(u"Debt-M Debt Management Software\n\n" \
                            u"© 2011 yɛlɛman s.à.r.l\n" \
                            u"Hippodrome, Avenue Al Quds, \n" \
                            u"BPE. 3713 - Bamako (Mali)\n" \
                            u"Tel: (223) 76 33 30 05\n" \
                            u"www.yeleman.com\n" \
                            u"info@yeleman.com\n\n" \
                            "Ibrahima Fadiga, \n"))
