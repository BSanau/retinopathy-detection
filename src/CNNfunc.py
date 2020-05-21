import os
import pandas as pd

from keras.applications.inception_v3 import InceptionV3
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.layers import Input, Dense
from keras.models import Model
from keras.preprocessing.image import ImageDataGenerator
from keras import backend as K
print(K.tensorflow_backend._get_available_gpus())


def CNNmodel(imsize=224, batchsize=16, lastlayer="softmax", opt="Adam", Nepochs=30, steps=10):

    """
    Esta función entrena una CNN de tipo funcional a partir de un modelo pre-entrenado 
    InceptionV3. 
    """

    # IMAGE GENERATOR
    train_datagen = ImageDataGenerator(
            # Image standardization
            samplewise_center=True, 
            samplewise_std_normalization=True, 
         
            #horizontal_flip = True, 
            #vertical_flip = False, 
            #height_shift_range= 0.05, 
            #width_shift_range=0.1, 
            #rotation_range=15, 
            #zoom_range=0.15,
        
            # Dividiremos el conjunto de imágenes en 80% train y 20% test
            validation_split=0.2)

    # SPLITTING IMAGES IN TRAINING AND TESTING
    traindir = 'rawdata/train/'

    train_generator = train_datagen.flow_from_directory(
            traindir,
            target_size=(imsize , imsize),
            batch_size=batchsize,
            subset='training',  # One of "training" or "validation". 
                                # Only used if validation_split is set in ImageDataGenerator
            #class_mode='categorical', # "binary", "categorical", "input", "multi_output", "raw", "sparse" or None.
                                       # "categorical" by default.
            ) 
    validation_generator = train_datagen.flow_from_directory(
            traindir,
            target_size=(imsize , imsize),
            batch_size=batchsize,
            subset='validation',
            #class_mode='categorical' # "categorical" by default.
            )

    #valid_X, valid_Y = next(validation_generator) # Elements from validation_generator

    """
    MODELO FUNCIONAL
    Creamos un modelo funcional a partir del modelo pre entrenado InceptionV3.

    Creamos un nodo (Tensor obj.) de entrada al modelo. Aquí sólo especificamos el tipo de 
    nuestro dataset: imágenes de (224, 224, 3). El modelo Inception3 sólo funciona con 
    imágenes RGB, por lo que el input tiene que tener tres canales.
    """
    
    img_in = Input((imsize, imsize, 3))

    """
    De modo que img_in contiene información sobre la forma y el tipo de dato que se espera 
    ingresar en el modelo
    $img_in.shape --> TensorShape([Dimension(None), Dimension(224), Dimension(224), Dimension(3)])
    $img_in.dtype --> tf.float32

    La primera parte será un modelo pre entrenado al que nosotros le metemos un input, y del 
    que obtenemos un output tensor x1.
    """

    pretrained_model =  InceptionV3(
                include_top= False,
                weights='imagenet',       
                input_tensor= img_in, 
                input_shape= (imsize, imsize, 3), 
                pooling ='avg'
                )  
                                
    x1 = pretrained_model.output

    # Pasamos el output de ese primer modelo a dos capas densas, obteniendo un output tensor x2
    x1_ = Dense(100, activation='relu', name="capa_previa")(x1)
    x2 = Dense(4, activation=lastlayer, name="predictions")(x1_)

    # LLegados a este punto, creamos un Modelo especificando sus entradas y salidas en las capas de gráficas.
    model = Model(inputs = img_in, outputs = x2)

    # Compilamos el modelo
    model.compile(optimizer = opt, 
                    loss = 'categorical_crossentropy',
                    metrics = ['accuracy'])


    # save model structure
    fname=f"fun_{imsize}_{batchsize}_{lastlayer}_{opt}_{Nepochs}_{steps}"
    model.save(f"{fname}_structure.h5")

    # CHECKPOINTS
    filepath=f"models/{fname}_weights.hdf5"

    checkpoint = ModelCheckpoint(filepath, #guarda los checkpoints en esta ruta
                             monitor='val_accuracy', # parámetro que tiene en cuenta para guardar el modelo
                             verbose=1, 
                             save_best_only=True, # sobreescribe el archivo y guarda sólo el mejor modelo con 
                                                  # la mejor val_accuracy
                             #save_weights_only=True, # Por defecto, guarda el modelo y los weights
                             #mode='max'
                            )
    callbacks_list = [checkpoint]

    history = model.fit_generator(train_generator, 
                                  steps_per_epoch = steps, 
                                  validation_data = validation_generator,
                                  epochs = Nepochs, 
                                  callbacks=callbacks_list
                             )
    history_model = pd.DataFrame(history.history)
    history_model.to_csv(f"models/{fname}.csv")


if __name__ == '__main__':
    CNNmodel()