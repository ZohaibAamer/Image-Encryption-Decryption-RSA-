from rsa import *
import numpy as np
import cv2 as cv
import ctypes
import matplotlib.pyplot as plt



def main():
    obj = rsa()

    img_name = input("enter the name of image file:")
    img = cv.imread(img_name,cv.IMREAD_COLOR)

    cv.imshow('image to be encrypted/decrypted',img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    height, width, channels = img.shape
    temp = np.zeros((height,width,3), dtype=np.uint64)
        
    for a in range (0,height):
        for b in range (0,width):
                x,y,z =  img[a][b]
                x = np.int(x)
                y = np.int(y)
                z = np.int(z)
                x = obj.Cipher(x)
                y = obj.Cipher(y)
                z = obj.Cipher(z)
                temp[a][b] = x,y,z

    cv.imshow('encrypted picture',np.array(temp,dtype = np.uint8))
    cv.waitKey(0)
    cv.destroyAllWindows()
    
    temp1 = np.zeros((height,width,3), np.uint8)

    for a in range (0,height):
        for b in range (0,width):
                x,y,z =  temp[a][b]
                x = np.int(x)
                y = np.int(y)
                z = np.int(z)
                x = obj.deCipher(x)
                y = obj.deCipher(y)
                z = obj.deCipher(z)
                x = np.uint8(x)
                y = np.uint8(y)
                z = np.uint8(z)
                temp1[a][b] = x,y,z
        
    cv.imshow('depcrypted picture',temp1)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()