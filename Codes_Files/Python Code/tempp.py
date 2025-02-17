'''
This file is temporary only.
Will only be used for running small modules till rectified from errors.
It may contain previous code.
<sign out !!!!!!!!!!!!>
'''

import pandas as pd
import numpy as np
print(np.__version__)
print(pd.__version__)


'''
import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def getLabel(filepath):
    label = filepath.split('\\')[9]
    label = label.split('-')[0]
    return label

def format(label, labels):
    arr = []
    l = len(labels)
    for i in label:
        j = labels.index(i)
        val = [0]*l
        val[j] = 1
        arr.append(val)
    return np.array(arr)

filenames = []
filepath=''

for subdir, dirs, files in os.walk("C:\\Users\Com-6\\AppData\\Local\\Programs\\Python\\Python311\\Training_Dataset"):
    for file in files:
        filepath = subdir + os.sep + file #os.sep = '/'
        if filepath.endswith(".csv"):
            filenames.append(filepath)

print(filepath)
print(len(filenames))

data = []
label = []
labelled_data = []
l = len(filenames)

for i in range(l):
    filename = filenames[i]
    with open(filename, 'r') as f:
        tsd = []
        for line in f:
            dt = [float(i) for i in line.split(',')]
            tsd.append(dt)

        #Give the min&max values of the mpu6050 and flex sensors
        #normalize data
        min_val_acc_gyro = [-32768]*6
        min_val_flex = [200]*5
        tsd.append(min_val_acc_gyro + min_val_flex)
        max_val_acc_gyro = [32768]*6
        max_val_flex = [600]*5
        tsd.append(max_val_acc_gyro + max_val_flex)

        df = pd.DataFrame(tsd, columns=np.arange(11))
        print("DF: ",df)
        print("Size of DF: ",df.shape)
        #scale acc and gyro values between -1 and 1
        for j in range(6):
            df[j] = df.apply(lambda x:(2*(x.astype(float) - min(x)))/(max(x)-min(x))-1)[j]

        #scale flex sensor values between 0 to 2
        for j in range(6,11):
            df[j] = df.apply(lambda x:(x.astype(float) - min(x))/(max(x)-min(x)))[j]

        #removing last two rows of min and max values of sensors
        df = df[:-2]

        print("After scaling values acc and gyro values...")
        print("DF: ",df)
        print("Size of DF: ",df.shape)
        
'''
