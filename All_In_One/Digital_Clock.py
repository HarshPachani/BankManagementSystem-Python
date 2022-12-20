from tkinter import Label, Tk
import time

def clock():
    root = Tk()
    root.title("Digital Clock")
    root.geometry("420x150")
    root.resizable(0, 0)
    label = Label(root, font = "Boulder 68 bold", bg = "light blue", fg = "black", bd = 25)
    label.grid(row = 0, column = 1)

    def digital_clock():
        time_live = time.strftime("%H:%M:%S")
        label.config(text = time_live)
        #in after method 200 millisecond is passed i.e. after 1 seconds digital clock function will be called.
        label.after(200, digital_clock)

    digital_clock()

    root.mainloop()

if __name__ == "__main__":
    clock()
