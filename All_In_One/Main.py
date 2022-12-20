from tkinter import *
from tkinter import messagebox as msgb
import sqlite3
import time
import tkinter.ttk as ttk
import time
from Calculator import startFile

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

class BankManagementSystem(Tk): #Class BankManagementSystem is Inherited with Tkinter now
    def __init__(self):#Where we used to write root is now become self
        super().__init__() #Calling a super class's constructor. 
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")
        self.title("Bank Management System")
        
    def is_number(s):
        try:
            int(s)
            return 1
        except ValueError:
            return 0

    def checkIfExists(name, amount, pin):
        query = f"SELECT * FROM data WHERE name = '{name}' AND pin = {pin}"
        myCur.execute(query)
        data = myCur.fetchall()
        if not data:
            return False
        else:
            return True

    def quitCreate(self, master):
        master.destroy()

    def createAcc(master, name, amount, pin):
        if((BankManagementSystem.is_number(name)) or (BankManagementSystem.is_number(pin) == 0) or name == ""):
            msgb.showinfo("Warning", "Invalid Credentials!!")
            master.destroy()
            return
        
        if(BankManagementSystem.checkIfExists(name, amount, pin)):
            msgb.showinfo("Already Exists!", "This Account Already Exists!!")
            master.destroy()
            return
        
        myCur.execute("INSERT INTO data(name, balance, pin) VALUES(?, ?, ?)", (name, amount, pin))
        conn.commit()

        myCur.execute(f"SELECT acc_no from data WHERE name = '{name}' AND balance = '{amount}' AND pin = '{pin}'")
        acc_no = myCur.fetchall()
        msgb.showinfo("Successfull!", f"Your Account is Created Successfully!!\nYour Account Number is: {acc_no[0][0]}")
        master.destroy()
        return

    def home_Return(master):
        """Function to destroy a widget and return to home."""
        master.destroy()
        bms = BankManagementSystem()
        bms.main_screen()

    def is_exists(name, acc_no, pin):
        query = f"SELECT * FROM data WHERE name = '{name}' AND acc_No = '{acc_no}' AND pin = {pin}"
        myCur.execute(query)
        data = myCur.fetchall()
        
        if not data:
            return False
        else:
            return True

    def credit_write(master, ammount, acc_no, name):
        if (BankManagementSystem.is_number(ammount) == 0):
            msgb.showinfo("Error", "Invalid Credentials!\nTry Again!")
            master.destroy()
            return
        
        query = f"SELECT balance FROM data WHERE acc_No = {acc_no} AND name = '{name}'"
        myCur.execute(query)
        getBalance = myCur.fetchall()
        bal = int(getBalance[0][0])
        # print(bal)
        newBalance = bal + int(ammount)
        # print(newBalance)

        query = f"UPDATE data set balance = {newBalance} WHERE name = '{name}' AND acc_No = '{acc_no}'"
        myCur.execute(query)
        conn.commit()

        msgb.showinfo("Operation Successfull!", "Amount Credited Successfully!")
        BankManagementSystem.write_History(acc_no, name, "credit", ammount)
        master.destroy()
        return 

    def creditAmount(acc_no, name):
        creditRoot = Tk()
        creditRoot.geometry("600x300")
        creditRoot.title("Credit Amount")
        creditRoot.config(bg = "SteelBlue1")

        l_title = Message(creditRoot, text = "BANK MANAGEMENT SYSTEM", relief= "raised", width = 2000, padx = 600, pady = 0, fg = "white", bg = "blue4", justify = "center", anchor = "center")
        l_title.config(font = ("Arial", "15", "bold"))
        l_title.pack(side = "top")

        l_title2 = Message(creditRoot, text = "Credit Amount", bg = "blue4", fg = "white", relief= "raised", width= 200, padx = 600, pady = 0, justify= "center", anchor = "center")
        l_title2.config(font = "Arial 12 italic bold")
        l_title2.pack(side = "top")

        l1 = Label(creditRoot, relief= "raised", font = ("Times", 16), text = "Enter Amount to be Credited: ")
        e1 = Entry(creditRoot, relief= "raised")
        l1.pack(side = "top")
        e1.pack(side = "top")
        b = Button(creditRoot, text = "Credit", bg = "green", fg = "white", font = ("Times",16), relief= "raised", command = lambda:BankManagementSystem.credit_write(creditRoot, e1.get(), acc_no, name))
        b.pack(side = "top")
        creditRoot.mainloop()

    def getAmount(acc_no, name):
        query = f"SELECT balance FROM data WHERE acc_No = {acc_no} AND name = '{name}'"
        myCur.execute(query)
        getBalance = myCur.fetchall()
        bal = int(getBalance[0][0])
        return bal

    def debit_write(master, amount, acc_no, name):
        if(BankManagementSystem.is_number(amount) == 0):
            msgb.showinfo("Error", "Invalid Credentials!\nTry Again\n")
            master.destroy()
            return
        bal = BankManagementSystem.getAmount(acc_no, name)
        amount = int(amount)
        if bal < amount:
            msgb.showinfo("Error", "You Don't have Sufficient Balance!!")
            master.destroy()
        else:
            newBalance = bal - amount
            query = f"UPDATE data SET balance = {newBalance} WHERE name = '{name}' AND acc_No = {acc_no}"
            myCur.execute(query)
            conn.commit()
            msgb.showinfo("Operation Successfull!", "Amount Debited Successfully!\nCollect Your Amount")
            BankManagementSystem.write_History(acc_no, name, "debit", amount)
            master.destroy()
            return

    def debitAmount(acc_no, name):
        debitRoot = Tk()
        debitRoot.geometry("600x300")
        debitRoot.title("Debit Amount")
        debitRoot.config(bg = "SteelBlue1")
        l_title = Message(debitRoot, text = "BANK MANAGEMENT SYSTEM", relief= "raised", width = 2000, padx = 600, pady = 0, fg = "white", bg = "blue4", justify = "center", anchor = "center")
        l_title.config(font = ("Arial", "15", "bold"))
        l_title.pack(side = "top")

        l_title2 = Message(debitRoot, text = "Debit Amount", bg = "blue4", fg = "white", relief= "raised", width= 200, padx = 600, pady = 0, justify= "center", anchor = "center")
        l_title2.config(font = "Arial 12 italic bold")
        l_title2.pack(side = "top")

        l1 = Label(debitRoot, relief= "raised", font = ("Times", 16), text = "Enter Amount to be Debited: ")
        e1 = Entry(debitRoot, relief= "raised")
        l1.pack(side = "top")
        e1.pack(side = "top")
        b = Button(debitRoot, text = "Debit", bg = "green", fg = "white", font = ("Times",16), relief= "raised", command = lambda:BankManagementSystem.debit_write(debitRoot, e1.get(), acc_no, name))
        b.pack(side = "top")

    def displayBalance(acc_no, name):
        bal = BankManagementSystem.getAmount(acc_no, name)
        msgb.showinfo("Display Balance", f"Your Current Balance is: {bal}")

    def write_History(acc_no, name, status, amount):
        date = time.strftime("%d-%m-%Y")
        Time = time.strftime("%H:%M:%S")
        balance = BankManagementSystem.getAmount(acc_no, name)
        myCur.execute("INSERT INTO transactionHistory(acc_no, name, status, amount, date, time, balance) VALUES(?, ?, ?, ?, ?, ?, ?)", (int(acc_no), name, status, amount, date, Time, balance))
        conn.commit()
        
    def display_records(tree, acc_no, name):
        tree.delete(*tree.get_children())
        myCur.execute(f"SELECT * FROM transactionHistory WHERE acc_no = {acc_no} AND name = '{name}'")
        data = myCur.fetchall()

        for d in data:
            tree.insert("", END, values = d)

    def display_Transaction_History(acc_no, name):
        history = Tk()
        tree = ttk.Treeview(history, height = 50)
        history.title("History of - " + acc_no)
        history.geometry("855x655")

        tree['columns'] = ("Acc_no", "Name", "Status", "Amount D/C", "Date", "Time", "Balance")

        xscrollbar = Scrollbar(history, orient = HORIZONTAL, command=tree.xview)
        yscrollbar = Scrollbar(history, orient = VERTICAL, command=tree.yview)

        tree.column("#0", width = 0, stretch= NO)
        tree.column("Acc_no", anchor = CENTER, width = 120)
        tree.column("Name", anchor = CENTER, width = 120)
        tree.column("Status", anchor = CENTER, width = 120)
        tree.column("Amount D/C", anchor = CENTER, width = 120)
        tree.column("Date", anchor = CENTER, width = 120)
        tree.column("Time", anchor = CENTER, width = 120)
        tree.column("Balance", anchor = CENTER, width = 120)

        tree.heading('Acc_no', text='Acc_no', anchor=CENTER)
        tree.heading('Name', text='Name', anchor=CENTER)
        tree.heading('Status', text='Status', anchor=CENTER)
        tree.heading('Amount D/C', text='Amount D/C', anchor=CENTER)
        tree.heading('Date', text='Date', anchor=CENTER)
        tree.heading('Time', text='Time', anchor=CENTER)
        tree.heading('Balance', text='Balance', anchor=CENTER)

        xscrollbar.pack(side = BOTTOM, fill = X)
        yscrollbar.pack(side = RIGHT, fill = Y)

        tree.config(yscrollcommand= yscrollbar.set, xscrollcommand= xscrollbar.set)
        tree.pack()

        BankManagementSystem.display_records(tree, acc_no, name)

    def logout(master):
        msgb.showinfo("Logged Out", "You Have Been Successfully Logged Out!!")
        master.destroy()
        bms = BankManagementSystem()
        bms.main_screen()
        return

    def logged_in_Menu(name, acc_num):
        rootw = Tk()
        screen_width = rootw.winfo_screenwidth()
        screen_height = rootw.winfo_screenheight()
        rootw.geometry(f"{screen_width}x{screen_height}")
        rootw.config(bg = "steelblue")
        rootw.title("Bank | Welcome - " + name)

        l_title = Message(rootw, text = "BANK MANAGEMENT SYSTEM", relief="raised",width=2000, padx = 600, pady = 0, fg = "white", bg = "blue4", justify= "center", anchor="center")
        l_title.config(font = "Arial 50 bold")
        l_title.pack(side = "top")

        label = Label(rootw, text = "Logged in as: " + name, relief= "raised", bg = "blue3", font = "Times 16", fg = "white", justify= "center", anchor = "center")
        label.pack(side = "top")

        b2 = Button(rootw, text = "Credit Amount", font = "Times 13 bold", command = lambda : BankManagementSystem.creditAmount(acc_num, name))
        b3 = Button(rootw, text = "Debit Amount", font = "Times 13 bold", command = lambda : BankManagementSystem.debitAmount(acc_num, name))
        b4 = Button(rootw, text = "Display Amount", font = "Times 13 bold", command = lambda : BankManagementSystem.displayBalance(acc_num, name))
        b5 = Button(rootw, text = "Display History", font = "Times 13 bold", command = lambda : BankManagementSystem.display_Transaction_History(acc_num, name))
        b6 = Button(rootw, text = "Logout", bg = "red", fg = "white", font = "Times 13 bold",command = lambda : BankManagementSystem.logout(rootw))

        b2.place(x = 100, y = 150)
        b3.place(x = 100, y = 220)
        b4.place(x = 1150, y = 150)
        b5.place(x = 1150, y = 220)
        b6.place(x = 650, y = 400)

        rootw.mainloop()

    def check_log_in(master, name, acc_num, pin):
        if (BankManagementSystem.is_exists(name, acc_num, pin)):
            master.destroy()
            BankManagementSystem.logged_in_Menu(name, acc_num)
        else:
            # msgb.showinfo("No", "No")
            msgb.showinfo("Error", "Invalid Credentials!!\nTry Again")
            master.destroy()
            bms = BankManagementSystem()
            bms.main_screen()
            return

    def loginAcc(master):
        master.destroy()

        login = Tk()

        login.title("Login")
        screen_width = login.winfo_screenwidth()
        screen_height = login.winfo_screenheight()
        login.geometry(f"{screen_width}x{screen_height}")

        label = Label(login, text = "BANK MANAGEMENT SYSTEM",padx = 600, font = "lucida 26 bold", bg = "blue", fg = "white").pack(side = "top")

        login.config(bg = "steelblue1")
        l1 = Label(login, text = "Enter Name: ", font = "Times 16", relief = "raised")
        l1.pack(side = "top")
        e1 = Entry(login)
        e1.pack(side = "top")
        l2 = Label(login, text= "Enter Account Number: ", font = "Times 16", relief = "raised")
        l2.pack(side = "top")
        e2 = Entry(login)
        e2.pack(side = "top")
        l3 = Label(login, text = "Enter PIN: ", font = "Times 16", relief= "raised")
        l3.pack(side = "top")
        e3 = Entry(login, show = "*")
        e3.pack(side = "top")

        b = Button(login, text = "Submit", fg = "white", bg = "green", font = "Times 13", command = lambda : BankManagementSystem.check_log_in(login, e1.get(), e2.get(), e3.get()))
        # b.pack(side = "top", pady = 25)
        b.place(x = 650, y = 250)

        b1 = Button(login, text = "HOME", font = "Times 16",  relief = "raised", bg = "blue4", fg = "white", command = lambda : BankManagementSystem.home_Return(login))
        b1.place(x = 640, y = 600)

    def createNewAcc(self):
        create = Tk()
        create.title("Create New Account")
        screen_width = create.winfo_screenwidth()
        screen_height = create.winfo_screenheight()
        create.geometry(f"{screen_width}x{screen_height}")

        label = Label(create, text = "BANK MANAGEMENT SYSTEM",padx = 600, font = "lucida 26 bold", bg = "blue", fg = "white").pack(side = "top")
    
        quitApp = Button(create, text = "Quit", fg = "red", padx = 35, font = "lucida 13 bold", command = lambda : self.quitCreate(create))
        quitApp.place(x = 620, y = 600)
        create.config(bg = "steelblue1")

        nameLabel = Label(create, text = "Enter Name: ", font = "Times 16", relief = "raised")
        nameEntry = Entry(create)
        nameLabel.pack(side = "top")
        nameEntry.pack(side = "top")

        creditLabel = Label(create, text = "Enter Opening Credit", font = "Times 16", relief = "raised")
        creditEntry = Entry(create)
        creditLabel.pack(side = "top")
        creditEntry.pack(side = "top")

        pinLabel = Label(create, text = "Enter PIN", font = "Times 16", relief = "raised") 
        pinEntry = Entry(create, show = "*")
        pinLabel.pack(side = "top")
        pinEntry.pack(side = "top")

        submitButton = Button(create, text = "Submit", fg = "white", bg = "green", font = "Times 16", command = lambda : BankManagementSystem.createAcc(create, nameEntry.get(), creditEntry.get(), pinEntry.get()))
        submitButton.pack(side = "top", pady = 25)

        create.mainloop()

    def quitCommand(self):
        self.destroy()

    #main_screen 
    def main_screen(self):
        self.config(bg = "steelblue1")
        self.bmsLabel = Label(self, text = "BANK MANAGEMENT SYSTEM",padx = 600, font = "lucida 22 bold", bg = "blue", fg = "white").pack(side = "top")
        login = Button(self, text = "Login", fg = "green", padx = 45, font = "lucida 12 bold", command = lambda : self.loginAcc())
        login.place(x = 650, y = 200)

        create = Button(self, text = "Create New Account", fg = "black", font = "lucida 12 bold", command = lambda : self.createNewAcc())
        create.place(x = 640, y = 300)

        quitApp = Button(self, text = " Quit ", padx = 45, fg = "red", bg = "grey", font = "lucida 12 bold", command = lambda : self.quitCommand())
        quitApp.place(x = 650, y = 400)

class DigitalClock(Tk):
    def __init__(self):

        def digitalclock():
            time_live = time.strftime("%H:%M:%S")
            label.config(text = time_live)
            #in after method 200 millisecond is passed i.e. after 1 seconds digital clock function will be called.
            label.after(1, digitalclock)

        super().__init__()
        global label
        self.title("Digital Clock - Harsh Pachani")
        self.geometry("420x150")
        self.resizable(0, 0)
        label = Label(self, font = "Boulder 68 bold", bg = "light blue", fg = "black", bd = 25)
        label.grid(row = 0, column = 1)
        digitalclock()

class CRUD(Tk):

    def Exit(self):
        ans = msgb.askquestion("Python - CRUD Application", "Are you sure you want to Exit the App?", icon = "warning")
        if ans == "yes":
            self.destroy()

    #=============================METHODS==================================#
    def create(self, fname, lname, password, uname, gender):
        print(fname)
        if fname == "" or lname == "" or password == "" or uname == "" or gender == "":
            txt_result.config(text = "Please Complete the require field!", fg = "red")
            
        else:
            # database()
            myCursor.execute("INSERT INTO member(firstname, lastname, gender, address, username, password) VALUES(?, ?, ?, ?, ?)", (str(FIRSTNAME.get()), str(LASTNAME.get()), str(GENDER.get()), str(ADDRESS.get()), str(USERNAME.get()), str(PASSWORD.get())))
            conn.commit()
            FIRSTNAME.set("")
            LASTNAME.set("")
            GENDER.set("")
            ADDRESS.set("")
            USERNAME.set("")
            PASSWORD.set("")
            myCursor.close()
            conn.close()
            txt_result.config(text = "Created a data!", fg = "green")

    def __init__(self):

        def database():
            global myCursor
            conn = sqlite3.connect("CRUD-Data.db")
            myCursor = conn.cursor()
            myCursor.execute("""CREATE TABLE IF NOT EXISTS member(
                                mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                firstname TEXT,
                                lastname TEXT, 
                                gender TEXT, 
                                address TEXT, 
                                username TEXT, 
                                password TEXT
                        )""")

        super().__init__()
        screen_height = self.winfo_screenheight()
        screen_width = self.winfo_screenwidth()

        width = 900
        height = 500
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.geometry("%dx%d+%d+%d" %(width, height, x, y))

        self.resizable(0, 0)
        self.title("CRUD - Application")
        
        #=======================VARIABLES==========================

        global GENDER
        global FIRSTNAME
        global LASTNAME
        global ADDRESS
        global USERNAME
        global PASSWORD
        global txt_result

        GENDER = StringVar()
        FIRSTNAME = StringVar() 
        LASTNAME = StringVar() 
        ADDRESS = StringVar()
        USERNAME = StringVar()
        PASSWORD = StringVar()

        #========================FRAMES================================#
        top = Frame(self, width = 900, height = 50, border = 8, relief="raised")
        top.pack(side = "top")
        left = Frame(self, width = 300, height = 500, border = 8, relief = "raised")
        left.pack(side = "left")
        right = Frame(self, width = 600, height = 500, border=8, relief = "raised")
        right.pack(side = "right")
        forms = Frame(left, width = 300, height = 450)
        forms.pack(side = TOP)
        buttons = Frame(left, width = 300, height = 100, border = 8, relief = RAISED)
        buttons.pack(side = BOTTOM)

        radioGroup = Frame(forms)

        GENDER.set("Radio")

        male = Radiobutton(radioGroup, text = "Male", value = "Male", variable = GENDER, font = "arial 16").pack(side = LEFT)
        female = Radiobutton(radioGroup, text = "Female", value = "Female", variable = GENDER, font = "arial 16").pack(side = LEFT)

        #======================LABEL WIDGET=========================#
        txt_title = Label(top, text = "Python - CRUD Operation", font = "arial 24", width = 900)
        txt_title.pack()

        """By default, when a cell(frame) is larger than the widget it contains, the grid geometry manager places the widget
        at the center of the cell horizontally and vertically.
        - To Change this default behaviour, you can use the sticky option.
        The sticky option specifies which edge of the cell the widget should stick to.
        - The value of sticky has the following valid values:
                N, S, E, W, NW, NE, SE, SW, NS, EW.
        """
        txt_firstname = Label(forms, text = "Firstname: ", font = "arial 16", bd = 15)
        txt_firstname.grid(row = 0, sticky = "e")
        txt_lastname = Label(forms, text="Lastname:", font=('arial', 16), bd=15)
        txt_lastname.grid(row=1, stick="e")
        txt_gender = Label(forms, text="Gender:", font=('arial', 16), bd=15)
        txt_gender.grid(row=2, stick="e")
        txt_address = Label(forms, text="Address:", font=('arial', 16), bd=15)
        txt_address.grid(row=3, stick="e")
        txt_username = Label(forms, text="Username:", font=('arial', 16), bd=15)
        txt_username.grid(row=4, stick="e")
        txt_password = Label(forms, text="Password:", font=('arial', 16), bd=15)
        txt_password.grid(row=5, stick="e")

        txt_result = Label(buttons)
        txt_result.pack(side = "top")

        #=============================ENTRY WIDGET======================================#
        firstName = Entry(forms, textvariable = FIRSTNAME, width = 30)
        firstName.grid(row = 0, column = 1)
        lastname = Entry(forms, textvariable=LASTNAME, width=30)
        lastname.grid(row=1, column=1)
        radioGroup.grid(row=2, column=1)
        address = Entry(forms, textvariable=ADDRESS, width=30)
        address.grid(row=3, column=1)
        username = Entry(forms, textvariable=USERNAME, width=30)
        username.grid(row=4, column=1)
        password = Entry(forms, textvariable=PASSWORD, show="*", width=30)
        password.grid(row=5, column=1)

        #=============================BUTTON WIDGET==============================#
        btn_create = Button(buttons, text = "Create", width = 10, command = lambda : self.create(FIRSTNAME.get(), LASTNAME.get(), PASSWORD.get(), USERNAME.get(), GENDER.get()))
        btn_create.pack(side = "left")
        btn_read = Button(buttons, text = "Read", width = 10)
        btn_read.pack(side = "left")
        btn_update = Button(buttons, text = "Update", width = 10, state = DISABLED)
        btn_update.pack(side = "left")
        btn_delete = Button(buttons, text = "Delete", width = 10, state = DISABLED)
        btn_delete.pack(side = "left")
        btn_exit = Button(buttons, text = "Exit", width = 10, command = lambda : self.Exit())
        btn_exit.pack(side = "left")

        #========================================LIST WIDGET======================================#

        scrollbarx = Scrollbar(right, orient = HORIZONTAL)
        scrollbary = Scrollbar(right, orient = VERTICAL)

        tree = ttk.Treeview(right, columns = ("Firstname", "Lastname", "Gender", "Address", "Username", "Password"), selectmode = "extended", height = 500, xscrollcommand = scrollbarx.set, yscrollcommand = scrollbary.set)
        scrollbarx.config(command = tree.xview)
        scrollbarx.pack(side = BOTTOM, fill = X)
        scrollbary.config(command = tree.yview)
        scrollbary.pack(side = RIGHT, fill = Y)

        tree.heading("Firstname", text = "FirstName", anchor = W)
        tree.heading("Lastname", text = "LastName", anchor = W)
        tree.heading("Gender", text = "Gender", anchor = W)
        tree.heading("Address", text = "Address", anchor = W)
        tree.heading("Username", text = "UserName", anchor = W)
        tree.heading("Password", text = "Password", anchor = W)

        tree.column('#0', stretch= NO, minwidth=0, width=0)
        tree.column('#1', stretch= NO, minwidth=0, width=80)
        tree.column('#2', stretch= NO, minwidth=0, width=120)
        tree.column('#3', stretch= NO, minwidth=0, width=80)
        tree.column('#4', stretch= NO, minwidth=0, width=150)
        tree.column('#5', stretch= NO, minwidth=0, width=120)
        tree.column('#6', stretch= NO, minwidth=0, width=120)

        tree.pack()

class ListScreen(Tk):
    def __init__(self):
        super().__init__()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.title("Projects - By Harsh Pachani")
        self.geometry(f"{screen_width}x{screen_height}")
        self.resizable(0, 0)
        self.config(bg = "Grey")

#=====================ALL PROJECT OBJECTS==========================#
    def bankManagementSystem(self):
        bms = BankManagementSystem()
        bms.main_screen()
        bms.mainloop()

    def calculator(self):
        startFile()

    def digitalClock(self):
        clock = DigitalClock()
        clock.mainloop()

    def crudApp(self):
        crud = CRUD()
        crud.mainloop()

    def quitApp(self):
        self.destroy()

    #============================PROJECT NAMES WITH ACCESSIBLE BUTTONS=======================#
    def projectNames(self):
        frame = Frame(self)
        frame.pack(side = "top")

        label = Message(frame, text = "Projects - By Harsh Pachani", width = 1200, padx = 800, font = "lucida 20 bold",relief = "raised", fg = "white", bg = "blue")
        label.pack(side = "top")

        frame2 = Frame(self)
        frame2.pack(side = "left")
        bank = Button(self, text = " Bank Management System ", font = "Times 13", bg = "blue", fg = "white", command = lambda :  self.bankManagementSystem())
        bank.place(x = 120, y = 140)

        calc = Button(self, text = "Calculator", font = "Times 13", bg = "blue", fg = "white", width = 21, command = lambda : self.calculator())
        calc.place(x = 120, y = 270)

        digital = Button(self, text = "Digital Clock", font = "Times 13", bg = "blue", fg = "white", width = 21, command = lambda : self.digitalClock())
        digital.place(x = 120, y = 450)
        
        crud = Button(self, text = "CRUD Operation", font = "Times 13", bg = "blue", fg = "white", width = 21, command = lambda : self.crudApp())
        crud.place(x = 1040, y = 120)

        quitButton = Button(self, text = "Quit", font = "Times 13", width = 21, fg = "white", bg = "red", command = lambda : self.quitApp())
        quitButton.place(x = 720, y = 520)

if __name__ == "__main__":
    listScreen = ListScreen()
    listScreen.projectNames()
    listScreen.mainloop()