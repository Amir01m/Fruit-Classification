import tkinter as ttk
from file_chooser import chooose_file
from PIL import ImageTk
#GUI
def gui():
    root = ttk.Tk()
    root.geometry("450x500")
    root.resizable(False,False)

    top = ttk.Label(root,text="Fruit Classifiction",font=("Arial",14))    
    top.pack(pady=15)
    
    
    def select_image():
        result , user_img = chooose_file()

        if user_img is not None:
            label.config(text=result)
            user_img = user_img.resize((280,280))
            tk_image = ImageTk.PhotoImage(user_img)
            user_img_label.config(image=tk_image)
            user_img_label.image = tk_image
            
            
            
    
    btn = ttk.Button(root,text="choose file",command=select_image)
    btn.pack(pady=10)
    
    label = ttk.Label(root,text="None",bg="lightgray",bd=2,width=15,height=2)
    label.pack(pady=10)

    exitbtn = ttk.Button(root,text="Exit",command=root.destroy,width=10,height=1,bg="red",fg="white")
    exitbtn.pack(pady=5,side="bottom")

    
    user_img_label = ttk.Label(root,text="User Image",font=("Arial",12),image="",width=280,height=280,border=2,relief="solid",bg="white")
    user_img_label.pack(padx=100,pady=38)

    root.mainloop()

if __name__ == "__main__":
    gui()