#!/usr/bin/env python
# encoding=utf-8
# maintainer: Fad

import gettext
from datetime import date, datetime

import sqlalchemy
from sqlalchemy import desc, func
from sqlalchemy.orm import exc

from database import *


def _(*args, **kwargs):
    return gettext.gettext(*args, **kwargs)


def alert():
    """ """
    list_alert = []
    dbets = session.query(Debt).all()
    datetoday = datetime.today()
    for debt in dbets:
        days_remaining = (datetime.today() - debt.end_date).days
        if days_remaining > - 5 and days_remaining < 0:
            list_alert.append((debt, u"%s days" % days_remaining))
        if days_remaining == 0:
            list_alert.append((debt, u"Today is the last days"))
        if days_remaining > 0:
            list_alert.append((debt, \
                                u"Le delais est expiré il y a %s days" %\
                                                        days_remaining))

    return list_alert


def debt_summary(debt):
    return (debt.creditor.first_name, debt.designation, debt.amount_debt,\
                        debt.end_date.strftime(u"%d/%B/%y %H:%M"), debt)


def remaining():
    pass
