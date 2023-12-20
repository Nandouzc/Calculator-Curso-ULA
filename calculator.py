"""claculator"""
import tkinter as tk

#General settings
calcu = tk.Tk()
calcu.title("Calculadora")
calcu.geometry("200x300")
calcu.resizable(width=False, height=False)
calcu.config(bg="gray25")
calcu.iconbitmap(
    r"D:\Users\Quetzal\Documents\Monero\Practica-Python\calcu\calculator.ico.ico")

#Screen
pantalla = tk.Entry(calcu, bd=5, width=12, justify="right",
                    bg="LightBlue3", font=("Consolas", 20), fg="dodgerblue4")
pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

#Buttons
buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]
for (text, row, column) in buttons:
    btn = tk.Button(calcu, text=text, font=("Consolas", 13), padx=10, pady=10, bg="lightblue4", fg="dodgerblue4")
    btn.grid(row=row, column=column)
    
calcu.mainloop()
