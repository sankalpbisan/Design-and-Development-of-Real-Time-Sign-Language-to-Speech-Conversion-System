import serial
import time
import numpy as np
import pandas as pd
import datetime
import csv
import pyttsx3
from keras.models import model_from_json

engine = pyttsx3.init()

comport = serial.Serial('COM6',9600,timeout=1)
if not comport.isOpen():
    comport.open()
    print('COM6 is open : ', comport.isOpen())
    print("Established serial connection !!!")
else:
    print("Try Connecting again !")

c=0

#offset for the IMU
#offset = [2324, 88, 4942, 47, 6, -37, 0,0,0,0,0]
#offset = [0,0,0,0,0,0,0,0,0,0,0]

labels=["welcome","sorry"]
row = []


 #load model 0
json_file = open('E:\\Sankalp\\Project Files\\Trained Model\\model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("E:\\Sankalp\\Project Files\\Trained Model\\model.h5")
print("Loaded model from disk")
loaded_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])

labels = np.load("E:\Sankalp\\Project Files\\Dataset\\my dataset\\NPYdataset\\labels_list.npy")

inp=[]
x=1

a = input("Start collecting data(y/n)").lower()
if a == 'y':
    print("Wait time 2 seconds...")
    time.sleep(2)
    
    print ("[START ACTION]")
    time.sleep(0.5)
    print(time.ctime())
    while True:
        sensor_data = comport.readline().decode('utf-8').strip()
        if sensor_data=='':
            continue
            print('It did not skipped the empty string data !!!!!')

        data = []
        row=[]
        #split into the three segments
        sensor_data = sensor_data.split(' ')
        
        #conversion of each item from str to float 
        for item in sensor_data:
            item = float(item)
            data.append(item)

        row.append(data)
        print(x,"Data: \n",data)

        min_val_acc_gyro = [-32768] * 6
        min_val_flex = [200] * 5
        row.append(min_val_acc_gyro + min_val_flex)
        max_val_acc_gyro = [32768] * 6
        max_val_flex = [600] * 5
        row.append(max_val_acc_gyro + max_val_flex)

        df = pd.DataFrame(row, columns=np.arange(11))

        '''
        #scale acc and gyro values between -1 and 1
        for j in range(6):
            df[j] = df.apply(lambda x:(2*(x.astype(float) - min(x)))/(max(x)-min(x))-1)[j]

        #scale flex sensor values between 0 to 2
        for j in range(6,11):
            df[j] = df.apply(lambda x:(x.astype(float) - min(x))/(max(x)-min(x)))[j]
        '''
        df = df[:-2]  # removing last two rows of min and max sensor values

        tsd_norm = df.values    #df.values returns the dataframe without any numbering
        inp.append(tsd_norm)
        df.size

        x=x+1
        c=c+1
        if c==50: #set c===50 for 1sec and c==100 for 2sec of data
            break

    print(time.ctime())

else:
    print("OK!!!")
    exit()
print("\ndata collected\n..............\n.............\................\n ")
print("Collected Data is :\n",inp)

inp = np.array(inp)
inp.shape
inp = inp.reshape((1,50,11))

prediction = loaded_model.predict(inp)
pred = list(prediction[0])
#print(pred)
p = max(pred)
i = pred.index(p)
pred_label = labels[i]

#Speech as end-Output
engine.say(pred_label)
engine.runAndWait()
print(p, i, pred_label)






            
