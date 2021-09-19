from tkinter import *
from tkinter import messagebox

window2 = Tk()


def open_main():
    """Function used for login.py to open main_contact.py"""
    pass


def add_contact():
    """add_contact function will get data passed from Entry widget, then store into listbox widget"""
    display_details = name_ent.get(), last_ent.get(), num_ent.get(), email_ent.get()

    if not name_ent.get() or not last_ent.get() or not num_ent.get() or not email_ent.get():
        messagebox.showerror("Error", "Fields cannot be empty.")
    else:
        display.insert(END, display_details)


def delete_contact():
    """delete_contact function will delete data select by user from listbox"""
    display.delete(display.curselection())


# firstname
name = Label(window2, text="Firstname")
name.place(x=18, y=10)
name_ent = Entry(window2, width=28)
name_ent.place(x=20, y=30)

# lastname
last = Label(window2, text="Lastname")
last.place(x=18, y=60)
last_ent = Entry(window2, width=28)
last_ent.place(x=20, y=80)

# contact
num = Label(window2, text="Mobile number")
num.place(x=18, y=110)
num_ent = Entry(window2, width=28)
num_ent.place(x=20, y=130)

# email
email = Label(window2, text="Email address")
email.place(x=18, y=160)
email_ent = Entry(window2, width=28)
email_ent.place(x=20, y=180)

# listbox widget that will store and remove contacts
display = Listbox(window2, width=62, height=21, highlightbackground="#28B9D0", highlightthickness=0.4)
display.place(x=210, y=18)

# creating scroll bar
scroll = Scrollbar(window2)
scroll.pack(side=RIGHT, fill=BOTH)
display.config(yscrollcommand=scroll.set)
scroll.config(command=display.yview)

# add button
add_c = Button(window2, width=23, height=2, text="Add", bg="#28B9D0", command=add_contact)
add_c.place(x=20, y=210)

# delete button
del_c = Button(window2, width=23, height=2, text="Delete", bg="#28B9D0", command=delete_contact)
del_c.place(x=20, y=265)

# exit application button
exit_c = Button(window2, width=23, height=2, text="Exit", bg="#28B9D0", command=exit)
exit_c.place(x=20, y=320)

# window configurations/features
window2.geometry("600x380")
window2.resizable(0, 0)
window2.title("Contact book")
window2.attributes("-topmost", True)
window2.mainloop()
