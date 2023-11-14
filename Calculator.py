import tkinter as tk

def on_button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
window = tk.Tk()
window.title("Basic Calculator")

# Entry widget for displaying and entering numbers
entry = tk.Entry(window, width=20, font=('Arial', 14), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Define the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Add buttons to the grid
row_val = 1
col_val = 0
for button in buttons:
    tk.Button(window, text=button, padx=20, pady=20, font=('Arial', 12),
              command=lambda button=button: on_button_click(button) if button != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
tk.Button(window, text='C', padx=20, pady=20, font=('Arial', 12), command=clear_entry).grid(row=row_val, column=col_val)

# Run the application
window.mainloop()
