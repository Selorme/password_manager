from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
import os
from dotenv import load_dotenv

load_dotenv()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list

    # shuffle password
    shuffle(password_list)

    # print password
    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_inputs():
    website = website_input.get()
    email = email_username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="please fill in all fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"these are the details entered: \nWebsite: {website}"
                                                              f"\nEmail: {email}, \nPassword: {password} "
                                                              f"\nIs it ok to save?")

        if is_ok:
            try:
                with open("data.json", "r") as all_data:
                    # read old data
                    data = json.load(all_data)
            except FileNotFoundError:
                # create a new empty dictionary called data if it doesn't already exist
                data = {}
            if website in data:
                messagebox.showinfo(title="Already Exists!", message="Information for this website already exists")
            else:
                # update old data with new data
                data.update(new_data)

                with open("data.json", "w") as all_data:
                    # saving updated data
                    json.dump(data, all_data, indent=4)
                website_input.delete(0, END)
                password_input.delete(0, END)
                messagebox.showinfo(title="Saved", message="Information successfully saved!")


# ---------------------------- EXISTING WEBSITE ----------------------- #
def website_exists():
    website = website_input.get()
    try:
        with open("data.json", "r") as all_data:
            data = json.load(all_data)
        if website in data:
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"website: {website}\npassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
    except FileNotFoundError:
        messagebox.showinfo(title="Not Found", message="This file does not exist. You can create it by "
                                                       "generating password and using the add button!")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(window, height=200, width=200)
padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(row=0, column=1)

# Labels
website_text = Label(text="Website:")
website_text.grid(row=1, column=0)
email_username_text = Label(text="Email/Username:")
email_username_text.grid(row=2, column=0, pady=5)
password_text = Label(text="Password:")
password_text.grid(row=3, column=0, pady=5)

# Entries
website_input = Entry(width=33)
website_input.grid(row=1, column=1)
website_input.focus()
email_username_input = Entry(width=52)
email_username_input.grid(row=2, column=1, columnspan=2)
email_username_input.insert(0, os.environ["MY_EMAIL"])
password_input = Entry(width=33)
password_input.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=44, command=add_inputs)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=15, command=website_exists)
search_button.grid(row=1, column=2)

window.mainloop()
