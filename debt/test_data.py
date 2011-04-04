#!/usr/bin/env python
# encoding= utf-8
#maintainer : Fad

from datetime import date
from database import *

c = Creditor("Madou", "Fofana", "Boulcity", "6712132")
d = Debt("1 Moto ktm", 325000, datetime(2010, 10, 01,10,50),datetime(2011, 11, 20,18,20))
d.creditor = c

op = Operation(50000)
op.debt = d

c1 = Creditor("Alou", "Coulibaly", "sangarebougou", "75025441")
d1 = Debt("personal", 3000000, datetime(2011, 01, 01,10,50),datetime(2011, 02, 01,18,20))
d1.creditor = c1

op1 = Operation(150000)
op1.debt = d1
try:
    session.add_all((c, d, op))
    session.commit()
    print "YES"
except:
    session.rollback()
    print "oh no"
