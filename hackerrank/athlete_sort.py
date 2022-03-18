#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/python-sort-sort/problem

if __name__ == '__main__':
    n = [int(x) for x  in (input().split(' '))]
    A = [[0 for x in range(n[1])] for x in range(n[0])] 
    for i in range(0,n[0]):
        A[i] = [int(x) for x  in (input().split(' '))]
    k = int(input())
    def getKey(item):
        return item[k]
    B = sorted(A, key=getKey)
    for i in range(n[0]):
        print (' '.join(str(x) for x in B[i]))