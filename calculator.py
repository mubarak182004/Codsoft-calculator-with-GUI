import tkinter as tk
from tkinter import font

# Create main application window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x500")
root.configure(bg='lightblue')

# Define fonts
font_large = font.Font(family="Helvetica", size=18, weight="bold")
font_small = font.Font(family="Helvetica", size=14)

# Create display widget
display = tk.Entry(root, font=font_large, bd=10, insertwidth=2, width=14, borderwidth=4, justify='right', bg='white')
display.grid(row=0, column=0, columnspan=4, pady=20)

# Define button click functions
def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    try:
        result = str(eval(display.get()))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Create a style function to change button color on hover
def on_enter(e):
    e.widget['background'] = 'lightgrey'

def on_leave(e):
    e.widget['background'] = 'white'

# Create buttons
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 1, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 2, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 3, 3),
    ('C', 1, 0), ('0', 5, 0), ('=', 4, 3), ('+', 5, 3)
]

for (text, row, col) in buttons:
    action = lambda x=text: button_click(x) if x not in {'=', 'C'} else button_equal() if x == '=' else button_clear()
    button = tk.Button(root, text=text, padx=20, pady=20, font=font_small, command=action, bg='white', borderwidth=0)
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

# Additional styling for specific buttons
buttons_dict = {
    'C': (button_clear, 1, 0),
    '/': (lambda: button_click('/'), 1, 3),
    '*': (lambda: button_click('*'), 2, 3),
    '-': (lambda: button_click('-'), 3, 3),
    '+': (lambda: button_click('+'), 5, 3),
    '=': (button_equal, 4, 3)
}

for btn, (cmd, r, c) in buttons_dict.items():
    button = tk.Button(root, text=btn, padx=20, pady=20, font=font_small, command=cmd, bg='lightcoral', borderwidth=0)
    button.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

# Configure grid layout
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Run the main loop
root.mainloop()
