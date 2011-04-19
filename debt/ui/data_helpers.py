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
    list_alert = [ (op.amount_paid, op.amount_paid)\
                    for op in session.query(Operation).all()]

