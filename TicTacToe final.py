from tkinter import *
import random
from tkinter import messagebox
from functools import partial
count=0
turn=0
flag=0
a='O'
y=0

    
    
def hard():
    if b5["text"]!=" ":
        if ((b4["text"]==b6["text"]=="O") or (b2["text"]==b8["text"]=="O") or (b1["text"]==b9["text"]=="O") or (b3["text"]==b7["text"]=="O")) and (b5["text"]==" ") :return(b5.invoke())     
        if ((b2["text"]==b3["text"]=="O") or (b4["text"]==b7["text"]=="O") or (b5["text"]==b9["text"]=="O")) and (b1["text"]==" "):return(b1.invoke())
        if ((b1["text"]==b2["text"]=="O") or (b6["text"]==b9["text"]=="O") or (b5["text"]==b7["text"]=="O")) and (b3["text"]==" "):return(b3.invoke())
        if ((b8["text"]==b9["text"]=="O") or (b1["text"]==b4["text"]=="O") or (b3["text"]==b5["text"]=="O")) and (b7["text"]==" "):return(b7.invoke())
        if ((b7["text"]==b8["text"]=="O") or (b3["text"]==b6["text"]=="O") or (b1["text"]==b5["text"]=="O")) and (b9["text"]==" "):return(b9.invoke())
        if ((b1["text"]==b3["text"]=="O") or (b5["text"]==b8["text"]=="O")) and (b2["text"]==" "):return(b2.invoke())
        if ((b5["text"]==b6["text"]=="O") or (b1["text"]==b7["text"]=="O")) and (b4["text"]==" "):return(b4.invoke())
        if ((b4["text"]==b5["text"]=="O") or (b3["text"]==b9["text"]=="O")) and (b6["text"]==" "):return(b6.invoke())
        if ((b7["text"]==b9["text"]=="O") or (b2["text"]==b5["text"]=="O")) and (b8["text"]==" "):return(b8.invoke())
        if ((b4["text"]==b6["text"]=="X") or (b2["text"]==b8["text"]=="X") or (b1["text"]==b9["text"]=="X") or (b3["text"]==b7["text"]=="X")) and (b5["text"]==" ") :return(b5.invoke())     
        if ((b2["text"]==b3["text"]=="X") or (b4["text"]==b7["text"]=="X") or (b5["text"]==b9["text"]=="X")) and (b1["text"]==" "):return(b1.invoke())
        if ((b1["text"]==b2["text"]=="X") or (b6["text"]==b9["text"]=="X") or (b5["text"]==b7["text"]=="X")) and (b3["text"]==" "):return(b3.invoke())
        if ((b8["text"]==b9["text"]=="X") or (b1["text"]==b4["text"]=="X") or (b3["text"]==b5["text"]=="X")) and (b7["text"]==" "):return(b7.invoke())
        if ((b7["text"]==b8["text"]=="X") or (b3["text"]==b6["text"]=="X") or (b1["text"]==b5["text"]=="X")) and (b9["text"]==" "):return(b9.invoke())
        if ((b1["text"]==b3["text"]=="X") or (b5["text"]==b8["text"]=="X")) and (b2["text"]==" "):return(b2.invoke())
        if ((b5["text"]==b6["text"]=="X") or (b1["text"]==b7["text"]=="X")) and (b4["text"]==" "):return(b4.invoke())
        if ((b4["text"]==b5["text"]=="X") or (b3["text"]==b9["text"]=="X")) and (b6["text"]==" "):return(b6.invoke())
        if ((b7["text"]==b9["text"]=="X") or (b2["text"]==b5["text"]=="X")) and (b8["text"]==" "):return(b8.invoke())
        if b5["text"]=="X":
            if b1["text"]==" " :return(b1.invoke())
            if b3["text"]==" " :return(b3.invoke())
            if b7["text"]==" " :return(b7.invoke())
            if b9["text"]==" " :return(b9.invoke())
            if b2["text"]==" " :return(b2.invoke())
            if b4["text"]==" " :return(b4.invoke())
            if b6["text"]==" " :return(b6.invoke())
            if b8["text"]==" " :return(b8.invoke())
        if b5["text"]=="O":
            if b2["text"]==" " :return(b2.invoke())
            if b4["text"]==" " :return(b4.invoke())
            if b6["text"]==" " :return(b6.invoke())
            if b8["text"]==" " :return(b8.invoke())
            if b1["text"]==" " :return(b1.invoke())
            if b3["text"]==" " :return(b3.invoke())
            if b7["text"]==" " :return(b7.invoke())
            if b9["text"]==" " :return(b9.invoke())
    else :
        return(b5.invoke())
def change_color(x):
    global count,y
    a=0
    if (b1["text"]==b2["text"]==b3["text"]!=" "):
        b1["bg"]="light green"
        b2["bg"]="light green"
        b3["bg"]="light green"
        a=1
    if (b4["text"]==b5["text"]==b6["text"]!=" "):
        b4["bg"]="light green"
        b5["bg"]="light green"
        b6["bg"]="light green"
        a=1
    if (b7["text"]==b8["text"]==b9["text"]!=" "):
        b7["bg"]="light green"
        b8["bg"]="light green"
        b9["bg"]="light green"
        a=1
    if (b1["text"]==b4["text"]==b7["text"]!=" "):
        b1["bg"]="light green"
        b4["bg"]="light green"
        b7["bg"]="light green"
        a=1
    if (b2["text"]==b5["text"]==b8["text"]!=" "):
        b2["bg"]="light green"
        b5["bg"]="light green"
        b8["bg"]="light green"
        a=1
    if (b3["text"]==b6["text"]==b9["text"]!=" "):
        b3["bg"]="light green"
        b6["bg"]="light green"
        b9["bg"]="light green"
        a=1
    if (b1["text"]==b5["text"]==b9["text"]!=" "):
        b1["bg"]="light green"
        b5["bg"]="light green"
        b9["bg"]="light green"
        a=1
    if (b3["text"]==b5["text"]==b7["text"]!=" "):
        b3["bg"]="light green"
        b5["bg"]="light green"
        b7["bg"]="light green"
        a=1
    if (a==1) or (count==9):
        b1["state"]=DISABLED
        b2["state"]=DISABLED
        b3["state"]=DISABLED
        b4["state"]=DISABLED
        b5["state"]=DISABLED
        b6["state"]=DISABLED
        b7["state"]=DISABLED
        b8["state"]=DISABLED
        b9["state"]=DISABLED
    if (a==1):
        print(x,"Won")
        messagebox.showinfo("showinfo", x+"   WON   ")
        y=1
    if (a==0)and(count==9):
        print("Draw")
        messagebox.showinfo("showinfo", "   DRAW   ")
        y=1
def random_mode():
    y=0
    while y==0 :
        
        x=random.randint(1,9)
        if (x==1)and(b1["text"]==" "):
            y=1
            return(b1.invoke())
        if (x==2)and(b2["text"]==" "):
            y=1
            return(b2.invoke())
        if (x==3)and(b3["text"]==" "):
            y=1
            return(b3.invoke())
        if (x==4)and(b4["text"]==" "):
            y=1
            return(b4.invoke())
        if (x==5)and(b5["text"]==" "):
            y=1
            return(b5.invoke())
        if (x==6)and(b6["text"]==" "):
            y=1
            return(b6.invoke())
        if (x==7)and(b7["text"]==" "):
            y=1
            return(b7.invoke())
        if (x==8)and(b8["text"]==" "):
            y=1
            return(b8.invoke())
        if (x==9)and(b9["text"]==" "):
            y=1
            return(b9.invoke())

        
def set_b(b):
    global turn,count,a,y
    if (turn==0) and (b["text"]==" "):
        b["text"]='X'
        turn=1
        count=count+1
        if turn == 0 : a="O"
        if turn == 1 : a="X"
        change_color(a)
        if y==1:return
        if flag==1 : hard()
        if flag==2 : random_mode()
    if (turn==1) and (b["text"]==" "):
        b["text"]='O'
        turn=0
        count=count+1
    if y==1:return
    if turn == 0 : a="O"
    if turn == 1 : a="X"
    change_color(a)
def reset(canvas,root):
    global b1,b2,b3,b4,b5,b6,b7,b8,b9,count,turn,y
    count=0
    turn=0
    y=0
    b1=Button(canvas,text=" ",bg="green",fg="white",activebackground="red",command=lambda : set_b(b1),width=10,height=5,font=7)
    b2=Button(canvas,text=" ",bg="green",fg="white",activebackground="red",command=lambda : set_b(b2),width=10,height=5,font=7)
    b3=Button(canvas,text=" ",bg="green",fg="white",activebackground="red",command=lambda : set_b(b3),width=10,height=5,font=7)
    b4=Button(canvas,text=" ",bg="green",fg="white",activebackground="red",command=lambda : set_b(b4),width=10,height=5,font=7)
    b5=Button(canvas,text=" ",bg="green",fg="white",activebackground="red",command=lambda : set_b(b5),width=10,height=5,font=7)
    b6=Button(canvas,text=" ",bg="green",fg="white",activebackground="red",command=lambda : set_b(b6),width=10,height=5,font=7)
    b7=Button(canvas,text=" ",bg="green",fg="white",activebackground="red",command=lambda : set_b(b7),width=10,height=5,font=7)
    b8=Button(canvas,text=" ",bg="green",fg="white",activebackground="red",command=lambda : set_b(b8),width=10,height=5,font=7)
    b9=Button(canvas,text=" ",bg="green",fg="white",activebackground="red",command=lambda : set_b(b9),width=10,height=5,font=7)
    b1.grid(row=1,column=1)
    b2.grid(row=1,column=2)
    b3.grid(row=1,column=3)
    b4.grid(row=2,column=1)
    b5.grid(row=2,column=2)
    b6.grid(row=2,column=3)
    b7.grid(row=3,column=1)
    b8.grid(row=3,column=2)
    b9.grid(row=3,column=3)


def play():
	menu = Tk()
	menu.geometry("500x500")
	menu.title("Tic Tac Toe")
	menu.configure(background='orange')
	l1=Label(menu, text = "---Welcome to Tic-Tac-Toe---", bg = "green",fg = "yellow",font=("times 20 bold"))
	B1 = Button(menu, text = "Vs Computer", command = lambda:abc(menu,1),activeforeground = 'green',activebackground = "yellow", bg = "red",fg = "yellow", width = 20, font = 'summer', bd = 5)
	B2 = Button(menu, text = "Vs Friend", command = lambda: xyz(menu,0),
				activebackground = "yellow", bg = "red", fg = "yellow",
				width = 20, font = 'summer', bd = 5)
	
	B3 = Button(menu, text = "Exit", command = menu.destroy,
				activebackground = "yellow", bg = "green", fg = "yellow",
			width = 10, font = 'summer', bd = 5)
	l1.place(relx=0.5,y=125 , anchor=CENTER)
	B1.place(relx=0.5,y=200 , anchor=CENTER)
	B2.place(relx=0.5,y=250 , anchor=CENTER)
	B3.place(relx=0.5,y=325 , anchor=CENTER)
	menu.mainloop()
def home(menu):
    menu.destroy()
    play()
def back1(menu,t):
    if t==0:
        menu.destroy()
        play()
    if (t==1) or (t==2):abc(menu,t)
        
def abc(root,t):
    root.destroy()
    menu = Tk()
    menu.geometry("500x500")
    menu.title("Tic Tac Toe")
    menu.configure(background='orange')
    l1=Label(menu, text = "---Tic-Tac-Toe---", bg = "green",fg = "yellow",font=("times 20 bold"))
    B1 = Button(menu, text = "Easy", command = lambda:xyz(menu,2),activeforeground = 'green',activebackground = "yellow", bg = "red",fg = "yellow", width = 20, font = 'summer', bd = 5)
    B2 = Button(menu, text = "Hard", command = lambda: xyz(menu,1),
				activebackground = "yellow", bg = "red", fg = "yellow",
				width = 20, font = 'summer', bd = 5)
	
    B3 = Button(menu, text = "Back", command = lambda:home(menu),
				activebackground = "yellow", bg = "green", fg = "yellow",
			width = 10, font = 'summer', bd = 5)
    l1.place(relx=0.5,y=125 , anchor=CENTER)
    B1.place(relx=0.5,y=200 , anchor=CENTER)
    B2.place(relx=0.5,y=250 , anchor=CENTER)
    B3.place(relx=0.5,y=325 , anchor=CENTER)
    menu.mainloop()
    
def xyz(root,t):
    global flag
    flag=t
    root.destroy()
    root=Tk()
    root.configure(background='orange')
    root.geometry("500x500")
    root.title("TIC TAC TOE")
    canvas = Canvas(root)
    canvas.place(relx=0.5,y=225 , anchor=CENTER)
    b0=Button(root,text=" Reset ",bg="red",fg="yellow",activebackground="yellow",command = partial (reset,canvas,root)).place(relx=0.3,y=450 , anchor=CENTER)
    b11=Button(root,text=" Home ",bg="red",fg="yellow",activebackground="yellow",command = partial (home,root)).place(relx=0.5,y=450 , anchor=CENTER)
    b12=Button(root,text=" Back ",bg="red",fg="yellow",activebackground="yellow",command = partial (back1,root,t)).place(relx=0.7,y=450 , anchor=CENTER)
    reset(canvas,root)
    root.mainloop()
play()

