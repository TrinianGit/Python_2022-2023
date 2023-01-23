import PyPDF2  # pip install PyPDF2
import tkinter as tk
from tkinter import filedialog, Text, Menu
import tkinter.font as font

okno = tk.Tk()
# dodać tytuł, rozmiar
okno.title("My PDF text extractor")
okno.geometry("900x600")
myFont = font.Font(family='Arial', size=10, weight='bold')
# dodać widget Text i umieściś z jakimś marginesem
text = Text(okno, height=400, width=600, font=myFont)
text.grid(row=0, column=0, columnspan=4)
text.pack(padx=100, pady=50)
def clear_text():
   text.delete("1.0", "end")

def open_pdf():
   file = filedialog.askopenfilename(title="Select a PDF", filetypes=(("PDF    Files","*.pdf"),("All Files","*.*")))
   if file:
      pdf_file= PyPDF2.PdfReader(file)
      for i in range(len(pdf_file.pages)):
         page = pdf_file.pages[i]
         content=page.extract_text()
         text.insert(tk.END, content)

def quit_app():
   okno.destroy()

# utworzyć widget Menu i jego strukturę jak na rysunku
# Open powinno wołać open_pdf
# Clear powinno wołać clear_text
# Quit powinno wołać quit_app

menu = Menu(okno)
menubar = Menu(menu, tearoff=0)
menubar.add_command(label="Open", command=open_pdf)
menubar.add_command(label="Clear", command=clear_text)
menubar.add_command(label="Quit", command=quit_app)
menu.add_cascade(label="File", menu=menubar)
okno.config(menu=menu)

okno.mainloop()