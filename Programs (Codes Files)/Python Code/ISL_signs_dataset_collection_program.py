import serial
import time
import numpy as np
import pandas as pd
import datetime
import csv

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

print("Select Label from :",labels)
indx=int(input("Give index number to select the label: "))
print("Collecting Data for",labels[indx])
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
        
        #split into the three segments
        sensor_data = sensor_data.split(' ')
        
        #conversion of each item from str to float 
        for item in sensor_data:
            item = float(item)
            data.append(item)

        row.append(data)
        print("Data: \n",data)

        c=c+1
        if c==50: #set c===50 for 1sec and c==100 for 2sec of data
            break        
        
    print(time.ctime())

else:
    print("OK!!!")
    exit()
print("\ndata collected\n..............\n.............\................\n ")
print("Collected Data is :\n",row)

'''
df = pd.DataFrame(row, columns=np.arange(11))
print("Means (df) \n",df.mean())
print("DataFrame: \n",df)
'''

a = input("Save Data?(y/n)").lower()
if a == 'y':
    #s -= 1
    tm = datetime.datetime.now()
    #tm = '-'.join(str(tm).split())
    tm = datetime.datetime.now()
    tm = str(tm)
    datim=''
    for char in tm:
        if char==':' or char==' ':
            datim=datim+'_'
            continue
        datim=datim+char
    fname = "Training_Dataset\\"+labels[indx]+"-"+datim+".csv"
    try:
        with open(fname, 'w',newline='') as f:
            writer = csv.writer(f)
            #for r in row:
            writer.writerows(row)
        f.close()
        print("File Saved Successfully with name",labels[indx]+"-"+datim+".csv")
    except KeyError:
        print("[Exit]")

else:
    print("OK!!!")
    exit()
