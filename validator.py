#!/usr/bin/env python3
import sys

def sum_digits(digit):
    if digit < 10:
        return digit
    else:
        sum = (digit % 10) + (digit // 10)

    return sum

def validate(ccnum):
    ccnum = ccnum[::-1]

    ccnum = [int(x) for x in ccnum]
    dsd_list = list()
    digits = list(enumerate(ccnum, start=1))
    for index, digit in digits:
        if index % 2 == 0:
            dsd_list.append(digit *2)
        else:
            dsd_list.append(digit)
    
    dsd_list = [sum_digits(x) for x in dsd_list]
    sum_of_digits = sum(dsd_list)

    return sum_of_digits % 10 == 0

if len(sys.argv) < 2:
    print("You must supply a credit card number")
else:
    ccnum = sys.argv[1]
    print(validate(str(ccnum)))