#!/usr/bin/env python
# coding=utf-8

def d2b(n):
    if n//2 == 0:
        return n%2
    else:
        return n%2+10*(d2b(n//2))

print(d2b(13))
