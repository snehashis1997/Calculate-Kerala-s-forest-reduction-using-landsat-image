# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 08:19:01 2019

@author: user
"""
import matplotlib.pyplot as plt
import cv2
import numpy as np
import copy
after='C:/Users/user/Desktop/forest/india/kerala/after/'
before='C:/Users/user/Desktop/forest/india/kerala/before/'

bef=[]
aft=[]

for i in range(1,8):
     bef.append(cv2.imread(before+str(i)+".tif",0))
     
for i in range(1,7):
     aft.append(cv2.imread(after+str(i)+".tif",0))
     
befn=[]
aftn=[]
for i in range(7):
     befn.append(np.float32(cv2.equalizeHist(bef[i])))

for i in range(6):
     aftn.append(np.float32(cv2.equalizeHist(aft[i])))
    
before=cv2.merge((befn[0],befn[1],befn[2],befn[3],befn[4],befn[5],befn[6]))
after=cv2.merge((aftn[0],aftn[1],aftn[2],aftn[3],aftn[4],aftn[5]))

before_n=before.reshape((-1,7))
after_n=after.reshape((-1,6))

criteria = (cv2. TERM_CRITERIA_EPS + cv2. TERM_CRITERIA_MAX_ITER, 20, 1.0)
ret,label,center=cv2.kmeans(before_n,6,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)


center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((before.shape))
before_final=copy.deepcopy(res2[:][:,:,:3])

criteria = (cv2. TERM_CRITERIA_EPS + cv2. TERM_CRITERIA_MAX_ITER, 20, 1.0)
ret,label,center=cv2.kmeans(after_n,6,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)


center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((after.shape))
after_final=copy.deepcopy(res2[:][:,:,:3])


cv2.imwrite("2005" +".tif",after_final)
cv2.imwrite("1990" +".tif",before_final)



fi=np.hstack((before_final,after_final))


d=0
q=0
for i in range(len(after_final)):
    for j in range(len(after_final[i])):
        if np.sum(after_final[i][j]<=669) or np.sum(after_final[i][j]>=667):
            d+=1
            if (np.sum(before_final[i][j]<=195) or np.sum(before_final[i][j]>=192)):
                q=q+1
                
area=q*900
print('total forest destroy area: ',area,'square meters' )
      
plt.imshow(fi),plt.title(str(area)+' sq mtrs forest reduction')
plt.show()



    
                    
                    


            
    

