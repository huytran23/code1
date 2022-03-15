def is_leap(year):
    leap = False
    if 1900 <= year <= 10e5:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    leap = True
                else:
                    leap = False
            else:
                leap = True
        else:
            leap = False
    else:
        leap = False
    return leap

year = int(input())
print(is_leap(year))