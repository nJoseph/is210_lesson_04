#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Looping mathematical calculations"""

TOTAL = 0
import data
for x in data.TRANSACTIONS:
    for y in x:
        TOTAL = TOTAL + y
    if y < TOTAL:
        MINIMUM = y
        
