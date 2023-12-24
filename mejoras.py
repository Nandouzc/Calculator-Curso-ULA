"""calculator"""
import tkinter as tk
import re

# General settings
calcu = tk.Tk()
calcu.title("Calculadora")
calcu.geometry("205x410+00+100")
calcu.resizable(width=False, height=False)
calcu.config(bg="gray25")
calcu.iconbitmap(
    r"D:\Users\Quetzal\Documents\Monero\Practica-Python\calcu\calculator.ico.ico")

# Screen
pantalla = tk.Entry(calcu, bd=5, width=12, justify="right",
                    bg="LightBlue3", font=("Consolas", 20), fg="dodgerblue4")
pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=10)

# Buttons
buttons = [
    ('%', 1, 0, 1,"w,e",1,1), ('ª', 1, 1, 1,"w,e",1,1), ('AC', 1, 2, 1,"w,e",1,1), ('C', 1, 3, 1,"w,e",1,1),
    ('√', 2, 0, 1,"w,e",1,1), ('(', 2, 1, 1,"w,e",1,1), (')', 2, 2, 1,"w,e",1,1), ('/', 2, 3, 1,"w,e",1,1),
    ('7', 3, 0, 1,"w,e",1,1), ('8', 3, 1, 1,"w,e",1,1), ('9', 3, 2, 1,"w,e",1,1), ('*', 3, 3, 1,"w,e",1,1),
    ('4', 4, 0, 1,"w,e",1,1), ('5', 4, 1, 1,"w,e",1,1), ('6', 4, 2, 1,"w,e",1,1), ('-', 4, 3, 1,"w,e",1,1),
    ('1', 5, 0, 1,"w,e",1,1), ('2', 5, 1, 1,"w,e",1,1), ('3', 5, 2, 1,"w,e",1,1), ('+', 5, 3, 1,"w,e",1,1),
    ('0', 6, 0, 1,"w,e",1,1), ('.', 6, 1, 1,"w,e",1,1), ('=', 6, 2,2,"w,e",1,1)
]
# Functions
def is_math(expression):
    """verificar que es una operacion matemática"""
    texto = re.compile(r'^[-+*/0-9).(\s]+$')
    return bool(texto.match(expression))

def button_click(value):
    """click button"""
    current = pantalla.get()

    if value == 'AC':
        pantalla.delete(0, tk.END)
    elif value == 'C':
        last_digit = len(current[:-1])
        pantalla.delete(last_digit)
        new_current = pantalla.get()
        pantalla.delete(0,tk.END)
        pantalla.insert(0,new_current)
    elif value == '=':
        if is_math(current):
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

for (text, row, column,span,sticky,px,py) in buttons:
    btn = tk.Button(calcu, text=text, font=("Consolas", 13), padx=10, pady=10,bd=3, 
                    bg="lightblue4", fg="dodgerblue4", cursor="hand2", command=lambda t=text: button_click(t))
    btn.grid(row=row, column=column, columnspan=span, sticky=sticky,padx=px,pady=py)    
calcu.mainloop()
