import tkinter as tk

root = tk.Tk()
text = tk.StringVar()

def main():
	input_text = update_input()
	text.set(input_text)

	label = tk.Label(root, bd=8, wraplength=350, textvariable=text, heigh=5, font=('Helvetica 25 bold'))
	label.pack()

	root.focus_set()
	pad=3
	root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth()-pad, root.winfo_screenheight()-pad))

	root.attributes('-fullscreen', True)
	root.wm_attributes("-topmost", 1)

	#root.after(5000, root.destroy)
	root.bind('<Escape>',exit)

	mainloop()

def update_input():
	f = open("input.txt", "r")
	input_text = f.read()
	f.close()

	return input_text

def exit(event):
	root.destroy()

def mainloop(self):
	root.mainloop()

main()