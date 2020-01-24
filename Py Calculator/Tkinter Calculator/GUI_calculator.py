from tkinter import *

root = Tk()
root.title('Simple Calculator')

# Text field for user input
e = Entry(root, width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=5,padx=10,pady=10)

# Function to Handle individual number buttons clicked
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

# Clears input field
def clear_clicked():
    e.delete(0,END)

# Functions to handle arithmetic buttons
def add_clicked():
    global f_num
    global math 
    math = 'addition'
    first_number = e.get()
    f_num = int(first_number)
    e.delete(0,END)

def subtract_clicked():
    global f_num
    global math 
    math = 'subtraction'
    first_number = e.get()
    f_num = int(first_number)
    e.delete(0,END)

def multiply_clicked():
    global f_num
    global math 
    math = 'multiplication'
    first_number = e.get()
    f_num = int(first_number)
    e.delete(0,END)

def division_clicked():
    global f_num
    global math 
    math = 'division'
    first_number = e.get()
    f_num = int(first_number)
    e.delete(0,END)

def equals_clicked():
    second_number = e.get()
    e.delete(0,END)

    # Test to see what arithmetic method was selected, perform that function, then display in input field
    if math == 'addition':
        sum = f_num + int(second_number)
        e.insert(0,sum)
    elif math == 'subtraction':
        difference = f_num - int(second_number)
        e.insert(0,difference)
    elif math == 'multiplication':
        product = f_num * int(second_number)
        e.insert(0,product)
    elif math == 'division':
        qoutient = f_num / int(second_number)
        e.insert(0,qoutient)

#Define Buttons and put them on the screen with the grid() function

button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1)).grid(row=3,column=0)
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2)).grid(row=3,column=1)
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3)).grid(row=3,column=2)

button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4)).grid(row=2, column=0)
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5)).grid(row=2,column=1)
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6)).grid(row=2,column=2)

button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7)).grid(row=1,column=0)
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8)).grid(row=1,column=1)
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9)).grid(row=1,column=2)

button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0)).grid(row=4,column=0)
button_clear = Button(root, text='Clear', padx=77, pady=20, command=clear_clicked).grid(row=4,column=1,columnspan=2)

button_add = Button(root, text='+', padx=39, pady=20, command=add_clicked).grid(row=1,column=4)
button_equals = Button(root, text='=', padx=87, pady=20, command=equals_clicked).grid(row=5,column=1,columnspan=2)

button_subtract = Button(root, text='-', padx=40, pady=20, command=subtract_clicked).grid(row=2,column=4)
button_subtract = Button(root,text='*', padx=40, pady=20, command=multiply_clicked).grid(row=3,column=4)
button_subtract = Button(root,text='/', padx=40, pady=20, command=division_clicked).grid(row=4,column=4)

# Empty Stylistic buttons for grid layout
style_button1 = Button(root, text=' ', padx=41, pady=20).grid(row=5,column=0)
style_button2 = Button(root, text=' ', padx=41, pady=20).grid(row=5,column=4)

root.mainloop()