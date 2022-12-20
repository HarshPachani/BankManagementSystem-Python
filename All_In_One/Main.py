from tkinter import *
from tkinter import messagebox as msgb
import customtkinter
import sqlite3
import time
import tkinter.ttk as ttk
import time
import BankManagement

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
customtkinter.set_default_color_theme("blue")

def quitApp(master):
        master.destroy()

def bankManagement():
    BankManagement.mainMenu()

def projectNames(root):
    frame = customtkinter.CTkFrame(master = root)
    frame.pack(side = "top")

    label = Message(frame, text = "Projects - By Harsh Pachani", width = 1200, padx = 800, font = "lucida 20 bold",relief = "raised", fg = "white", bg = "blue")
    label.pack(side = "top")

    bank = customtkinter.CTkButton(master = root, text = " Bank Management System ", text_font = "Times 13", fg_color = "blue", command = lambda : bankManagement())
    bank.place(x = 120, y = 140)

    calc = customtkinter.CTkButton(master = root, text = "Calculator", text_font = "Times 13", fg_color = "blue", width = 21)
    calc.place(x = 120, y = 270)

    digital = customtkinter.CTkButton(master = root, text = "Digital Clock", text_font = "Times 13", fg_color = "blue", width = 21)
    digital.place(x = 120, y = 450)
        
    crud = customtkinter.CTkButton(master = root, text = "CRUD Operation", text_font = "Times 13", fg_color = "blue", width = 21)
    crud.place(x = 1040, y = 120)

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
        bank = Button(self, text = " Bank Management System ", font = "Times 13", bg = "blue", fg = "white")
        bank.place(x = 120, y = 140)

        calc = Button(self, text = "Calculator", font = "Times 13", bg = "blue", fg = "white", width = 21)
        calc.place(x = 120, y = 270)

        digital = Button(self, text = "Digital Clock", font = "Times 13", bg = "blue", fg = "white", width = 21)
        digital.place(x = 120, y = 450)
        
        crud = Button(self, text = "CRUD Operation", font = "Times 13", bg = "blue", fg = "white", width = 21)
        crud.place(x = 1040, y = 120)

        quitButton = Button(self, text = "Quit", font = "Times 13", width = 21, fg = "white", bg = "red", command = lambda : self.quitApp())
        quitButton.place(x = 720, y = 520)

if __name__ == "__main__":
    listScreen()