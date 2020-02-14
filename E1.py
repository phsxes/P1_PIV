from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import cv2

levels = [8, 7, 6, 5, 4, 3, 2, 1, 0]

def Image1():
    img1.configure(image=root.photo1)
    root.image=1
    img2.configure(image=root.photo1)


def Image2():
    img1.configure(image=root.photo2)
    root.image=2
    img2.configure(image=root.photo2)


def Image3():
    img1.configure(image=root.photo3)
    root.image=3
    img2.configure(image=root.photo3)


def filter(self):
    if root.image == 1:
        img = cv2.imread('Image1.png')
    elif root.image == 2:
        img = cv2.imread('Image2.jpg')
    else:
        img = cv2.imread('Image3.jpg')
    
    img8 = np.array(img)
    k = int(k_slider.get())
    k = levels[k]
    mult = 2**k
    resp = img8 // mult * mult
    cv2.imwrite('resp.png',resp)
    result = ImageTk.PhotoImage(Image.open('resp.png'))
    img2.configure(image=result)
    img2.image = result


root = Tk()
root.title("Quantization")
root.geometry("1300x550")
root.image = 1

root.photo1 = ImageTk.PhotoImage(Image.open("Image1.png"))
root.photo2 = ImageTk.PhotoImage(Image.open("Image2.jpg"))
root.photo3 = ImageTk.PhotoImage(Image.open("Image3.jpg"))

b1 = Button(root,text="Image 1",command=Image1)
b1.pack(side=LEFT)
b2 = Button(root,text="Image 2",command=Image2)
b2.pack(side=LEFT)
b3 = Button(root,text="Image 3",command=Image3)
b3.pack(side=LEFT)
k_slider = Scale(root, from_=8, to=1, command=filter)
k_slider.pack(side=LEFT)
k_slider.set(8)
img2 = Label(root, image=root.photo1)
img2.pack(side=RIGHT)
img1 = Label(root, image=root.photo1)
img1.pack(side=RIGHT)

root.mainloop()
