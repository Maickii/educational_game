import tkinter as tk
from level import *

class Game:
	def __init__(self):
		self.init_globals()
		#grade4_levels(self.root)
		main_menu_args = (("Grade 1", self.level4_valid), ("Grade 2", self.level4_valid), ("Grade 3", self.level4_valid),
					  ("Grade 4", self.level4_valid), (None), ("About", "red", self.about), ("Exit Game", "red", quit))
		self.main_menu_frame = menu_buttons(self.root, "ArithMagic!", *main_menu_args)
		self.all_frames = [self.main_menu_frame]
		self.main_menu_frame.show()
		tk.mainloop()

	def init_globals(self):
		self.root = tk.Tk()
		self.root.attributes("-fullscreen", True)
		self.root.bg_color='#dccdc7'
		self.root.configure(background=self.root.bg_color)
		self.screen_width = self.root.winfo_screenwidth()
		self.screen_height = self.root.winfo_screenheight()
		self.root.button_width=350
		self.root.button_height=45

		self.menu_widgets = []
		self.about_widgets = []
		self.level4_widgets = []

		self.about_text = "Developed by Michael Santana, Justin Dom, Liliana Byan, Michael Batbouta"
		self.score = 0
		self.stopwatch = 0
		self.score_var_obj = tk.StringVar()
		self.score_var_obj.set('Score: ' + str(self.score))
		self.watch_var_obj = tk.StringVar()
		self.watch_var_obj.set('time: ' + str(self.stopwatch) + ' seconds')
		self.playing = False

	def hide_all(self):
		for aw in self.about_widgets:
			aw.pi = aw.place_info()
			aw.place_forget()
		for l4w in self.level4_widgets:
			l4w.pi = l4w.place_info()
			l4w.place_forget()
		for frame in self.all_frames:
			frame.hide()

	def show_main(self):
		self.hide_all()
		self.main_menu_frame.show()
		self.playing = False
	
	def about(self):
		self.hide_all()

		w1 = tk.Label(self.root, text="About", font="Times 72", fg="red", bg=self.root.bg_color)
		w1.place(x=-100000, y=-100000)
		w1.update() #stupid library wont give the actual width until you first call place and update
		label_width = w1.winfo_width()
		w1.place(x=self.screen_width/2 - label_width/2, y=self.screen_height/6)
		w2 = tk.Button(self.root, text="Back", bg="red", font="Times 32", fg="white", command=self.show_main)
		w2.place(x=self.screen_width/2 - self.root.button_width/2, y=self.screen_height/2 + self.root.button_height*6.25, width=self.root.button_width, height=self.root.button_height)
		w3 = tk.Label(self.root, text=self.about_text, font="Times 16", fg="black", bg=self.root.bg_color)
		w3.place(x=self.screen_width/2 - self.root.button_width, y=self.screen_height/2 - self.root.button_height*1.25, width=self.root.button_width*2, height=self.root.button_height)
		self.about_widgets = [w1, w2, w3]
	
	def correct(self):
		self.score = self.score + 10
		self.score_var_obj.set('Score: ' + str(self.score))
	
	def wrong(self):
		self.score = self.score - 5
		if self.score < 0:
			self.score = 0
		self.score_var_obj.set('Score: ' + str(self.score))
	
	def update_watch(self):
		if self.playing:
			self.stopwatch = self.stopwatch + 1
			self.watch_var_obj.set('time: ' + str(self.stopwatch) + ' seconds')
			self.root.after(1000, self.update_watch)
	
	def level4(self):
		pass

	def level4_valid(self):
		self.main_menu_frame.hide()
		grade4_levels(self.root, self.main_menu_frame)

	def level4t(self): #TODO this was a big copy paste from the start_menu_buttons. make sure everything is correct
		self.playing = True
		self.stopwatch = 0
		self.hide_all()
		w0 = tk.Label(self.root, text="What is the next number in the sequence?\n3, 6, 9, 12, 15", font="Times 48", fg="red", bg=self.root.bg_color)
		w0.place(x=-100000, y=-100000)
		w0.update() #stupid library wont give the actual width until you first call place and update
		label_width = w0.winfo_width()
		w0.place(x=self.screen_width/2 - label_width/2, y=self.screen_height/6)
		w1 = tk.Radiobutton(self.root, text="5", bg="blue", font="Times 32", fg="white", command=self.wrong)
		w1.place(x=self.screen_width/2 - self.root.button_width/2, y=self.screen_height/2 - self.root.button_height*1.25, width=self.root.button_width, height=self.root.button_height)
		w2 = tk.Radiobutton(self.root, text="20", bg="blue", font="Times 32", fg="white", command=self.wrong)
		w2.place(x=self.screen_width/2 - self.root.button_width/2, y=self.screen_height/2, width=self.root.button_width, height=self.root.button_height)
		w3 = tk.Radiobutton(self.root, text="18", bg="blue", font="Times 32", fg="white", command=self.correct)
		w3.place(x=self.screen_width/2 - self.root.button_width/2, y=self.screen_height/2 + self.root.button_height*1.25, width=self.root.button_width, height=self.root.button_height)
		w4 = tk.Radiobutton(self.root, text="17", bg="blue", font="Times 32", fg="white", command=self.wrong)
		w4.place(x=self.screen_width/2 - self.root.button_width/2, y=self.screen_height/2 + self.root.button_height*2.5, width=self.root.button_width, height=self.root.button_height)
		w5 = tk.Button(self.root, text="Back", bg="red", font="Times 32", fg="white", command=self.show_main)
		w5.place(x=self.screen_width/2 - self.root.button_width/2, y=self.screen_height/2 + self.root.button_height*6.25, width=self.root.button_width, height=self.root.button_height)
		w6 = tk.Label(self.root, textvariable=self.score_var_obj, bg="red", font="Times 32", fg="white")
		w6.place(x=0, y=0, width=self.root.button_width, height=self.root.button_height)
		w7 = tk.Label(self.root, textvariable=self.watch_var_obj, bg="red", font="Times 32", fg="white")
		w7.place(x=0, y=self.root.button_height, width=self.root.button_width, height=self.root.button_height)
	
		self.root.after(1000, self.update_watch)
		self.level4_widgets = [w0, w1, w2, w3, w4, w5, w6, w7]

def main():
	game = Game()

if __name__=="__main__":
    main()
