# -*- coding: utf-8 -*-
"""Copy of convolutional_neural_network.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lHq1gVIaocVIrB_eq95kHk_kw1JhZTU8

# Convolutional Neural Network
"""

import kagglehub

# Download latest version
path = kagglehub.dataset_download("dansbecker/food-101")

print("Path to dataset files:", path)

"""### Importing the libraries"""

import tensorflow as tf from tensorflow.keras.models import Sequential from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout from tensorflow.keras.preprocessing.image import ImageDataGenerator

tf.__version__

"""## Part 1 - Data Preprocessing

### Preprocessing
"""

train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2) train_generator = train_datagen.flow_from_directory( 'path_to_food_101_dataset/train', target_size=(224, 224), batch_size=32, class_mode='categorical', subset='training' ) validation_generator = train_datagen.flow_from_directory( 'path_to_food_101_dataset/train', target_size=(224, 224), batch_size=32, class_mode='categorical', subset='validation' )

"""## Part 2 - Building the CNN

### Model Architecture
"""

model = Sequential([ Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)), MaxPooling2D(pool_size=(2, 2)), Conv2D(64, (3, 3), activation='relu'), MaxPooling2D(pool_size=(2, 2)), Flatten(), Dense(128, activation='relu'), Dropout(0.5), Dense(101, activation='softmax') ])

"""## Part 3 - Training the CNN

### Compiling the CNN
"""

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

"""### Training the CNN on the Training set and evaluating it on the Test set"""

model.fit(train_generator, validation_data=validation_generator, epochs=10)

model.save('food_classifier_model.h5')