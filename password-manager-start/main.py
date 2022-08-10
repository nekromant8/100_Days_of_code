import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]

    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    password_list += [random.choice(numbers) for _ in range(nr_symbols)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {website.title(): {
        "username": username,
        "password": password

    }}
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title='Attention!', message='Don\'t leave any fields empty!')
    else:
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            with open('data.json', 'w') as f:
                json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as f:

                json.dump(data, f, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

def search_password():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showwarning(title='Attention!', message='Don\'t leave any fields empty!')
    else:
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            messagebox.showwarning(title='Attention!', message='File with password data is not found')
        else:
            try:
                user_pwd = data[website.title()]
            except KeyError:
                messagebox.showwarning(title='Warning', message=f'Information about {website.title()} is not found in database')
            else:
                messagebox.showinfo(title=f'Userdata for the {website.title()}', message=f'Userdata for the {website.title()} is:\n'
                                                                                     f'Username: {user_pwd["username"]}\n'
                                                                                     f'Password: {user_pwd["password"]}')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)
# Label
website_label = Label()
website_label.config(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label()
username_label.config(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label()
password_label.config(text="Password:")
password_label.grid(column=0, row=3)

# Entry

website_entry = Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
username_entry = Entry(width=40)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(1, '@gmail.com')
password_entry = Entry(width=22, highlightthickness=0)
password_entry.grid(column=1, row=3)

# Button
search_button = Button(text='Search', width=6, command=search_password)
search_button.grid(column=2, row=1)

generate_button = Button(text="Generate password", width=15, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()
