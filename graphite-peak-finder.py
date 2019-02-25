#Program allows user to analyze graphite grayscale histogram
#Made such that RAM being exceeded should not be an issue

#Import relevant modules
import numpy as np 
import matplotlib.pyplot as plt 
import skimage
import glob
import scipy
import pandas as pd 

#Specify files location, and collect these names using glob
folder_path = ''
image_slice_names = glob.glob(folder_path + '/*')
image_histogram = np.ones(255)
image_stack = []

#Prompt user for some additional information about the data
start_slice = int(input('Which slice should the program start on?: '))
final_slice = int(input('Which slice should the program finish on?: '))
filename = input('What would you like to call the file? ')

#Load the image slices and apply median filter, then create three dimensional volume
for counter, image_slice in enumerate(image_slice_names[start_slice:final_slice]):
    print('Working: ', counter)
    image = skimage.io.imread(image_slice)
    image_smoothed = skimage.filters.median(image)
    image_stack.append(image_smoothed)

image_stack = np.array(image_stack)

#From the 3D volume, produce a histogram of grayscale values
image_histogram = np.histogram(image_stack, bins=255)[0]

#Find the peaks using scipy function
peaks = scipy.signal.find_peaks(image_histogram, prominence=500)[0]

#Output data to file (If user chooses to)
output_hist = pd.DataFrame({'Histogram': image_histogram})
output_hist.to_csv(folder_path + filename + '.csv', index=False)

output_peaks = pd.DataFrame({'Peaks': peaks})
output_peaks.to_csv(folder_path + filename + '.csv', index=False)

#Plot the histogram, with vertical lines at peaks to check the output
#Figure is also saved
fig, ax = plt.subplots()
ax.plot(list(range(0,255)), image_histogram)
ax.set_title('Histogram')
ax.set_ylabel('Counts')
ax.set_xlabel('Grayscale Value')
ax.vlines(peaks[0], 0, image_histogram[peaks[0]])
ax.vlines(peaks[1], 0, image_histogram[peaks[1]])
plt.savefig(folder_path + filename +'.png')
plt.show()