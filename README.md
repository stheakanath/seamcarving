# Context Aware Seam Carving
Implementing context aware resizement of images based on paper as described by Shai Avidan and Ariel Shamir: http://perso.crans.org/frenoy/matlab2012/seamcarving.pdf

![Seam Carving](http://i.imgur.com/vWPqYKT.gif)

## Background

Generally when we resize an image, we have to crop out a predefined amount out. This may lead to getting rid of the most important parts of an image, say an object. The main goal of this project is to get the "least important" aspects of a picture out while preserving the main aspects. To do this we implement an algorithm called "seam carving", which does exactly as said. We get an end result as below:

## Algorithm

Seam carving involves the process of resizing images by removing seams in the images while taking the context of the image into consideration. A seam is defined as a 8-connected path, which extends from an edge of an image to another edge. We choose this seam by defining an "energy function", which differentiates the important features (called high energy) from the not important features (called low energy). Once we generate a finite amount of seams for consideration, we select the seam with the least energy. This seam is then removed, and we repeat this process until the image is of the size the user defined. 


To implement the energy function, we use the Sobel energy function as defined as below: 

![Algorithm](http://i.imgur.com/KU8WC5u.png)

The Sobel edge detection filter is a good way to determine where object and features are. Once we calculate the "energy" of each pixel, we employ dynamic programming to find the minimum seam as we move along the picture. We delete the seam found and repeat this process until the image is of the desired height.

## Running Code
```
python main.py <image name> <desired width> <desired height>
```
## Running on Example
```
python main.py couch.jpg 375 450
```

## Example Results

![Seam Carving](http://i.imgur.com/http://imgur.com/2qZWViy.png)
![Seam Carving](http://i.imgur.com/http://imgur.com/QyAR5c8.png)