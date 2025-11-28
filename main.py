import numpy as np
import sklearn
import matplotlib as plt
from PIL import Image
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import glob 
import tkinter as ttk
from tkinter import filedialog

def chooose_file():
    file = filedialog.askopenfilename(
        title="Selcet a file",
        filetypes=[("All Files","*.*"),("Images", "*.png;*.jpg;*.bmp")]
    )
    img = Image.open(file)
    img = np.resize(img,(280,280))
    arrimg = np.array(img)
    user_file = arrimg.flatten()
    main(user_file)

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
    
    global label
    predict_asl = model.predict([user_file])
    label.config(text=predict_asl[0])
    
def gui():
    global label
    root = ttk.Tk()
    root.geometry("400x450")
    root.resizable(False,False)

    top = ttk.Label(root,text="Fruit Classifiction",font=("Arial",14))    
    top.pack(pady=15)
    
    btn = ttk.Button(root,text="choose file",command=chooose_file)
    btn.pack(pady=10)
    
    label = ttk.Label(root,text="None",bg="lightgray",bd=2,width=15,height=2)
    label.pack(pady=10)

    

    canva = ttk.Canvas(root,width=350,height=200,bg="lightgray")
    canva.pack()

    exitbtn = ttk.Button(root,text="Exit",command=root.destroy)
    exitbtn.pack(pady=25)
    root.mainloop()

gui()

#add test pic and show pic of user have been choosen