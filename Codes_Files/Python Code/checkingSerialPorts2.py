import serial
import time


#arduino = serial.Serial('COM3',9600)
arduino = serial.Serial('COM6',9600,timeout=1)
if not arduino.isOpen():
  arduino.open()
print('com6 is open : ', arduino.isOpen())
print("Established serial connection to Arduino")
c,b=0,1
x=int(input("To start recording data press 1 and 0 to discard !\n"))
data=[]
print(time.ctime())
if x==1:
    while(1):
        
        list_in_floats = []
        sensor_data = float(arduino.readline().decode('utf-8').strip())
        if sensor_data==' ':
            continue
        print(b," : ",sensor_data)
        b=b+1
        #sensor_data = sensor_data.split()
        #print("\nTime Point: ",c,"\nValues: ",sensor_data)
        print(type(sensor_data))
        #for item in sensor_data:
         #   item = int(item)
          #  data.append(item)
        #data.extend(data)
        c=c+1
        if c==100:
            break
    print("100 values has been recorded")
    print(time.ctime())

    
    '''
        decoded_values = str(sensor_data[0:len(arduino_data)].decode("utf-8"))
        list_values = decoded_values.split('x')

        for item in list_values:
            list_in_floats.append(str(item))
        
        print(f'collected gesture readings : {list_in_floats}')

        
        arduino_data=0
        list_in_floats.clear()
        list_values.clear()
        #arduino.close()
    '''

else:
    print("Run again !")
