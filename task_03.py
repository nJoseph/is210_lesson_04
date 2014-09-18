#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Looping mathematical calculations"""

LEAST = None
COUNTER = 0
TOTAL = 0
MAXIMUM = 0
COUNT = 0
import data
for x in data.TRANSACTIONS:
    for y in x:
        TOTAL = TOTAL + y

for z in data.TRANSACTIONS:
    if sum(z) > COUNTER:
        MAXIMUM = sum(z)
        COUNTER = sum(z)

for k in data.TRANSACTIONS:
    if sum(k) < COUNT:
        MINIMUM = sum(k)
        COUNT = sum(k)
        
                    


