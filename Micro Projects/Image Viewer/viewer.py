from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Image Viewer')

img_1 = ImageTk.PhotoImage(Image.open('Images/code.jpg'))
img_2 = ImageTk.PhotoImage(Image.open('Images/art-1.jpg'))
img_3 = ImageTk.PhotoImage(Image.open('Images/art-2.jpg'))
img_4 = ImageTk.PhotoImage(Image.open('Images/art-3.jpg'))

img_label = Label(image=img_1)
img_label.grid(row=0, column=0, columnspan=3)

images_list = [img_1,img_2,img_3,img_4]

# Creates and displays status bar when application is started
status = Label(root, text="Image 1 of " + str(len(images_list)), bd=1, relief=SUNKEN, anchor=E, pady=5)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def forward(image_number):
    global img_label
    global back_button
    global forward_button
    
    # Removes Current Label Widget that contains the image
    img_label.grid_forget()

    # Creates new Label widget based on number passed in
    img_label = Label(image=images_list[image_number-1])

    # Updates the buttons
    back_button = Button(root, text='<-', padx=20, pady=10, command=lambda: backward(image_number-1))
    forward_button = Button(root, text='->', padx=20, pady=10, command=lambda: forward(image_number+1))
    
    # DISABLES forward button if at last image
    if image_number == 4:
        forward_button = Button(root, text='->', padx=20, pady=10, state=DISABLED)

    # Redisplays Label and Button widgets
    img_label.grid(row=0,column=0,columnspan=3)
    forward_button.grid(row=1, column=2)
    back_button.grid(row=1, column=0)

    # Update Status Bar
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(images_list)), bd=1, relief=SUNKEN, anchor=E, pady=5)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def backward(image_number):
    global img_label
    global back_button
    global forward_button
    
    # Removes Current Label Widget that contains the image
    img_label.grid_forget()

    # Creates new Label widget based on number passed in
    img_label = Label(image=images_list[image_number-1])

    # Updates the buttons
    back_button = Button(root, text='<-', padx=20, pady=10, command=lambda: backward(image_number-1))
    forward_button = Button(root, text='->', padx=20, pady=10, command=lambda: forward(image_number+1))
    
    #DISABLES back button if at the first image
    if image_number == 1:
        back_button = Button(root, text='<-', padx=20, pady=10, state=DISABLED)

    # Redisplays Label and Button widgets
    img_label.grid(row=0,column=0,columnspan=3)
    forward_button.grid(row=1, column=2)
    back_button.grid(row=1, column=0)

    # Update Status Bar
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(images_list)), bd=1, relief=SUNKEN, anchor=E, pady=5)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


# Creation of buttons when program is started
back_button = Button(root, text='<-', padx=20, pady=10, command=backward).grid(row=1, column=0)
exit_button = Button(root, text='Exit', padx=20, pady=10, command=root.quit).grid(row=1, column=1)
forward_button = Button(root, text='->', padx=20, pady=10, command=lambda: forward(2)).grid(row=1, column=2)

root.mainloop()