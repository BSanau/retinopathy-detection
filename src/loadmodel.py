import numpy as np

from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.train import latest_checkpoint


def predictClass(path_image, imsize = 224):


    # Loading the model
    mymodel = load_model("models/fun_224_16_softmax_Adam_100_20_structure.h5")
    mymodel.load_weights("models/fun_224_16_softmax_Adam_100_20_weights.hdf5")
   
    # Open image 
    img = Image.open(path_image)
    img_res = img.resize((imsize,imsize)) # resize
    img_array = np.array(img_res) # convert to np.array

    # Standardize
    img_array_std = (img_array - img_array.mean()) / img_array.std()

    # From greyscale to RGB
    img_trans = np.zeros((1, imsize, imsize,3))

    img_trans[0, :, :, 0] = img_array_std
    img_trans[0, :, :, 1] = img_array_std
    img_trans[0, :, :, 2] = img_array_std

    # Predicting class
    y_pred = mymodel.predict(img_trans)

    return list(y_pred[0])


#if __name__ == '__main__':
#    predictClass()