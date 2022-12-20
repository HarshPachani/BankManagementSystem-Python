from tkinter import *

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

def mainMenu():
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

if __name__ == "__main__":
    mainMenu()