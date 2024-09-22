import tkinter as tk
from tkinter import font as tkFont

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
def equalpress():
    try:
        global expression
        total = str(eval(expression)) 
        equation.set(total)
        expression = total
    except:
        equation.set(" error ")
        expression = ""
def clear():
    global expression
    expression = ""
    equation.set("")
def key_event(event):
    char = event.char
    if char.isdigit() or char in "+-*/":
        press(char)
    elif char == '\r': 
        equalpress()
    elif char == '\x08':  
        clear()
root = tk.Tk()
root.title("Calculator")
root.geometry("420x600")
root.configure(bg="#1E1E1E")
display_font = tkFont.Font(family='Helvetica', size=24, weight='bold')
button_font = tkFont.Font(family='Helvetica', size=18, weight='bold')
title_font = tkFont.Font(family='Helvetica', size=22, weight='bold')

expression = ""
equation = tk.StringVar()
title_label = tk.Label(root, text=" CALCULATOR", font=title_font, fg="#FF8C00", bg="#1E1E1E")
title_label.grid(row=0, column=0, columnspan=4, pady=10)
display = tk.Entry(root, textvariable=equation, font=display_font, justify='right', bd=10, bg="#333333", fg="white")
display.grid(row=1, column=0, columnspan=4, ipadx=8, ipady=15, padx=10, pady=10)

def create_button(text, row, col, color="#393E46", command=None, width=5, height=2):
    return tk.Button(root, text=text, font=button_font, fg="white", bg=color, bd=0, command=command,
                     width=width, height=height).grid(row=row, column=col, padx=5, pady=5)

create_button("mrc", 2, 0, color="#686D76")
create_button("m-", 2, 1, color="#686D76")
create_button("m+", 2, 2, color="#686D76")
create_button("/", 2, 3, color="#1ca3b2", command=lambda: press("/"))

create_button("7", 3, 0, color="#393E46", command=lambda: press(7))
create_button("8", 3, 1, color="#393E46", command=lambda: press(8))
create_button("9", 3, 2, color="#393E46", command=lambda: press(9))
create_button("*", 3, 3, color="#1ca3b2", command=lambda: press("*"))  

create_button("4", 4, 0, color="#393E46", command=lambda: press(4))
create_button("5", 4, 1, color="#393E46", command=lambda: press(5))
create_button("6", 4, 2, color="#393E46", command=lambda: press(6))
create_button("-", 4, 3, color="#1ca3b2", command=lambda: press("-"))

create_button("1", 5, 0, color="#393E46", command=lambda: press(1))
create_button("2", 5, 1, color="#393E46", command=lambda: press(2))
create_button("3", 5, 2, color="#393E46", command=lambda: press(3))
create_button("+", 5, 3, color="#1ca3b2", command=lambda: press("+"))

create_button("0", 6, 0, color="#393E46", command=lambda: press(0))
create_button(".", 6, 1, color="#393E46", command=lambda: press("."))
create_button("C", 6, 2, color="#FF5722", command=clear)
create_button("=", 6, 3, color="#5eb03a", command=equalpress)

root.bind("<Key>", key_event)

root.mainloop()