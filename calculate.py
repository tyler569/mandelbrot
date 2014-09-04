#!/usr/bin/env python3

"""
Python Mandelbrot drawer
Copyright (c) 2014, Tyler Philbrick
All rights reserved
See COPYING for license information
"""

import os

from coord import MandelbrotCoord


def makeMandel(size, cent):

	for i in range(size[1]):
		for j in range(size[0]):
			cplx = complex(
				(cent[0] - j) / cent[0],
				(cent[1] - i) / cent[1]
			)
			m = MandelbrotCoord(cplx)
			yield m
		yield None

if __name__ == "__main__":
	size = [100, 30]
	cent = [35, 15]

	mandel = makeMandel(size, cent)
	for i in mandel:
		if i is None:
			print()
		else:
			print(i, end="")
