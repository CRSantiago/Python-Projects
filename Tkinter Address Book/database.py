from tkinter import *
import sqlite3

root = Tk()
root.geometry("400x600")

# Database

#Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# Create a cursor
curs = conn.cursor()

# Create Table
'''
curs.execute(""" CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text, 
        state text,
        zipcode integer
    )""")
'''

# Create Submit Function for database
def submit():
    #Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create a cursor
    curs = conn.cursor()

    #Insert into table
    curs.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'zipcode': zipcode.get()
        })

    # Commit changes
    conn.commit()

    # Close Connection
    conn.close()


    # Clear Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Create Query Function for database
def query():
    #Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create a cursor
    curs = conn.cursor()

    # Query the database
    curs.execute("SELECT *, oid FROM addresses")
    records = curs.fetchall()
    # print(records)

    table_format = " First Name | Last Name | Address | City | State | Zipcode"
    Label(root, text=table_format).grid(row=11,column=0,columnspan=2)

    # Loop through results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[2]) + " " + str(record[3]) + " " + str(record[4]) + " " + str(record[5]) + " " + str(record[6]) +'\n\n'

    #query_label
    Label(root, text=print_records).grid(row=12, column=0, columnspan=2,padx=10)

    # Commit changes
    conn.commit()

    # Close Connection
    conn.close()

def delete_record():

    #Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create a cursor
    curs = conn.cursor()

    # Delete Record
    curs.execute("DELETE FROM addresses WHERE oid= " + delete_prompt.get())

    # Commit changes
    conn.commit()

    # Close Connection
    conn.close()

def update():
    #Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create a cursor
    curs = conn.cursor()

    record_id = delete_prompt.get()
    curs.execute("""UPDATE addresses SET
		first_name = :first,
		last_name = :last,
		address = :address,
		city = :city,
		state = :state,
		zipcode = :zipcode 
		WHERE oid = :oid""",
		{
		'first': f_name_editor.get(),
		'last': l_name_editor.get(),
		'address': address_editor.get(),
		'city': city_editor.get(),
		'state': state_editor.get(),
		'zipcode': zipcode_editor.get(),
		'oid': record_id
		})


     # Commit changes
    conn.commit()

    # Close Connection
    conn.close()

    editor.destroy()
    root.deiconify()

# Update record function
def edit():
    root.withdraw()
    global editor
    editor = Tk()
    editor.geometry("400x600")

    #Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create a cursor
    curs = conn.cursor()

    record_id = delete_prompt.get()
    # Query the database
    curs.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = curs.fetchall()

    #Create Global Variables for text box names
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # Create Text Box
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1)
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)
    

    # Create Text Box Labels
    f_name_lbl = Label(editor, text="First Name:")
    f_name_lbl.grid(row=0, column=0, padx=10)
    l_name_lbl = Label(editor, text="Last Name:")
    l_name_lbl.grid(row=1, column=0, padx=10)
    address_lbl = Label(editor, text="Address:")
    address_lbl.grid(row=2, column=0, padx=10)
    city_lbl = Label(editor, text="City:")
    city_lbl.grid(row=3, column=0, padx=10)
    state_lbl = Label(editor, text="State:")
    state_lbl.grid(row=4, column=0, padx=10)
    zipcode_lbl = Label(editor, text="Zipcode:")
    zipcode_lbl.grid(row=5, column=0, padx=10)

    # Save Button
    Button(editor, text="Save Record", command=update).grid(row=6,column=0, columnspan=2, padx=20, ipadx=120)

    # Loop thru results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])
    
    # END OF EDIT

# Create Text Box
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)
delete_prompt = Entry(root,width=30)
delete_prompt.grid(row=8,column=1)

# Create Text Box Labels
f_name_lbl = Label(root, text="First Name:")
f_name_lbl.grid(row=0, column=0, padx=10)
l_name_lbl = Label(root, text="Last Name:")
l_name_lbl.grid(row=1, column=0, padx=10)
address_lbl = Label(root, text="Address:")
address_lbl.grid(row=2, column=0, padx=10)
city_lbl = Label(root, text="City:")
city_lbl.grid(row=3, column=0, padx=10)
state_lbl = Label(root, text="State:")
state_lbl.grid(row=4, column=0, padx=10)
zipcode_lbl = Label(root, text="Zipcode:")
zipcode_lbl.grid(row=5, column=0, padx=10)
delete_prompt_lbl = Label(root, text='Select ID')
delete_prompt_lbl.grid(row=8,column=0)


# Creat Submit Button
submit_btn = Button(root, text="Add Record To Database", command=submit).grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# Create Query Button
query_btn = Button(root, text="Show Records", command=query).grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=128)

# Create Delete Button
delete_btn = Button(root, text="Delete Record", command=delete_record).grid(row=9,column=0,columnspan=2, padx=10, pady=10, ipadx=129)

# Create an Update Button
update_btn = Button(root, text="Update Record", command=edit).grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=129)

# Commit changes
conn.commit()

# Close Connection
conn.close()

root.mainloop()