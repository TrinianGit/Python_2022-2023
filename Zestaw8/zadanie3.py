import tkinter as tk
from tkinter import Label, StringVar
from datetime import datetime
from tkcalendar import Calendar  # pip install tkcalendar
import tkinter.font as font

okno = tk.Tk()
# tytuł, rozmiar, blokada wielkości
okno.title("Zegar i kalendarz")
okno.geometry("400x400")
okno.minsize(400, 400)
okno.maxsize(400, 400)
# utwórz StringVar()
text = StringVar()
myFont = font.Font(family='Arial', size=38, weight='bold')
date_time = Label(okno, textvariable=text, font=myFont, background="black", foreground="white")
def update_date_time():
	# dzien = i tak dalej... miesiac, rok, czas, dzien
	# czytamy datetime.today().strftime('%A')
	# kody https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
	dt = datetime.today().strftime("%d %B %Y\n%A %H:%M:%S")
	# dt = dzien + ... + "\n" + ...
	# ustaw za pomocą .set dt dla StringVar zrobinego powyżej
	# ważne: rekurencyjne odświeżanie etykiety - patrz poniżej
	text.set(dt)
	date_time.after(1000, update_date_time)

# widget Label ustawiony na StringVar zrobiony na początku, rozmiar, czcionki, tło - wg uznania 
# date_time = Label(...
date_time.pack(anchor="center")

current_time = datetime.now()
# przyda się do kalendarza
# day = odczytaj przez .strftime('%d')
# month = 
# year = 

# utwórz cal = Calendar(...
# wstaw przez .pack poniżej zegara
cal = Calendar(okno, year = datetime.today().year, month = datetime.today().month, day = datetime.today().day)
cal.pack(anchor="center", pady=20, padx=50)
update_date_time()

okno.mainloop()