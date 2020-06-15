from tkinter import *
from PIL import ImageTk, Image

r = Tk()
r.title("Image viewer")

img1 = ImageTk.PhotoImage(Image.open("c:/Users/Rishi Kumar/pics/20190629_020038"))
img2 = ImageTk.PhotoImage(Image.open("c:/Users/Rishi Kumar/pics/20190702_161340"))
img3 = ImageTk.PhotoImage(Image.open("c:/Users/Rishi Kumar/pics/20190706_144843"))
img4 = ImageTk.PhotoImage(Image.open("c:/Users/Rishi Kumar/pics/20190706_144904"))
img5 = ImageTk.PhotoImage(Image.open("c:/Users/Rishi Kumar/pics/20171018103510_IMG_2475"))

img_lst = [img1, img2, img3, img4, img5]
button_quit = Button(r, text="Exit", command=r.quit).grid(row=1, column=1)
i = Label(image=img1)
i.grid(row=0, column=0, columnspan=3)
c = 0


def next_i():
    global c
    global i
    i.grid_forget()
    if c < 4:
        c = c+1
    else:
        c = 0
    i = Label(image=img_lst[c])


def back_i():
    global c
    global i
    i.grid_forget()
    if c > 0:
        c = c-1
    else:
        c = 4
    i = Label(image=img_lst[c])


B_next = Button(r, text="-->", command=next_i).grid(row=1, column=2)
B_prev = Button(r, text="<--", command=back_i).grid(row=1, column=0)


r.mainloop()


