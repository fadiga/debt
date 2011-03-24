#!/usr/bin/env python
# encoding= utf-8
#maintainer : Fad

from datetime import date
from database import *

start_date = datetime(2011, 01, 01)
end_date = datetime(2011, 03, 31)


c = Creditor("Madou", "Fofana", "Boulcity", "6712132")
d = Debt(1200000, start_date, end_date)
d.creditor = c

op = Operation(50000)
op.debt = d

session.add_all((c, d, op))
session.commit()
