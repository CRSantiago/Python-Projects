from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()

def open():
    global img
    root.filename = filedialog.askopenfilename(initialdir='\Tkinter\Image Viewer', title="Select A File", filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
    Label(root, text=root.filename).pack()
    img = ImageTk.PhotoImage(Image.open(root.filename))
    Label(image=img).pack()

Button(root, text='Open File', command=open).pack()

root.mainloop()