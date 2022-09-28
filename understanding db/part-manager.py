from tkinter import *
from tkinter import messagebox
from tokenize import String
from csproject import Database
db = Database("store.db")
# ---------------------------- FUNCTIONS ------------------------------- #
def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row)

def add_item():
   if part_text.get() == "" or customer_text.get() == "" or retailer_text.get() == "" or price_text.get() == "":
        messagebox.showerror("Required Fields","Please include all fields")
   db.insert(part_text.get(), customer_text.get(), retailer_text.get(), price_text.get())
   parts_list.delete(0, END)
   parts_list.insert(END, (customer_text.get(), retailer_text.get(), price_text.get()))
   clear_text()
   populate_list()

def select_item(event):
    try:
        global selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)
    
        part_entry.delete(0, END)
        part_entry.insert(END, selected_item[1])
        customer_entry.delete(0, END)
        customer_entry.insert(END, selected_item[2])
        retailer_entry.delete(0, END)
        retailer_entry.insert(END, selected_item[3])
        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[4])
    except IndexError:
        pass

def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()

def clear_text():
    part_entry.delete(0, END)
    customer_entry.delete(0, END)
    retailer_entry.delete(0, END)
    price_entry.delete(0, END)

def update_item():
    db.update(selected_item[0], part_text.get(), customer_text.get(), retailer_text.get(), price_text.get())
    populate_list()


window = Tk()

# Part
part_text = StringVar()
part_label = Label(window, text="Part Name", font=('bold', 14), pady=20)
part_label.grid(row=0,column=0, sticky=W)
part_entry = Entry(window, textvariable=part_text)
part_entry.grid(row=0, column=1)

# Customer
customer_text = StringVar()
customer_label = Label(window, text="Customer ", font=('bold', 14))
customer_label.grid(row=0,column=2, sticky=W)
customer_entry = Entry(window, textvariable=customer_text)
customer_entry.grid(row=0, column=3)

# Retailer
retailer_text = StringVar()
retailer_label = Label(window, text="Retailer", font=('bold', 14))
retailer_label.grid(row=1,column=0, sticky=W)
retailer_entry = Entry(window, textvariable=retailer_text)
retailer_entry.grid(row=1, column=1)

# Retailer
price_text = StringVar()
price_label = Label(window, text="Price", font=('bold', 14))
price_label.grid(row=1,column=2, sticky=W)
price_entry = Entry(window, textvariable=price_text)
price_entry.grid(row=1, column=3)

#Parts List (listbox)
parts_list = Listbox(window, height=8, width=50, border=0)
parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

# Creating a scrollbar
scrollbar = Scrollbar(window)
scrollbar.grid(row=3,column=3)
# Set scroll to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)
# Bind select
parts_list.bind("<<ListboxSelect>>", select_item)
#Buttons
add_button = Button(window, text="Add Part", width = 12, command = add_item)
add_button.grid(row=2, column=0, pady=20)

remove_button = Button(window, text="Remove Part", width = 12, command = remove_item)
remove_button.grid(row=2, column=1)

update_button = Button(window, text="Update Part", width = 12, command = update_item)
update_button.grid(row=2, column=2)

clear_button = Button(window, text="Clear Input", width = 12, command = clear_text)
clear_button.grid(row=2, column=3)



populate_list()

window.title("Part Manager")
window.geometry("1600x900")

#Start Program
window.mainloop()