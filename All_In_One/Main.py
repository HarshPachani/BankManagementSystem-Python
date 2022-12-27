from tkinter import *
from tkinter import messagebox as msgb
import customtkinter
import sqlite3
import tkinter.ttk as ttk
import time
import BankManagement
import Digital_Clock
import File_Explorer
import Password_Manager
import sys
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import random
from tkinter import messagebox
import pyperclip


conn = sqlite3.connect('BankDetails.db')
myCur = conn.cursor()
createTable = """CREATE TABLE IF NOT EXISTS data(
                acc_No INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                balance REAL NOT NULL,
                pin INTEGER);"""
myCur.execute(createTable)

createHistoryTable = """CREATE TABLE IF NOT EXISTS transactionHistory(
                    acc_no INTEGER NOT NULL,
                    name TEXT NOT NULL,
                    status TEXT NOT NULL,
                    amount REAL NOT NULL,
                    date TEXT NOT NULL,
                    time TEXT NOT NULL,
                    balance REAL NOT NULL
                );"""
myCur.execute(createHistoryTable)

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")


#====================================== CALCULATOR IMPLEMENTATION ===================================================#

#=============================HANDLING THE EVENT==========================#
def clicked(event):
    #event.widget will give the button which is clicked, and .cget() function will help to take the text from the button.
    text = event.widget.cget("text")
    # print(text)
    if text == "=":
        if text_Input.get().isdigit():
            value = int(text_Input.get())
        else:
            try:
                value = eval(txtDisplay.get())
                # print(value)
            except Exception as e:
                # print(e)
                value = "Error"
        # print(value)
        text_Input.set(value)
        txtDisplay.update()
            
    elif text == "C":
        text_Input.set("")
        txtDisplay.update()
            
    else:
        # print(text_Input .get() + text)
        text_Input.set(text_Input.get() + text)
        txtDisplay.update()

def calciMainMenu():
    root = Tk()
    root.title("My Calculator - Harsh")
    root.geometry("310x456")
    root.resizable(0, 0)

    #==============================================ENTRY WIDGET==================================================#
    global text_Input
    global txtDisplay

    text_Input = StringVar()
    text_Input.set("")
    txtDisplay = Entry(root, textvariable = text_Input, font = "Arial 20 bold", border = 5, bg = "white", justify=RIGHT)
    txtDisplay.grid(columnspan = 4)#Columnspan is number of columns widgetoccupies, default is 1.

    #=================================================BUTTONS=====================================================#
            
    btn7 = Button(root, text = "7", font = "arial 20 bold", padx = 16, pady = 16, fg = "black", bg = "powder blue")
    btn7.grid(row = 1, column = 0)
    btn7.bind("<Button-1>", clicked)
            
    btn8 = Button(root, text = "8", font = "arial 20 bold", padx = 16, pady = 16, fg = "black", bg = "powder blue")
    btn8.grid(row = 1, column = 1)
    btn8.bind("<Button-1>", clicked)

    btn9 = Button(root, text = "9", font = "arial 20 bold", padx = 16, pady = 16, fg = "black", bg = "powder blue")
    btn9.grid(row = 1, column = 2)
    btn9.bind("<Button-1>", clicked)

    addition = Button(root, text = "+", font = "arial 20 bold", padx = 16, pady = 16, fg = "black", bg = "powder blue")
    addition.grid(row = 1, column = 3)
    addition.bind("<Button-1>", clicked)

    btn4 = Button(root, text = "4", font = "arial 20 bold", padx = 16, pady = 16, fg = "black", bg = "powder blue")
    btn4.grid(row = 2, column = 0)
    btn4.bind("<Button-1>", clicked)

    btn5 = Button(root, text = "5", font = "arial 20 bold", padx = 16, pady = 16, fg = "black", bg = "powder blue")
    btn5.grid(row = 2, column = 1)
    btn5.bind("<Button-1>", clicked)

    btn6 = Button(root, text = "6", font = "arial 20 bold", padx = 16, pady = 16, fg = "black", bg = "powder blue")
    btn6.grid(row = 2, column = 2)
    btn6.bind("<Button-1>", clicked)

    substraction = Button(root, text = "-", font = "arial 20 bold", padx = 16, pady = 16, fg = "black", bg = "powder blue")
    substraction.grid(row = 2, column = 3)
    substraction.bind("<Button-1>", clicked)

    btn1 = Button(root, text = "1", font = "arial 20 bold", padx = 16, pady = 16, fg = "black", bg = "powder blue")
    btn1.grid(row = 3, column = 0)
    btn1.bind("<Button-1>", clicked)
    btn2 = Button(root, text = "2", font = "arial 20 bold", padx = 16, pady = 16, fg = "black", bg = "powder blue")
    btn2.grid(row = 3, column = 1)
    btn2.bind("<Button-1>", clicked)
    btn3 = Button(root, text = "3", font = "arial 20 bold", padx = 16, pady = 16, fg = "black", bg = "powder blue")
    btn3.grid(row = 3, column = 2)
    btn3.bind("<Button-1>", clicked)
    multiply = Button(root, text = "*", font = "arial 20 bold", padx = 16, pady = 16, fg = "black", bg = "powder blue")
    multiply.grid(row = 3, column = 3)
    multiply.bind("<Button-1>", clicked)
    btn0 = Button(root, text = "0", font = "arial 20 bold", padx = 16, pady = 16, fg = "black", bg = "powder blue")
    btn0.grid(row = 4, column = 0)
    btn0.bind("<Button-1>", clicked)
    btnc = Button(root, text = "C", font = "arial 20 bold", padx = 16, pady = 16, fg = "black", bg = "powder blue")
    btnc.grid(row = 4, column = 1)
    btnc.bind("<Button-1>", clicked)
    decimal = Button(root, text = ".", font = "arial 20 bold", padx = 16, pady = 16, fg = "black", bg = "powder blue")
    decimal.grid(row = 4, column = 2)
    decimal.bind("<Button-1>", clicked)
    division = Button(root, text = "/", font = "arial 20 bold", padx = 16, pady = 16, fg = "black", bg = "powder blue")
    division.grid(row = 4, column = 3)
    division.bind("<Button-1>", clicked)

    btnequal = Button(root, text = "=", width = 16, border = 4, font = "ariel 20 bold", padx = 16, pady = 16, fg = "black", bg = "powder blue")
    btnequal.grid(columnspan=4)
    btnequal.bind("<Button-1>", clicked)

    root.mainloop()

#============================ NOTEPAD IMPLEMENTATION ================================#
#==================METHODS===================#
def newFile(root):
    global file
    root.title("Untitled - Notepad")
    file = None

    #Here 1.0 means 0th character or 1st line, Delete Everything.
    textArea.delete(1.0, END)

def openFile(root):
    global file
    file = askopenfilename(defaultextension= ".txt", filetypes= [("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])

    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textArea.delete(1.0, END)
        f = open(file, "r")
        textArea.insert(1.0, f.read())
        f.close()

def saveFile(root):
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt",
                    defaultextension=".txt", filetypes=[("All Files", "*.*"),
                                                        ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            #save as new file
            f = open(file, "w")
            f.write(textArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
            # print("File Saved")
    else:
        #Save the file
        f = open(file, "w")
        f.write(textArea.get(1.0, END))
        f.close()

def quitApp(root):
    root.destroy()

def cut():
    textArea.event_generate(("<<Cut>>"))

def copy():
    textArea.event_generate(("<<Copy>>"))

def paste():
    textArea.event_generate(("<<Paste>>"))

def about():
    msgb.showinfo("Notepad", "Notepad by Harsh Pachani")

def mainScreen():
    root = Tk()
    root.title("Untitled - Notepad")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}")

    #==========================Add TextArea=======================#
    file = None
    global textArea
    textArea = Text(root, font = "Calibri 13")
    textArea.pack(expand=True, fill = BOTH)

    #=========================Menubar====================#
    menuBar = Menu(root)

    #Filemenu Starts
    fileMenu = Menu(menuBar, tearoff = 0)
    #To Open New File
    fileMenu.add_command(label = "New", command = lambda : newFile(root))
    #To Open Already Existing file
    fileMenu.add_command(label = "Open", command = lambda : openFile(root))

    #To save the current file
    fileMenu.add_command(label = "Save", command = lambda : saveFile(root))
    fileMenu.add_separator()
    fileMenu.add_command(label = "Exit", command = lambda : quitApp(root))

    menuBar.add_cascade(label = "File", menu = fileMenu)
    #Filemenu Ends

    #Edit Menu Starts
    editMenu = Menu(menuBar, tearoff=0)
    editMenu.add_command(label = "Cut", command = cut)
    editMenu.add_command(label = "Copy", command = copy)
    editMenu.add_command(label = "Paste", command = paste)

    menuBar.add_cascade(label = "Edit", menu = editMenu)
    #Edit Menu Ends

    #Help menu Starts
    helpMenu = Menu(menuBar, tearoff=0)
    helpMenu.add_command(label = "About Notepad", command = about)
    menuBar.add_cascade(label = "Help", menu = helpMenu)
    #Help menu Ends

    root.config(menu = menuBar)

    #Adding Scrollbar
    scrollbar = Scrollbar(textArea)
    scrollbar.pack(side = RIGHT, fill = Y)
    scrollbar.config(command = textArea.yview)
    textArea.config(yscrollcommand = scrollbar.set)
    root.mainloop()
#====================================END OF NOTEPAD ============================================================#

#======================== START OF PASSWORD MANAGER ==============================

customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode("Dark")

conn = sqlite3.connect('passwords.db')
myCursor = conn.cursor()
myCursor.execute("""CREATE TABLE IF NOT EXISTS pass(
                        website TEXT NOT NULL,
                        email TEXT NOT NULL,
                        password TEXT NOT NULL 
                        );""")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', "$", '%', '&', '(', ')', '*', '+']

def save_password():
    # getting user entry data
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    # Dialog to user to make sure password is correct
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you have not left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title="Confirm entries", message=f"These are the details you entered\n"
                                                                        f"Email: {email}"
                                                                        f"\nPassword: {password}\nIs it okay to save ?")
        if is_ok:
            #Copying password to our clipboard
            pyperclip.copy(password)

            # new user data to be entered into current password into the sqlite database
            myCursor.execute("INSERT INTO pass(website, email, password) VALUES(?, ?, ?)", (website, email, password))
            conn.commit()

def search_password():
    # Getting user website entry
    website = website_entry.get()
    # Get password data
    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please enter a website to search")
    else:
        query = f"SELECT * FROM pass WHERE website = '{website}'"
        myCursor.execute(query)
        data = myCursor.fetchall()
        if not data:
            messagebox.showinfo("No passwords saved", f"There are no passwords save for the website '{website}'")
        else:
            # website = data[0][0]
            email = data[0][1]
            password = data[0][2]
            is_clipboard = messagebox.askokcancel(title=website, message=f"Email: {email}\nPassword: {password}"
                                                                             f"\n\nSave to clipboard ?")
            if is_clipboard:
                # saving password to clipboard
                pyperclip.copy(password)
                messagebox.showinfo(title="Saved to clipboard", message="Password has been saved to clipboard")

def get_password():
    # Generate new password from password generator
    password = pass_generator()
    # Copying password to our clipboard
    pyperclip.copy(password)
    # print(password)

    # clear password entry widget
    password_entry.delete(0, END)
    # entering new password to password entry widget
    password_entry.insert(END, password)

def pass_generator():
    # no of random latters, symbols and numbers
    nr_letters = random.randint(8, 10) #Returns a number between 8 and 10 both included.
    # print(nr_latters)
    nr_symbols = random.randint(2, 4)
    # print(nr_symbols)
    nr_numbers = random.randint(2, 4)
    # print(nr_numbers)

    # initialising password variable to populate with for loop
    password = [random.choice(letters) for i in range(nr_letters)]
    # print(password)
    password += [random.choice(symbols) for i in range(nr_symbols)]
    # print(password)
    password += [random.choice(numbers) for i in range(nr_numbers)]
    # print(password)

    #shuffling password characters
    random.shuffle(password)
    # print("Shuffled Pass: ", password)
    password = "".join(password) #For converting a list into the string.
    return password

# print(type([print(pass_generator()) for i in range(5)]))
# generated = pass_generator()
# print(generated)
def mainScreen():
    
    # ---------------------------- UI COLORS AND FONT ------------------------------- #
    WINDOW_BG = "black" #For background of the window.
    FONT = ("Courier", 15, "normal")
    LABEL_COLOR = "white"
    FIELD_COLORS = "#dddddd"
    FIELD_FONT_COLOR = "#c70039"

    global password_entry
    global password_label
    global website_entry
    global email_entry

    root = customtkinter.CTk()
    root.title("Password Manager")
    root.config(padx = 20, pady = 20, bg = WINDOW_BG)
    root.geometry("850x400")
    root.resizable(0, 0)

    # PASS_IMG = PhotoImage(file = "logo.png")
    # canvas = Canvas(root, width = 200, height = 200, bg = WINDOW_BG, highlightthickness=0) #for removing the highlighted border.
    # canvas.config()
    # canvas.create_image(100, 100, image = PASS_IMG)
    # canvas.grid(row = 0, column = 1)

    # Label
    # Label for Website
    website_label = customtkinter.CTkLabel(text="Website", padx=20, text_font=FONT, fg_color = WINDOW_BG)
    website_label.grid(column=0, row=1, sticky=W)

    # Label for Email/Username
    email_label = customtkinter.CTkLabel(text="Email/Username", padx=20, text_font=FONT, fg_color = WINDOW_BG)
    email_label.grid(column=0, row=2, sticky=W)

    # Label for Password
    password_label = customtkinter.CTkLabel(text="Password", padx=20, text_font=FONT, fg_color = WINDOW_BG)
    password_label.grid(column=0, row=3,sticky=W)
    root.grid_columnconfigure(1, weight=1)

    # Entry
    website_entry = customtkinter.CTkEntry(master = root, width=350, text_font=FONT)
    website_entry.insert(END, string="")
    website_entry.grid(column=1, row=1)

    # starting cursor focus
    website_entry.focus()

    email_entry = customtkinter.CTkEntry(master = root, width=350, text_font=FONT)
    email_entry.insert(END, string="")
    email_entry.grid(column=1, row=2)
    # set default email
    email_entry.insert(0, "example@email.com")

    password_entry = customtkinter.CTkEntry(master = root, width=350, text_font=FONT)
    password_entry.insert(END, string="")
    password_entry.grid(column=1, row=3)

    # buttons
    search_button = customtkinter.CTkButton(text="Search", padx=95, text_font=FONT, command=search_password)
    search_button.grid(column=3, row=1)

    generate_button = customtkinter.CTkButton(text="Generate Password", command=get_password, text_font=FONT)
    generate_button.grid(column=3, row=3)

    add_button = customtkinter.CTkButton(text="Add", width=100, fg_color = "green", command=save_password, text_font=FONT)
    add_button.grid(column=1, row=6, columnspan=5, sticky=W)

    root.mainloop()
#=========================================END OF PASSWORD MANAGER ========================================================

def quitApp(master):
        sys.exit()
        master.destroy()

def bankManagement():
    BankManagement.mainMenu()

def calci():
    calciMainMenu()

def clock():
    Digital_Clock.clock()

def fileExplorer():
    File_Explorer.mainScreen()

def notepad():
    mainScreen()

def passwordManager():
    Password_Manager.mainScreen()

def projectNames(root):
    frame = customtkinter.CTkFrame(master = root)
    frame.pack(side = "top")

    label = Message(frame, text = "Projects - By Harsh Pachani", width = 1200, padx = 800, font = "lucida 20 bold",relief = "raised", fg = "white", bg = "blue")
    label.pack(side = "top")

    bank = customtkinter.CTkButton(master = root, text = " Bank Management System ", text_font = "Times 13", fg_color = "blue", command = lambda : bankManagement())
    bank.place(x = 120, y = 140)

    calc = customtkinter.CTkButton(master = root, text = "Calculator", text_font = "Times 13", fg_color = "blue", width = 21, command = lambda : calci())
    calc.place(x = 120, y = 270)

    digital = customtkinter.CTkButton(master = root, text = "Digital Clock", text_font = "Times 13", fg_color = "blue", width = 21, command = lambda : clock())
    digital.place(x = 120, y = 450)
        
    crud = customtkinter.CTkButton(master = root, text = "File Explorer", text_font = "Times 13", fg_color = "blue", width = 21, command = lambda : fileExplorer())
    crud.place(x = 1040, y = 120)

    note_pad = customtkinter.CTkButton(master = root, text = "Notepad", text_font = "Times 13", fg_color = "blue", width = 21, command = lambda : notepad())
    note_pad.place(x = 1040, y = 420)

    passwordManage = customtkinter.CTkButton(master = root, text = "Password Manager", text_font = "Times 12", fg_color = "blue", width = 21, command = lambda : passwordManager())
    passwordManage.place(x = 1040, y = 220)

    quitButton = customtkinter.CTkButton(master = root, text = "Quit", text_font = "Times 13", width = 21, fg_color = "red", command = lambda : quitApp(root))
    quitButton.place(x = 720, y = 520)

def listScreen():
    root = customtkinter.CTk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.title("Projects - By Harsh Pachani")
    root.geometry(f"{screen_width}x{screen_height}")
    root.resizable(0, 0)
    projectNames(root)
    root.mainloop()

if __name__ == "__main__":
    listScreen()