import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("220x300")
expression = ""

def press(n):
    global expression
    expression += n
    equation.set(expression)
def equalpress():
    global expression
    try:
        expression = str(eval(expression))
    except:
        expression = "error"
    equation.set(expression)
def clear():
    global expression
    expression = ""
    equation.set(expression)

equation = tk.StringVar()

entry = tk.Entry(root, textvariable= equation , font=("verdana", 18), borderwidth = 3, relief = "solid")
entry.pack(expand=True, fill="both")

frame1 = tk.Frame(root)
frame1.pack(expand=True, fill="both")

btn1 = tk.Button(frame1, text="1", font=("verdana", 18), command = lambda: press("1"), border=4)
btn1.pack(side="left", expand=True, fill="both")    

btn2 = tk.Button(frame1, text="2", font=("verdana", 18),command = lambda: press("2"), border=4)
btn2.pack(side="left", expand=True, fill="both")

btn3 = tk.Button(frame1, text="3", font=("verdana", 18),command = lambda: press("3"), border=4)
btn3.pack(side="left", expand=True, fill="both")

btn_plus = tk.Button(frame1, text="+", font=("verdana", 18),command = lambda: press("+"), border=4)
btn_plus.pack(side="left", expand=True, fill="both")


frame2 = tk.Frame(root)
frame2.pack(expand=True, fill="both")

btn4 = tk.Button(frame2, text="4", font=("verdana", 18),command = lambda: press("4"), border=4)
btn4.pack(side="left", expand=True, fill="both")

btn5 = tk.Button(frame2, text="5", font=("verdana", 18),command = lambda: press("5"),  border=4)
btn5.pack(side="left", expand=True, fill="both")

btn6 = tk.Button(frame2, text="6", font=("verdana", 18),command = lambda: press("6"), border=4)
btn6.pack(side="left", expand=True, fill="both")

btn_sub = tk.Button(frame2, text="-", font=("verdana", 18),command = lambda: press("-"), border=4)
btn_sub.pack(side="left", expand=True, fill="both")


frame3 = tk.Frame(root)
frame3.pack(expand=True, fill="both")

btn7 = tk.Button(frame3, text="7", font=("verdana", 18),command = lambda: press("7"), border=4)
btn7.pack(side="left", expand=True, fill="both")

btn8 = tk.Button(frame3, text="8", font=("verdana", 18),command = lambda: press("8"), border=4)
btn8.pack(side="left", expand=True, fill="both")

btn9 = tk.Button(frame3, text="9", font=("verdana", 18),command = lambda: press("9"), border=4)
btn9.pack(side="left", expand=True, fill="both")

btn_multi = tk.Button(frame3, text="*", font=("verdana", 18),command = lambda: press("*"), border=4)
btn_multi.pack(side="left", expand=True, fill="both")


frame4 = tk.Frame(root)
frame4.pack(expand=True, fill="both")

btn_clear = tk.Button(frame4, text="C", font=("verdana", 18),command = lambda:clear(), border=4)
btn_clear.pack(side="left", expand=True, fill="both")

btn_zero = tk.Button(frame4, text="0", font=("verdana", 18),command = lambda: press("0"), border=4)
btn_zero.pack(side="left", expand=True, fill="both")

btn_equal = tk.Button(frame4, text="=", font=("verdana", 18),command = lambda: equalpress(), border=4)
btn_equal.pack(side="left", expand=True, fill="both")

btn_div = tk.Button(frame4, text="/", font=("verdana", 18),command = lambda: press("/"), border=4)
btn_div.pack(side="left", expand=True, fill="both")


root.mainloop()
