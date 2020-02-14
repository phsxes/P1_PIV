import cv2
import numpy as np
from tkinter import *

window = Tk()
window.geometry("200x150")
window.title("N-Res")
filename = 'Image1.png'
im = cv2.imread(filename)
cv2.imshow("Img", im)


def down_sampling(path, n):
    im = cv2.imread(filename)
    setting = t_btn.cget('text')
    fr, fg, fb = cv2.split(im)
    for y in range(0, im.shape[0], n):
        for x in range(0, im.shape[1], n):
            if setting == "max":
                fr[y:y+n, x:x+n] = np.max(fr[y:y+n, x:x+n])
                fg[y:y + n, x:x + n] = np.max(fg[y:y + n, x:x + n])
                fb[y:y + n, x:x + n] = np.max(fb[y:y + n, x:x + n])
            else:
                fr[y:y + n, x:x + n] = np.min(fr[y:y + n, x:x + n])
                fg[y:y + n, x:x + n] = np.min(fg[y:y + n, x:x + n])
                fb[y:y + n, x:x + n] = np.min(fb[y:y + n, x:x + n])
    im = cv2.merge((fr, fg, fb))
    cv2.imshow("Img", im)
    cv2.waitKey(1)


def update_value(self):
    n = n_slider.get()
    down_sampling(filename, n)


def toggle():
    index_dict = {"max": "min", "min": "max"}
    index[0] = index_dict[index[0]]
    t_btn['text'] = index[0]


n_slider = Scale(window, from_=15, to=1, command=update_value)
n_slider.pack()
index = ["max"]
t_btn = Button(text=index[0], width=12, command=toggle)
t_btn.pack(pady=5)
window.mainloop()
