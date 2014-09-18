#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Looping mathematical calculations"""

LEAST = 0
COUNTER = 1
TOTAL = 0
MAXIMUM = 0
import data
for x in data.TRANSACTIONS:
    for y in x:
        TOTAL = TOTAL + y

for z in data.TRANSACTIONS:
    if z > data.TRANSACTIONS[COUNTER]:
        MAX = z
        COUNTER = COUNTER + 1

for y in MAX:
    MAXIMUM = MAXIMUM + y

