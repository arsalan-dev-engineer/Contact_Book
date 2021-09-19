from tkinter import *
import tkinter.messagebox


def authenticator():
    """Function will authenticate user input and if password == "Admin",
     system will then close current window, then open another window"""
    if (lgnName_Entry.get() == "Admin") and (lgnPass_Entry.get() == "Admin"):
        tkinter.messagebox.showinfo("Login", f"Login Successful")
        window.destroy()
        from main_contact import open_main
        open_main()

    else:
        tkinter.messagebox.showwarning("Login Error", "Incorrect Password")


window = Tk()

# login label
lgnLabel = Label(window, text="Enter Login Details")
lgnLabel.place(x=140, y=60)

# username
lgnName_Label = Label(window, text="Username")
lgnName_Label.place(x=75, y=90)

# password
lgnPass_Label = Label(window, text="Password")
lgnPass_Label.place(x=75, y=120)

# username entry
lgnName_Entry = Entry(window, width=35)
lgnName_Entry.place(x=140, y=90)

# password entry
lgnPass_Entry = Entry(window, width=35, show="*")
lgnPass_Entry.place(x=140, y=120)

# submit button
submitBtn = Button(window, text="Log In", width=15,
                   height=2, bg="#28B9D0", command=authenticator)
submitBtn.place(x=140, y=150)

# window configurations/features
window.title("Arsalan : Azzy001")
window.geometry("700x380")
window.resizable(0, 0)
window.attributes("-topmost", True)
window.mainloop()

