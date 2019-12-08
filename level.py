import tkinter as tk
import sys

class frame:
	def __init__(self, root):
		self.widgets = []
		self.root = root
		self.hidden = False
		self.screen_width = self.root.winfo_screenwidth()
		self.screen_height = self.root.winfo_screenheight()

	def hide(self):
		for w in self.widgets:
			if not w.place_info():
				continue # widget is already hidden
			w.pi = w.place_info()
			w.place_forget()

	def show(self):
		for w in self.widgets:
			w.place(w.pi)

	def toggle(self):
		if self.hidden:
			self.show()
			self.hidden = False
		else:
			self.hide()
			self.hidden = True

class choice(frame): #TODO
	def __init__(self, frame_arr, root, question, answer1, answer2, answer3, answer4, correct):
		frame.__init__(self, root)
		self.append_self(frame_arr)
		w0 = tk.Label(root, text=question, font="Times 48", fg="red", bg=root.bg_color)
		w0.place(x=-100000, y=-100000)
		w0.update() #stupid library wont give the actual width until you first call place and update
		label_width = w0.winfo_width()
		w0.place(x=self.screen_width/2 - label_width/2, y=self.screen_height/6)
		self.widgets.append(w0)
		self.var = -1
		self.i = 0
		self.default_button(answer1, -self.screen_width/8, -self.root.button_height*2.5)
		self.default_button(answer2, self.screen_width/8, -self.root.button_height*2.5)
		self.default_button(answer3, -self.screen_width/8, self.root.button_height*1.25)
		self.default_button(answer4, self.screen_width/8, self.root.button_height*1.25)
		self.default_button("next", self.screen_width/2 -self.root.button_width/2, self.screen_height/2 - 3*self.root.button_height/2, 0)
		self.hide()

	def default_button(self, txt, xpos, ypos, button_type=1):
		if button_type:
			w = tk.Radiobutton(self.root, text=txt, activebackground="khaki", bg="blue", 
				font="Times 32", #fg="white", 
				indicatoron=0, variable=self.var, value=self.i)
		else:
			w = tk.Button(self.root, text=txt, activebackground="khaki", bg="red", 
				font="Times 32", command=self.next_frame)

		w.place(x=self.screen_width/2 - self.root.button_width/2 + xpos, y=self.screen_height/2 - self.root.button_height/2 + ypos, width=self.root.button_width, height=self.root.button_height)
		self.widgets.append(w)
		self.i = self.i + 1
		return w

	def append_self(self, frame_arr):
		self.frame_arr = frame_arr
		self.frame_arr.append(self)

	def next_frame(self):
		if len(self.frame_arr) <= 1:
			print("If you see this message it means you dont have a callback frame and you are probably seeing an empty screen")
		self.hide()
		self.frame_arr.pop()
		if len(self.frame_arr) > 0:
			self.frame_arr[len(self.frame_arr)-1].show()

class menu_buttons(frame): #This is a generic class use to create main manu and other frames similar to the main menu
	def __init__(self, root, title, *argv):
		frame.__init__(self, root)
		i = -1.25
		w = tk.Label(self.root, text=title, font="Times 72 italic", fg="red", bg=self.root.bg_color)
		w.place(x=-100000, y=-100000)
		w.update() #stupid library wont give the actual width until you first call place and update
		label_width = w.winfo_width()
		w.place(x=self.screen_width/2 - label_width/2, y=self.screen_height/6)
		self.widgets.append(w)

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
				w.place(x=self.screen_width/2 - root.button_width/2, y=self.screen_height/2 + root.button_height*i, width=root.button_width, height=root.button_height)
				self.widgets.append(w)
			i = i + 1.25
		self.hide()

class grade4_levels():
	def __init__(self, root, callback_frame):
		self.frame_arr = []
		self.frame_arr.append(callback_frame)
		grade4 = choice(self.frame_arr, root, "What is the next number in the sequence?\n3, 6, 9, 12, 15", "5", "20", "18", "17", 3)
		choice(self.frame_arr, root, "What is the next number in the sequence?\n3, 6, 9, 12, 15", "5", "30", "18", "13", 3)
		choice(self.frame_arr, root, "What is the next number in the sequence?\n3, 6, 9, 12, 15", "7", "21", "18", "15", 3)
		choice(self.frame_arr, root, "What is the next number in the sequence?\n3, 6, 9, 12, 15", "9", "23", "18", "19", 3)
		first = choice(self.frame_arr, root, "What is the next number in the sequence?\n3, 6, 9, 12, 15", "3", "25", "18", "14", 3)
		first.show()

