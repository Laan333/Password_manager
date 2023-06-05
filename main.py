from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)


def generate_password():

    password_entry.delete(0,END)
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    random_letters = [random.choice(letters[letter]) for letter in range(nr_letters)]
    random_symbols = [random.choice(symbols[symb]) for symb in range(nr_symbols)]
    random_numbers = [random.choice(numbers[num]) for num in range(nr_numbers)]

    all_pass = (random_numbers + random_letters + random_symbols)
    random.shuffle(all_pass)
    password = "".join(all_pass)
    password_entry.insert(0,f"{password}")
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def take_data():
    global empty_fields
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please dont leave any fields empty")
    else:
        is_ok=messagebox.askokcancel(title=f"{website}",
                               message=f"These are the details entered:\nEmail:{email}\n"
                                       f"Password:{password}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", mode="a", encoding="utf-8") as file:
                file.write(f"{website}|{email}|{password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.minsize(width=300,height=300)
window.configure(padx=20,pady=20)


canvas = Canvas(width=200, height=189)
photo_lock = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=photo_lock)
canvas.grid(row=0,column=1)
frame = Frame(window)
frame.grid(row=1, column=1, sticky=EW)

label_website = Label(frame,text="Website:")
label_website.grid(row=1,column=0)

website_entry = Entry(frame,width=35)
website_entry.grid(row=1,column=1,columnspan=2,sticky=W)
website_entry.focus() #focusing on website entry

label_email = Label(frame,text="Email/Username:")
label_email.grid(row=2, column=0)

email_entry = Entry(frame,width=35)
email_entry.grid(row=2,column=1,columnspan=2,sticky=W)
email_entry.insert(END, "example@email.ru")

label_password = Label(frame,text="Password:", width=21)
label_password.grid(row=3,column=0,sticky=W)

password_entry = Entry(frame,width=21)
password_entry.grid(row=3, column=1,sticky=W)

button_generate = Button(frame,text="Generate Password", command=generate_password)
button_generate.grid(row=3, column=2,sticky=W)

button_add = Button(frame,text="Add",width=36, command=take_data)
button_add.grid(row=4, column=1,columnspan=2,sticky=W)



window.mainloop()