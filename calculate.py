#!/usr/bin/env python3

"""
Python Mandelbrot drawer
Copyright (c) 2014, Tyler Philbrick
All rights reserved
See COPYING for license information
"""

import os


def make_mandel(size, cent, perms):

	for i in range(size[1]):
		for j in range(size[0]):
			cplx = complex(
				(cent[0] - j) / cent[0],
				(cent[1] - i) / cent[1]
			)
			
			z = 0
			for perm in range(perms):
				z = (z ** 2) + cplx
				if abs(z) > 25:
					ret = perm >> 6
					break
			else:
				ret = 0

			yield ret
		yield None
		print("\r", str(100 * i / size[1]) + "% complete", end="")
			

if __name__ == "__main__":
	size = [100, 30]
	cent = [35, 15]

	mandel = make_mandel(size, cent, 50)
	for i in mandel:
		if i is None:
			print()
		elif i is True:
			print(".", end="")
		else:
			print(" ", end="")
