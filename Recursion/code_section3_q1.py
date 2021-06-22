#!/usr/bin/env python
# coding=utf-8

def digits_sum(n):
    assert n>=0 and int(n)==n, "the input number should be the non negative number"
    if n < 10:
        return n
    else:
        return n%10+digits_sum(int(n/10))


print(digits_sum(1))
