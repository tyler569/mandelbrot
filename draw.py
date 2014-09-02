#!/usr/bin/env python3

"""
Python Mandelbrot drawer
Copyright (c) 2014, Tyler Philbrick
All rights reserved
See COPYING for license information
"""

import os

from coord import MandelbrotCoord


if __name__ == "__main__":

	size = {"x": 100, "y": 30}
	cent = {"x": 35, "y": 15}

	for i in range(size["y"]):
		for j in range(size["x"]):
			cplx = complex(
				(cent["x"] - j) / cent["x"],
				(cent["y"] - i) / cent["y"]
			)
			m = MandelbrotCoord(cplx)
			print(m, end="")
		print()
