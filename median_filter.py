def median(pad_img,output,p_size,size1):
    row = pad_img.shape[0]
    col = pad_img.shape[1]
    s=size1**2
    median=[0]*s
    for x in np.arange(p_size,row-p_size):
        for y in np.arange(p_size, col - p_size):
            selected_pixels = pad_img[x - p_size:x + p_size + 1, y - p_size:y + p_size + 1]  # Extracting original image pixels equal to the size of mask
            a=0
            for i in range(size1):
                for j in range(size1):
                    median[a]=selected_pixels[i,j]
                    a=a+1
            for i in range(len(median)):
                for j in range(i + 1, len(median)):
                    if median[i] > median[j]:
                        median[i], median[j] = median[j], median[i]
            index=math.ceil(s/2)
            output[x - p_size][y - p_size] = median[index]
    return output
img1 = cv2.imread('D:\Semester 6\Digital Image Processing\pictures\lab5\Beans.tif',cv2.IMREAD_GRAYSCALE)
row=img1.shape[0]
col=img1.shape[1]
output = np.zeros([row , col] , dtype=np.uint8)
size1=int(input('Size of neighborhood?'))
p_size=math.floor(size1/2)
pad_img=Padding(img1,p_size)
output1=median(pad_img,output,p_size,size1)
output1=normalization(output1)
cv2.imshow('lab1', output1)