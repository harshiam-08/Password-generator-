
import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for length.")
        return

    use_digits = digits_var.get()
    use_special = special_var.get()

    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "No characters selected to generate password.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

def copy_password():
    password = password_var.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Please generate a password first.")

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x250")

tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.insert(0, "12")
length_entry.pack()

digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Digits (0-9)", variable=digits_var).pack()
tk.Checkbutton(root, text="Include Special Characters (!@#$)", variable=special_var).pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, font=("Courier", 12), width=30).pack()

tk.Button(root, text="Copy to Clipboard", command=copy_password).pack(pady=5)

root.mainloop()
