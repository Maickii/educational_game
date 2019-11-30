import tkinter as tk
import sys

class frame:
	def __init__(self, root):
		self.widgets = []
		self.root = root
		self.hidden = False

	def hide(self):
		for w in self.widgets:
			w.pi = w.place_info()
			w.place_forget()

	def show(self):
		for w in self.widgets:
			w.pi = w.place(w.pi)

	def toggle(self):
		print(self)
		if self.hidden:
			self.show()
			self.hidden = False
		else:
			self.hide()
			self.hidden = True

class choice(frame): #TODO
	def __init__(self, root):
		frame.__init__(self, root)
		self.w6 = tk.Button(self.root, text="Exit Game", bg="red", font="Times 32", fg="white")
		self.w6.place(x=200, y=200, width=200, height=100)
		self.w7 = tk.Button(self.root, text="Toggle", bg="red", font="Times 32", fg="white", command=self.toggle)
		self.w7.place(x=400, y=400, width=200, height=100)
		self.widgets.append(self.w6)
		print("hello there!")

class menu_buttons(frame): #This is a generic class use to create main manu and other frames similar to the main menu
	def __init__(self, root, *argv):
		frame.__init__(self, root)
		screen_width = root.winfo_screenwidth()
		screen_height = root.winfo_screenheight()
		i = -1.25
		print(len(argv))
		for arg in argv:
			if arg is not None:
				button_str = arg[0]
				color = "blue"
				fun = None
				if type(button_str) is not str:
					print("I dont know what type this is. should have been a string for the button. exiting.")
					sys.exit(0)
				if len(arg) == 1: #no-opt. just need it for the last else case at the bottom
					pass
				elif len(arg) == 2:
					if arg[1] is str:
						color = arg[1]
					elif callable(arg[1]):
						fun = arg[1]
					else:
						print("I dont know what type this is. should have been a string for color or a callback function. exiting.")
						sys.exit(0)
				elif len(arg) == 3:
					if type(arg[1]) is not str or not callable(arg[2]):	
						print("I dont know what type this is. should have been a string for color and a callback function. exiting.")
						sys.exit(0)
					color = arg[1]
					fun = arg[2]
				else:
					print("I dont know what type this is.")
					sys.exit(0)
				w = tk.Button(root, text=button_str, bg=color, font="Times 32", fg="white", command=fun)
				w.place(x=screen_width/2 - root.button_width/2, y=screen_height/2 + root.button_height*i, width=root.button_width, height=root.button_height)
				self.widgets.append(w)
			print("i: " + str(i))
			print("height pos: " + str(screen_height/2 - root.button_height*i))
			print("screen_height: " + str(screen_height) + " root.button_height: " + str(root.button_height))
			i = i + 1.25
		#self.hide()
