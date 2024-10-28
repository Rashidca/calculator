import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")

display = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def update_display(value):
    display.insert(tk.END, value)

def clear_display():
    display.delete(0, tk.END)

def backspace():
    display.delete(len(display.get())-1, tk.END)

def calculate():
    try:
        result = eval(display.get())
        clear_display()
        display.insert(tk.END, result)
    except ZeroDivisionError:
        clear_display()
        display.insert(tk.END, "Cannot divide by zero")
    except Exception:
        clear_display()
        display.insert(tk.END, "Error")

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 3), ('=', 4, 2)
]

for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, height=3, width=9, font=("Arial", 15), command=calculate)
    else:
        button = tk.Button(root, text=text, height=3, width=9, font=("Arial", 15), command=lambda txt=text: update_display(txt))
    button.grid(row=row, column=col, padx=5, pady=5)

clear_button = tk.Button(root, text="C", height=3, width=9, font=("Arial", 15), command=clear_display)
clear_button.grid(row=5, column=3, padx=5, pady=5)

backspace_button = tk.Button(root, text="⌫", height=3, width=9, font=("Arial", 15), command=backspace)
backspace_button.grid(row=5, column=2, padx=5, pady=5)


root.bind('<Return>', lambda event: calculate())
root.bind('<BackSpace>', lambda event: backspace())
root.bind('<Escape>', lambda event: clear_display())
for key in '0123456789/*-+.':
    root.bind(key, lambda event, digit=key: update_display(digit))

root.mainloop()



