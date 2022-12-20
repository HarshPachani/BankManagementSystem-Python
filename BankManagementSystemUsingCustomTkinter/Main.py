import tkinter
from tkinter import messagebox as msgb
import tkinter.ttk as ttk
import customtkinter
import sqlite3
import time

conn = sqlite3.connect("BankDetails.db")
cur = conn.cursor()

createTable = """CREATE TABLE IF NOT EXISTS data(
                acc_No INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                balance REAL NOT NULL,
                pin INTEGER);"""
cur.execute(createTable)

createHistoryTable = """CREATE TABLE IF NOT EXISTS transactionHistory(
                    acc_no INTEGER NOT NULL,
                    name TEXT NOT NULL,
                    status TEXT NOT NULL,
                    amount REAL NOT NULL,
                    date TEXT NOT NULL,
                    time TEXT NOT NULL,
                    balance REAL NOT NULL
                );"""
cur.execute(createHistoryTable)

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

def change_appearance_mode(new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

def home_Return(master):
    """Function to distroy a widget and return to home."""
    master.destroy()
    mainMenu()

def getAmount(acc_no, name):
    query = f"SELECT balance FROM data WHERE acc_No = {acc_no} AND name = '{name}'"
    cur.execute(query)
    getBalance = cur.fetchall()
    bal = int(getBalance[0][0])
    return bal

def write_History(acc_no, name, status, amount):
        date = time.strftime("%d-%m-%Y")
        Time = time.strftime("%H:%M:%S")
        balance = getAmount(acc_no, name)
        cur.execute("INSERT INTO transactionHistory(acc_no, name, status, amount, date, time, balance) VALUES(?, ?, ?, ?, ?, ?, ?)", (int(acc_no), name, status, amount, date, Time, balance))
        conn.commit()

def credit_write(master, ammount, acc_no, name):
    if is_number(ammount) == 0:
        msgb.showinfo("Error", "Invalid Credentials!\nTry Again!")
        master.destroy()
        return
    query = f"SELECT balance FROM data WHERE acc_No = {acc_no} AND name = '{name}'"
    cur.execute(query)
    getBalance = cur.fetchall()
    bal = int(getBalance[0][0])
    # print(bal)
    newBalance = bal + int(ammount)
    # print(newBalance)

    query = f"UPDATE data set balance = {newBalance} WHERE name = '{name}' AND acc_No = {acc_no}"
    cur.execute(query)
    conn.commit()

    msgb.showinfo("Operation Successfull!", "Amount Credited Successfully!")
    write_History(acc_no, name, "credit", ammount)
    master.destroy()
    return 

def creditAmount(acc_no, name):
    creditw = customtkinter.CTk()
    creditw.geometry("600x300")
    creditw.title("Credit Amount")
    l_title = tkinter.Message(creditw, text = "BANK MANAGEMENT SYSTEM", relief= "raised", width = 2000, padx = 600, pady = 0, fg = "white", bg = "blue4", justify = "center", anchor = "center")
    l_title.config(font = ("Arial", "15", "bold"))
    l_title.pack(side = "top")

    l_title2 = tkinter.Message(creditw, text = "Credit Amount", bg = "blue4", fg = "white", relief= "raised", width= 200, padx = 600, pady = 0, justify= "center", anchor = "center")
    l_title2.config(font = "Arial 12 italic bold")
    l_title2.pack(side = "top")

    l1 = customtkinter.CTkLabel(master = creditw, relief= "raised", text_font = ("Times", 16), text = "Enter Amount to be Credited: ")
    e1 = customtkinter.CTkEntry(master = creditw, relief= "raised")
    l1.pack(side = "top")
    e1.pack(side = "top")
    b = customtkinter.CTkButton(master = creditw, text = "Credit", fg_color = "green", text_font = ("Times",16), relief= "raised", command = lambda:credit_write(creditw, e1.get(), acc_no, name))
    b.pack(side = "top")
    creditw.mainloop()

def logout(master):
    msgb.showinfo("Logged Out", "You Have Been Successfully Logged Out!!")
    master.destroy()
    mainMenu()
    return

def debit_write(master, amount, acc_no, name):
    if(is_number(amount) == 0):
        msgb.showinfo("Error", "Invalid Credentials!\nTry Again\n")
        master.destroy()
        return

    bal = getAmount(acc_no, name)
    amount = int(amount)
    if bal < amount:
        msgb.showinfo("Error", "You Don't have Sufficient Balance!!")
        master.destroy()
    else:
        newBalance = bal - amount
        query = f"UPDATE data SET balance = {newBalance} WHERE name = '{name}' AND acc_No = {acc_no}"
        cur.execute(query)
        conn.commit()
        msgb.showinfo("Operation Successfull!", "Amount Debited Successfully!\nCollect Your Amount")
        write_History(acc_no, name, "debit", amount)
        master.destroy()
        return

def debitAmount(acc_no, name):
    debitw = customtkinter.CTk()
    debitw.geometry("600x300")
    debitw.title("Debit Amount")
    l_title = tkinter.Message(debitw, text = "BANK MANAGEMENT SYSTEM", relief= "raised", width = 2000, padx = 600, pady = 0, fg = "white", bg = "blue4", justify = "center", anchor = "center")
    l_title.config(font = ("Arial", "15", "bold"))
    l_title.pack(side = "top")

    l_title2 = tkinter.Message(debitw, text = "Debit Amount", bg = "blue4", fg = "white", relief= "raised", width= 200, padx = 600, pady = 0, justify= "center", anchor = "center")
    l_title2.config(font = "Arial 12 italic bold")
    l_title2.pack(side = "top")

    l1 = customtkinter.CTkLabel(master = debitw, relief= "raised", text_font = ("Times", 16), text = "Enter Amount to be Debited: ")
    e1 = customtkinter.CTkEntry(master = debitw, relief= "raised")
    l1.pack(side = "top")
    e1.pack(side = "top")
    b = customtkinter.CTkButton(master = debitw, text = "Debit", fg_color = "green", text_font = ("Times",16), relief= "raised", command = lambda:debit_write(debitw, e1.get(), acc_no, name))
    b.pack(side = "top")

    debitw.mainloop()

def display_records(tree, acc_no, name):
        tree.delete(*tree.get_children())
        cur.execute(f"SELECT * FROM transactionHistory WHERE acc_no = {acc_no} AND name = '{name}'")
        data = cur.fetchall()

        for d in data:
            tree.insert("", "end", values = d)

def display_Transaction_History(acc_no, name):
    history = customtkinter.CTk()
    tree = ttk.Treeview(history, height = 50)
    history.title("History of - " + acc_no)
    history.geometry("855x655")

    tree['columns'] = ("Acc_no", "Name", "Status", "Amount D/C", "Date", "Time", "Balance")

    xscrollbar = customtkinter.CTkScrollbar(master = history, orientation = "horizontal", command=tree.xview)
    yscrollbar = customtkinter.CTkScrollbar(master = history, orientation = "vertical", command=tree.yview)

    tree.column("#0", width = 0, stretch= "no")
    tree.column("Acc_no", anchor = "center", width = 120)
    tree.column("Name", anchor = "center", width = 120)
    tree.column("Status", anchor = "center", width = 120)
    tree.column("Amount D/C", anchor = "center", width = 120)
    tree.column("Date", anchor = "center", width = 120)
    tree.column("Time", anchor = "center", width = 120)
    tree.column("Balance", anchor = "center", width = 120)

    tree.heading('Acc_no', text='Acc_no', anchor="center")
    tree.heading('Name', text='Name', anchor="center")
    tree.heading('Status', text='Status', anchor="center")
    tree.heading('Amount D/C', text='Amount D/C', anchor="center")
    tree.heading('Date', text='Date', anchor="center")
    tree.heading('Time', text='Time', anchor="center")
    tree.heading('Balance', text='Balance', anchor="center")

    xscrollbar.pack(side = "bottom", fill = "x")
    yscrollbar.pack(side = "right", fill = "y")

    tree.config(yscrollcommand= yscrollbar.set, xscrollcommand= xscrollbar.set)
    tree.pack()

    display_records(tree, acc_no, name)
    history.mainloop()

def displayBalance(acc_no, name):
    bal = getAmount(acc_no, name)
    msgb.showinfo("Display Balance", f"Your Current Balance is: {bal}")

def logged_in_Menu(name, acc_num):
    rootw = customtkinter.CTk()
    rootw.geometry("1600x700")
    rootw.title("Bank | Welcome - "+ name)

    fr1 = customtkinter.CTkFrame(master = rootw)
    fr1.pack(side = "top")

    l_title = tkinter.Message(fr1, text = "BANK MANAGEMENT SYSTEM", relief="raised",width=2000, padx = 600, pady = 0, fg = "white", bg = "blue4", justify= "center", anchor="center")
    l_title.config(font = "Arial 50 bold")
    l_title.pack(side = "top")

    label = customtkinter.CTkLabel(master = rootw, text = "Logged in as: " + name, relief= "raised", text_font = "Times 16", fg_color = "green", justify= "center", anchor = "center")
    label.pack(side = "top")

    b2 = customtkinter.CTkButton(master = rootw, text = "Credit Amount", command = lambda : creditAmount(acc_num, name))
    b3= customtkinter.CTkButton(master = rootw, text = "Debit Amount", command = lambda : debitAmount(acc_num, name))
    b4 = customtkinter.CTkButton(master = rootw, text = "Display Amount", command = lambda : displayBalance(acc_num, name))
    b5 = customtkinter.CTkButton(master = rootw, text = "Display History", command = lambda : display_Transaction_History(acc_num, name))
    b6 = customtkinter.CTkButton(master = rootw, text = "Logout", fg_color = "red", command = lambda : logout(rootw))

    b2.place(x = 100, y = 150)
    b3.place(x = 100, y = 220)
    b4.place(x = 1150, y = 150)
    b5.place(x = 1150, y = 220)
    b6.place(x = 615, y = 400)

    rootw.mainloop()

def check_log_in(master, name, acc_num, pin):
    if(is_exists(name, acc_num, pin)):
        # msgb.showinfo("Yes", "Yes")
        master.destroy()
        logged_in_Menu(name, acc_num)
    else:
        # msgb.showinfo("No", "No")
        msgb.showinfo("Error", "Invalid Credentials!!\nTry Again")
        master.destroy()
        mainMenu()
        return

def log_in(master):
    master.destroy()
    login = customtkinter.CTk()
    login.geometry("1600x700")
    login.title("Login")
    # login.config(bg = "SteelBlue1")
    # fr1 = tk.Frame(login, bg = "blue")
    l_title = tkinter.Message(login, text = "BANK MANAGEMENT SYSTEM", relief= "raised", width= 2000, padx = 600, pady =0 , fg = "white", bg = "blue4", justify= "center", anchor="center")
    l_title.config(font = "Arial 50 bold")
    l_title.pack(side = "top")

    l1 = customtkinter.CTkLabel(master = login, text = "Enter Name: ", text_font = "Times 16", relief = "raised")
    l1.pack(side = "top")
    e1 = customtkinter.CTkEntry(master = login)
    e1.pack(side = "top")
    l2 = customtkinter.CTkLabel(master = login, text= "Enter Account Number: ", text_font = "Times 16", relief = "raised")
    l2.pack(side = "top")
    e2 = customtkinter.CTkEntry(master = login)
    e2.pack(side = "top")
    l3 = customtkinter.CTkLabel(master = login, text = "Enter PIN: ", text_font = "Times 16", relief= "raised")
    l3.pack(side = "top")
    e3 = customtkinter.CTkEntry(master = login, show = "*")
    e3.pack(side = "top")

    b = customtkinter.CTkButton(master = login, text = "Submit", fg_color = "green",command = lambda : check_log_in(login, e1.get(), e2.get(), e3.get()))
    # b.pack(side = "top", pady = 25)
    b.place(x = 615, y = 250)

    b1 = customtkinter.CTkButton(master = login, text = "HOME", text_font = "Times 16",  relief = "raised", command = lambda : home_Return(login))
    b1.place(x = 615, y = 600)
    login.mainloop()

def is_number(s):
    try:
        float(s)
        return 1
    except ValueError:
        return 0

def checkIfExists(name, amount, pin):
    query = f"SELECT * FROM data WHERE name = '{name}' AND pin = {pin}"
    cur.execute(query)
    data = cur.fetchall()
    if not data:
        return False
    else:
        return True

def is_exists(name, acc_no, pin):
    query = f"SELECT * from data WHERE name = '{name}' AND acc_No = {acc_no} AND pin = {pin}"
    cur.execute(query)
    data = cur.fetchall()
    if not data:
        return False
    else:
        return True

def write(master, name, amount, pin):
    # msgb.showinfo("info", f"name: {name},amount: {amount}, pin: {pin}")
    if((is_number(name)) or (is_number(amount) == 0) or (is_number(pin) == 0) or name == ""):
        msgb.showwarning("Warning", "Invalid Credentials!!")
        master.destroy()
        mainMenu()
        return

    if (checkIfExists(name, amount, pin)):
        msgb.showinfo("Exists", "This Account Already Exists")
        master.destroy()
        mainMenu()
        return

    cur.execute("INSERT INTO data(name, balance, pin) VALUES(?, ?, ?)", (name, amount, pin))
    conn.commit()

    cur.execute(f"SELECT acc_no FROM data WHERE name = '{name}' AND balance = {amount} AND pin = {pin}")
    acc_no = cur.fetchall()
    msgb.showinfo("Successfull!", f"Your Account is Created Successfully!!\nYour Account Number is: {acc_no[0][0]}")
    master.destroy()
    mainMenu()
    return

def create(master):
    master.destroy()
    crwn = customtkinter.CTk()
    crwn.geometry("1600x700")
    crwn.title("Create Account")
    # crwn.configure(bg = "SteelBlue1") #config and configure are same.
    fr1 = customtkinter.CTkFrame(master = crwn, bg_color = "blue")
    l_title = tkinter.Message(crwn, text = "BANK MANAGEMENT SYSTEM", relief= "raised", width = 2000, padx = 600, pady = 0, fg = "white", bg = "blue4", anchor="center")
    l_title.config(font = "Arial 50 bold")
    l_title.pack(side = "top")

    quitButton = customtkinter.CTkButton(master = crwn, text = "Quit", fg_color = "red", text_font = "lucida 13 bold", command = crwn.destroy)
    quitButton.place(x = 520, y = 600)
    homeButton = customtkinter.CTkButton(master = crwn, text = "HOME", fg_color = "blue", text_font = "lucida 13 bold", command = lambda : home_Return(crwn))
    homeButton.place(x = 670, y = 600)

    l1 = customtkinter.CTkLabel(master = crwn, text = "Enter Name: ", text_font = "jelley 16", relief = "raised")
    l1.pack(side = "top")
    e1 = customtkinter.CTkEntry(master = crwn)
    e1.pack(side = "top")

    l2 = customtkinter.CTkLabel(master = crwn, text = "Enter Opening Credit: ", text_font = "Times 16", relief = "raised")
    l2.pack(side = "top")
    e2 = customtkinter.CTkEntry(master = crwn)
    e2.pack(side = "top")

    l3 = customtkinter.CTkLabel(master = crwn, text = "Enter Your PIN: ", text_font = "Times 16", relief= "raised")
    l3.pack(side = "top")
    e3 = customtkinter.CTkEntry(master = crwn, show = "*")
    e3.pack(side = "top")

    b = customtkinter.CTkButton(master = crwn, text = "Submit", text_font = "Times 16", fg_color = "green", command = lambda : write(crwn, e1.get(), e2.get(), e3.get()))
    b.pack(side = "top", pady = 25)
    crwn.mainloop()



def mainMenu():
    root = customtkinter.CTk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    
    root.geometry(f"{width}x{height}")
    root.title("BANK MANAGEMENT SYSTEM")
    # root.configure()
    
    l_title = tkinter.Message(root, text = "BANK MANAGEMENT SYSTEM", relief= "raised", width = 2000, padx = 600, pady = 0, fg = "green", justify="center", anchor="center")
    l_title.config(font = "Verdana 40 bold")
    l_title.pack(side = "top")
    b1 = customtkinter.CTkButton(master = root, text = "Login", text_font = "Times 20", command = lambda : log_in(root))
    b2 = customtkinter.CTkButton(master = root, text = "Create New Account", text_font = "Times 20", command = lambda : create(root))
    b3 = customtkinter.CTkButton(master = root, text = "Quit", fg_color="red", text_font = "Times 20", command = root.destroy)

    label_mode = customtkinter.CTkLabel(master=root, text="Appearance Mode:")
    label_mode.place(x = 1220, y = 500)

    optionmenu_1 = customtkinter.CTkOptionMenu(master=root,values=["Dark", "Light", "System"], command=change_appearance_mode)
    optionmenu_1.place(x = 1220, y = 525)
    b1.place(x = 620, y = 200)
    b2.place(x = 620, y = 300)
    b3.place(x = 620, y = 400)
    root.mainloop()

mainMenu()