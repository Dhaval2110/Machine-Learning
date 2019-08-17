'''
Ref : 
https://goo.gl/yCGqtZ
https://goo.gl/eeyzkk
nvidia.com/en-us/data-center/tesla_k80
http://playground.tensorflow.org
https://notebooks.azure.com/mehtadhaval21/projects/NeuralNetworks-1

*Important Def:
1)Activation Function
2)Gradient Descent
3)Learning rate
4)Loss
5)XOR Challenge
6)Types of activation functions
7)Relu
8)Hyperparameters
9)Keras
'''

#Introduction to Neural Networks

#1) Import packages
from keras.datasets import mnist
from keras.preprocessing.image import load_img, array_to_img
from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

#2) Load the data
(X_train, y_train), (X_test, y_test) = mnist.load_data()
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)
#(60000, 28, 28)
#(60000,)
#(10000, 28, 28)
#(10000,)

#3) Understanding the image data
X_train[0].shape
plt.imshow(X_train[0],cmap='gray')
y_train[0]

# 4) Preprocessing the image datay_train = to_categorical(y_train,10)
y_test = to_categorical(y_test,10)
print(y_train.shape)
print(y_test.shape)
image_height,image_width = 28,28
X_train = X_train.reshape(60000, image_height*image_width)
X_test = X_test.reshape(10000, image_height*image_width)
print(X_train.shape)
print(X_test.shape)
print(X_train[0])
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')           											# to get data in between 0 -255 (Gray scale image)
X_train /= 255.0                     													# to get data in between 0 & 1
X_test /= 255.0
print(X_train[0])
print(y_train.shape)
print(y_test.shape)


# 5) Build a model
model = Sequential()                                                                      # input model
model.add(Dense(512, activation='relu', input_shape=(784,)))
model.add(Dense(512, activation='relu'))                                                  # intermideate layers
model.add(Dense(10,activation='softmax'))                                                 # output layer

# 6) Compile a model
model.compile(optimizer='adam',loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

# 7) Train a model
history = model.fit(X_train, y_train, epochs=20, validation_data=(X_test, y_test))

#8) Accuracy of a model
plt.plot(history.history['acc'])                                                             #Plot the accuracy of the training model
plt.plot(history.history['val_acc'])       													 #Plot the accuracy of the validation set
plt.plot(history.history['loss'])															 #Plot the accuracy of the loss

# 9) Evoluting a model
score=model.evaluate(X_test,y_test)
score                                                                                         # second arg as percentage accuracy
