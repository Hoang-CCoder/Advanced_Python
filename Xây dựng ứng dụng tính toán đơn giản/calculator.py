import tkinter as tk
from tkinter import ttk

# Function for addition
def add_numbers():
    result = float(num_a.get()) + float(num_b.get())
    result_var.set(result)

# Function for subtraction
def subtract_numbers():
    result = float(num_a.get()) - float(num_b.get())
    result_var.set(result)

# Function for multiplication
def multiply_numbers():
    result = float(num_a.get()) * float(num_b.get())
    result_var.set(result)

# Function for division
def divide_numbers():
    try:
        result = float(num_a.get()) / float(num_b.get())
        result_var.set(result)
    except ZeroDivisionError:
        result_var.set("Error: Division by zero!")

if __name__ == '__main__':
    # Initialize main Tk window
    win = tk.Tk()
    win.title("Calculator")

    # Tab control
    tab_control = ttk.Notebook(win)
    tab_basic = ttk.Frame(tab_control)
    tab_control.add(tab_basic, text="Tính Toán Cơ Bản")
    tab_control.pack(expand=1, fill='both')

    # Frame for input
    input_frame = ttk.LabelFrame(tab_basic, text=" Input Parameters ")
    input_frame.grid(column=0, row=0, padx=10, pady=10)

    # Label and Entry for number a
    ttk.Label(input_frame, text="Number A: ").grid(column=0, row=0, padx=5, pady=5)
    num_a = tk.StringVar()
    ttk.Entry(input_frame, textvariable=num_a).grid(column=1, row=0)

    # Label and Entry for number b
    ttk.Label(input_frame, text="Number B: ").grid(column=0, row=1, padx=5, pady=5)
    num_b = tk.StringVar()
    ttk.Entry(input_frame, textvariable=num_b).grid(column=1, row=1)

    # Frame for operations
    operation_frame = ttk.LabelFrame(tab_basic, text=" Operations ")
    operation_frame.grid(column=1, row=0, padx=10, pady=10)

    # Operation buttons
    ttk.Button(operation_frame, text="+", command=add_numbers).grid(column=0, row=0, padx=5, pady=5)
    ttk.Button(operation_frame, text="-", command=subtract_numbers).grid(column=0, row=1, padx=5, pady=5)
    ttk.Button(operation_frame, text="*", command=multiply_numbers).grid(column=0, row=2, padx=5, pady=5)
    ttk.Button(operation_frame, text="/", command=divide_numbers).grid(column=0, row=3, padx=5, pady=5)

    # Display result
    result_var = tk.StringVar()
    ttk.Label(tab_basic, text="Result: ").grid(column=0, row=1, padx=5, pady=5)
    ttk.Label(tab_basic, textvariable=result_var, font=("Arial", 12)).grid(column=1, row=1, padx=5, pady=5)

    # Start the main loop
    win.mainloop()
