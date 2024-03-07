from tkinter import *


root = Tk()
root.title("Calculator")


e = Entry(root, width = 35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady = 10)




def button_click(number):
   current = e.get()
   e.delete(0, END)
   e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_num = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_num)
    e.delete(0, END)

def button_subtract():
    first_num = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_num)
    e.delete(0, END)

def button_multiply():
    first_num = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_num)
    e.delete(0, END)

def button_divide():
    first_num = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_num)
    e.delete(0, END)

def button_power():
    first_num = e.get()
    global f_num
    global math
    math = "power of"
    f_num = int(first_num)
    e.delete(0, END)

def button_sqrt():
    first_num = e.get()
    global f_num
    global math
    math = "square root"
    f_num = int(first_num)
    e.delete(0, END)

def button_mod():
    first_num = e.get()
    global f_num
    global math
    math = "modulus"
    f_num = int(first_num)
    e.delete(0, END)


def button_equals():
    second_num = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_num))
    elif math == "subtraction":
        e.insert(0, f_num - int(second_num))
    elif math == "multiplication":
        e.insert(0, f_num * int(second_num))
    elif math == "division":
        e.insert(0, f_num / int(second_num))
    elif math == "power of":
        e.insert(0, f_num ** int(second_num))
    elif math == "square root":
        e.insert(0, f_num  / int(second_num))
    elif math == "modulus":
        e.insert(0, f_num % int(second_num))


button_1 = Button(root, text="1", padx=40, pady=20, command= lambda: button_click(1), fg = "Black", bg = "white")
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2), fg = "Black", bg = "white")
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3), fg = "Black", bg = "white")
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4), fg = "Black", bg = "white")
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5), fg = "Black", bg = "white")
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6), fg = "Black", bg = "white")
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7), fg = "Black", bg = "white")
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8), fg = "Black", bg = "white")
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9), fg = "Black", bg = "white")
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0), fg = "Black", bg = "white")

button_add = Button(root, text="+", padx=39, pady=20, command= button_add, fg = "Black", bg = "white")
button_subtract = Button(root, text="-", padx=40, pady=20, command= button_subtract, fg = "Black", bg = "white")
button_multiply = Button(root, text="x", padx=40, pady=20, command= button_multiply, fg = "Black", bg = "white")
button_divide = Button(root, text="÷", padx=39, pady=20, command= button_divide, fg = "Black", bg = "white")
button_power = Button(root, text="^", padx=39, pady=20, command= button_power, fg = "Black", bg = "white")
button_sqrt = Button(root, text="√", padx=39, pady=20, command= button_sqrt, fg = "Black", bg = "white")
button_remainder = Button(root, text="%", padx=39, pady=20, command= button_mod, fg = "Black", bg = "white")

button_decimal = Button(root, text=".", padx=40, pady=20,  fg = "Black", bg = "white")
button_backspace = Button(root, text="<-", padx=40, pady=20, fg = "Black", bg = "white")
button_fraction = Button(root, text="/", padx=39, pady=20, fg = "Black", bg = "white")

button_equal = Button(root, text="=", padx=91, pady=20, command=button_equals, fg = "Black", bg = "white")
button_clear = Button(root, text="clear", padx=79, pady=20, command= button_clear, fg = "Black", bg = "white")

button_1.grid(row=4, column=1)
button_2.grid(row=4, column=2)
button_3.grid(row=4, column=3)

button_4.grid(row=3, column=1)
button_5.grid(row=3, column=2)
button_6.grid(row=3, column=3)

button_7.grid(row=2, column=1)
button_8.grid(row=2, column=2)
button_9.grid(row=2, column=3)

button_0.grid(row=5, column=1)

button_add.grid(row=6, column=1)
button_subtract.grid(row=2, column=0)
button_multiply.grid(row=3, column=0)
button_divide.grid(row=4, column=0)
button_power.grid(row=5, column=0)
button_sqrt.grid(row=5, column=3)
button_remainder.grid(row=6, column=0)

button_decimal.grid(row=1, column=1)
button_backspace.grid(row=1, column=3)
button_fraction.grid(row=1, column=2)

button_equal.grid(row=5, column=2, columnspan=2)
button_clear.grid(row=6, column=2, columnspan=2)

root.mainloop()