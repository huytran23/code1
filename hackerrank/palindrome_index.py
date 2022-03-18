#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def check_palindrome(s):
	l = len(s)
	if (l < 2):
		return True
	elif (s[0] == s[l - 1]):
		return check_palindrome(s[1: l - 1])
	else:
		return False

def palindromeIndex(s):
	l = len(s)
	i = 0
	j = l-1
	while i<l:
		if s[i]!=s[j]:
			break
		i+=1
		j-=1
	if i>j: return -1
	a = i+1
	b = j
	while a<j and b>i+1:
		if s[a]!=s[b]:
			return j
		a+=1
		b-=1
	return i
	# if (l < 2):
	# 	return -1
	# else:
	# 	if (check_palindrome(s) == True):
	# 		return -1
	# 	else:
	# 		for i in range(l):
	# 			temp_s = ''.join([s[j] for j in range(l) if j != i])
	# 			if (check_palindrome(temp_s) == True):
	# 				return i
	# 			elif (i == (l-1) and check_palindrome(temp_s) == False):
	# 				return -1

    

q = int(input().strip())
for q_itr in range(q):
	s = input().strip()
	result = palindromeIndex(s)
	print (result)
