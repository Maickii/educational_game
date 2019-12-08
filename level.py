import tkinter as tk
import sys
import random

# <root generated by tk.Tk()> <optional array of frames> <function to call next_frame is called, but before the frame is shown>
class frame:
	def __init__(self, root, frame_arr=None, func=None):
		self.widgets = []
		self.root = root
		self.hidden = False
		self.func=func
		self.frame_arr = frame_arr
		self.screen_width = self.root.winfo_screenwidth()
		self.screen_height = self.root.winfo_screenheight()
		if self.frame_arr is not None:
			self.frame_arr.append(self)
		else:
			self.func = None

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

	def generate_next_button(self, append=False):
		w = tk.Button(self.root, text="next", activebackground="khaki", bg="red",
			font="Times 32", command=self.next_frame)

		xpos = self.screen_width/2 - self.root.button_width/2
		ypos = self.screen_height/2 - 3*self.root.button_height/2

		w.place(x=self.screen_width/2 - self.root.button_width/2 + xpos, y=self.screen_height/2 - self.root.button_height/2 + ypos, width=self.root.button_width, height=self.root.button_height)
		w.pi = w.place_info()
		w.place_forget()
		if append:
			self.widgets.append(w)

		return w

	def next_frame(self):
		self.hide()
		if self.frame_arr is not None:
			self.frame_arr.pop()
			if len(self.frame_arr) > 0:
				if len(self.frame_arr) > 1 and self.frame_arr[len(self.frame_arr)-1].func is not None:
					self.frame_arr[len(self.frame_arr)-1].func()
				self.frame_arr[len(self.frame_arr)-1].show()

class choice(frame): #TODO
	def __init__(self, frame_arr, scores, time_bonus, root, question, answer1, answer2, answer3, answer4, correct):
		frame.__init__(self, root, frame_arr)
		self.scores = scores
		self.time_bonus = time_bonus
		w0 = tk.Label(root, text=question, font="Times 48", fg="red", bg=root.bg_color)
		w0.place(x=-100000, y=-100000)
		w0.update() # library wont give the actual width until you first call place and update
		label_width = w0.winfo_width()
		w0.place(x=self.screen_width/2 - label_width/2, y=self.screen_height/6)
		self.widgets.append(w0)
		self.var = tk.IntVar()
		self.var.set(-1)
		self.idx = 1 # button index
		self.correct = correct
		self.selected = False
		self.default_button(answer1, -self.screen_width/8, -self.root.button_height*2.5)
		self.default_button(answer2, self.screen_width/8, -self.root.button_height*2.5)
		self.default_button(answer3, -self.screen_width/8, self.root.button_height*1.25)
		self.default_button(answer4, self.screen_width/8, self.root.button_height*1.25)
		self.next_button = self.generate_next_button()
#self.default_button("next", self.screen_width/2 -self.root.button_width/2, self.screen_height/2 - 3*self.root.button_height/2, 0)
		self.hide()

	def default_button(self, txt, xpos, ypos, button_type=1):
		w = tk.Radiobutton(self.root, text=txt, activebackground="khaki", bg="blue",
				font="Times 32", #fg="white",
				indicatoron=0, variable=self.var, value=self.idx, command=self.selection_made)

		w.place(x=self.screen_width/2 - self.root.button_width/2 + xpos, y=self.screen_height/2 - self.root.button_height/2 + ypos, width=self.root.button_width, height=self.root.button_height)

		self.widgets.append(w)
		self.idx = self.idx + 1
		return w

	def next_frame(self):
		if len(self.frame_arr) <= 1:
			print("If you see this message it means you dont have a callback frame and you are probably seeing an empty screen")
		if self.correct == self.var.get():
			print("correct selection")
			self.scores.append(10)
		else:
			print("incorrect")
			self.scores.append(0)
		self.time_bonus.append(random.randint(0, 5)) #you weren't supposed to see this...
		super().next_frame()

	def selection_made(self):
		if self.selected == False:
			self.selected = True
			self.next_button.place(self.next_button.pi)
			self.widgets.append(self.next_button)

class menu_buttons(frame): #This is a generic class use to create main manu and other frames similar to the main menu
	def __init__(self, root, title, *argv, buttons=True, frame_arr=None, func=None):
		frame.__init__(self, root, frame_arr=frame_arr, func=func)
		i = -1.25 * 2
		w = tk.Label(self.root, text=title, font="Times 72 italic", fg="red", bg=self.root.bg_color)
		w.place(x=-100000, y=-100000)
		w.update() #stupid library wont give the actual width until you first call place and update
		label_width = w.winfo_width()
		w.place(x=self.screen_width/2 - label_width/2, y=self.screen_height/6)
		self.widgets.append(w)

		for arg in argv:
			if arg is not None:
				if tk.StringVar != type(arg):
					button_str = arg[0]
				else:
					button_str = ""
				color = "blue"
				fun = None
				if type(button_str) is not str:
					print("I dont know what type this is. should have been a string for the button. exiting.")
					sys.exit(0)
				if (tk.StringVar == type(arg) or type(arg) is str) and buttons == False:
					pass
				elif len(arg) == 1: #no-opt. just need it for the last else case at the bottom
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
					print("I dont know what type this is. arg length: " + str(len(arg)))
					sys.exit(0)
				if buttons:
					w = tk.Button(root, text=button_str, bg=color, font="Times 32", fg="white", command=fun)
					w.place(x=self.screen_width/2 - root.button_width/2, y=self.screen_height/2 + root.button_height*i, width=root.button_width, height=root.button_height)
				else:
					w = tk.Label(root, textvariable=arg, bg=root.bg_color, font="Times 32", fg="black")
					w.place(x=-100000, y=-100000)
					w.update() #stupid library wont give the actual width until you first call place and update
					label_width = 1000 #w.winfo_width()
					w.place(x=self.screen_width/2 - label_width/2, y=self.screen_height/2 + root.button_height*i, width=label_width, height=root.button_height)

				self.widgets.append(w)
			i = i + 1.25
			self.hide()

class grade4_levels():
	def __init__(self, root, callback_frame): #this behaves like a stack. the top of the stack is whats gets shown first, then the top of the stack gets poped off and the new top gets shown, etc
		self.frame_arr = []
		self.scores = []
		self.time_bonus = [] # TODO: add a bonus for quick answers
		self.frame_arr.append(callback_frame)
		self.scores_args = (tk.StringVar(), tk.StringVar(), tk.StringVar(),
						tk.StringVar(), tk.StringVar())
		self.scores_frame = menu_buttons(root, "Scores", *self.scores_args, buttons=False, frame_arr=self.frame_arr, func=self.update_scores)
		self.scores_frame.generate_next_button(append=True)

		grade4 = choice(self.frame_arr, self.scores, self.time_bonus, root, "What is the next number in the sequence?\n3, 6, 9, 12, 15", "5", "20", "18", "17", 3)
		choice(self.frame_arr, self.scores, self.time_bonus, root, "What is the next number in the sequence?\n3, 6, 9, 12, 15", "5", "30", "18", "13", 3)
		choice(self.frame_arr, self.scores, self.time_bonus, root, "What is the next number in the sequence?\n3, 6, 9, 12, 15", "7", "21", "18", "15", 3)
		choice(self.frame_arr, self.scores, self.time_bonus, root, "What is the next number in the sequence?\n3, 6, 9, 12, 15", "9", "23", "18", "19", 3)
		first = choice(self.frame_arr, self.scores, self.time_bonus, root, "What is the next number in the sequence?\n3, 6, 9, 12, 15", "3", "25", "18", "14", 3)
		first.show()

	def update_scores(self):
		if len(self.scores) != len(self.scores_args):
			print("Warning: the number of scores do not match the number of labels")
		size = min(len(self.scores), len(self.scores_args))
		for i in range(size):
			out = "Challenge #" + str(i) + " score: " + str(self.scores[i])
			if self.scores[i] != 0 and self.time_bonus[i] != 0:
				out += " + time bonus " + str(self.time_bonus[i])
			self.scores_args[i].set(out)
