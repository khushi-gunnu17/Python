# tkinter is distributed along with python software. It is a cross platform, stable, reliable and easy to learn package.
# Tkinter has a variety of commonly use GUI elements like Button, Labels, Menu, Text Area, etc. which can be used to build the interface. These elements are called Widget.

# --- Widgets --->
# Frame
# Label 
# Button
# CheckButton
# RadioButton
# Text
# Message (Multiple lines)
# Combo Box (Drop down list)
# List Box
# Scroll Bar
# Canvas (to draw something)
# Menu (File Menu, edit menu)











# from tkinter import Tk, Label
# root = Tk()
# l1 = Label(root, text = "Welcome to my Home.") 
# l1.pack()
# root.mainloop()

# l2 = Label(root, text = "Welcome Home")  
# l2.pack()









# import tkinter
# from tkinter import Tk, Button
# root = Tk()  

# root.geometry("400x400")
# root.title("Button")

# b1 = Button(root, text = "Press Me !", width = 25, command = root.destroy)
# b1.pack()


# def func() :
#     for i in range(6) :
#         print(i)

# b2 = Button(root, text = "Function", width = 25, command = func)   
# b2.pack()

# root.mainloop()












# Entry with button 



# import tkinter
# from tkinter import Tk, Entry, Button
# root = Tk()
# textBox = Entry(root)
# def func() :
#     print(textBox.get())

# b1 = Button(root, text = "save", command = func)
# textBox.pack()
# b1.pack()
# root.geometry("400x250")  
# root.title("Python_Class") 

# root.mainloop()











# import tkinter as tk
# root = tk.Tk()
# root.geometry("400x300")
# root.title("Python_class") 

# name_var = tk.StringVar()
# name_pass = tk.StringVar()

# username = tk.Label(root, text = "Username : ", font = ("arial", 16, "bold"), bg = "pink") 

# entryBox = tk.Entry(root, textvariable = name_var)           

# pass_name = tk.Label(root, text = "Password : ", font = ("arial", 16, "bold"))

# password = tk.Entry(root, textvariable = name_pass, show = "*")


# def submit() :
#     a = name_var.get()
#     b = name_pass.get()
#     print(a, b)  
#     name_var.set("")
#     name_pass.set("")

# sub_btn = tk.Button(root, text = "Submit", command = submit)
# username.grid(row = 0, column = 0)
# entryBox.grid(row = 0, column = 1)
# pass_name.grid(row = 1, column = 0)
# password.grid(row = 1, column = 1)
# sub_btn.grid(row = 2, column = 0)

# root.mainloop()










from tkinter import *
root = Tk()
root.geometry("400x300")
root.title("Python_class")

canvas = Canvas(root, width = 300, height = 300)

img = PhotoImage(file = 'priyanshi_home.png')

# coordinates and then anchor direction for the image
canvas.create_image(100, 100, anchor = CENTER, image = img)

canvas.pack()

root.mainloop()











# import tkinter as tk
# root = tk.Tk()
# root.title("Python_class")

# img = tk.PhotoImage(file = 'priyanshi_home.png')

# image_label = tk.Label(root, image = img)
# image_label.pack()
# root.mainloop()













































































# import tkinter as tk

# root = tk.Tk()

# root.geometry("400x300")
# root.title("Button Demo")

# button = tk.Button(root, text = 'Stop', width = 25, command = root.destroy)

# button.pack()

# root.mainloop()





# import tkinter as tk

# root = tk.Tk()

# root.geometry("400x400")
# root.title("Labels")

# label1 = tk.Label(root, text = "Welcome to my Home.")
# label1.pack()

# label2 = tk.Label(root, text = "Welcome to my Office.")
# label2.pack()

# root.mainloop()








# import tkinter as tk

# root = tk.Tk()

# root.geometry("400x400")
# root.title("Button")

# b1 = tk.Button(root, text = "Press Me!", width = 25, command = root.destroy)

# b1.pack()


# def func() :
#     for i in range(6) :
#         print(i)

# b2 = tk.Button(root, text = "Function execution", width = 30, command = func)

# b2.pack()

# root.mainloop()












# entry with button

# import tkinter as tk

# root = tk.Tk()

# root.geometry("400x300")
# root.title("Buttons")

# textBox = tk.Entry(root)

# def func() :
#     print(textBox.get())


# b1 = tk.Button(root, text = "Save", command = func)
# textBox.pack()
# b1.pack()

# root.mainloop()











# import tkinter as tk

# root = tk.Tk()

# root.geometry("400x300")
# root.title("Python_class")

# canvas = tk.Canvas(root, width = 300, height = 300)

# img = tk.PhotoImage(file = 'priyanshi_home.png')

# canvas.create_image(300, 300, image = img)

# canvas.pack()

# root.mainloop()









# import tkinter as tk

# root = tk.Tk()

# root.title("Class")

# img = tk.PhotoImage(file = 'priyanshi_home.png')

# image_label = tk.Label(root, image = img)

# image_label.pack()

# root.mainloop()















# import tkinter as tk

# root = tk.Tk()

# root.geometry("400x300")
# root.title("Python_class")

# canvas = tk.Canvas(root, width = 100, height = 100)

# canvas.pack()

# canvas_height = 20
# canvas_width = 100

# y = int(canvas_height / 2)

# canvas.create_line(0, y, canvas_width, y)       # x1, y1, to x2, y2
# canvas.create_line(0, y + 10, canvas_width, y + 10)       


# root.mainloop()












# checkButton


# import tkinter as tk

# root = tk.Tk()

# root.geometry("400x300")
# root.title("checkButton")

# var1 = tk.IntVar()

# checkbutton_male = tk.Checkbutton(root, text = 'Male', variable = var1)

# checkbutton_male.grid(row = 0, sticky = 'W')

# var2 = tk.IntVar()
# checkbutton_female = tk.Checkbutton(root, text = "Female", variable = var2)
# checkbutton_female.grid(row = 1, sticky = 'W')


# root.mainloop()














# import tkinter as tk

# root = tk.Tk()

# root.geometry("400x300")
# root.title("entry")

# first_name = tk.Label(root, text = "First Name : ")
# first_name.grid(row = 0)

# first_entry = tk.Entry(root)
# first_entry.grid(row = 0, column = 1)

# last_name = tk.Label(root, text = "Last Name : ")
# last_name.grid(row=1, column=0)

# last_entry = tk.Entry(root)
# last_entry.grid(row=1, column=1)

# root.mainloop()
















# import tkinter as tk

# root = tk.Tk()

# root.geometry("400x300")
# root.title("Python_class") 

# name_var = tk.StringVar()
# name_pass = tk.StringVar()

# username = tk.Label(root, text = "Username : ", font = ("arial", 16, "bold"))

# entryBox = tk.Entry(root, textvariable = name_var)

# pass_name = tk.Label(root, text = "Password : ", font = ("arial", 16, "bold"))

# password = tk.Entry(root, textvariable = name_pass, show = "*")


# def submit() :
#     name = name_var.get()
#     pass_value = name_pass.get()

#     print(f"Name : {name} and his/her password is : {pass_value}")
#     name_var.set("")
#     name_pass.set("")

# sub_btn = tk.Button(root, text = "Submit", command = submit)

# username.grid(row = 0, column = 0)
# entryBox.grid(row = 0, column = 1)
# pass_name.grid(row = 1, column = 0)
# password.grid(row = 1, column = 1)
# sub_btn.grid(row = 2, column = 0)

# root.mainloop()