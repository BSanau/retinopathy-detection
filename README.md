# retinopathy-detection

## Objective
In this project, an executable program that diagnoses diseases in the retina and recommends a treatment based on the patient's risk factors has been developed. 

## Development
From a dataset of 80000 images classified in CNV (Choroidal Neurovascularization), DME (Diabetic Macular Edema), Drusen and Normal, a convolutional neural network has been developed by transferring and adapting the architecture of the trained model InceptionV3. 

Thus, by developing a functional model in Keras, an accuracy of 93% has been obtained with a loss value of 0.23.

## User Interface
The PyQt5 library has been used to design the graphic interface. Through it, the user can select the image, know its diagnostic, save it in a PDF and discover the treatments that have been done to patients with the same pathology and similar risk factors.

## Links
kaggle dataset: https://www.kaggle.com/paultimothymooney/kermany2018