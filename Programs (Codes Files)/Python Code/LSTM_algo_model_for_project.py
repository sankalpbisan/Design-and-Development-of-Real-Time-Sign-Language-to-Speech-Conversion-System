import glob
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Activation
from keras import optimizers
from keras.preprocessing import sequence
from keras.models import model_from_json
import h5py
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.losses import SparseCategoricalCrossentropy
from tensorflow.keras import layers
from sklearn.metrics import accuracy_score
from sys import getsizeof

#load Training and Validation data
train_data = np.load('/train_data.npy')
val_data = np.load('/val_data.npy')
test_data = np.load('/test_data.npy')

#load Training and Validation labels
train_label = np.load('/train_label.npy')
val_label = np.load('/val_label.npy')
test_label = np.load('/test_label.npy')
labels =np.load(glob.glob('/labels_list.npy'))

print("train_data.shape: ",train_data.shape)

print("len(train_label): ",len(train_label))

print("test_data.shape: ",test_data.shape)

print("len(test_label): ",len(test_label))

print("train_data.dtype: ",train_data.dtype)
print("train_label.dtype",train_label.dtype)


model = Sequential([
  LSTM(50, input_shape=(50, 11)),
  Dense(100),
  Dropout(0.4),
  Dense(26, activation='softmax'),
])


# Choose an appropriate optimizer and loss function based on your task
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# If your labels are not one-hot encoded, uncomment the following line
# train_label = keras.utils.to_categorical(train_label)


print(model.input_shape)

model.fit(train_data, train_label, epochs=10)

model.evaluate(test_data,test_label)

model.summary

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
hist = model.fit(train_data, train_label, validation_data = (val_data, val_label),
                batch_size=64, epochs=30)
loss, accuracy = model.evaluate(test_data, test_label)

print("loss & accuracy: ",loss, accuracy)

'''
#Plot Loss and Accuracy Curves
import matplotlib.pyplot as plt
plt.figure(figsize=(12,8))
plt.subplot(211)
x = np.arange(1,len(hist.history['acc'])+1)
plt.scatter(x, hist.history['acc'], color='blue', s=10)
plt.plot(x,hist.history['acc'], 'b')
plt.scatter(x, hist.history['val_acc'], color='green', s=10)
plt.plot(x, hist.history['val_acc'], 'g')
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.legend(['Training', 'Validation'], loc='lower right')

plt.subplot(212)
plt.scatter(x, hist.history['loss'], color='blue', s=10)
plt.plot(x,hist.history['loss'], 'b')
plt.scatter(x, hist.history['val_loss'], color='green', s=10)
plt.plot(x, hist.history['val_loss'], 'g')
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Training', 'Validation'], loc='upper right')
plt.savefig('plots/loss_acc_curves.png',bbox_inches='tight')
'''




