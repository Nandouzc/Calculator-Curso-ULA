"""calculator"""
import tkinter as tk
import re

# General settings
calcu = tk.Tk()
calcu.title("Calculadora")
calcu.geometry("200x400")
calcu.resizable(width=False, height=False)
calcu.config(bg="gray25")
calcu.iconbitmap(
    r"D:\Users\Quetzal\Documents\Monero\Practica-Python\calcu\calculator.ico.ico")

# Screen
pantalla = tk.Entry(calcu, bd=5, width=12, justify="right",
                    bg="LightBlue3", font=("Consolas", 20), fg="dodgerblue4")
pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=15)

# Buttons
buttons = [
    ('%', 1, 0, 1,"w,e"), ('ª', 1, 1, 1,"w,e"), ('AC', 1, 2, 1,"w,e"), ('C', 1, 3, 1,"w,e"),
    ('√', 2, 0, 1,"w,e"), ('(', 2, 1, 1,"w,e"), (')', 2, 2, 1,"w,e"), ('/', 2, 3, 1,"w,e"),
    ('7', 3, 0, 1,"w,e"), ('8', 3, 1, 1,"w,e"), ('9', 3, 2, 1,"w,e"), ('*', 3, 3, 1,"w,e"),
    ('4', 4, 0, 1,"w,e"), ('5', 4, 1, 1,"w,e"), ('6', 4, 2, 1,"w,e"), ('-', 4, 3, 1,"w,e"),
    ('1', 5, 0, 1,"w,e"), ('2', 5, 1, 1,"w,e"), ('3', 5, 2, 1,"w,e"), ('+', 5, 3, 1,"w,e"),
    ('0', 6, 0, 1,"w,e"), ('.', 6, 1, 1,"w,e"), ('=', 6, 2,2,"w,e")
]
# Functions
def is_valid_math_expression(expression):
    """verificar que no sea letras"""
    pattern = re.compile(r'^[.()-+*/0-9\s]+$')
    return bool(pattern.match(expression))

def button_click(value):
    """click button"""
    current = pantalla.get()

    if value == 'AC':
        pantalla.delete(0, tk.END)
    elif value == '=':
        if is_valid_math_expression(current):
            try:
                result = eval(current)
                pantalla.delete(0, tk.END)
                pantalla.insert(tk.END, str(result))
            except (ZeroDivisionError, TypeError,SyntaxError):
                pantalla.delete(0, tk.END)
                pantalla.insert(tk.END, " Error ")
        else:
            pantalla.delete(0, tk.END)
            pantalla.insert(tk.END, "No válido",)
    else:
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, current + value)
for (text, row, column,span,sticky) in buttons:
    btn = tk.Button(calcu, text=text, font=("Consolas", 13), padx=10, pady=10,bd=3,
                    bg="lightblue4", fg="dodgerblue4", command=lambda t=text: button_click(t))
    btn.grid(row=row, column=column, columnspan=span, sticky=sticky)    
calcu.mainloop()
