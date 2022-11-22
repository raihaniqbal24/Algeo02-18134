from PIL import Image 
from numpy import matrix
from numpy import dot
import numpy as np
import cv2 
from cv2 import norm
from os import path 
import os 
import pickle
from matplotlib import projections
im = cv2.imread(r"C:\Users\dhiwa\python\download.jpg")
ar = im.flatten() 
at = ar.transpose()
ac = np.cov(ar)
def dekomQR(mtr) : 
    q = np.empty(mtr.shape)
    for i in range(mtr.shape[1]): 
        v = mtr[:,i] 
        for j in range(0,i): 
            v = v - projections(mtr[:,i],q[:,j])[0]
        q[:,i] = v 
    for r in range(q.shape[0]): 
        q[:,r] = norm(q[:,r])
    z = np.zeros(mtr.shape)
    for x in range(z.shape[0]):
        for y in range(x,z.shape[1]): 
            z[x][y] = dot(q[:,x],mtr[:,y])
    return q, z 
def eigenvalue(mtr):
    a = np.identity(mtr.shape[0])
    v1 = mtr 
    for i in range(50): 
        q, r = dekomQR(v1) 
        a = a @ q
        v1 = r @ q
    return v1.diagonal(),a
def addfile(image_path):
    print("memperbarui database\n")
    database_path='src/'
    file = [os.path.join(image_path,p) for p in sorted(os.listdir(image_path))] 
    res = {}
    for i in file : 
        name = i.split('/')[-1].lower()
        res[name] = cv2.imread(i) 
    if os.path.exists(database_path): 
        os.remove(database_path)
    nbfile = open(database_path,'ab')
    pickle.dump(res, nbfile) 
    nbfile.close()

    print('gambar sampel telah selesai di upload')
    return         

eigenvalue(im)