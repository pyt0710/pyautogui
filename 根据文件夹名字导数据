import pandas as pd
import glob
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import os

ACCs = pd.read_excel("ACC20201218.xlsx",header=None)

dirct = 'C:/Users/Proking/Desktop/新建文件夹/ppggsr/新建文件夹/加速度'
dirList=[]
fileList=[]
files=os.listdir(dirct)  #文件夹下所有目录的列表


for f in files:
    if os.path.isdir(dirct + '/'+f):   #这里是绝对路径，该句判断目录是否是文件夹
        dirList.append(f)

print('files:',files)
print(dirList)

for file in dirList:
    print(file)
    ACCfileLists = glob.glob('./加速度/' + file + '/*/GSACC*.csv')
    print(ACCfileLists)
    for ACCfileList in ACCfileLists:
        ACC = pd.read_csv( ACCfileList,header=None)
        ACC[4] = np.sqrt(ACC[1]*ACC[1] + ACC[2]*ACC[2] + ACC[3]*ACC[3])
        print(ACC)
        print("1")
        ACCs[file + "时间"] = ACC[0]
        ACCs[file] = ACC[4]
        print("ok")
        print(ACCs)
ACCs.to_excel("ACC20201218.xlsx",index = False)
