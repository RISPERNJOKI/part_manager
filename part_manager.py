
from  tkinter import *
from tkinter  import messagebox
from db import Database

db = Database('store.db')


#we are creating function for the method/items we callled
def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row)
        
def add_item():
    if part_text.get() == '' or customer_text.get() == '' or retail_text.get() == '' or price_text.get() == '' :
        messagebox.showerror('required fields', ' please include all fields')
        return
    # get data from the entry
    db.insert(part_text.get(), customer_text.get(), retail_text.get(), price_text.get())
    parts_list.delete(0, END)
    parts_list.insert(END, (part_text.get(), customer_text.get(), retail_text.get(), price_text.get()))
    clear_text()
    populate_list()
# bid list box to select
def select_item(event):
    global selected_item
    index = parts_list.curselection()[0]
    selected_item = parts_list.get(index)
    
    
    part_entry.delete(0, END)
    part_entry.insert(END, selected_item[1])
    customer_entry.delete(0, END)
    customer_entry.insert(END, selected_item[2])
    retail_entry.delete(0, END)
    retail_entry.insert(END, selected_item[3])
    price_entry.delete(0, END)
    price_entry.insert(END, selected_item[4])
     
      
def remove_item():
   db.remove(selected_item[0] )
   clear_text()
   populate_list()
def update_item():
    db.update(selected_item[0], part_text.get(), customer_text.get(), retail_text.get(), price_text.get())
    populate_list()
def clear_text():
    part_entry.delete(0, END)
    customer_entry.delete(0, END)
    retail_entry.delete(0, END)
    price_entry.delete(0, END)
   
     
      



#create window object
app = Tk()
#part
part_text = StringVar()
part_label = Label(app, text='Part name', font=('bold', 14), pady=20)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

#customer
customer_text = StringVar()
customer_label = Label(app, text='Customer', font=('bold', 14))
customer_label.grid(row=0, column=2, sticky=W)
customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=3)
#retail
retail_text = StringVar()
retail_label = Label(app, text='retail', font=('bold', 14), )
retail_label.grid(row=1, column=0, sticky=W)
retail_entry = Entry(app, textvariable=retail_text)
retail_entry.grid(row=1, column=1)

#price
price_text = StringVar()
price_label = Label(app, text='Price', font=('bold', 14))
price_label.grid(row=1, column=2, sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3)
# Parts LIst (Listbox)
parts_list = Listbox(app, height=8, width=50)
parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
# adding the scrollbar

scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)
#set scroll to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)
#bind select
parts_list.bind('<<ListboxSelect>>', select_item)

#buttons 
add_btn = Button(app, text='Add Part', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text='Remove part', width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text='Update Part', width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Clear Part', width=12, command=clear_text)
clear_btn.grid(row=2, column=3)


app.title('Part Manager')
#resixing the window
# app.newGeometry('700*350')
#populate data
populate_list()
#Start program
app.mainloop()
 
 