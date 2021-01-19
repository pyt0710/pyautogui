import pandas as pd
import numpy as np
import math
import sys


input_file = input()
juniorSchool = pd.read_excel(input_file,header=None)

dateFrame = juniorSchool

#初中IAT判断抑郁

i = 2
MSSMHS_S = []
MSSMHS = []
for z in range(len(dateFrame)-2):
    MSSMHS = dateFrame.loc[i][2]
    MSSMHS_S.append(MSSMHS)
    i = i + 1
i = 2
#print(MSSMHS_S)
for x in MSSMHS_S:
    
    if math.isnan(x):
        dateFrame.at[i,3] = 0
    elif ((((x + 0.1036) / 0.2486) * 10) + 50) < 63.80:
        dateFrame.at[i,3] = 0 
    elif ((((x + 0.1036) / 0.2486) * 10) + 50) >= 63.80:
        dateFrame.at[i,3] = 2

    


        
    i = i + 1
dateFrame.at[0,3] = 'IAT抑郁'
#初中MSSMHS判断抑郁



i = 2
MSSMHS_S = []
MSSMHS = []
for z in range(len(dateFrame)-2):
    MSSMHS = dateFrame.loc[i][7]
    MSSMHS_S.append(MSSMHS)
    i = i + 1
i = 2
#print(MSSMHS_S)
for x in MSSMHS_S:

    if np.max(x) < 2:
        dateFrame.at[i,8] = 0 
    elif np.max(x) < 3:
        dateFrame.at[i,8] = 1
    elif np.max(x) < 4:
        dateFrame.at[i,8] = 2
    elif np.max(x) >= 4:
        dateFrame.at[i,8] = 3
    elif math.isnan(x) :
        dateFrame.at[i,8] = 0
    
        
    i = i + 1
dateFrame.at[0,8] = 'MSS抑郁'
dateFrame.at[0,9] = '抑郁综合'

#初中判断抑郁



i = 2
MSSMHS_S = []
MSSMHS = []
for z in range(len(dateFrame)-2):
    MSSMHS = list(dateFrame.loc[i][[3,8]])
    MSSMHS_S.append(MSSMHS)
    i = i + 1
i = 2
#print(MSSMHS_S)
for x in MSSMHS_S:
    

    if np.max(x) < 1:
        dateFrame.at[i,9] = 0 
    elif np.max(x) < 2:
        dateFrame.at[i,9] = 1
    elif np.max(x) < 3:
        dateFrame.at[i,9] = 2
    elif np.max(x) >= 3:
        dateFrame.at[i,9] = 3
    elif math.isnan(x) :
        dateFrame.at[i,9] = 0
    
        
    i = i + 1


IAT = dateFrame[[1,3,8,9]]
#初中问卷

juniorSchool = pd.read_excel(input_file,header=None)
dateFrame = juniorSchool



#初中MSS问卷
i = 2

MSSMHS_S = []
for z in range(len(dateFrame)-2):
    MSSMHS = list(dateFrame.loc[i][[3,4,5,6,7,8,9,10,11,12]])
    MSSMHS_S.append(MSSMHS)
    i = i + 1
i = 2
for x in MSSMHS_S:
    

    if np.max(x) < 2:
        dateFrame.at[i,12] = 0 
    elif np.max(x) < 3:
        dateFrame.at[i,12] = 1
    elif np.max(x) < 4:
        dateFrame.at[i,12] = 2
    elif np.max(x) >= 4:
        dateFrame.at[i,12] = 3
    elif math.isnan(np.max(x)) :
        dateFrame.at[i,12] = 0 
    i = i + 1

#初中MHT问卷
i = 2
MSSMHS_S = []
for z in range(len(dateFrame)-2):
    MSSMHS = list(dateFrame.loc[i][[14,15,16,17,18,19,20,21]])
    MSSMHS_S.append(MSSMHS)
    i = i + 1
i = 2
for x in MSSMHS_S:
    

    if dateFrame.loc[i][22] > 7 :       
        dateFrame.at[i,22] = 0
    elif np.max(x) < 8 :
        dateFrame.at[i,22] = 0
    elif np.max(x) >= 8 :
        dateFrame.at[i,22] = 1
    
    elif dateFrame.loc[i][14] < 65:
        dateFrame.at[i,22] = 0
    elif dateFrame.loc[i][14] >= 65:
        dateFrame.at[i,22] = 1  
    elif math.isnan(np.max(x)) :
        dateFrame.at[i,22] = 0
    else:
        dateFrame.at[i,22] = 1
    i = i + 1

dateFrame.at[0,12] = 'MSS问卷'
dateFrame.at[0,22] = 'MHT问卷'

i = 2
MSSMHS_S = []
MSSMHS = []
for z in range(len(dateFrame)-2):
    MSSMHS = list(dateFrame.loc[i][[12,22]])
    MSSMHS_S.append(MSSMHS)
    i = i + 1
i = 2
for x in MSSMHS_S:
    if np.max(x) < 1:
        dateFrame.at[i,21] = 0 
    elif np.max(x) < 2:
        dateFrame.at[i,21] = 1
    elif np.max(x) < 3:
        dateFrame.at[i,21] = 2
    elif np.max(x) >= 3:
        dateFrame.at[i,21] = 3
    i = i + 1
dateFrame.at[0,21] = '问卷综合'
    
IAT['MSS'] = dateFrame[12]
IAT['MHT'] = dateFrame[22]
IAT['问卷综合'] = dateFrame[21]
IAT.drop(index=[1],inplace=True)
IAT.to_excel('初中综合预警.xlsx',header=None,index=None)
