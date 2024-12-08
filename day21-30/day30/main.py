from tkinter import *
from tkinter import messagebox
from os import path
import pyperclip
import json
from password_generator import generate

BASE_PATH = path.dirname(__file__)
IMAGE_PATH = path.join(BASE_PATH, "logo.png")
DATA_PATH = path.join(BASE_PATH, "data.json")

FONT = ("Arial", 10, "bold")


def copy_random_password():
    """
    Generate a random password, display it in the password field,
    and copy it to the clipboard.
    """
    password = generate()
    password_input.delete(0, END)
    password_input.insert(END, password)
    pyperclip.copy(password)


def save_data():
    """
    Save website, email/username, and password to a JSON file.
    """
    website = website_input.get().strip()
    email = email_input.get().strip()
    password = password_input.get().strip()

    if website.lower() == "default_email":
        messagebox.showinfo(title="Error", message="Please use another website name.")
        return

    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty.")
        return

    # Confirm data before saving
    save = messagebox.askyesno(title="Password Confirmation", message=f"This is the data entered:\nWebsite: {website}\nEmail/Username: {email}\nPassword: {password}\nDo you confirm this data?")

    if save:
        new_data = {
            website.lower(): {
                "email": email,
                "password": password,
            }
        }
        try:
            # Load existing data
            with open(DATA_PATH) as file:
                data = json.load(file)
        except FileNotFoundError:
            # Create a new file if it doesn't exist
            with open(DATA_PATH, "w") as file:
                json.dump(new_data, file, indent=4)
        except json.JSONDecodeError:
            # Handle corrupted data file
            user_confirmation = messagebox.askyesno(title="Data file corrupted", message="The data file is corrupted. Do you want to overwrite it?")
            if user_confirmation:
                with open(DATA_PATH, "w") as file:
                    json.dump(new_data, file, indent=4)
        else:
            # Update existing data
            data.update(new_data)
            with open(DATA_PATH, "w") as file:
                json.dump(data, file, indent=4)
        finally:
            clean_input_fields()


def clean_input_fields():
    """
    Clear the input fields for website and password.
    """
    website_input.delete(0, END)
    password_input.delete(0, END)


def search_website_data():
    """
    Search for website data in the JSON file and display it to the user.
    """
    website = website_input.get().strip()

    if website.lower() == "default_email":
        messagebox.showinfo(title="Error", message="This website name can't be searched. Please try another one.")
        return

    if website == "":
        messagebox.showinfo(title="Error", message="Please provide a website name.")
        return
    try:
        with open(DATA_PATH) as file:
            data = json.load(file)

        website_data = data.get(website.lower())
        if website_data:
            messagebox.showinfo(title=website,
                message=f"Email/Username: {website_data['email']}\nPassword: {website_data['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"No data found for {website}.")
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showinfo(title="Error", message="The data file is missing or corrupted.")


def set_default_email():
    """
    Set the default email/username to be pre-filled in the email field.
    """
    try:
        with open(DATA_PATH) as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
        user_confirmation = messagebox.askyesno(title="Data file corrupted", message="The data file is missing or corrupted. Do you want to overwrite it?")
        if not user_confirmation:
            return

    email = email_input.get().strip()
    if email:
        user_confirmation = messagebox.askyesno(title="Default email/username", message=f'Do you want to set "{email}" as your default email/username?')
        if user_confirmation:
            data["default_email"] = email
            with open(DATA_PATH, "w") as file:
                json.dump(data, file, indent=4)
    else:
        messagebox.showinfo(title="Error", message="Please enter your email/username.")


def get_default_email():
    """
    Load and pre-fill the default email/username into the email input field.
    """
    try:
        with open(DATA_PATH) as file:
            data = json.load(file)
            email_input.insert(END, data.get("default_email", ""))
    except:
        return

# ---------------------------- UI Setup ---------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Configure row padding
for i in range(5):
    window.grid_rowconfigure(i, pad=5)

# Logo
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file=IMAGE_PATH)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", font=FONT)
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", font=FONT)
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", font=FONT)
password_label.grid(row=3, column=0)

# Inputs
website_input = Entry(width=33)
website_input.grid(row=1, column=1)
website_input.focus()
email_input = Entry(width=33)
email_input.grid(row=2, column=1)
password_input = Entry(width=33)
password_input.grid(row=3, column=1)

# Load default email
get_default_email()

# Buttons
website_search_button = Button(text="Search", width=15, command=search_website_data)
website_search_button.grid(row=1, column=2)
default_email_button = Button(text="Set default", width=15, command=set_default_email)
default_email_button.grid(row=2, column=2)
password_generate_button = Button(text="Generate Password", width=15, command=copy_random_password)
password_generate_button.grid(row=3, column=2)
password_add_button = Button(text="Add", width=44, command=save_data)
password_add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
