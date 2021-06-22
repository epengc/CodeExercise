#!/usr/bin/env python
# coding=utf-8
def number_power(base, exp):
    assert exp >= 1 and int(exp) == exp, "exp should be a positive integer."
    if exp == 0:
        return 1
    if exp ==1:
        return base
    return base*number_power(base, exp-1)

print(number_power(2, 0))
