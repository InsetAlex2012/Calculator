from tkinter import *

window = Tk()
window.geometry("750x400")
window.title("Calculator!")
window.configure(bg="#DADBDD")
window.resizable(False, False)

math_img = PhotoImage(file = "math.png")

window.iconphoto(True, math_img)

result = ""

def Press(num):
    global result
    result += str(num)
    equation.set(result)

def Clear():
    global result
    result = ""
    equation.set("")

def EqualPress(event):
    try:
        global result
        total = str(eval(result))
        equation.set(total)
        result = ""
    except:
        equation.set("Format Error")
        result = ""



equation = StringVar()

txt = Entry(window, bg="light gray", textvariable=equation, font=("Arial", 27), state="readonly")
txt.grid(row=0, column=0, columnspan=5, sticky="we")


btn1 = Button(window, text = 1, bg = "light gray" , activebackground="#BFBFBF", font = ("Arial", 27), width = 5, command = lambda: Press(1))
btn1.grid(row = 1, column = 0, pady = 5)

btn2 = Button(window, text = 2, bg = "light gray" , activebackground="#BFBFBF", font = ("Arial", 27), width = 5, command = lambda: Press(2))
btn2.grid(row = 1, column = 1, pady = 5)

btn3 = Button(window, text = 3, bg = "light gray" , activebackground="#BFBFBF", font = ("Arial", 27), width = 5, command = lambda: Press(3))
btn3.grid(row = 1, column = 2, pady = 5)

btn4 = Button(window, text = 4, bg = "light gray" , activebackground="#BFBFBF", font = ("Arial", 27), width = 5, command = lambda: Press(4))
btn4.grid(row = 2, column = 0, pady = 5)

btn5 = Button(window, text = 5, bg = "light gray" , activebackground="#BFBFBF", font = ("Arial", 27), width = 5, command = lambda: Press(5))
btn5.grid(row = 2, column = 1, pady = 5)

btn6 = Button(window, text = 6, bg = "light gray" , activebackground="#BFBFBF", font = ("Arial", 27), width = 5, command = lambda: Press(6))
btn6.grid(row = 2, column = 2, pady = 5)

btn7 = Button(window, text = 7, bg = "light gray" , activebackground="#BFBFBF", font = ("Arial", 27), width = 5, command = lambda: Press(7))
btn7.grid(row = 3, column = 0, pady = 5)

btn8 = Button(window, text = 8, bg = "light gray" , activebackground="#BFBFBF", font = ("Arial", 27), width = 5, command = lambda: Press(8))
btn8.grid(row = 3, column = 1, pady = 5)

btn9 = Button(window, text = 9, bg = "light gray" , activebackground="#BFBFBF", font = ("Arial", 27), width = 5, command = lambda: Press(9))
btn9.grid(row = 3, column = 2, pady = 5)

btn0 = Button(window, text = 0, bg = "light gray" , activebackground="#BFBFBF", font = ("Arial", 27), width = 5, command = lambda: Press(0))
btn0.grid(row = 4, column = 1, pady = 5)

clear_btn = Button(window, text = "Clear", bg = "light gray" , activebackground="dark gray", font = ("Arial", 27), width = 5, command = Clear)
clear_btn.grid(row = 4, column = 0, pady = 5)

period_btn = Button(window, text = ".", bg = "light gray" , activebackground="dark gray", font = ("Arial", 27), width = 5, command = lambda: Press("."))
period_btn.grid(row = 4, column = 2, pady = 5)

plus_btn = Button(window, text = "+", bg = "#e38c22" , activebackground="#bf7c2a", font = ("Arial", 27), width = 5, command = lambda: Press("+"))
plus_btn.grid(row = 1, column = 3, pady = 5, padx = 20)

minus_btn = Button(window, text = "-", bg = "#e38c22" , activebackground="#bf7c2a", font = ("Arial", 27), width = 5, command = lambda: Press("-"))
minus_btn.grid(row = 2, column = 3, pady = 5, padx = 20)

multi_btn = Button(window, text = "x", bg = "#e38c22" , activebackground="#bf7c2a", font = ("Arial", 27), width = 5, command = lambda: Press("*"))
multi_btn.grid(row = 3, column = 3, pady = 5, padx = 20)

divide_btn = Button(window, text = "÷", bg = "#e38c22" , activebackground="#bf7c2a", font = ("Arial", 27), width = 5, command = lambda: Press("/"))
divide_btn.grid(row = 4, column = 3, pady = 5, padx = 20)

btn_lpar = Button(window, text = "(", bg = "#b36e00" , activebackground="#7d4d00", font = ("Arial", 27), width = 5, command = lambda: Press("("))
btn_lpar.grid(row = 1, column = 4, pady = 5)

btn_rpar = Button(window, text = ")", bg = "#b36e00" , activebackground="#7d4d00", font = ("Arial", 27), width = 5, command = lambda: Press(")"))
btn_rpar.grid(row = 2, column = 4, pady = 5)

btn_pow = Button(window, text = "Power", bg = "#b36e00" , activebackground="#7d4d00", font = ("Arial", 27), width = 5, command = lambda: Press("**"))
btn_pow.grid(row = 3, column = 4, pady = 5)

for i in range(5):
    window.grid_columnconfigure(i, weight=1)

window.bind("1", lambda event: Press("1"))
window.bind("2", lambda event: Press("2"))
window.bind("3", lambda event: Press("3"))
window.bind("4", lambda event: Press("4"))
window.bind("5", lambda event: Press("5"))
window.bind("6", lambda event: Press("6"))
window.bind("7", lambda event: Press("7"))
window.bind("8", lambda event: Press("8"))
window.bind("9", lambda event: Press("9"))
window.bind("0", lambda event: Press("0"))


window.bind("+", lambda event: Press("+"))
window.bind("-", lambda event: Press("-"))
window.bind("*", lambda event: Press("*"))
window.bind("/", lambda event: Press("/"))
window.bind(".", lambda event: Press("."))
window.bind("p", lambda event: Press("**"))
window.bind("P", lambda event: Press("**"))

window.bind("(", lambda event: Press("("))
window.bind(")", lambda event: Press(")"))
window.bind("[", lambda event: Press("("))
window.bind("]", lambda event: Press(")"))
window.bind("{", lambda event: Press("("))
window.bind("}", lambda event: Press(")"))

window.bind("c", lambda event: Clear())
window.bind("C", lambda event: Clear())




window.bind("<Return>", EqualPress)
window.mainloop()