from tkinter import *

root = Tk()
root.title("Radio Buttons!")

MODES = [
    ("Small","S"),
    ("Medium","M"),
    ("Large","L"),
    ("Extra Large","XL")
]

opt = StringVar()
opt.set(" ")

for text,mode in MODES:
    Radiobutton(root, text=text, variable=opt, value=mode).pack(anchor=W)

def clicked(value):
    label = Label(root, text=value).pack()

btn = Button(root, text="Submit Size", command=lambda: clicked(opt.get())).pack()

root.mainloop()