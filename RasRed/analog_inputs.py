#!/usr/bin/python

import sys
import redpitaya_scpi as scpi
import matplotlib.pyplot as plt
import numpy as np

rp_s = scpi.scpi(sys.argv[1])

v=[]
I=[]

for i in range(4):
    rp_s.tx_txt('ANALOG:PIN? AIN' + str(i))
    value = float(rp_s.rx_txt())
    v.append(value)
    I.append(i)
    print ("Measured voltage on AI["+str(i)+"] = "+str(value)+"V")
    print(v)

plt.plot(v)
plt.show()

