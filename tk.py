from tkinter import *
from PIL import Image
# import tensorflow as tf


def paint(event):
    x1, y1 = (event.x-5), (event.y-5)
    x2, y2 = (event.x+5), (event.y+5)
    cv.create_oval(x1, y1, x2, y2, fill='black', outline='black')


def save():
    cv.postscript(file='draw.ps', colormode='color')
    psimage = Image.open('draw.ps')
    psimage.save('draw.png')
    img = Image.open('draw.png')
    resized_img = img.resize((28, 28), Image.ANTIALIAS)
    resized_img.save('num.png')


tk = Tk()
cv = Canvas(tk, width=112, height=112)
cv.bind('<B1-Motion>', paint)
cv.pack()
btn_save = Button(text="save", command=save)
btn_save.pack()

tk.mainloop()
