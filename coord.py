"""
MandelbrotCoord class for my Mandelbrot drawer
Copyright (c) 2014, Tyler Philbrick
All rights reserved
See COPYING for license information
"""

def in_set(cplx, perms):
	z = 0
	c = cplx
	for perm in range(perms):
		z = z**2 + c
		if abs(z) > 25:
			return False
	return True

