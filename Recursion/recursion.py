#!/usr/bin/env python
# coding=utf-8
import sys
sys.setrecursionlimit(10000)


def factorial(n):
    assert n>=0 and int(n) == n, 'The number must be positive integer only!'
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)


def main():

    print(factorial(10))

    return 0;

if __name__ == "__main__":

    main()
