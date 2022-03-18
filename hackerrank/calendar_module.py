import calendar

# https://www.hackerrank.com/challenges/calendar-module/problem
# Read input from STDIN. Print output to STDOUT
DAY = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
date = [int(i) for i  in (input().split(' '))]
d = calendar.weekday(date[2], date[0], date[1])
print (DAY[d])