#!/usr/bin/env python3

"""
Mandelbrot PNG renderer in Python
Copyright (c) 2014, Tyler Philbrick
All rights reserved
See COPYING for license information
"""

import argparse ## Will be used later for proper arguments

import png
from calculate import makeMandel


def mapImage(mandel):
	pngList = [[]]
	for i in mandel:
		if i is None:
			pngList.append([])
		else:
			pngList[-1].append(bool(i))
	return pngList

def writeImage(mapng, filename):
	with open(filename, "wb") as f:
		w = png.Writer(len(mapng[0]), len(mapng), greyscale=True, bitdepth=1)
		w.write(f, mapng)


if __name__ == "__main__":

	## Constant values temporary

	mandel = makeMandel([800, 500], [250, 250])
	mapping = mapImage(mandel)
	writeImage(mapping, "test.png")

