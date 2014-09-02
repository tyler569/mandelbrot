"""
MandelbrotCoord class for my Mandelbrot drawer
Copyright (c) 2014, Tyler Philbrick
All rights reserved
See COPYING for license information
"""

class MandelbrotCoord(object):
	def __init__(self, val: complex, perms=50, max=50):
		self.val = val
		self.perms = perms
		self.max = max

		self.bool = self.in_set()

	def in_set(self):
		z = 0
		c = self.val
		for perm in range(self.perms):
			z = z**2 + c
			if abs(z) > self.max:
				return False
		return True

	def __bool__(self):
		return self.bool

	def __str__(self):
		if self.bool:
			return "·"
		else:
			return " "
