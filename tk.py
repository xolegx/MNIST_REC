from tkinter import *
from PIL import Image, ImageDraw


def paint(event):
    x1, y1 = (event.x-1), (event.y-1)
    x2, y2 = (event.x+1), (event.y+1)
    cv.create_oval(x1, y1, x2, y2, fill='black', outline='black')


win = Tk()
cv = Canvas(win, width=280, height=280, bg='white')
cv.bind('<B1-Motion>', paint)
cv.pack()
img = Image.new('RGB',(28, 28), (255, 255, 255))
drw = ImageDraw.Draw(img)
img.save('111.jpg')
win.mainloop()