from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import db
import subprocess
from subprocess import call
import tkinter.font as font

root = Tk()
root.title("Password Manager")
root.geometry("500x300")
menu = Menu(root)
root.config(menu=menu)

db.createDB()
#This function is to recover the forgotten password
def recovery():
    recoverWin.title("Recover Password")
    recoverWin.geometry("400x400")
    v = StringVar()
    v.set("one")
    title = Label(recoverWin, text="Recover Password", font=("Arial", 20, "bold"))
    title.grid(row=0, columnspan=1, column=0)
    msg = Label(recoverWin, text="Please select a question and type in your answer to save it")
    msg.grid(row=1, column=0)
    gapL = Label(recoverWin, text="\n").grid(row=2,column=0)
    option1 = Radiobutton(recoverWin, text="What is the name of your Best Friend", variable=v, value="one").grid(row=3, column=0, columnspan=1, sticky=W)
    option2 = Radiobutton(recoverWin, text="What is the name of your favorite book?", variable=v, value="two").grid(row=4, column=0, columnspan=1, sticky=W)
    option3 = Radiobutton(recoverWin, text="What is your special talent?", variable=v, value="three").grid(row=5, column=0, columnspan=1, sticky=W)
    username = Label(recoverWin, text="Username:", pady=10).grid(row=6, column=0,sticky=W, columnspan=1)
    unameEE = Entry(recoverWin)
    unameEE.grid(row=6, column=0, padx=90, sticky=W)
    password = Label(recoverWin, text="Answer:", pady=10).grid(row=7, column=0,sticky=W, columnspan=1)
    passwordE = Entry(recoverWin)
    passwordE.grid(row=7, column=0, padx=90, sticky=W)
    def get_ans():
        opt2 = v.get()
        ans2 = passwordE.get()
        um = unameEE.get()
        val = db.passRecovery(ans2, opt2, um)
        
        if ans2 == "" or um == "":
            messagebox.showwarning("Blank Entries", "Please Fill all the required details")
        elif value == answer:
            gapL = Label(recoverWin, text=answer)
        elif value == "false":
            gapL = Label(recoverWin, text="Wrong Option Selected")
        elif value == "no":
            gapL = Label(recoverWin, text="Wrong Answer. Please Contact with admin if you forgot the password")
        elif value == "error":
            gapL = Label(recoverWin, text="Wrong Username")

    submit = Button(recoverWin, text="Submit", width=20, height=2, bg="green", fg="white").grid(row=9, padx=10, pady=10,column=0, sticky=W)
    #------- E N D   L A Y O U T ----------
    recoverWin.mainloop()

def dash():
    DashWin = Tk()
    DashWin.title("Dashboard")
    DashWin.geometry("500x300")

    title = Label(DashWin, text="Dashboard", font=("Arial", 25, "bold")).grid(row=0, column=1, columnspan=1, sticky=E+W)

    label = Label(DashWin, text="add new accounts").grid(row=1, column=1)

    #Make Labels
    uname = Label(DashWin, text="Username:")
    psswd = Label(DashWin, text="Password:")
    app = Label(DashWin, text="Application name:")
    url = Label(DashWin, text="Website(if any):")
    mail = Label(DashWin, text="Email used:")

    #Make Input Boxes
    unameE = Entry(DashWin, width=30)
    psswdE = Entry(DashWin, width=30, show="*")
    appE = Entry(DashWin, width=30)
    urlE = Entry(DashWin, width=30)
    mailE = Entry(DashWin, width=30)

    #Place labels and input boxes
    uname.grid(row=2, column=0, pady=5)
    psswd.grid(row=3, column=0, pady=5)
    app.grid(row=4, column=0, pady=5)
    url.grid(row=5, column=0, pady=5)
    mail.grid(row=6, column=0, pady=5)

    unameE.grid(row=2, column=1, pady=5)
    psswdE.grid(row=3, column=1, pady=5)
    appE.grid(row=4, column=1, pady=5)
    urlE.grid(row=5, column=1, pady=5)
    mailE.grid(row=6, column=1, pady=5)

    add = Button(DashWin, text="Add accounts", width=30, pady=3).grid(row=7, column=1, pady=10)

    label2 = Label(DashWin, text="List of added accounts").grid(row=8, column=0, sticky=W)

    DashWin.mainloop()


#This function is to create the login
def login():
	root.destroy()
	LoginWin = Tk()
	LoginWin.title("Password Recovery")
	LoginWin.geometry("500x300")
	menuLogin = Menu(LoginWin)
	LoginWin.config(menu=menuLogin)
	#-------------- M E N U -------------------------
	file_menu_login = Menu(menuLogin)
	menuLogin.add_cascade(label="Option", menu=file_menu_login)
	file_menu_login.add_command(label="Admin Login")
	file_menu_login.add_separator()
	file_menu_login.add_command(label="About")
	file_menu_login.add_separator()
	file_menu_login.add_command(label="Exit", command=LoginWin.destroy)
	#------------- E N D   M E N U -----------------

	title = Label(LoginWin, text="LOGIN", font=("Arial", 20, "bold")).grid(row=0, column=1,columnspan=1, sticky=W)

	message = Label(LoginWin, text="Login using your username and password").grid(row=1, column=0, padx=10)

	gapL = Label(LoginWin, text="\n").grid(row=2, column=0, pady=10)

	uname = Label(LoginWin, text="Username")
	psswd = Label(LoginWin, text="Password")
	unameE = Entry(LoginWin, width=30)
	psswdE = Entry(LoginWin, width=30, show="*")

	uname.grid(column=0, row=3)
	psswd.grid(column=0, row=4)
	unameE.grid(column=1, row=3,sticky=W)
	psswdE.grid(column=1, row=4,sticky=W)

	login = Button(LoginWin, text="Login", width=10, fg="green", font="10").grid(row=5, column=0, pady=15)
	line = font.Font(underline=1)
	reset = Button(LoginWin, text="Forgot Password?", width=15, fg="blue", border="0", font=(line), command=recovery).grid(row=5, column=1)

	LoginWin.mainloop()

#-------------- M E N U -------------------------
file_menu = Menu(menu)
menu.add_cascade(label="Option", menu=file_menu)
file_menu.add_command(label="Admin Login")
file_menu.add_separator()
file_menu.add_command(label="About")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
#------------- E N D   M E N U -----------------


#-------------- L A Y O U T ---------------------  , font=txt)
title = Label(root, text="Password Manager", font=('Helvatica', 20, 'bold'))
title.grid(row=0, columnspan=2)
#WELCOME message
wlcm = Label(root, text="Signup to start using Password Manager\n\nEnter the details below:")
wlcm.grid(row=1, column=1, pady=20)

#Create Input Boxes
username = Entry(root, width=30, border=2)
username.grid(row=2, column=1, padx=10, pady=3)
password = Entry(root, width=30, border=2)
password.grid(row=3, column=1, padx=10, pady=3)
#Create Text Box Labels
username_label = Label(root, text = "Username")
username_label.grid(row=2, column=0)
password_label = Label(root, text = "password")
password_label.grid(row=3, column=0)

#This is for storing a password recovery option
def recoveryOpt():
    root.destroy()
    recoveryWin = Tk()
    recoveryWin.title("Security Question")
    recoveryWin.geometry("400x400")
    v = StringVar()
    v.set("one")

    #-------- L A Y O U T   D E S I G N -----------------
    title = Label(recoveryWin, text="Password Recovery option", font=("Arial", 20, "bold"))
    title.grid(row=0, columnspan=1, column=0)

    msg = Label(recoveryWin, text="Please select a question and type in your answer to save it")
    msg.grid(row=1, column=0)

    gapL = Label(recoveryWin, text="\n").grid(row=2,column=0)

    option1 = Radiobutton(recoveryWin, text="What is the name of your Best Friend", variable=v, value="one").grid(row=3, column=0, sticky=W)
    option2 = Radiobutton(recoveryWin, text="What is the name of your favorite book?", variable=v, value="two").grid(row=4, column=0, sticky=W)
    option3 = Radiobutton(recoveryWin, text="What is your special talent?", variable=v, value="three").grid(row=5, column=0, sticky=W)

    label = Label(recoveryWin, text="Your answer: ", font=("bold")).grid(row=6, column=0,pady=20, padx=10,stick=W)
    answer = Entry(recoveryWin, width=30, border=3, fg="black", bg="#eeeeee")
    answer.grid(row=7, column=0, columnspan=2,padx=10, sticky=W)

    def give_ans():
        opt = v.get()
        ans = answer.get()
        db.storeRecovery(ans, opt)
        recoveryWin.destroy()
        dash()

    submit = Button(recoveryWin, text="Submit", width=20, height=2, bg="green", fg="white", command=give_ans).grid(row=8, padx=10, pady=10,column=0, sticky=W,)
    #------- E N D   L A Y O U T ----------
    recoveryWin.mainloop()

#This function is for registering users
def signup():
    name = username.get()
    passWD = password.get()

    value = db.loginUser(name, passWD)
    if name == "" or passWD == "":
        messagebox.showwarning("Blank entries!","PLease fill all the details")
    elif value == "yes":
        messagebox.showinfo("User Registered!", "User already registered. Please login")
    elif value == "no":
        messagebox.showwarning("Incorrect Password", "You typed a wrong password")
    elif value == "error":
        db.createUser(name, passWD)
        recoveryOpt()


#SIGNUP LAYOUT
singup = Button(root, text="Signup", relief="groove", border=3, command=signup)
singup.grid(row=4, column=0, pady=20, columnspan=1)

#LOGIN LAYOUT
login = Button(root, text="Already have an account? Log in here", command=login)
login.grid(row=4, column=1)

#-------E N D  O F  L A Y O U T ----------

root.mainloop()
#db.createDB()
