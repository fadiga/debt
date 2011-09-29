#!/usr/bin/env python
# -*- coding: utf-8 -*-
#maintainer : Fad

import sys
import gettext
import locale

from gettext import gettext as _
from PyQt4 import QtCore, QtGui

import gettext_windows
from ui.mainviews import MainWindows


if __name__ == "__main__":
    gettext_windows.setup_env()
    locale.setlocale(locale.LC_ALL, '')

    gettext.install('debt', localedir='locale', unicode=True)
    app = QtGui.QApplication(sys.argv)
    qb = MainWindows()
    qb.show()
    sys.exit(app.exec_())
