#!/usr/bin/env python
# coding=utf-8

def gcd(q1, q2):
    assert int(q1) == q1 and int(q2) == q2, 'The numbers must be integer only!'

    if q1 < 0:
        q1 = -1*q1
    if q2 < 0:
        q2 = -1*q2

    if q1%q2 == 0:
        return q2
    else:
        return gcd(q2, q1%q2)

print(gcd(32, 16))
