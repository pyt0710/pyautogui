import pandas as pd
import numpy as np
import math
import sys


input_file = input()
highSchool = pd.read_excel(input_file,header=None)

dateFrame = highSchool

#高中IAT判断抑郁


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
        dateFrame.at[i,4] = 0
    elif ((((x + 0.1036) / 0.2486) * 10) + 50) < 63.80:
        dateFrame.at[i,4] = 0
    elif ((((x + 0.1036) / 0.2486) * 10) + 50) >= 63.80:
        dateFrame.at[i,4] = 2
    i = i + 1

    
#高中PHQ抑郁

i = 2
MSSMHS_S = []
MSSMHS = []
for z in range(len(dateFrame)-2):
    MSSMHS = dateFrame.loc[i][3]
    MSSMHS_S.append(MSSMHS)
    i = i + 1
i = 2
#print(MSSMHS_S)
for x in MSSMHS_S:
    

    if x < 6:
        dateFrame.at[i,5] = 0 
    elif x < 10:
        dateFrame.at[i,5] = 1
    elif x < 15:
        dateFrame.at[i,5] = 2
    elif x >= 15:
        dateFrame.at[i,5] = 3
    elif math.isnan(x):
        dateFrame.at[i,5] = 0
    i = i + 1
    

    
    
#高中SCL抑郁
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
    

    if x < 2:
        dateFrame.at[i,8] = 0 
    elif x < 3:
        dateFrame.at[i,8] = 1
    elif x >= 3:
        dateFrame.at[i,8] = 2
    elif math.isnan(x):
        dateFrame.at[i,8] = 0
    i = i + 1
    

#高中MSS抑郁
i = 2
MSSMHS_S = []
MSSMHS = []
for z in range(len(dateFrame)-2):
    MSSMHS = dateFrame.loc[i][21]
    MSSMHS_S.append(MSSMHS)
    i = i + 1
i = 2
#print(MSSMHS_S)
for x in MSSMHS_S:
    

    if x < 2:
        dateFrame.at[i,22] = 0 
    elif x < 3:
        dateFrame.at[i,22] = 1
    elif x < 4:
        dateFrame.at[i,22] = 2
    elif x >= 4:
        dateFrame.at[i,22] = 3
    elif math.isnan(x):
        dateFrame.at[i,22] = 0
    i = i + 1
    
IAT = dateFrame[[1,4,5,8,22,23]]
IAT.at[0,4] = 'IAT抑郁'
IAT.at[0,5] = 'PHQ抑郁'
IAT.at[0,22] = 'MSS抑郁'
IAT.at[0,22] = 'MSS抑郁'
IAT.at[0,8] = 'SCL抑郁'



#抑郁综合
i = 2
MSSMHS_S = []
MSSMHS = []
for z in range(len(dateFrame)-2):
    MSSMHS = list(IAT.loc[i][[4,5,8,22]])
    MSSMHS_S.append(MSSMHS)
    i = i + 1
i = 2
#print(MSSMHS_S)
for x in MSSMHS_S:

    

    if np.max(x) < 1:
        IAT.at[i,23] = 0 
    elif np.max(x) < 2:
        IAT.at[i,23] = 1
    elif np.max(x) < 3:
        IAT.at[i,23] = 2
    elif np.max(x) >= 3:
        IAT.at[i,23] = 3
    elif math.isnan(x):
        IAT.at[i,23] = 0
    i = i + 1
    
IAT.at[0,23] = '抑郁综合'
IAT.columns = (0,1,2,3,4,5)




highSchool = pd.read_excel(input_file,header=None)

dateFrame = highSchool

#高中PHQ
i = 2
MSSMHS_S = []
MSSMHS = []
for z in range(len(dateFrame)-2):
    MSSMHS = dateFrame.loc[i][3]
    MSSMHS_S.append(MSSMHS)
    i = i + 1
i = 2
for x in MSSMHS_S:
    if math.isnan(x):
        dateFrame.at[i,2] = 0
    elif x < 6:
        dateFrame.at[i,2] = 0 
    elif x < 10:
        dateFrame.at[i,2] = 1
    elif x < 15:
        dateFrame.at[i,2] = 2
    elif x >= 15:
        dateFrame.at[i,2] = 3
    i = i + 1
    
    
#高中SCL
i = 2
MSSMHS_S = []
MSSMHS = []
for z in range(len(dateFrame)-2):
    MSSMHS = list(dateFrame.loc[i][[4,5,6,7,8,9,10,11,12]])
    MSSMHS_S.append(MSSMHS)
    i = i + 1
i = 2
for x in MSSMHS_S:

    if np.max(x) < 2:
        dateFrame.at[i,13] = 0 
    elif np.max(x) < 3:
        dateFrame.at[i,13] = 1
    elif np.max(x) >= 3:
        dateFrame.at[i,13] = 2
    elif math.isnan(np.max(x)):
        dateFrame.at[i,13] = 0
    i = i + 1
    
    
#高中MSS
i = 2
MSSMHS_S = []
for z in range(len(dateFrame)-2):
    MSSMHS = list(dateFrame.loc[i][[17,18,19,20,21,22,23,24,25,26]])
    MSSMHS_S.append(MSSMHS)
    i = i + 1
i = 2
for x in MSSMHS_S:
    

    if np.max(x) < 2:
        dateFrame.at[i,16] = 0 
    elif np.max(x) < 3:
        dateFrame.at[i,16] = 1
    elif np.max(x) < 4:
        dateFrame.at[i,16] = 2
    elif np.max(x) >= 4:
        dateFrame.at[i,16] = 3
    elif math.isnan(np.max(x)):
        dateFrame.at[i,16] = 0
    i = i + 1
dateFrame.at[0,2] = 'PHQ' 
dateFrame.at[0,13] = 'SCL' 
dateFrame.at[0,16] = 'MSS' 


IAT[['PHQ','SCL','MSS']] = dateFrame[[2,13,16]]



# 问卷综合预警
dateFrame = dateFrame[[1,2,13,16]]
dateFrame.columns = (0,1,2,3)

i = 2
MSSMHS_S = []
MSSMHS = []
for z in range(len(dateFrame)-2):
    MSSMHS = list(dateFrame.loc[i][[1,2,3]])
    MSSMHS_S.append(MSSMHS)
    i = i + 1
i = 2
for x in MSSMHS_S:
    if np.max(x) < 1:
        dateFrame.at[i,2] = 0 
    elif np.max(x) < 2:
        dateFrame.at[i,2] = 1
    elif np.max(x) < 3:
        dateFrame.at[i,2] = 2
    elif np.max(x) >= 3:
        dateFrame.at[i,2] = 3
    i = i + 1

dateFrame.at[0,2] = '问卷综合'
IAT['问卷综合'] = dateFrame[2]


#IAT.insert(5,dateFrame[2]) 


IAT.drop(index=[1],inplace=True)
IAT.to_excel('高中综合预警.xlsx',index=None,header=None)

print('ok')
