#Muhammad Rehman Rabbani(137364)
#Connencted component implementation using 4 adjacency

#importing required libraries
import PIL
from PIL import ImageFilter
from PIL import Image
import numpy as np
import random

#defining the binarization function here
def binarization():

	for element in arrayData:
	    pixValue = (element[0] + element[1] + element[2]) / 3
	    if(pixValue > 130):
        	pixValue = 255
	    else:
        	pixValue = 0
	    comb_val = (pixValue, pixValue, pixValue)
	    binImage.append(comb_val)
	    arr.append(pixValue)
		
#creating image object
image = Image.open("Lab4-image.png")
arrayData = list(image.getdata())
binImage = []
arr = []

#converting RGB image into binary image
binarization()
#creating a new image with same dimenssions of original image
newImage = Image.new(image.mode, image.size)
#put the binImage list values in it
newImage.putdata(binImage)
#Saving the binarized image
newImage.save('binarized.jpg')
arrayData = list(newImage.getdata())
newarr = arrayData
image= newImage
width,height =  image.size
data = np.zeros([height, width])
elementels = image.load()

for i in range(height):
    for j in range(width):
        r,g,b =  elementels[j,i]
        if r == 255:
            data[i,j] = 1
			
upperElement = -1
elem_lft = -1
wght = 0
# Dictionary of point:label pairs
labels = {}
print "actual image data after binarization"
print data

#1st iteration
for i in range(height):
    for j in range(width):
        if(data[i][j] == 1):
            if(i == 0):
                if(j == 0):
                    upperElement = -1
                    elem_lft = -1
                else:
                    elem_lft = data[i][j-1]
                    upperElement = -1
            else:
                if(j == 0):
                    upperElement = data[i-1][j]
                    elem_lft = -1
                else:
                    upperElement = data[i-1][j]
                    elem_lft = data[i][j-1]    
            if(upperElement == 0 or upperElement == -1):
                if(elem_lft == 0 or elem_lft == -1):
                    wght = wght + 1;
                    data[i][j] = wght;
                else:
                    data[i][j] = elem_lft;
            else:
                if(elem_lft == 0 or elem_lft == -1):
                    data[i][j] = upperElement;
                else:
                    if(upperElement > elem_lft):
                        labels[upperElement] = elem_lft;
                        data[i][j] = elem_lft;
                    else:
                        labels[elem_lft] = upperElement
                        data[i][j] = upperElement; 
						
print "Image data after the labeling (1st iteration): "
print data

#2nd iteration
for i in range(height):
    for j in range(width):
        if(labels.has_key(data[i][j])):
            data[i][j] = labels[data[i][j]];
			
print "Image data after the labeling (2st iteration):"
print data
print labels

"""
# Image to display the components in a nice, colorful way
output_img = Image.new("RGB", (height, width))
outinfo = output_img.load()
colors = {}
for (x, y) in labels.items():
 
    # Name of the component the current point belongs to
    component = labels[x]
    # Associate a random color with this component 
    colors[component] = (random.randint(0,255), random.randint(0,255),random.randint(0,255))
    # Colorize the image
    outinfo[x, y] = colors[component]
	
output_img.show()
"""
# Image to display the components
newImage = Image.fromarray(data)
	   
newImage.show()
