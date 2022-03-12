import numpy as np
import tensorflow as tf
from tensorflow import keras

allHands=[]

#(i_train,o_train), (i_test, o_test) = Huge amounts of data
cd = []
for i in range(len(allHands[1]["lmList"])):
    #This will be a list of tuples
    cd[i] = allHands[1]["lmList"][i]
    

num_chords = 9
model = keras.Sequential([
    keras
    keras.layers.Dense(units=256, activation='relu'),
    keras.layers.Dense(units=256, activation='relu'),
    keras.layers.Dense(units=256, activation='relu'),
    keras.layers.Dense(units=num_chords, activation='softmax')
])