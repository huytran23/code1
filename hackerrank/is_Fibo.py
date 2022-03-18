#!/bin/python3

import os
import sys
import math

# https://www.hackerrank.com/challenges/is-fibo/problems
def is_square(x):
    return math.sqrt(x).is_integer()
def isFib(a):
    return is_square(5*a*a + 4) or is_square(5*a*a - 4)
n = int(input())
for i in range(n):
    num = int(input())
    if (isFib(num) == True):
        print ('IsFibo')
    else:
        print ('IsNotFibo')
