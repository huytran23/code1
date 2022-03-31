#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2):
	set1 = set(list(s1))
	set2 = set(list(s2))
	set_difference = set1 - set2
	if (set_difference == set1):
		return 'NO'
	else:
		return 'YES'

q = int(input().strip())

for q_itr in range(q):
	s1 = input()
	s2 = input()
	result = twoStrings(s1, s2)
	print(result)