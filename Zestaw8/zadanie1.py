import tkinter as tk
from tkinter import StringVar, Button, Entry
import tkinter.font as font

okno = tk.Tk()
okno.title("Calculator")

myFont = font.Font(family='Arial', size=20, weight='bold')

ans_entry =  Entry(okno, bd=5, width=20, font=myFont, bg="gray", fg="white")
ans_entry.grid(row=0, column=0, columnspan=4)

buttons = []
znaki = ['1','2','3','/','4','5','6','*','7','8','9','-','C','0', '=', '+']
number = 0
# przykładowy pierwszy Button
for i in range(4):
    for j in range(4):
        btn = Button(okno, text=znaki[number],padx=20, pady=10)
        btn['font'] = myFont
        btn.grid(row = i + 1, column = j)
        buttons.append(btn)
        number += 1
            

def count(text_num):
    if('+' in text_num):
        return count(text_num.rsplit("+", 1)[0]) + count(text_num.rsplit("+", 1)[1])
    elif('-' in text_num):
        return count(text_num.rsplit("-", 1)[0]) - count(text_num.rsplit("-", 1)[1])
    elif('*' in text_num):
        return count(text_num.rsplit("*", 1)[0]) * count(text_num.rsplit("*", 1)[1])
    elif('/' in text_num):
        return count(text_num.rsplit("/", 1)[0]) / count(text_num.rsplit("/", 1)[1])
    else:
        return int(text_num)

def mouse_button_release(event):
    global result
    try:
        widg = event.widget
        text = widg.cget("text")

        if text in "0123456789+-*/":
            ans_entry.insert(len(ans_entry.get()), text)

        if text == "C":
            ans_entry.delete(0, len(ans_entry.get()))

        if text == "=":
            tmp = ans_entry.get()
            ans_entry.delete(0, len(ans_entry.get()))
            if (int(count(tmp)) == count(tmp)):
                ans_entry.insert(0, int(count(tmp)))
            else:
                ans_entry.insert(0, count(tmp))
# 55*46+49/7 
    except:
        pass

        

# sposób na reakcję 
okno.bind("<ButtonRelease-1>", mouse_button_release)

okno.mainloop()
