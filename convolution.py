import numpy as np 
import cv2 
import math
 def Mask():    
 size=int(input('What is the size of the mask?'))  
   mask = np.zeros([size, size], dtype=np.uint8)     
print('Enter the values please!')     
 for x in range(size):        
 for y in range(size):          
   mask[x][y]=input()     #Entering the values of the mask     ans=input('Is it a box filter? Enter y or n')  
   if ans=='y':  #Smoothing filter       mask=mask/(size*size)     print(mask)    
 return mask,size 
 def Padding(img,p_size):     row = img.shape[0]     col = img.shape[1] 
    pad_img = np.zeros([row +(2*p_size), col+(2*p_size)], dtype=np.uint8)     pad_img[p_size:row+p_size,p_size:col+p_size]=img  #Pixel Replication     return pad_img 
 def convolution(pad_img,mask,p_size,output): 
    row = pad_img.shape[0]     col = pad_img.shape[1]     for x in np.arange(p_size,row-p_size):         for y in np.arange(p_size, col - p_size): 
            selected_pixels=pad_img[x-p_size:x+p_size+1,y-p_size:y+p_size+1] 
#Extracting original image pixels equal to the size of mask 
            c=(selected_pixels*mask).sum() #Multiplying pixel by pixel and then adding             output[x-p_size][y-p_size]=c     return output 
 def normalization(output):     row = output.shape[0]     col = output.shape[1]     histogram = [0] * 256 
    PDF = [0] * 256 
    CDF = [0] * 256     TF = [0] * 256     for x in range(row): 
        for y in range(col): 
            histogram[img[x][y]] += 1     for i in range(256): 
        PDF[i] = histogram[i] / (row * col)     CDF[0] = PDF[0]     for i in range(1, 256): 
        CDF[i] = PDF[i] + CDF[i - 1]     for i in range(256): 
        TF[i] = round(CDF[i] * 255) 
    normalized = np.zeros([row, col], dtype=np.uint8)     for x in range(row):         for y in range(col): 
            normalized[x][y] = TF[img[x][y]]     return normalized 
 
img = cv2.imread('D:\Semester 6\Digital Image 
Processing\pictures\lab5\Cameraman.tif',cv2.IMREAD_GRAYSCALE) mask,size=Mask() 
row=img.shape[0] col=img.shape[1] 
output = np.zeros([row , col], dtype=np.uint8) 
p_size=math.floor(size/2) #number of rows and columns to be added pad_img=Padding(img,p_size) 
output=convolution(pad_img,mask,p_size,output) normalized=normalization(output) cv2.imshow('lab1', normalized) cv2.waitKey(60000) 
cv2.imwrite('box.jpg', normalized) 
