from tkinter import *
from tkinter import messagebox
from random import choice,shuffle,randint
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    pass_letters=[choice(letters) for _ in range(randint(8,10))]
    pass_symbols=[choice(symbols) for _ in range(randint(2,4))]
    pass_numbers=[choice(numbers) for _ in range(randint(2,4))]
    password_list=pass_letters+pass_symbols+pass_numbers
    shuffle(password_list)
    password="".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    web=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    new_data={web:
                  {
                      "Email":email,
                      "Password":password
                  }}
    if len(web)==0 or len(email)==0 or len(password)==0:
        messagebox.showinfo(title="Website",message="Please make sure you haven't left any field empty")
    else:
        try:
            with open("data.json","r") as data_file:
                data=json.load(data_file)

        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data, indent=4)
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0, END)
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    website=website_entry.get()
    try:
        with open("data.json","r") as data_file:
           data= json.load(data_file)
    except:
        messagebox.showinfo(title="Error",message="No data file found!")
    else:
        if website in data:
            e=data[website]["Email"]
            p=data[website]["Password"]
            messagebox.showinfo(title=f"{website}",message=f"Email:{e}\nPassword:{p}")
        else:
            messagebox.showinfo(message="No password saved for {website}")
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Generator")
window.config(padx=50,pady=50,bg="#F5F5F7")

canvas=Canvas(width=200,height=200,bg="#F5F5F7",highlightthickness=0)
image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image)
canvas.grid(row=0,column=1)
web=Label(text="Website:")
web.grid(row=1,column=0)
email=Label(text="Email/Username:")
email.grid(row=2,column=0)
password=Label(text="Password:")
password.grid(row=3,column=0)


website_entry=Entry(width=26)
website_entry.grid(row=1,column=1)
website_entry.focus()
search_button=Button(text="Search",width=13,command=search)
search_button.grid(row=1,column=2)
email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"manvithamili1@gmail.com")
password_entry=Entry(width=26)

password_entry.grid(row=3,column=1)
generate=Button(text="Genarate Password",command=generate_password)
generate.grid(row=3,column=2)
add=Button(text="Add",width=36,command=save_password)
add.grid(row=4,column=1,columnspan=2)




window.mainloop()