#!/usr/bin/env python3

"""
Mandelbrot PNG renderer in Python
Copyright (c) 2014, Tyler Philbrick
All rights reserved
See COPYING for license information
"""

import argparse ## Will be used later for proper arguments

import png
from calculate import make_mandel


def map_image(mandel):
	png_list = [[]]
	for i in mandel:
		if i is None:
			png_list.append([])
		else:
			png_list[-1].append(bool(i))
	return png_list

def write_image(mapng, filename):
	with open(filename, "wb") as f:
		w = png.Writer(len(mapng[0]), len(mapng), greyscale=True, bitdepth=1)
		w.write(f, mapng)


if __name__ == "__main__":

	## Constant values temporary

	mandel = make_mandel([800, 500], [250, 250], 30)
	mapping = map_image(mandel)
	write_image(mapping, "test.png")

