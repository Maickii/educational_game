import tkinter as tk
from level import *

root = tk.Tk()
root.attributes("-fullscreen", True)
bg_color='#dccdc7'
root.configure(background=bg_color)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
button_width=400
button_height=50
root.button_width=400
root.button_height=50

menu_widgets = []
about_widgets = []
level4_widgets = []

about_text = "Developed by Michael Santana, Justin Dom, Liliana Byan, Michael Batbouta"
score = 0
stopwatch = 0
score_var_obj = tk.StringVar()
score_var_obj.set('Score: ' + str(score))
watch_var_obj = tk.StringVar()
watch_var_obj.set('time: ' + str(stopwatch) + ' seconds')
playing = False

def game_title():
	global menu_widgets
	w = tk.Label(root, text="ArithMagic!", font="Times 72 italic", fg="red", bg=bg_color)
	w.place(x=-100000, y=-100000)
	w.update() #stupid library wont give the actual width until you first call place and update
	label_width = w.winfo_width()
	w.place(x=screen_width/2 - label_width/2, y=screen_height/6)
	menu_widgets.append(w)

def show_main():
	global playing
	for aw in about_widgets:
		aw.pi = aw.place_info()
		aw.place_forget()
	for l4w in level4_widgets:
		l4w.pi = l4w.place_info()
		l4w.place_forget()
	for mw in menu_widgets:
		mw.place(mw.pi)
	playing = False

def about():
	global about_widgets
	for w in menu_widgets:
		w.pi = w.place_info()
		w.place_forget()

	w1 = tk.Label(root, text="About", font="Times 72", fg="red", bg=bg_color)
	w1.place(x=-100000, y=-100000)
	w1.update() #stupid library wont give the actual width until you first call place and update
	label_width = w1.winfo_width()
	w1.place(x=screen_width/2 - label_width/2, y=screen_height/6)
	w2 = tk.Button(root, text="Back", bg="red", font="Times 32", fg="white", command=show_main)
	w2.place(x=screen_width/2 - button_width/2, y=screen_height/2 + button_height*6.25, width=button_width, height=button_height)
	w3 = tk.Label(root, text=about_text, font="Times 16", fg="black", bg=bg_color)
	w3.place(x=screen_width/2 - button_width, y=screen_height/2 - button_height*1.25, width=button_width*2, height=button_height)
	about_widgets = [w1, w2, w3]

def correct():
	global score
	global score_var_obj
	score = score + 10
	score_var_obj.set('Score: ' + str(score))

def wrong():
	global score
	global score_var_obj
	score = score - 5
	if score < 0:
		score = 0
	score_var_obj.set('Score: ' + str(score))

def update_watch():
	if playing:
		global stopwatch
		stopwatch = stopwatch + 1
		global watch_var_obj
		watch_var_obj.set('time: ' + str(stopwatch) + ' seconds')
		root.after(1000, update_watch)

def level4(): #TODO this was a big copy paste from the start_menu_buttons. make sure everything is correct
	global playing
	playing = True
	global stopwatch
	stopwatch = 0
	global level4_widgets
	for w in menu_widgets:
		w.pi = w.place_info()
		w.place_forget()
	w0 = tk.Label(root, text="What is the next number in the sequence?\n3, 6, 9, 12, 15", font="Times 48", fg="red", bg=bg_color)
	w0.place(x=-100000, y=-100000)
	w0.update() #stupid library wont give the actual width until you first call place and update
	label_width = w0.winfo_width()
	w0.place(x=screen_width/2 - label_width/2, y=screen_height/6)
	w1 = tk.Radiobutton(root, text="5", bg="blue", font="Times 32", fg="white", command=wrong)
	w1.place(x=screen_width/2 - button_width/2, y=screen_height/2 - button_height*1.25, width=button_width, height=button_height)
	w2 = tk.Radiobutton(root, text="20", bg="blue", font="Times 32", fg="white", command=wrong)
	w2.place(x=screen_width/2 - button_width/2, y=screen_height/2, width=button_width, height=button_height)
	w3 = tk.Radiobutton(root, text="18", bg="blue", font="Times 32", fg="white", command=correct)
	w3.place(x=screen_width/2 - button_width/2, y=screen_height/2 + button_height*1.25, width=button_width, height=button_height)
	w4 = tk.Radiobutton(root, text="17", bg="blue", font="Times 32", fg="white", command=wrong)
	w4.place(x=screen_width/2 - button_width/2, y=screen_height/2 + button_height*2.5, width=button_width, height=button_height)
	w5 = tk.Button(root, text="Back", bg="red", font="Times 32", fg="white", command=show_main)
	w5.place(x=screen_width/2 - button_width/2, y=screen_height/2 + button_height*6.25, width=button_width, height=button_height)
	w6 = tk.Label(root, textvariable=score_var_obj, bg="red", font="Times 32", fg="white")
	w6.place(x=0, y=0, width=button_width, height=button_height)
	w7 = tk.Label(root, textvariable=watch_var_obj, bg="red", font="Times 32", fg="white")
	w7.place(x=0, y=button_height, width=button_width, height=button_height)

	root.after(1000, update_watch)
	level4_widgets = [w0, w1, w2, w3, w4, w5, w6, w7]

def start_menu_buttons():
	global menu_widgets
	w1 = tk.Button(root, text="Grade 1", bg="blue", font="Times 32", fg="white", command=level4)
	w1.place(x=screen_width/2 - button_width/2, y=screen_height/2 - button_height*1.25, width=button_width, height=button_height)
	w2 = tk.Button(root, text="Grade 2", bg="blue", font="Times 32", fg="white", command=level4)
	w2.place(x=screen_width/2 - button_width/2, y=screen_height/2, width=button_width, height=button_height)
	w3 = tk.Button(root, text="Grade 3", bg="blue", font="Times 32", fg="white", command=level4)
	w3.place(x=screen_width/2 - button_width/2, y=screen_height/2 + button_height*1.25, width=button_width, height=button_height)
	w4 = tk.Button(root, text="Grade 4", bg="blue", font="Times 32", fg="white", command=level4)
	w4.place(x=screen_width/2 - button_width/2, y=screen_height/2 + button_height*2.5, width=button_width, height=button_height)
	w5 = tk.Button(root, text="About", bg="red", font="Times 32",fg="white", command=about)
	w5.place(x=screen_width/2 - button_width/2, y=screen_height/2 + button_height*5, width=button_width, height=button_height)
	w6 = tk.Button(root, text="Exit Game", bg="red", font="Times 32", fg="white", command=quit)
	w6.place(x=screen_width/2 - button_width/2, y=screen_height/2 + button_height*6.25, width=button_width, height=button_height)
	menu_widgets.extend([w1,w2,w3,w4,w5,w6])

def main():
	game_title()
	#start_menu_buttons()
	main_menu_args = (("Grade 1", level4), ("Grade 2", level4), ("Grade 3", level4),
					  ("Grade 4", level4), (None), ("About", "red", about), ("Exit Game", "red", quit))
	mylevel = menu_buttons(root, *main_menu_args)
	tk.mainloop()

if __name__=="__main__":
    main()
