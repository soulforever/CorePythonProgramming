#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Problem 6-2
Check if a input string is valid for variable
"""
__author__ = 'guti'

import string
import keyword

alphas = string.letters + '_'
nums = string.digits

print 'Welcome to the Identifier Checker v1.1'  # change version ^_^
print 'Testees must be at least 2 chars long.'
myInput = raw_input('Identifier to test?')

if len(myInput) > 1:
    if myInput[0] not in alphas:
        print 'Invalid: first symbol must be alphabetic.'
    elif myInput in keyword.kwlist:  # add to check if input is keyword
        print 'Invalid: keyword can not be a identifier.'
    else:
        for otherChar in myInput[1:]:
            if otherChar not in alphas+nums:
                print 'Invalid: remaining symbols must be alphanumberic.'
                break
        else:
            print 'Okay as an identifier.'
elif len(myInput) == 1:  # add to check single symbol
    if myInput in alphas:
        print 'Okay as an identifier.'
    else:
        print 'Invalid: single symbol must be alphabetic.'
else:
    print 'Invalid: empty input.'