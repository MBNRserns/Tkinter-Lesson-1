# import everything from tkinter module
from tkinter import *

# create a tkinter window
root = Tk()

#output window size
root.geometry('500x500')

#create a Button
btn = Button(root, text="1", bd='5', background="cyan", command=root.destroy)

# Set the position of button on the top of the window.
#try side = bottom, right, left, top
btn.pack(side="top")

root.mainloop()

# import everything from tkinter module
from tkinter import *

# create a tkinter window
root = Tk()

#output window size
root.geometry('500x500')

#create a Button
btn = Button(root, text="2", bd='5', background="cyan", command=root.destroy)

# Set the position of button on the top of the window.
#try side = bottom, right, left, top
btn.pack(side="bottom")

root.mainloop()

# import everything from tkinter module
from tkinter import *

# create a tkinter window
root = Tk()

#output window size
root.geometry('500x500')

#create a Button
btn = Button(root, text="3", bd='5', background="cyan", command=root.destroy)

# Set the position of button on the top of the window.
#try side = bottom, right, left, top
btn.pack(side="left")

root.mainloop()

# import everything from tkinter module
from tkinter import *

# create a tkinter window
root = Tk()

#output window size
root.geometry('500x500')

#create a Button
btn = Button(root, text="4", bd='5', background="cyan", command=root.destroy)

# Set the position of button on the top of the window.
#try side = bottom, right, left, top
btn.pack(side="right")

root.mainloop()

