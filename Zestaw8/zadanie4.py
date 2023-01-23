from tkinter import Label, StringVar, Button, PhotoImage, Entry, filedialog, Frame
import tkinter as tk 
from PIL import Image
import tkinter.font as font

okno = tk.Tk()
# tytuł, geometria, nieskalowalne
okno.title("Image resizer")
okno.geometry("700x400")
okno.minsize(700, 400)
okno.maxsize(700, 400)

myFont = font.Font(family='Arial', size=10, weight='bold')

image_fp = None  
data_image = None
photo_image = None

def open_handler():
	global image_fp, data_image
	image_fp = filedialog.askopenfilename(initialdir=".", filetypes=(("PNG Files", "*.png"),))
	if image_fp:
		data_image = PhotoImage(file=image_fp)
		image_label.config(image=data_image)

def width_modified(event):
	global image_fp
	if image_fp:
		w = width_entry.get()
		if w != "" and w.isdigit():
			w = int(w)
			image = Image.open(image_fp)
			image_width = image.width
			image_height = image.height
			width_percentage = int((w*100)/image_width)
			height_set_to = int(image_height * (width_percentage/100))
			height_entry_str.set(str(height_set_to))

def height_modified(event):
	global image_fp
	if image_fp:
		h = height_entry.get()
		if h != "" and h.isdigit():
			h = int(h)
			image = Image.open(image_fp)
			image_width = image.width
			image_height = image.height
			height_percentage = int((h*100)/image_height)
			width_set_to = int(image_width * (height_percentage/100))
			width_entry_str.set(str(width_set_to))

def resize_handler():
	global image_fp, photo_image
	if image_fp:
		w = width_entry_str.get()
		h = height_entry_str.get()

		if w != "" and w.isdigit() and h != "" and h.isdigit():
			w = int(w)
			h = int(h)
			image = Image.open(image_fp)
			image.thumbnail((w,h), Image.LANCZOS)
			image.save('temp.png')
			photo_image = PhotoImage(file='temp.png')
			image_label.config(image=photo_image)

def save_handler():
	global image_fp, photo_image
	if image_fp:
		image_save_fp = filedialog.askopenfilename(initialdir=".", filetypes=(("PNG files","*.png"),), defaultextension=".png")
		if image_save_fp:
			w = width_entry_str.get()
			h = height_entry_str.get()
			if w != "" and w.isdigit() and h != "" and h.isdigit():
				w = int(w)
				h = int(h)
				image = Image.open(image_fp)
				image.thumbnail((w,h), Image.LANCZOS)
				image.save(image_save_fp)


f = Frame(okno)
f.pack()
# open_bnt = Button(... z open_handler)
open_btn = Button(f, text="Open", command=open_handler)
# width_label = Label(...
width_label = Label(f, text="Width:", font=myFont)
width_entry_str = StringVar()
# width_entry = Entry(...
width_entry = Entry(f)
width_entry.bind("<KeyRelease>", width_modified)

# height_label = Label(...
height_label = Label(f, text="Height:", font=myFont)
height_entry_str = StringVar()
# height_entry = Entry(...
height_entry = Entry(f)
height_entry.bind("<KeyRelease>", height_modified)

# resize_btn = Button(... z resize_handler)
resize_btn = Button(f, text="Resize", command=resize_handler)
# save_btn = Button(... z save_handler)
save_btn = Button(f, text="Save", command=save_handler)

image_label = Label(okno)
image_label.config(image="")
image_label.pack(fill="both", padx=10, pady=50)
open_btn.pack(side = tk.LEFT)
width_label.pack(side = tk.LEFT)
width_entry.pack(side = tk.LEFT)
height_label.pack(side = tk.LEFT)
height_entry.pack(side = tk.LEFT)
resize_btn.pack(side = tk.LEFT)
save_btn.pack(side = tk.LEFT)

okno.mainloop()
