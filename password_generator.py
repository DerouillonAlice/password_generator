import string
from random import randint,choice
from tkinter import *

def generate_password():
    password_min = 6
    password_max = 20
    all_chars = string.ascii_letters + string.punctuation + string.digits

    password = "".join(choice(all_chars)for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)   

#creer fenetre
window = Tk()
window.title("Password Generator")
window.geometry("720x480")
# window.iconbitmap("favicon.ico")
window.config(background="#6c5eba")

#creer frame principale
frame = Frame(window,bg="#6c5eba")

#creation d'image
width = 300
height = 300
image = PhotoImage(file="padlock.png").zoom(13).subsample(32)
canvas = Canvas(frame, width=width, height=height, bg="#6c5eba", bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

#creer une sous boite
right_frame = Frame(frame, bg="#6c5eba")

#creer titre
label_title = Label(right_frame, text="Password", font=("Arial",20),bg="#6c5eba",fg="white")
label_title.pack()

#creer un champs/entrée/input
password_entry = Entry(right_frame, font=("Arial",20),bg="#6c5eba",fg="white")
password_entry.pack()

#creer un bouton
generate_password_button= Button(right_frame,text="Generate", font=("Arial",15),bg="#6c5eba",fg="white", command=generate_password)
generate_password_button.pack(fill=X)


#on place la sous boite a droite de la frame principale
right_frame.grid(row=0, column=1, sticky=W)

#afficher frame
frame.pack(expand=YES)

#creation d'une barre de menu
menu_bar = Menu(window)

#creer un premier menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)


#configurer notre fenetre pour ajouter menu bar
window.config(menu=menu_bar)

#afficher la fenetre
window.mainloop()