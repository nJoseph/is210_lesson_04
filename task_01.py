#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Analyzing a string"""

import data
KIM= data.SHAKESPEARE.split("\n")

print KIM[0]
MAXIMUM_WORDS=0
COUNTER = 0
for x in data.SHAKESPEARE.split("\n"):
    if len(x.split()) < COUNTER:
        MAXIMUM_WORDS = len(x.split())
    COUNTER = COUNTER + 1

print COUNTER
print MAXIMUM_WORDS
