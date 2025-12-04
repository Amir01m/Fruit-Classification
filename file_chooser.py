from tkinter import filedialog
from PIL import Image 
import numpy as np
from model import main
#file chooser
def chooose_file():
    file = filedialog.askopenfilename(
        title="Selcet a file",
        filetypes=[("All Files","*.*"),("Images", "*.png;*.jpg;*.bmp")]
    )
    user_img0 = Image.open(file)
    imgresize = np.resize(user_img0,(280,280))
    arrimg = np.array(imgresize)
    user_file = arrimg.flatten()
    result = main(user_file)
    return result,user_img0