import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = calculate(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

def shunting_yard(tokens):
    output = []
    operator_stack = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    for token in tokens:
        if token.isdigit() or '.' in token:
            output.append(float(token))
        elif token in precedence:
            while (operator_stack and operator_stack[-1] in precedence
                   and precedence[token] <= precedence[operator_stack[-1]]):
                output.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            operator_stack.pop()

    while operator_stack:
        output.append(operator_stack.pop())

    return output

def evaluate_postfix(expression):
    stack = []
    operators = {'+': lambda x, y: x + y, '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y, '/': lambda x, y: x / y}

    for token in expression:
        if isinstance(token, float):
            stack.append(token)
        elif token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operators[token](operand1, operand2)
            stack.append(result)

    return stack[0]

def calculate(expression):
    tokens = []
    current = ''
    for char in expression:
        if char.isdigit() or char == '.':
            current += char
        else:
            if current:
                tokens.append(current)
            current = ''
            tokens.append(char)
    if current:
        tokens.append(current)

    tokens = shunting_yard(tokens)
    result = evaluate_postfix(tokens)
    return result

root = tk.Tk()
root.title("Calculadora")

entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
    ("=", 5, 0)
]

for (text, row, column) in buttons:
    btn = tk.Button(root, text=text, font=("Arial", 15), padx=20, pady=10)
    btn.grid(row=row, column=column)
    btn.bind("<Button-1>", click)

root.mainloop()