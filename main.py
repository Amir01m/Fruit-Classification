import numpy as np
import sklearn
import matplotlib as plt
from PIL import Image , ImageTk
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import glob 
import tkinter as ttk
from tkinter import filedialog

#file chooser
def chooose_file():
    global user_img0
    file = filedialog.askopenfilename(
        title="Selcet a file",
        filetypes=[("All Files","*.*"),("Images", "*.png;*.jpg;*.bmp")]
    )
    user_img0 = Image.open(file)
    imgresize = np.resize(user_img0,(280,280))
    arrimg = np.array(imgresize)
    user_file = arrimg.flatten()
    main(user_file)


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
    
    global label,user_img0,tk_img
    predict_asl = model.predict([user_file])
    label.config(text=predict_asl[0])
    user_img0 = user_img0.resize((280,280))
    tk_img = ImageTk.PhotoImage(user_img0)
    user_img.config(image=tk_img)



#GUI
def gui():
    global label,user_img
    root = ttk.Tk()
    root.geometry("450x500")
    root.resizable(False,False)

    top = ttk.Label(root,text="Fruit Classifiction",font=("Arial",14))    
    top.pack(pady=15)
    
    btn = ttk.Button(root,text="choose file",command=chooose_file)
    btn.pack(pady=10)
    
    label = ttk.Label(root,text="None",bg="lightgray",bd=2,width=15,height=2)
    label.pack(pady=10)

    exitbtn = ttk.Button(root,text="Exit",command=root.destroy,width=10,height=1,bg="red",fg="white")
    exitbtn.pack(pady=5,side="bottom")

    user_img = ttk.Label(root,text="User Image",font=("Arial",12),image="",width=280,height=280,border=2,relief="solid",bg="white")
    user_img.pack(padx=100,pady=38)

    
    root.mainloop()

gui()
