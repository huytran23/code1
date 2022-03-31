#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
	# Write your code here
	num=int(input())
	pet=[]
	dist=[]
	for line in range(num):
		i=input().split(" ")
		pet.append(int(i[0]))
		dist.append(int(i[1]))
	bal=[]
	for i in range(num):
		bal.append(pet[i]-dist[i])

	small=0    
	for strt in range(num):
		s=bal[strt]
		i=(strt+1)%num
		while(s>=0 and i!=strt): 
			s+=bal[i]    
			i=(i+1)%num
		if(i==strt):
			small=strt
			break
			
	print(small)


n = int(input().strip())

petrolpumps = []

for _ in range(n):
	petrolpumps.append(list(map(int, input().rstrip().split())))

	result = truckTour(petrolpumps)

	print(result)