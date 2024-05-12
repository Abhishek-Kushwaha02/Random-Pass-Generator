
import string
from tkinter import *
import random
import pyperclip

def generate_password():
    password_field.delete(0, END)
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    all_chars = lowercase + uppercase + special_chars + digits

    password_length = int(length_input.get())

    if choice.get() == 1:
        password_field.insert(0, ''.join(random.sample(lowercase, password_length)))

    if choice.get() == 2:
        password_field.insert(0, ''.join(random.sample(lowercase + uppercase, password_length)))

    if choice.get() == 3:
        password_field.insert(0, ''.join(random.sample(all_chars, password_length)))

def copy_password():
    random_password = password_field.get()
    pyperclip.copy(random_password)

root = Tk()
root.config(bg='#1f242d')
choice = IntVar()
font = ('arial', 13, 'bold')

password_label = Label(root, text='Password Generator', font=('times new roman', 20, 'bold'), bg='#1f242d', fg='white')
password_label.grid(pady=10)

weak_radio_button = Radiobutton(root, text='Weak', value=1, variable=choice, font=font)
weak_radio_button.grid(pady=5)

medium_radio_button = Radiobutton(root, text='Medium', value=2, variable=choice, font=font)
medium_radio_button.grid(pady=5)

strong_radio_button = Radiobutton(root, text='Strong', value=3, variable=choice, font=font)
strong_radio_button.grid(pady=5)

length_label = Label(root, text='Password Length', font=font, bg='#1f242d', fg='white')
length_label.grid(pady=5)

length_input = Spinbox(root, from_=5, to_=18, width=5, font=font)
length_input.grid()

generate_button = Button(root, text='Generate', font=font, command=generate_password)
generate_button.grid(pady=5)

password_field = Entry(root, width=25, bd=2)
password_field.grid()

copy_button = Button(root, text='Copy', font=font, command=copy_password)
copy_button.grid(pady=5)

root.mainloop()
