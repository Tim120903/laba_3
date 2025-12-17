#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

EPS = 1e-10


if __name__ == '__main__':
    x = float(input("Enter x: "))
    n = int(input("Enter n(0,1,2): "))
    total = 0
    k = 0
    factor = (x / 2) ** n

    while True:
        chisl = (x * x / 4) ** k
        znam = math.factorial(k) * math.factorial(k + n)
        term = chisl / znam

        total += term

        if math.fabs(term) < EPS:
            break
        k += 1

    result = factor * total
    print(f'I_{n}({x}) = {result}')