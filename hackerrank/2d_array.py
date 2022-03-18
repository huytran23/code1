#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/2d-array/problem

def hourglassSum(arr):
    slist = []
    ro = len(arr) - 2
    co = len(arr[0]) - 2
    for i in range(ro):
        for j in range(co):
            s0 = 0
            submat = [[arr[b][a] for a in range(i,i+3) ] for b in range(j,j+3)]
            sumsub = sum(map(sum,submat))
            s0 = (sumsub) - (submat[1][0]) - (submat[1][2])
            slist.append(s0)
    return max(slist)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()