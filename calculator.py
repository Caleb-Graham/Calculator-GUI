from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=20, font=("Merriweather", 30)) #borderwidth=5 (option)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)



def button_click(number):
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))


def button_clear():
	e.delete(0, END)


def button_add():
	first_number = e.get()
	global f_num
	global math
	f_num = float(first_number)
	math = "addition"
	e.delete(0, END)


def button_subtract():
	first_number = e.get()
	global f_num
	global math
	f_num = float(first_number)
	math = "subtraction"
	e.delete(0, END)


def button_multiply():
	first_number = e.get()
	global f_num
	global math
	f_num = float(first_number)
	math = "multiplication"
	e.delete(0, END)


def button_divide():
	first_number = e.get()
	global f_num
	global math
	f_num = float(first_number)
	math = "division"
	e.delete(0, END)


def button_equal():
	second_number = e.get()
	e.delete(0, END)

	if math == "addition":
		e.insert(0, f_num + float(second_number))

	if math == "subtraction":
		e.insert(0, f_num - float(second_number))

	if math == "multiplication":
		e.insert(0, f_num * float(second_number))

	if math == "division":
		e.insert(0, f_num / float(second_number))




# Define Buttons

button_1 = Button(root, text="1", padx=45, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=45, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=45, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=45, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=45, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=45, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=45, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=45, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=45, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=45, pady=20, command=lambda: button_click(0))

button_equal = Button(root, text="=", padx=45, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=33, pady=20, command=button_clear)

button_add = Button(root, text="+", padx=42, pady=20, command=button_add)
button_subtract = Button(root, text="-", padx=43, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=43, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=45, pady=20, command=button_divide)



# Put the buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1) # columnspan=2 (makes it span two columns)
button_equal.grid(row=4, column=2)

button_add.grid(row=4, column=3)
button_subtract.grid(row=3, column=3)
button_multiply.grid(row=2, column=3)
button_divide.grid(row=1, column=3)



# Gets the requested values of the height and widht.
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
 
# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/3 - windowHeight/2)	# dividing by 3 centered more
 
# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))



root.mainloop()

