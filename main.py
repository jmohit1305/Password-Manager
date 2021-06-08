from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    input3.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char
    password = "".join(password_list)

    pyperclip.copy(password)
    input3.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website_name = input1.get()
    email = input2.get()
    password = input3.get()

    if not website_name.strip() or not email.strip() or not password.strip():
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:

        result = messagebox.askyesno(title=website_name,
                                     message=f"Email: {email}\nPassword: {password}\n Is it ok to save?")
        if result:
            with open("data.txt", "a") as file:
                file.write(f"{website_name} | {email} | {password}\n")
                input1.delete(0, END)
                input3.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# website:
label1 = Label(text="Website:")
label1.grid(column=0, row=1, pady=2)
input1 = Entry(width=52)
input1.grid(row=1, column=1, columnspan=2, pady=5)
input1.focus()

# email/username:
label2 = Label(text="Email/Username:")
label2.grid(column=0, row=2, pady=2)
input2 = Entry(width=52)
input2.grid(row=2, column=1, columnspan=2, pady=2)
input2.insert(0, "jxmay@gmail.com")

# password:
label3 = Label(text="Password:")
label3.grid(column=0, row=3, pady=2)
input3 = Entry(width=32)
input3.grid(row=3, column=1, pady=2)
generate_button = Button(text="Generate Password", bd=0, bg="white", command=generate_password)
generate_button.grid(row=3, column=2, pady=2, padx=8)

# add button
add_button = Button(text="Add", bg="white", width=44, bd=0, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, pady=2)

window.mainloop()
