#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    a = float(input("Value a from 0 to 1: "))
    b = float(input("Value a from 0 to 1: "))
    c = float(input("Value a from 0 to 1: "))

    if 0 < a < 1:
        print("The correct value", a)

    if 0 < b < 1:
        print("The correct value", b)

    if 0 < c < 1:
        print("The correct value", c)

    if not (0 < a < 1 or 0 < b < 1 or 0 < c < 1):
        print("Error: No values in range (0, 1)", file=sys.stderr)
        exit(1)
