from tkinter import *
from tkinter import messagebox as msgb
import customtkinter
import sqlite3
import time
import tkinter.ttk as ttk
import time
import BankManagement
import Calculator
import Digital_Clock
import File_Explorer
import Notepad
import Password_Manager

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

def calci():
    Calculator.mainMenu()

def clock():
    Digital_Clock.clock()

def fileExplorer():
    File_Explorer.mainScreen()

def notepad():
    Notepad.mainScreen()

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