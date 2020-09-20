from tkinter import *
import backEnd as be

window = Tk()

window.title("BookStore")

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
    


def view():
    list1.delete(0,END)
    for row in be.view():
        list1.insert(END,row)

def search():
    list1.delete(0,END)
    for row in be.search(titleText.get(),authorText.get(),yearText.get(),isbnText.get()):
        list1.insert(END,row)

def insert():
    be.insert(titleText.get(),authorText.get(),yearText.get(),isbnText.get())

def update():
    be.update(selected_tuple[0],titleText.get(),authorText.get(),yearText.get(),isbnText.get())

def delete():
    be.delete(selected_tuple[0])

# labels
l1 = Label(window,text="title")
l1.grid(row=0,column=0)

l2 = Label(window,text="Author")
l2.grid(row=0,column=2)

l3 = Label(window,text="Year")
l3.grid(row=1,column=0)

l4 = Label(window,text="ISBN")
l4.grid(row=1,column=2)

# Entry boxes
titleText = StringVar()
e1 = Entry(window, textvariable=titleText)
e1.grid(row=0,column=1)

authorText = StringVar()
e2 = Entry(window, textvariable=authorText)
e2.grid(row=0,column=3)

yearText = StringVar()
e3 = Entry(window, textvariable=yearText)
e3.grid(row=1,column=1)

isbnText = StringVar()
e4 = Entry(window, textvariable=isbnText)
e4.grid(row=1,column=3)

# listbox
list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0, rowspan=6,columnspan=2)

# scroll bar
sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

# configuring listbox and scrollbar
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View All", width=12, command=view)
b1.grid(row=2, column=3)

b2=Button(window,text="Search Entry", width=12,command=search)
b2.grid(row=3, column=3)

b3=Button(window,text="Add Entry", width=12,command=insert)
b3.grid(row=4, column=3)

b4=Button(window,text="Update Selected", width=12,command=update)
b4.grid(row=5, column=3)

b5=Button(window,text="Delete Selected", width=12, command=delete)
b5.grid(row=6, column=3)

b6=Button(window,text="Close", width=12,command= window.destroy)
b6.grid(row=7, column=3)

# mainloop
window.mainloop()