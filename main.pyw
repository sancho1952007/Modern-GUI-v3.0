"""
====== GUI Design By: Sancho Godinho (https://github.com/sancho1952007/Modern-GUI-v3.0) ======
====== Images By: Flaticon (https://flaticon.com) ======

\\ Please Do Not Delete the files Folder!

\\ Please Do Not Clear This Comment!

\\ You Are Allowed to Customize this Script.

\\ If you want to share this script or Customize and share: You Should Keep this complete comment with it.

"""

from tkinter.font import *
from tkinter import *
import os
path=os.path.dirname(os.path.realpath(__file__))+"\\"
app=Tk()
app.overrideredirect(True)
app.config(bg="#d3d3d3")
app.config(bd=1)
app.attributes('-alpha', 0.9)

with open(path+'files\\location', 'r') as readLoc:
    pos=readLoc.read().split('x')
    x_pos=''.join(pos[0])
    y_pos=''.join(pos[1])
    app.geometry(f"+{x_pos}+{y_pos}")
    readLoc.close()

def qut(): # Quit Function (Exit)
    with open(path+'files\\location', 'w+') as write_loc:
        write_loc.write(str(app.winfo_x())+'x'+str(app.winfo_y()))
        write_loc.close()
        app.destroy()

def detect_key_press(event):
    if event.keysym=='F5':
        big_screen()
    elif event.keysym=="F9":
        small_screen()
    elif event.keysym=="F1":
        qut()

def enter_close(event):
    close.config(image=close2)

def leave_close(event):
    close.config(image=close1)

def move(event):
    half1=str(app.winfo_width()/2)
    half2=half1.split('.')
    half=half2[0]
    app.geometry(f"+{event.x_root-int(''.join(half))}+{event.y_root-7}")

def small_screen():
    app.state('normal')
    size.config(image=maximize, command=big_screen)
    title.place(anchor=CENTER, relx=0.5, rely=0.5)

def big_screen():
    app.state("zoomed")
    size.config(image=minimize, command=small_screen)
    title.grid(row=0, column=2, sticky=W, padx=700)

close1=PhotoImage(file=path+"files\\close-1.png")
close2=PhotoImage(file=path+"files\\close-2.png")
minimize=PhotoImage(file=path+"files\\minimize.png")
maximize=PhotoImage(file=path+"files\\maximize.png")

Top=Frame(app, bd=2, bg="grey")
close=Button(Top, image=close1, bg="grey", bd=0,command=qut)
close.grid(row=0, column=0)

size=Button(Top, image=maximize, bg='grey',bd=0 ,  command=big_screen)
size.grid(row=0, column=1)

title=Label(Top, text="Title", bg="grey", font=("Comic Sans MS", 12))
title.place(anchor=CENTER, relx=0.5, rely=0.5)
Top.pack(fill=X, side='top')

root=Frame(app, bd=2, bg='#d3d3d3')
Label(root, text="Contents!", bg='#d3d3d3', font="10", width="72", height="20").grid()
root.pack()

#Bindings
app.attributes("-topmost", True)
app.bind("<Key>", detect_key_press)
close.bind("<Enter>", enter_close)
close.bind("<Leave>", leave_close)
Top.bind("<B1-Motion>", move)
title.bind("<B1-Motion>", move)


app.protocol('WM_DELETE_WINDOW', qut)
app.mainloop()
