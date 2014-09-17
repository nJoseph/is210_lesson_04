#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Prompting in a loop"""

import data
ACCESS = False
COUNT = 3

while ACCESS == False:
    INPUT=raw_input("What is your password? {n} attempts left.".format(n=COUNT))
    if INPUT == data.PASSWORD:
        print "Access is granted"
        ACCESS = True
    elif INPUT != data.PASSWORD:
        COUNT= COUNT - 1
    if COUNT == 0:
        print "Access is denied, please try again later"
        break
    
