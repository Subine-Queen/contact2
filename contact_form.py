import tkinter as tk
from tkinter import messagebox, ttk
import csv
import re
import os

# ---------------------- SAVE CONTACT ----------------------
def save_data():
    name = entry_name.get().strip()
    email = entry_email.get().strip()
    phone = entry_phone.get().strip()
    address = entry_address.get("1.0", tk.END).strip()

    # Validation
    if not (name and email and phone and address):
        messagebox.showwarning("Input Error", "All fields are required!")
        return
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showwarning("Invalid Email", "Please enter a valid email address.")
        return
    if not re.match(r"^\+?\d{7,15}$", phone):
        messagebox.showwarning("Invalid Phone", "Phone number must be digits and 7-15 characters long.")
        return

    # Save to CSV
    with open('contacts.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, phone, address])

    messagebox.showinfo("Success", "Contact saved successfully!")
    clear_fields()

# ---------------------- CLEAR FORM ----------------------
def clear_fields():
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_address.delete("1.0", tk.END)

# ---------------------- VIEW CONTACTS ----------------------
def view_contacts():
    if not os.path.exists("contacts.csv"):
        messagebox.showinfo("No Data", "No contacts found!")
        return

    view_window = tk.Toplevel(window)
    view_window.title("Saved Contacts")
    view_window.geometry("600x300")
    view_window.config(bg="#f3eeee")

    columns = ("Name", "Email", "Phone", "Address")
    tree = ttk.Treeview(view_window, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    with open("contacts.csv", newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            tree.insert("", tk.END, values=row)

    tree.pack(expand=True, fill="both", padx=10, pady=10)

# ---------------------- MAIN WINDOW ----------------------
window = tk.Tk()
window.title("Contact Form")
window.geometry("450x500")
window.config(bg="#eef2f3")

title_label = tk.Label(window, text="📇 Contact Form", font=("Helvetica", 18, "bold"), bg="#eef2f3", fg="#333")
title_label.pack(pady=15)

form_frame = tk.Frame(window, bg="#eef2f3")
form_frame.pack(pady=10)

# Name
tk.Label(form_frame, text="Full Name:", font=("Arial", 12), bg="#eef2f3").grid(row=0, column=0, sticky="w", pady=5)
entry_name = tk.Entry(form_frame, width=35, font=("Arial", 11))
entry_name.grid(row=0, column=1, pady=5)

# Email
tk.Label(form_frame, text="Email Address:", font=("Arial", 12), bg="#eef2f3").grid(row=1, column=0, sticky="w", pady=5)
entry_email = tk.Entry(form_frame, width=35, font=("Arial", 11))
entry_email.grid(row=1, column=1, pady=5)

# Phone
tk.Label(form_frame, text="Phone Number:", font=("Arial", 12), bg="#eef2f3").grid(row=2, column=0, sticky="w", pady=5)
entry_phone = tk.Entry(form_frame, width=35, font=("Arial", 11))
entry_phone.grid(row=2, column=1, pady=5)

# Address
tk.Label(form_frame, text="Address:", font=("Arial", 12), bg="#eef2f3").grid(row=3, column=0, sticky="nw", pady=5)
entry_address = tk.Text(form_frame, width=26, height=4, font=("Arial", 11))
entry_address.grid(row=3, column=1, pady=5)

# Buttons Frame
btn_frame = tk.Frame(window, bg="#eef2f3")
btn_frame.pack(pady=20)

style = {"font": ("Arial", 12, "bold"), "width": 12, "bd": 0, "fg": "white"}

btn_submit = tk.Button(btn_frame, text="Save", bg="#4CAF50", command=save_data, **style)
btn_submit.grid(row=0, column=0, padx=10)

btn_clear = tk.Button(btn_frame, text="Clear", bg="#f39c12", command=clear_fields, **style)
btn_clear.grid(row=0, column=1, padx=10)

btn_view = tk.Button(btn_frame, text="View", bg="#3498db", command=view_contacts, **style)
btn_view.grid(row=0, column=2, padx=10)

window.mainloop()
