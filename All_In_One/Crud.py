import tkinter as tk
from tkinter import messagebox as msgb
import tkinter.ttk as ttk
import sqlite3

def mainScreen():
    root = tk.Tk()
    root.title("Python: CRUD Application")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 900
    height = 500
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" %(width, height, x, y))
    root.resizable(0, 0)

    #====================METHODS====================
    def Database():
    global conn, myCursor
    conn = sqlite3.connect('Data.db')
    myCursor = conn.cursor()
    myCursor.execute("""CREATE TABLE IF NOT EXISTS `member` (
                            mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            firstname TEXT,
                            lastname TEXT, 
                            gender TEXT, 
                            address TEXT, 
                            username TEXT, 
                            password TEXT)
                    """)

    def create():
    if FIRSTNAME.get() == "" or LASTNAME.get() == "" or  GENDER.get() == "" or ADDRESS.get() == "" or USERNAME.get() == "" or PASSWORD.get() == "":
        txt_result.config(text = "Please Complete the required field!", fg = "red")
    else:
        Database()
        myCursor.execute("INSERT INTO member (firstname, lastname, gender, address, username, password) VALUES(?, ?, ?, ?, ?, ?)", (str(FIRSTNAME.get()), str(LASTNAME.get()), str(GENDER.get()), str(ADDRESS.get()), str(USERNAME.get()), str(PASSWORD.get())))
        conn.commit()
        FIRSTNAME.set("")
        LASTNAME.set("")
        GENDER.set("")
        ADDRESS.set("")
        USERNAME.set("")
        PASSWORD.set("")
        myCursor.close()
        conn.close()
        txt_result.config(text="Created a data!", fg="green")

    def read():
    tree.delete(*tree.get_children())
    Database()
    myCursor.execute("SELECT * FROM member ORDER BY lastname ASC")
    fetch = myCursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values= (data[1], data[2], data[3], data[4], data[5], data[6]))
    myCursor.close()
    conn.close()
    txt_result.config(text="Successfully read the data from database", fg="black")

    def Exit():
    result = msgb.askquestion('Python: Simple CRUD Applition', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


    #===================VARIABLES====================
    FIRSTNAME = tk.StringVar()
    LASTNAME = tk.StringVar()
    GENDER = tk.StringVar()
    ADDRESS = tk.StringVar()
    USERNAME = tk.StringVar()
    PASSWORD = tk.StringVar()

    #=================FRAMES=================
    top = tk.Frame(root, width = 900, height = 50, border = 8, relief="raised")
    top.pack(side = "top")
    left = tk.Frame(root, width = 300, height = 500, border = 8, relief = "raised")
    left.pack(side = "left")
    right = tk.Frame(root, width = 600, height = 500, border=8, relief = "raised")
    right.pack(side = "right")
    forms = tk.Frame(left, width = 300, height = 450)
    forms.pack(side = "top")
    buttons = tk.Frame(left, width = 300, height = 100, border = 8, relief= "raised")
    buttons.pack(side="bottom")
    radioGroup = tk.Frame(forms)
    GENDER.set("Radio")
    male = tk.Radiobutton(radioGroup, text = "Male", variable = GENDER, value="Male", font = "arial 16").pack(side = "left")
    female = tk.Radiobutton(radioGroup, text = "Female", variable = GENDER, value="Female", font = "arial 16").pack(side = "left")

    #=============================LABEL WIDGET==============================
    txt_title = tk.Label(top, text = "Python - CRUD Operation", font = "arial 24", width = 900)
    txt_title.pack()
    """By default, when a cell(frame) is larger than the widget it contains, the grid geometry manager places the widget
    at the center of the cell horizontally and vertically.
    - To Change this default behaviour, you can use the sticky option.
    The sticky option specifies which edge of the cell the widget should stick to.
    - The value of sticky has the following valid values:
            N, S, E, W, NW, NE, SE, SW, NS, EW.
    """
    txt_firstname = tk.Label(forms, text = "Firstname: ", font = "arial 16", bd = 15)
    txt_firstname.grid(row = 0, sticky = "e")
    txt_lastname = tk.Label(forms, text="Lastname:", font=('arial', 16), bd=15)
    txt_lastname.grid(row=1, stick="e")
    txt_gender = tk.Label(forms, text="Gender:", font=('arial', 16), bd=15)
    txt_gender.grid(row=2, stick="e")
    txt_address = tk.Label(forms, text="Address:", font=('arial', 16), bd=15)
    txt_address.grid(row=3, stick="e")
    txt_username = tk.Label(forms, text="Username:", font=('arial', 16), bd=15)
    txt_username.grid(row=4, stick="e")
    txt_password = tk.Label(forms, text="Password:", font=('arial', 16), bd=15)
    txt_password.grid(row=5, stick="e")

    txt_result = tk.Label(buttons)
    txt_result.pack(side = "top")

    #==========================ENTRY WIDGETS========================
    firstname = tk.Entry(forms, textvariable= FIRSTNAME, width = 30)
    firstname.grid(row = 0, column = 1)
    lastname = tk.Entry(forms, textvariable=LASTNAME, width=30)
    lastname.grid(row=1, column=1)
    radioGroup.grid(row=2, column=1)
    address = tk.Entry(forms, textvariable=ADDRESS, width=30)
    address.grid(row=3, column=1)
    username = tk.Entry(forms, textvariable=USERNAME, width=30)
    username.grid(row=4, column=1)
    password = tk.Entry(forms, textvariable=PASSWORD, show="*", width=30)
    password.grid(row=5, column=1)

    #======================BUTTON WIDGET========================
    btn_create = tk.Button(buttons, text = "Create", width = 10, command= create)
    btn_create.pack(side = "left")
    btn_read = tk.Button(buttons, width=10, text="Read", command=read )
    btn_read.pack(side="left")
    btn_update = tk.Button(buttons, width=10, text="Update", state=tk.DISABLED)
    btn_update.pack(side="left")
    btn_delete = tk.Button(buttons, width=10, text="Delete", state=tk.DISABLED)
    btn_delete.pack(side="left")
    btn_exit = tk.Button(buttons, width=10, text="Exit", command=Exit)
    btn_exit.pack(side="left")

    #========================LIST WIDGET==========================
    scrollbary = tk.Scrollbar(right, orient = tk.VERTICAL)
    scrollbarx = tk.Scrollbar(right, orient = tk.HORIZONTAL)
    tree = ttk.Treeview(right, columns=("Firstname", "Lastname", "Gender", "Address", "Username", "Password"), selectmode = "extended", height = 500, yscrollcommand= scrollbary.set, xscrollcommand= scrollbarx.set)
    scrollbary.config(command = tree.yview)
    scrollbary.pack(side = tk.RIGHT, fill = tk.Y)
    scrollbarx.config(command = tree.xview)
    scrollbarx.pack(side = tk.BOTTOM, fill = tk.X)

    tree.heading("Firstname", text = "FirstName", anchor= tk.W)
    tree.heading('Lastname', text="Lastname", anchor=tk.W)
    tree.heading('Gender', text="Gender", anchor=tk.W)
    tree.heading('Address', text="Address", anchor=tk.W)
    tree.heading('Username', text="Username", anchor=tk.W)
    tree.heading('Password', text="Password", anchor=tk.W)

    tree.column('#0', stretch=tk.NO, minwidth=0, width=0)
    tree.column('#1', stretch=tk.NO, minwidth=0, width=80)
    tree.column('#2', stretch=tk.NO, minwidth=0, width=120)
    tree.column('#3', stretch=tk.NO, minwidth=0, width=80)
    tree.column('#4', stretch=tk.NO, minwidth=0, width=150)
    tree.column('#5', stretch=tk.NO, minwidth=0, width=120)
    tree.column('#6', stretch=tk.NO, minwidth=0, width=120)

    tree.pack()
    root.mainloop()

if __name__ == "__main__":
    mainScreen()

