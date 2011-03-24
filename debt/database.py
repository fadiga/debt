#!/usr/bin/env python
# encoding=utf-8
# maintainer: Fad

#~ import gettext

from datetime import date, datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import mapper, relationship
from sqlalchemy import Table, Column, Integer, String, \
                       MetaData, ForeignKey, Date, DateTime, Unicode

DB_FILE = 'debt.db'

engine = create_engine('sqlite:///%s' % DB_FILE, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

metadata = MetaData()


creditors_table = Table('creditor', metadata,
    Column('id', Integer, primary_key=True),
    Column('last_name', Unicode(100)),
    Column('first_name', Unicode(100)),
    Column('adress', Unicode(100)),
    Column('phone', Unicode(10)),
)


debts_table = Table('debt', metadata,
    Column('id', Integer, primary_key=True),
    Column('creditor_id', Integer, ForeignKey('creditor.id')),
    Column('amount_debt', Integer),
    Column('start_date', Date),
    Column('end_date', Date),
)

operations_table = Table('operation', metadata,
    Column('id', Integer, primary_key=True),
    Column('debt_id', Integer, ForeignKey('debt.id')),
    Column('amount_paid', Integer),
    Column('registered_on', Date, nullable=True),
)

metadata.create_all(engine)


class Creditor(object):

    def __init__(self, first_name, last_name, adress, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.adress = adress
        self.phone = phone

    def __repr__(self):
        return ("<Creditor('%(first_name)s')>") %\
        {'first_name': self.first_name}

    def __unicode__(self):
        return (u"%(last_name)s") % {'name': self.last_name}


class Debt(object):

    def __init__(self, amount_debt, start_date, end_date, creditor=None):
        self.creditor = creditor
        self.amount_debt = amount_debt
        self.start_date = start_date
        self.end_date = end_date

    def __reper__(object):
        return ("<Debt('%(creditor)s')>,'%(amount_debt)s')>") %\
                {'amount_debt': self.amount_debt}

    def __unicde__(self):
        return (u"%(creditor)s %(amount_debt)s") % {'creditor': self.creditor,\
                    'amount_date': self.amount_date}


class Operation(object):

    def __init__(self, amount_paid, \
                 registered_on=datetime.now(), debt=None):
        self.debt = debt
        self.amount_paid = amount_paid
        self.registered_on = registered_on

    def __repr__(self):
        return ("<Operation('%(registered_on)s','%(amount_paid)s')>") \
                 % {'registered_on': self.registered_on,\
                  'amount_paid': self.amount_paid}

    def __unicode__(self):
        return (u"%(debt)s %(date)s: %(amount_paid)s") % {'debt': self.debt,\
                  'amount_paid': self.amount_paid, \
                  'registered_on': self.amount_date.strftime('%F')}


mapper(Creditor, creditors_table, properties={
    'debts': relationship(Debt, backref='creditor')
    })

mapper(Debt, debts_table, properties={
    'operations': relationship(Operation, backref='debt')
    })

mapper(Operation, operations_table)
