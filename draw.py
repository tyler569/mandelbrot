#!/usr/bin/env python3

"""
Python Mandlebrot drawer
Copyright (c) 2014, Tyler Philbrick
All rights reserved
See COPYING for license information
"""

import os

from coord import MandlebrotCoord


if __name__ == "__main__":

	size = {
		"x": 60,
		"y": 100
	}
	cent = {
		"x": 20,
		"y": 50
	}

	for i in range(size["x"]):
		for j in range(size["y"]):
			cplx = complex(
				((cent["x"] - i) / cent["x"]),
				((cent["y"] - j) / cent["y"])
			)
			m = MandlebrotCoord(cplx)
			print(m, end="")
		print()

