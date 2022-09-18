from tkinter import * #* makes u initialize all  

window = Tk()

window.title("My First Gui Program")

window.minsize(width=500, height=300)

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

#Label
my_label = Label(text="I am a Label", font=("Helvetica", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text sex"
my_label.config(text="New Teeext")

#Button 


button = Button(text="Click Me", command=button_clicked)
button.pack()

#Entry

input = Entry(width=10)
input_received = input.get()
input.pack()


window.mainloop()