#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    a = int(input("Value a from 1 to 7: "))

    if a == 1:
        print("Monday")
    elif a == 2:
        print("Tuesday")
    elif a == 3:
        print("Wednesday")
    elif a == 4:
        print("Thursday")
    elif a == 5:
        print("Friday")
    elif a == 6:
        print("Saturday")
    elif a == 7:
        print("Sunday")
    else:
        print("Illegal value of a", file=sys.stderr)
        exit(1)





