from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import cryptocode

window = Tk()
window.title("Secret Notes")
window.config(pady=40,padx=40)

#adding image
img = ImageTk.PhotoImage(Image.open("secret.png"))
image_label = Label()
image_label.config(image= img, width=500, height=500)
image_label.pack()

#title label
title_label = Label()
title_label.config(text="Enter your title", pady=10)
title_label.pack()

#title entry
title_entry = Entry()
title_entry.config(width=25)
title_entry.pack()

#secret label
secret_label = Label()
secret_label.config(text="Enter your secret", pady=10)
secret_label.pack()

#secret text
secret_text = Text(width=35,height=20)
secret_text.pack()

#master key label
masterKey_label = Label()
masterKey_label.config(text="Enter master key", pady=10)
masterKey_label.pack()

#master key entry
masterKey_entry = Entry(width=25)
masterKey_entry.pack()


def save_note():
    if title_entry.get() == "" or \
            secret_text.get("1.0",END) == "" or \
            masterKey_entry.get() == "":
        messagebox.showinfo(message="Please enter all information")
    else:
        encoded = cryptocode.encrypt(secret_text.get("1.0",END), masterKey_entry.get())
        file = open("SecretNotes.txt", "a")
        file.write(title_entry.get()+"\n"+encoded+"\n\n")
        file.close()
        title_entry.delete(0,END)
        secret_text.delete("1.0",END)
        masterKey_entry.delete(0,END)

def decrypt_func():
    decoded = cryptocode.decrypt(secret_text.get("1.0",END), masterKey_entry.get())
    secret_text.delete("1.0",END)
    secret_text.insert(END, decoded)


#Save & Encrypt Button
save_button = Button(text="Save & Encrypt", pady=10,command=save_note)
save_button.pack()

#Decrypt Button
decrypt_button = Button(text="Decrypt", pady=10,command=decrypt_func)
decrypt_button.pack()



window.mainloop()