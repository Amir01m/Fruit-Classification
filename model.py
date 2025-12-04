import glob 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from PIL import Image 
#ML model
def main(user_file):
    path = glob.glob("dataset/**/*.*")
    x = []
    for num in range(42):
        img = Image.open(path[num])
        img = np.resize(img,(280,280))
        arrimg = np.array(img)
        #arrimg = arrimg[:,:,0]
        arrimg = arrimg.flatten()
        x.append(arrimg)

    y = ["apple","apple","apple","apple","apple","apple","apple","apple","apple","apple","apple","apple","apple","apple","apple","apple","apple","apple","apple","apple","apple","apple",
        "bannana","bannana","bannana","bannana","bannana","bannana","bannana","bannana","bannana","bannana","bannana","bannana","bannana","bannana","bannana","bannana","bannana","bannana","bannana","bannana"
        ]

    xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.1)

    model = KNeighborsClassifier()
    model.fit(xtrain,ytrain)
    
    predict_asl = model.predict([user_file])
    return predict_asl[0]    
