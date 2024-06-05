import random
from tkinter import *
from tkinter import messagebox
import json


def fun_random_pass():
    index = 0
    abcd = ["a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G", "h", "H", "i", "I", "j", "J", "k", "K", "l", "L", "m", "M", "n", "N", "o", "O", "p", "P", "q", "Q", "r", "R", "s", "S", "t", "T", "u", "U", "v", "V", "w", "W", "x", "X", "y", "Y", "z", "Z"]
    caracteres_especiais = ['!', '@', '#', '$', '%', '^', '&', '*','-','+','|', ';', ':','<', '>', '/', '?', '`', '~']
    pass_list = [";;" for x in range(18)]
    pass_list = [";;" for x in range(18)]
    while ";;" in pass_list:
        if index<5:
            rand_pos = random.randint(0,len(pass_list)-1)
            if pass_list[rand_pos] == ";;":
                pass_list[rand_pos] = random.randint(1,9)
                index += 1
        elif 5<=index<13:
            rand_pos = random.randint(0,len(pass_list)-1)
            if pass_list[rand_pos] == ";;" and pass_list[rand_pos].isalnum() == False:
                pass_list[rand_pos] = abcd[(random.randint(0, (len(abcd)-1)))]
                index += 1
        else:
            rand_pos = random.randint(0, len(pass_list)-1)
            if pass_list[rand_pos] == ";;" and pass_list[rand_pos].isalnum() == False and pass_list[rand_pos].isalpha() == False:
                pass_list[rand_pos] = caracteres_especiais[(random.randint(0, (len(caracteres_especiais)-1)))]
    final_list = "".join([str(x) for x in pass_list])
    password.delete(0, END)
    password.insert(0,final_list)


def senhas_get():
    global text
    new_data = {
        f"{website.get()}": {
            "email": f"{email.get()}",
            "password": f"{password.get()}",
        }
    }
    if password.get() != "" and website.get() != "" and email.get() != "":
        is_ok = messagebox.askokcancel(title=website.get(),message=f"These are the details entered: \nEmail: {email.get()} \nPassword: {password.get()} \nIs it okay to save?")
        if is_ok:
                try:
                    with open("data.json", 'r') as data_file:
                        data = json.load(data_file)
                        data.update(new_data)
                    with open("data.json", 'w') as data_file:
                        json.dump(data, data_file, indent=4)
                except json.decoder.JSONDecodeError:
                    with open("data.json", 'w') as data_file:
                        json.dump(new_data, data_file, indent=4)
                finally:
                    website.delete(0, END)
                    password.delete(0, END)
                    text["text"] = "Senha enviada"

    else:
        text["text"] = "Preencha todos os campos para adicionar a senha"

def senhas_read():
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        if f"{website.get()}" in data:
            messagebox.showinfo(title=website.get(),message=f"These are the password details: \nEmail: {data[website.get()]["email"]} \nPassword: {data[website.get()]["password"]}")
        else:
            messagebox.showinfo(title="ERROR",message="The website entered is not in the system")



window = Tk()
window.title("Password Manager")
window.config(width=800, height=600)

canvas = Canvas(width=800, height=600)
img = PhotoImage(file="logo.png")
canvas.create_image(300,225,image=img)
canvas.place(x=110,y=-50)

website = Entry(width=30)
website.insert(END,string="")
website.focus()
website.place(x=250,y=350)
Label(text="Website:", font=("Courier",12)).place(x=145,y=348)
search_button = Button(text="Search Password",width=22, command=senhas_read)
search_button.place(x=450,y=347)

email = Entry(width=60)
email.insert(END,string="fernandopiccinini12@gmail.com")
Label(text="Email/Username:", font=("Courier",12)).place(x=76,y=398)
email.place(x=250,y=400)

password = Entry(width=30)
password.insert(END,string="")
password.place(x=250,y=450)
Label(text="Password:", font=("Courier",12)).place(x=136,y=448)
password_button = Button(text="Generate Password",width=22, command=fun_random_pass)
password_button.place(x=450,y=447)

text = Label(text="", font=("Courier",12))
text.place(x=244,y=550)

add_button = Button(text="add",width=50, command=senhas_get)
add_button.place(x=250,y=500)





























window.mainloop()