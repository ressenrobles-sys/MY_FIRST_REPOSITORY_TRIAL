import tkinter as tk
from tkinter import messagebox

def calculate_moment():
    try:
        P = float(entry_load.get())
        L = float(entry_length.get())

        M = (P * L) / 4

        result_label.config(text=f"Maximum Bending Moment = {M:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Create main window
root = tk.Tk()
root.title("Beam Moment Calculator")
root.geometry("350x250")

# Title
title_label = tk.Label(root, text="Simply Supported Beam\n(Central Point Load)", font=("Arial", 12, "bold"))
title_label.pack(pady=10)

# Load input
tk.Label(root, text="Load (P):").pack()
entry_load = tk.Entry(root)
entry_load.pack()

# Length input
tk.Label(root, text="Beam Length (L):").pack()
entry_length = tk.Entry(root)
entry_length.pack()

# Calculate button
calc_button = tk.Button(root, text="Calculate", command=calculate_moment)
calc_button.pack(pady=10)

# Result display
result_label = tk.Label(root, text="Maximum Bending Moment = ")
result_label.pack(pady=10)

# Run application
root.mainloop()