import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def getLabel(filepath):
    label = filepath.split('/')[1]
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

for subdir, dirs, files in os.walk("Projecte_Dir"):
    for file in files:
        filepath = subdir + os.sep + file #os.sep = '/'
        if filepath.endswith(".csv"):
            filenames.append(filepath)


data = []
label = []
labelled_data = []
l = len(filenames)

for i in range(l):
    filename = filenames[i]
    with open(filename, 'r') as f:
        tsd = []
        for line in f:
            dt = [int(i) for i in line.split(',')]
            tsd.append(dt)

#Give the min&max values of the mpu6050 and flex sensors
        #normalize data
        min_val_acc_gyro = [-32768]*6
        min_val_flex = [370]*5
        tsd.append(min_val_acc_gyro + min_val_flex)
        max_val_acc_gyro = [32768]*6
        max_val_flex = [670]*5
        tsd.append(max_val_acc_gyro + max_val_flex)

        df = pd.DataFrame(tsd, columns=np.arange(11))

        #scale acc and gyro values between -1 and 1
        for j in range(6):
            df[j] = df.apply(lambda x:(2*(x.astype(float) - min(x)))/(max(x)-min(x))-1)[j]

        #scale flex sensor values between 0 to 2
        for j in range(6,11):
            df[j] = df.apply(lambda x:(x.astype(float) - min(x))/(max(x)-min(x)))[j]
        df = df[:-2]

        tsd_norm = df.values
        data.append(tsd_norm)
        lab = getLabel(filename)
        label.append(lab)
        ld = [lab]
        for i in range(11):
            ld.append(df[i])
        labelled_data.append(ld)

data = np.array(data)
label = np.array(label)
labels = list(set(label))
labels.sort()
label = format(label, labels)
train_data, valtest_data, train_label, valtest_label = train_test_split(data, label, test_size=0.1)
val_data, test_data, val_label, test_label = train_test_split(valtest_data, valtest_label, test_size=0.5)
np.save('/put/your/path/here :)/labelled_data.npy', labelled_data)
np.save('/content/dotNPY_dataset/train_data.npy', train_data)
np.save('/content/dotNPY_dataset/val_data.npy', val_data)
np.save('/content/dotNPY_dataset/test_data.npy', test_data)
np.save('/content/dotNPY_dataset/train_label.npy', train_label)
np.save('/content/dotNPY_dataset/val_label.npy', val_label)
np.save('/content/dotNPY_dataset/test_label.npy', test_label)
np.save('/content/dotNPY_dataset/labels_list.npy', labels)
