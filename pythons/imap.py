#!/usr/bin/python
# -*- coding: utf-8 -*-

from functools import reduce

def normalize(name):
	return name.capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
	return reduce(lambda x, y : x * y, L)

r = prod([1, 2, 3])
print(r)
