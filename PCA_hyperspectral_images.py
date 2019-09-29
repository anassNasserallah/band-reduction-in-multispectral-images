# import the librairies for the task
import scipy.io as io
import numpy as np
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA


#Constants for the application
FILENAME = "./PaviaU.mat"     # Filename of the image we want to transform
RAW_IMAGE_DICT_KEY = "paviaU" # Key of the dictionary of the image containing the pixels and bands data
NB_BANDS = 3                  # Number of bands with want at the end of the process
RESCALE_F_RANGE = (0,1)       # rescale value range of the pixels (here, pixel value between 0 and 1)


#Functions for the band reducing of the image
# Allows to load and extract the data of the image
def load_image(file):
    data = io.loadmat(file)[RAW_IMAGE_DICT_KEY]
    # we need to gather the pixels arrays into 1d-array inside the matrix
    return (data.shape[0], data.shape[1], data.reshape(-1, data.shape[2]))

# We reduce the number of bands of the image using PCA
def reduce_bands_image(data):
    pca = PCA(n_components=NB_BANDS)
    return pca.fit_transform(data)

# After reduction, we rescale the 1d-array of pixels into a here, a 3d-array of pixels
# We also scaled the pixel values with a range of 0 to 1
def rescale_image(image, dimX, dimY):
    minMax_scaler = MinMaxScaler(feature_range=RESCALE_F_RANGE)
    feature_rescaled_image = minMax_scaler.fit_transform(image)
    return np.reshape(feature_rescaled_image, (dimX, dimY, NB_BANDS))

#Main program

def main():
    x, y, image = load_image(FILENAME)
    reduced_image = reduce_bands_image(image)
    exploitable_image = rescale_image(reduced_image, x, y)

    plt.imshow(exploitable_image)
    plt.show()
    
if __name__ == '__main__':
    main()





