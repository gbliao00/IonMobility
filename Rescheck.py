fname = open('files.txt', 'r')   #Open file
filename=[]
for file in iter(fname):
    file=file.strip() # 去掉頭尾空白
    filename.append(file)

print(str(filename))
fname.close()

import matplotlib.pyplot as plt
import numpy as np

for file in filename:
    fp = open(file, 'r')   #Open file
    dv=[]
    v=[]
    
    
    i=1
    for line in iter(fp):
        line=line.strip() # 去掉頭尾空白
        if i >10:
            Data=line.split(',')
            dv.append(int(Data[0]))
            v.append(float(Data[1]))
        i+=1

    fp.close()

    x=dv
    y=v

    # Annotation maxium
    xp=v.index(max(v))
    yp=max(v)
    yp1=min(v)
    
    
    # Data Shift
    data=[]
    for d in y:
        d1=d-min(v)
        data.append(d1)
    
    
    # FWHM
    count=0
    while data[data.index(max(data))]-data[data.index(max(data))+count]<=data[data.index(max(data))]/2:
        indexr=count
        count+=1

    count=0
    while data[data.index(max(data))]-data[data.index(max(data))+count]<=data[data.index(max(data))]/2:
        indexl=count
        count-=1

    print(indexr)
    print(indexl)
    print(data.index(max(data))+9)
    
    res=int((data.index(max(data))+9)/(indexr-indexl))
    print(res)
    resolution=str(res)
    
    
    
    #--line
    plt.plot([x[data.index(max(data))+indexl],x[data.index(max(data))+indexl]],[max(data),0],'k--', lw=1)
    plt.plot([x[data.index(max(data))+indexr],x[data.index(max(data))+indexr]],[max(data),0],'k--', lw=1)
    #plt.annotate(r'$242.3Da$', xy=(xp,yp))
    
    # Picture
    plt.plot(x,data,color='blue',linewidth=1.0)
    res, = plt.plot(x,data,color='blue',linewidth=1.0)
    plt.legend([res,], ['max peak res:'+resolution,])
    
    
    plt.xlabel("dV") 
    plt.ylabel("Voltage (mV)") 
    plt.title("Ion Mobility") 
    plt.show()
