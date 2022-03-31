#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gamingArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def gamingArray(arr):
	# cur_l = len(arr)
	# cur_arr = arr
	# c, cur_max, cur_id = 0, 0, 0
	# for i in range(len(arr)):
	# 	cur_max = max(cur_arr)
	# 	cur_id = cur_arr.index(cur_max)
	# 	cur_arr = cur_arr[:cur_id]
	# 	cur_l = len(cur_arr)
	# 	c += 1
	# 	if cur_l == 0:
	# 		print(c)
	# 		if (c % 2) == 0:
	# 			return 'ANDY'
	# 		else:
	# 			return 'BOB'
	if (len(arr) == 1):
		return 'BOB'
	else:
		c = 0
		cur_max = -float("inf")
		for i, num in enumerate(arr):
			if num > cur_max:
				cur_max = num
				c += 1
		if (c % 2) == 0:
			return 'ANDY'
		else:
			return 'BOB'

g = int(input().strip())

for g_itr in range(g):
	arr_count = int(input().strip())

	arr = list(map(int, input().rstrip().split()))

	result = gamingArray(arr)

	print(result)
