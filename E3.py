from tkinter import *
import numpy as np
import cv2

# Imagenes a utilizar
A = .5;
imgc = cv2.imread('D:\My local documents/cetys/2020/Spring/Diseno de videojuegos/Practica 1 equipo/Chess.png', 1);
imgcam = cv2.imread('D:\My local documents/cetys/2020/Spring/Diseno de videojuegos/Practica 1 equipo/Camino.png', 1);
imgcas = cv2.imread('D:\My local documents/cetys/2020/Spring/Diseno de videojuegos/Practica 1 equipo/Cascada.png', 1);
imgh = cv2.imread('D:\My local documents/cetys/2020/Spring/Diseno de videojuegos/Practica 1 equipo/Hielo.png', 1);
imgpo = cv2.imread('D:\My local documents/cetys/2020/Spring/Diseno de videojuegos/Practica 1 equipo/Pollo.png', 1);
imgpu = cv2.imread('D:\My local documents/cetys/2020/Spring/Diseno de videojuegos/Practica 1 equipo/Puente.png', 1);
img1 = [cv2.imread('D:\My local documents/cetys/2020/Spring/Diseno de videojuegos/Practica 1 equipo/Chess.png', 1)];
img1.clear();

window = Tk()
sz = [0];
window.title("Image Selection Menu. Select only 2. Numbers [0-->2] are recomended")

window.geometry('550x250')

# Texto inicial
lbl = Label(window, text=("Current number of selected images:" + str(sz[0])))
lbl2 = Label(window, text="Select a chess piece?")
lbl3 = Label(window, text="Select a walkway?")
lbl4 = Label(window, text="Select a waterfall?")
lbl5 = Label(window, text="Select an icy landscape?")
lbl6 = Label(window, text="Select a chicken (not actually a chicken)?")
lbl7 = Label(window, text="Select a bridge?")

# Posicion de los cuadros de texto
lbl.grid(column=0, row=0)
lbl2.grid(column=0, row=1)
lbl3.grid(column=0, row=2)
lbl4.grid(column=0, row=3)
lbl5.grid(column=0, row=4)
lbl6.grid(column=0, row=5)
lbl7.grid(column=0, row=6)

A = Entry(window, width=15)
A.insert(END, '.5')
A.grid(column=1, row=0)


def clicked():
    lbl.configure(text="Button was clicked !!")
    exit();


def pntimg():
    lbl.configure(text="just Printed")
    imga = img1[0].astype(np.float) / 255;
    imgb = img1[1].astype(np.float) / 255;
    img = (imga * float(A.get()) + imgb * (1 - float(A.get())));
    cv2.imshow('Processed', img);


def Scat():
    img1.append(imgc);
    lbl2.configure(text="Selected chess")
    sz[0] = len(img1);
    lbl.configure(text=("Current number of selected images:" + str(sz[0])))


def Swlk():
    img1.append(imgcam);
    lbl3.configure(text="Selected walkway")
    sz[0] = len(img1);
    lbl.configure(text=("Current number of selected images:" + str(sz[0])))


def Sfall():
    img1.append(imgcas);
    lbl4.configure(text="Selected waterfall")
    sz[0] = len(img1);
    lbl.configure(text=("Current number of selected images:" + str(sz[0])))


def Sice():
    img1.append(imgh)
    lbl5.configure(text="Selected icy landscape")
    sz[0] = len(img1);
    lbl.configure(text=("Current number of selected images:" + str(sz[0])))


def Schk():
    img1.append(imgpo);
    lbl6.configure(text="Selected the not-chicken")
    sz[0] = len(img1);
    lbl.configure(text=("Current number of selected images:" + str(sz[0])))


def Sbrg():
    img1.append(imgpu);
    lbl7.configure(text="Selected bridge")
    sz[0] = len(img1);
    lbl.configure(text=("Current number of selected images:" + str(sz[0])))


def reset():
    cv2.destroyAllWindows();
    img1.clear();
    sz[0] = len(img1);
    lbl.configure(text=("Current number of selected images:" + str(sz[0])))

    lbl2.configure(text="Select a Chess Piece?");
    lbl3.configure(text="Select a walkway?")
    lbl4.configure(text="Select a waterfall?")
    lbl5.configure(text="Select an icy landscape?")

window.mainloop()