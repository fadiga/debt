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
    operations = session.query(Operation).all()

    list_alert = [ (op.amount_paid, op.amount_paid)\
                    for op in session.query(Operation).all()]
    return list_alert

def testdate(date_op):
    datetoday = datetime.today()

    return
def debt_summary(debt):
    return (debt.creditor.first_name, debt.designation,\
                            debt.amount_debt, debt.end_date.strftime(u"%d/%B/%y %H:%M"),\
                            debt)
