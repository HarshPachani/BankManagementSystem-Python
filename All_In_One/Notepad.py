from tkinter import *
import tkinter.messagebox as msgb
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

#==================METHODS===================#
def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None

    #Here 1.0 means 0th character or 1st line, Delete Everything.
    textArea.delete(1.0, END)

def openFile():
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

def saveFile():
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

def quitApp():
    root.destroy()

def cut():
    textArea.event_generate(("<<Cut>>"))

def copy():
    textArea.event_generate(("<<Copy>>"))

def paste():
    textArea.event_generate(("<<Paste>>"))

def about():
    msgb.showinfo("Notepad", "Notepad by Harsh Pachani")

if __name__ == "__main__":
    root = Tk()
    root.title("Untitled - Notepad")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}")

    #==========================Add TextArea=======================#
    file = None
    textArea = Text(root, font = "Calibri 13")
    textArea.pack(expand=True, fill = BOTH)

    #=========================Menubar====================#
    menuBar = Menu(root)

    #Filemenu Starts
    fileMenu = Menu(menuBar, tearoff = 0)
    #To Open New File
    fileMenu.add_command(label = "New", command = newFile)
    #To Open Already Existing file
    fileMenu.add_command(label = "Open", command = openFile)

    #To save the current file
    fileMenu.add_command(label = "Save", command = saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label = "Exit", command = quitApp)

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