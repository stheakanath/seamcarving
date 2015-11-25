README.md

Project 4 - Seam Carving - Kuriakose Sony Theakanath
---------------------------------------------------------------

Usage:
python main.py <image name> <desired width> <desired height>

Ex (with image provided):
python main.py couch.jpg 375 450

Outputted file is saved as seamed_<image name>.jpg in directory.

---------------------------------------------------------------
Explanation of Code:

The first function is the main function in the code. It takes two parameters, im and dimensions, im is the image to apply the function on and dimensions is the desired dimension the user wants to make the original picture. The function then loops through the image, and applies the seam carving function repeatedly, until the image is resized to the amount the user wants it as. This is done in the vertical and horzontial alternatively. 

The second function is the seam finder as detailed in the paper. It takes one parameter, which is the image. The algorithm looks through the image and finds the seam with the lowest energy after comparing all possible purmutations. After that the values are ordered and then retruned as a function so that the seam_carving function can pick the best path.

The main code takes the image, and desired dimensions when the user types in the main.py function and then the seamed image is then saved in the directory the program is run from.# seamcarving
