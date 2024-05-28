from tkinter import *

root = Tk()
root.geometry('500x500')
root.title("Login Me")
root.config(background="pink")

#label for username
user_name=Label(root,text = "Username").place(x=40, y=60)
user_name_entry_area= Entry(root,width=30).place(x=110,y=60)

#label for password
password=Label(root,text = "Password").place(x=40, y=90)
password_entry_area= Entry(root,width=30,show="*").place(x=110, y=90)

#Submit Button
btn = Button(root, text="Submit", bd='5', background="cyan", command=root.destroy).place(x=4, y=120)


root.mainloop()