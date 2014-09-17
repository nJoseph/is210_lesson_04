#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Analyzing a string"""

import data
KIM= data.SHAKESPEARE.split("\n")

print KIM[0]
MAXIMUM_WORDS=0
COUNT = 0
TEMP= 0
TEMP2= 0
NUM_CRISPIAN = 0
for x in data.SHAKESPEARE.split("\n"):
    if len(x.split()) > TEMP:
        MAXIMUM_WORDS= len(x.split())
        TEMP = len(x.split())
    COUNT = COUNT + 1
    if "Crispian" in x:
        NUM_CRISPIAN = NUM_CRISPIAN + 1

for y in data.SHAKESPEARE.split("\n"):
    if len(y.split()) < TEMP2:
        MIN = len(y.split())
    TEMP2= len(y.split())

print COUNT
print MAXIMUM_WORDS
print MIN
TOTAL_WORDS = len(data.SHAKESPEARE.split())
print TOTAL_WORDS
AVERAGE_WORDS = float(TOTAL_WORDS) / COUNT
print AVERAGE_WORDS
print NUM_CRISPIAN
