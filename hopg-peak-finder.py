#Program allows the user to find the grayscale value of the peak HOPG
#Output images and csv files are sent to the same folder
#Import relevant modules
import numpy as np 
import pandas as pd 
import skimage
import scipy
import glob
import matplotlib.pyplot as plt 

#Specify files location, and collect these names using glob (tiff files only)
folder_path = '/home/ellis/image/'
image_slice_names = glob.glob(folder_path + '*.tif')
image_stack = []

#Prompt user for some additional information about the data
start_slice = int(input('Which slice should the program start on?: '))
final_slice = int(input('Which slice should the program finish on?: '))
filename = input('What would you like to call the file? ')

#Load the image slices and apply median filter, then create three dimensional volume
for counter, image_slice in enumerate(image_slice_names):
    print('Working: ', counter)
    image = skimage.io.imread(image_slice)
    image_smoothed = skimage.filters.median(image)
    image_stack.append(image_smoothed)

#From the 3D volume, produce a histogram of grayscale values
image_stack = np.array(image_stack)
image_histogram = np.histogram(image_stack, bins=255)[0]

#Find the peak location, by first finding the max and then finding the position of the max
peak_value = np.max(image_histogram)
peak_location = np.where(image_histogram == peak_value)[0]

print(peak_location)

output_peak = pd.DataFrame({'Peak Location': peak_location})
output_peak.to_csv(folder_path + filename + '.csv', index=False)

#Plot the histogram, with vertical lines at peaks to check the output
#Figure is also saved
fig, ax = plt.subplots()
ax.plot(list(range(0,255)), image_histogram)
ax.set_title('HOPG Histogram')
ax.set_ylabel('Counts')
ax.set_xlabel('Grayscale Value')
ax.vlines(peak_location, 0, image_histogram[peak_location])
plt.tight_layout()
plt.savefig(folder_path + filename +'.png')
plt.show()
