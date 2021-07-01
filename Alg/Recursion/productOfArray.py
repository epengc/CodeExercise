#!/usr/bin/env python
# coding=utf-8
def productOfArray(arr):
    if not arr:
        return 1
    else:arr.pop()*productOfArray(arr)

print(productOfArray([1,2,3]))
