"""
MandlebrotCoord class for my Mandlebrot drawer
Copyright (c) 2014, Tyler Philbrick
All rights reserved
See COPYING for license information
"""

class MandlebrotCoord(object):
	def __init__(self, val: complex, iter_=50):
		self.val = val
		self.iter = iter_

		self.bool = self.in_set()

	def in_set(self):
		z = 0
		c = self.val
		for perm in range(self.iter):
			z = z**2 + c
			if abs(z) > 50:
				return False
		return True

	def __bool__(self):
		return self.bool

	def __str__(self):
		if self.bool:
			return "·"
		else:
			return " "
