from tkinter import *
from tkinter import messagebox
from os import path
import pyperclip
from password_generator import generate

BASE_PATH = path.dirname(__file__)
IMAGE_PATH = path.join(BASE_PATH, "logo.png")
FILE_PATH = path.join(BASE_PATH, "passwords.txt")

FONT = ("Arial", 10, "bold")

def copy_random_password():
    password = generate()
    password_input.delete(0, END)
    password_input.insert(END, password)
    pyperclip.copy(password)

def save_data():
    website = website_input.get().strip()
    email = email_input.get().strip()
    password = password_input.get().strip()

    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty.")
        return

    save = messagebox.askyesno(title="Password Confirmation", message=f"This is the data entered:\nWebsite: {website}\nEmail/Username: {email}\nPassword: {password}\nDo you confirm this data?")

    if save:
        with open(FILE_PATH, "a") as file:
            file.write(f"{website} | {email} | {password}\n")
        clean_input_fields()

def clean_input_fields():
    website_input.delete(0, END)
    password_input.delete(0, END)

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file=IMAGE_PATH)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=FONT)
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", font=FONT)
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", font=FONT)
password_label.grid(row=3, column=0)

website_input = Entry(width=52)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()
email_input = Entry(width=52)
email_input.grid(row=2, column=1, columnspan=2)
password_input = Entry(width=33)
password_input.grid(row=3, column=1)

try:
    with open(FILE_PATH) as file:
        email = file.readline().split(" | ")[1]
        email_input.insert(END, email)
except FileNotFoundError:
    pass

password_generate_button = Button(text="Generate Password", command=copy_random_password)
password_generate_button.grid(row=3, column=2)
password_add_button = Button(text="Add", width=44, command=save_data)
password_add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()