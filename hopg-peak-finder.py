import numpy as np 
import pandas as pd 
import skimage
import scipy
import glob
import matplotlib.pyplot as plt 
folder_path = '/'

image_slice_names = glob.glob(folder_path + '*.tif')
image_stack = []

#Prompt user for some additional information about the data
start_slice = int(input('Which slice should the program start on?: '))
final_slice = int(input('Which slice should the program finish on?: '))
filename = input('What would you like to call the file? ')

for counter, image_slice in enumerate(image_slice_names):
    print('Working: ', counter)
    image = skimage.io.imread(image_slice)
    image_smoothed = skimage.filters.median(image)
    image_stack.append(image_smoothed)

image_stack = np.array(image_stack)
image_histogram = np.histogram(image_stack, bins=255)[0]

peak_value = np.max(image_histogram)
peak_location = np.where(image_histogram == peak_value)

print(peak_location)

fig, ax = plt.subplots()
ax.plot(list(range(0,255)), image_histogram)
ax.set_title('HOPG Histogram')
ax.set_ylabel('Counts')
ax.set_xlabel('Grayscale Value')
ax.vlines(peak_location, 0, image_histogram[peak_location])
plt.tight_layout()
plt.savefig(folder_path + filename +'.png')
plt.show()
