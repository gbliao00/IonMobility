# -*- coding: utf-8 -*-
import visa
import serial
ser=serial.Serial('COM5', 38400, timeout=0.1)
#ser.write('#A00C10D0148\r\n'.encode())
ser.write('#A00C10D03D7\r\n'.encode())   
Command=ser.read(16) # 小括號內可以填入一次要讀取的byte數
print(Command)
ser.close()