# Kuriakose Sony Theakanath
# Project 4
# Seam Carving

import numpy as np
from scipy import ndimage
from scipy import misc
from PIL import Image
import itertools
import sys

# Main Algorithm
# image - image to carve, dim - dimensions of new image to carve
def seam_carving(im, dimensions):
	horiz_vertic = [True, True]
	while True in horiz_vertic:
		if dimensions[1] != im.shape[1]:
			allpaths = reduce(lambda a, b: a + b, (seam["finalized_path"] for seam in seam_finder(ndimage.filters.laplace(im.sum(axis=-1) / 3.) ** 2)[:abs(im.shape[1] - dimensions[1])]))
			im[zip(*allpaths)] = -1
			im = im[im >= 0].reshape((im.shape[0], im.shape[1] - len(allpaths) // im.shape[0], im.shape[2]))
		else:
			horiz_vertic[1] = False
		if dimensions[0] != im.shape[0]:
			allpaths = reduce(lambda a, b: a + b, (seam["finalized_path"] for seam in seam_finder(ndimage.filters.laplace((im.sum(axis=-1) / 3.).T) ** 2)[:abs(im.shape[0] - dimensions[0])]))
			im.swapaxes(0, 1)[zip(*allpaths)] = -1
			im = im.swapaxes(0, 1)[im.swapaxes(0, 1) >= 0].reshape((im.swapaxes(0, 1).shape[0], im.swapaxes(0, 1).shape[1] - len(allpaths) // im.swapaxes(0, 1).shape[0], im.swapaxes(0, 1).shape[2])).swapaxes(0,1)
		else:
			horiz_vertic[0] = False
	return im

# Finds the seam based on vertical or horizonal. Helper function
# im - image to find seam
def seam_finder(im):
	all_seams, energy, seams, i = {}, {}, {}, im.shape[0] - 1
	for y in range(im.shape[1]):
		energy[(0, y)] = im[1, y]
	for x in range(im.shape[0]):
		energy[(x, -1)] = 9999999
		energy[(x, im.shape[1])] = 9999999
	for x, y in itertools.product(range(1, im.shape[0]), range(im.shape[1])): 
		lowest = min(energy[x - 1, y - 1], energy[x - 1, y], energy[x - 1, y + 1])
		energy[(x, y)] = lowest + im[x, y]
		all_seams[(x, y)] = (x - 1, y) if lowest == energy[x - 1, y] else (x-1, y-1) if lowest == energy[x - 1, y - 1] else (x - 1, y + 1) if lowest == energy[x - 1, y + 1] else all_seams[(x, y)]
	for j in range(im.shape[1]):
		path, total_cost, x, y, skip = [(i, j),], 0, i, j, False
		while x > 0:
			total_cost += energy[x, y]
			if total_cost > np.inf:
				skip = True
				continue
			x, y = all_seams[(x, y)]
			path = path + [(x, y)]
		if skip:
			skip = False
			continue
		total_cost += energy[x, y]
		if y in seams and total_cost > seams[y]["value"]: continue
		seams[y] = {"value": total_cost, "finalized_path": path}
	return sorted(seams.values(), key=lambda x : x["value"])

# Main Code 
# python main.py <image name> <desired width> <desired height>
image, d_width, d_height = np.asarray(Image.open(sys.argv[1]), dtype=np.float), int(sys.argv[3]), int(sys.argv[2])
seamed_image = np.zeros((d_width, d_height, 3))
seamed_image[0:d_width, 0:d_height] = seam_carving(image[0:image.shape[0], 0:image.shape[1]], (d_width, d_height))
misc.imsave('seamed_' + sys.argv[1], seamed_image)
