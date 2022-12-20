from tkinter import *
from tkinter import messagebox as msgb 
from tkinter import filedialog as fd
import os
import shutil #For file copy, paste and move.

#=====================FUNCTION====================#
def openAFile():
    #Selecting a file using askopenfilename of filedialog as fd
    files = fd.askopenfilename(title = "Select a file of any type", filetypes=[("All files", "*.*")])
    print(files)
    # print("os.path = ", os.path)
    # print("Absolute path = ", os.path.abspath(files))

    if files == "":
        msgb.showinfo("Terminated!", "Open Operation Cancelled!!")
        return
    
    os.startfile(os.path.abspath(files)) #This will trigger file manager to open a folder of the absolute path.

def copyAFile():
    # using the filedialog's askopenfilename() method to select the file
    copyTheFile = fd.askopenfilename(title = "Select a File to Copy", filetypes = [("All files", "*.*")])

    # print(copyTheFile)

    if copyTheFile == None:
        msgb.showinfo("Cancel!!", "Cancelled the copy Operation!!")
        return
    #Use the filedialog's askdirectory() method for selecting the directory.
    dirToPaste = fd.askdirectory(title = "Select the folder to paste the file")
    # print(dirToPaste)

    try:
        shutil.copy(copyTheFile, dirToPaste)
        msgb.showinfo(title = "File Copied!", message = "The File has been copied to the destination.")
    except:
        msgb.showerror(title = "Error!", message = "File is unable to copy. Please try again!")

def deleteAFile():
    # Selecting the file using the filedialog's askopenfilename() method
    files = fd.askopenfilename(title = "Choose a file to delete", filetypes=[("All files", "*.*")])
    
    #Delete the file using the remove() method
    os.remove(os.path.abspath(files))
    msgb.showinfo(title = "File deleted!", message = "The selected file has been deleted successfully!!")

def nameSubmit():
    renameName = fileNameEntered.get()

    fileNameEntered.set("")
    fileName = showFilePath()

    #Creating a new file name for the file
    newfileName = os.path.join(os.path.dirname(fileName), renameName + os.path.splitext(fileName)[1])
    os.rename(fileName, newfileName)
    msgb.showinfo(title = "File Renamed!", message = "The seleected file has been renamed.")


def renameAFile():
    rename_root = Toplevel(root)
    rename_root.title("Rename File")
    rename_root.geometry("300x100+300+250")
    rename_root.resizable(0, 0)
    rename_root.config(bg = "#F6EAD7")

    #===================LABEL================#
    rename_label = Label(rename_root, text = "Enter the file name", font = "Calibri 10", bg = "white", fg = "blue")
    rename_label.pack(pady = 4)

    rename_field = Entry(rename_root, width = 26, textvariable=fileNameEntered, relief=GROOVE, font = "Calibri 10", bg = "white", fg = "blue")
    rename_field.pack(pady = 4, padx = 4)

    #=====================BUTTON======================#
    submitButton = Button(rename_root, text = "Submit", width = 14, relief=GROOVE, font = "Calibri 9", bg = "white", fg = "blue", activebackground="#709218", activeforeground="#FFFFFF", command=nameSubmit)
    submitButton.pack(pady = 2)

def showFilePath():
    files = fd.askopenfilename(title = "Select the file to rename", filetypes=[("All files", "*.*")])
    return files

def openAFolder():
    # using the filedialog's askdirectory() method to select the folder
    folder1 = fd.askdirectory(title = "Select folder to Open")
    os.startfile(folder1)

def deleteAFolder():
    folderToDelete = fd.askdirectory(title = "Select Folder to delete")
    try:
        os.rmdir(folderToDelete)
        msgb.showinfo("Folder Deleted!", "The selected folder has been deleted")
    except:
        msgb.showinfo("Denied!!", "The Folder should not be carrying any file in it.\nFolder should be empty before Deleted!!\nClear the folder first.")
    


def moveAFolder():
    folderToMove = fd.askdirectory(title = "Select the folder you want to move")

    # print(folderToMove)
    if folderToMove == "":
        msgb.showinfo(title= "Terminated", message = "No Folder Selected to move!!")
        return
    
    msgb.showinfo(message = "Folder has been selected to move. Now select the desired destination.")
    des = fd.askdirectory(title = "Destination")

    try:
        shutil.move(folderToMove, des)
        msgb.showinfo("Folder moved!", "The selected folder has been moved to the desired destination")
    except:
        msgb.showerror("Error!", "The folder cannot be moved. Make sure that the destination exists")

def listFilesInFolder():
    i = 0
    #Using the askdirectory() method to select the folder
    folder1 = fd.askdirectory(title = "Select the folder")
    files = os.listdir(os.path.abspath(folder1))
    listFilesWindow = Toplevel(root)

    #Specifying the title of the pop-up window
    listFilesWindow.title(f"Files in {folder1}")
    listFilesWindow.geometry("300x500+300+200")
    listFilesWindow.resizable(0, 0)
    listFilesWindow.config(bg = "white")

    #Creating a list box
    lsb = Listbox(listFilesWindow, selectbackground="#F24FBF", font= "Calibri, 10", background="white")
    lsb.place(relx = 0, rely = 0, relheight=1, relwidth=1)

    #===============SCROLLBAR================#
    scroll = Scrollbar(lsb, orient= VERTICAL, command = lsb.yview)
    scroll.pack(side = RIGHT, fill = Y)
    lsb.config(yscrollcommand=scroll.set)

    #ITERATING THROUGH THE FILES IN THE FOLDER
    while i < len(files):
        # using the insert() method to insert the file details in the list box
        lsb.insert(END, '[' + str(i+1) + ']' + files[i])
        i += 1
    lsb.insert(END, "")
    lsb.insert(END, "Total Files: ", str(len(files)))

def quitApp(master):
    master.destroy()

def mainScreen():
    root = Tk()
    root.title("File Explorer")
    root.geometry("400x600+850+50")
    root.resizable(0, 0)
    root.configure(bg="white")

    #================FRAMES==================#
    header_frame = Frame(root, bg = "#D8E9E6")
    button_frame = Frame(root, bg = "skyblue")

    header_frame.pack(fill = BOTH)
    button_frame.pack(expand = TRUE, fill = BOTH)

    #==================LABLES===============#
    header_label = Label(header_frame, text = "File Explorer", font = "Calibri 16", bg = "white", fg = "blue")
    header_label.pack(expand = TRUE, fill = BOTH, pady = 12)

    #===========================BUTTONS=======================#
    openButton = Button(button_frame, text = "Open a File", font = "Calibri 15", width = 20, bg = "white", fg = "blue", relief = GROOVE, activebackground="lightgreen", command = openAFile)
    renameButton = Button(button_frame, text = "Rename a File", font = "Calibri 15", width = 20, bg = "white", fg = "blue", relief = GROOVE, activebackground="lightgreen", command = renameAFile)
    copyButton = Button(button_frame, text = "Copy the File", font = "Calibri 15", width = 20, bg = "white", fg = "blue", relief = GROOVE, activebackground="lightgreen", command = copyAFile)
    deleteButton = Button(button_frame, text = "Delete a File", font = "Calibri 15", width = 20, bg = "white", fg = "blue", relief = GROOVE, activebackground="lightgreen", command = deleteAFile)
    openFolderButton = Button(button_frame, text = "Open a Folder", font = "Calibri 15", width = 20, bg = "white", fg = "blue", relief = GROOVE, activebackground="lightgreen", command = openAFolder)
    deleteFolderButton = Button(button_frame, text = "Delete a Folder", font = "Calibri 15", width = 20, bg = "white", fg = "blue", relief = GROOVE, activebackground="lightgreen", command = deleteAFolder)
    moveFolderButton = Button(button_frame, text = "Move the Folder", font = "Calibri 15", width = 20, bg = "white", fg = "blue", relief = GROOVE, activebackground="lightgreen", command = moveAFolder)
    listButton = Button(button_frame, text = "List Files in Folder", font = "Calibri 15", width = 20, bg = "white", fg = "blue", relief = GROOVE, activebackground="lightgreen", command = listFilesInFolder)
    quitButton = Button(button_frame, text = "Quit", font = "Calibri 15", width = 20, bg = "white", fg = "red", relief = GROOVE, activebackground="lightgreen", command = lambda : quitApp(root))

    #======================PACKING ALL BUTTONS======================#
    openButton.pack(pady = 9)
    renameButton.pack(pady = 9)
    copyButton.pack(pady = 9)
    deleteButton.pack(pady = 9)
    moveFolderButton.pack(pady = 9)
    openFolderButton.pack(pady = 9)
    deleteFolderButton.pack(pady = 9)
    listButton.pack(pady = 10)
    quitButton.pack(pady = 12)

    fileNameEntered = StringVar()
    root.mainloop()
    
if __name__ == "__main__":
    mainScreen()