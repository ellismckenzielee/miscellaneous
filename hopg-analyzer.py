#Script which find the average, std and median variation with slice,
#of a three dimensional stack of grayscale images. Also plots these. This script
#is used in this case for analysis of HOPG.

import numpy as np 
import matplotlib.pyplot as plt 
import skimage
import glob
import scipy
import pandas as pd 

#Specify file location and use glob to get all filenames with type 'tif'
folder_path = '/'
image_slice_names = glob.glob(folder_path + '*tif')

#Initialize lists that will be used for plotting
average_grayscale = []
median_grayscale = []
standard_d_grayscale = []
slice_number = []

#Load image slice and smooth, thenfind the average, median and std. Append to above variables
for counter, image_slice in enumerate(image_slice_names[:]):
    print('Working: ', counter)
    image = skimage.io.imread(image_slice)
    image_smoothed = skimage.filters.median(image)
    average_grayscale.append(np.mean(image_smoothed))
    median_grayscale.append(np.median(image_smoothed))
    standard_d_grayscale.append(np.std(image_smoothed))
    slice_number.append(counter)


#Lists which are used in the plotting - contains data and labels
plot_data = [average_grayscale, median_grayscale, standard_d_grayscale]
titles = ['Average Grayscale Variation', 'Median Grayscale Variation', 'Standard Deviation Variation', 'Slice Number']

#Plot the three variables on a single figure
fig, ax = plt.subplots(3,1)

for counter, data in enumerate(plot_data):
    ax[counter].plot(slice_number, data)
    ax[counter].set_ylabel(titles[counter])
    ax[counter].set_xlabel(titles[-1])

fig.tight_layout()
plt.show()