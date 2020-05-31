import tkinter as tk

def updateLabel(string):
	svar.set(string)
	print('*updateLabel')


def read_text_file():

	input_text = ''
	f = open("input.txt", "r")
	input_text = f.read()
	f.close()
	return input_text

def set_label(svar, root):
	
	input_text = read_text_file()

	svar.set(input_text)

	labl = tk.Label(root, bd=8, wraplength=350, textvariable=svar, heigh=5, font=('Helvetica 25 bold'))

	labl.pack()

	print('msg: '+str(input_text))


root=tk.Tk()
svar = tk.StringVar()
root.attributes('-fullscreen', True)
root.wm_attributes("-topmost", 1)


def main():
		

	pad=3
	root.geometry("{0}x{1}+0+0".format(
		    root.winfo_screenwidth()-pad, root.winfo_screenheight()-pad))

	def exit(event):
		root.destroy()

	root.bind('<Escape>',exit)

	#root.after(5000, root.destroy)

	set_label(svar, root)


	root.mainloop()


main()