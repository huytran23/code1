#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisors' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
# https://www.hackerrank.com/challenges/sherlock-and-divisors/problem

even = lambda x: x & 1 == 0

def f(x):
    div = 1
    ret = 0
    while div * div < x:
        if x % div == 0:
            if even(div):
                ret += 1
            if even(x // div):
                ret += 1
        div += 1
    if div * div == x and even(div):
        ret += 1
    return ret

t = int(input())
for _ in range(t):
    print(f(int(input())))
