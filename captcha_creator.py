#from tkinter import *
import random as r

import tkinter as tk
import tkinter.ttk as ttk

from tkinter.font import Font

submit_text  = ""

def check():
	submit_text = e1.get()
	print("S: "+submit_text)	
	print("C: "+captcha_text)	
	if (submit_text != "") and (submit_text == captcha_text):
		print("Access allowed")
	else:
		print("Access denied")
		create()
		

def create():
	c.delete("all")
	h = []
	for i in range(0,5):
		a = r.randint(0,1)
		if a == 1:
			h.append(chr(r.randint(65,90)))
		if a == 0:
			h.append(chr(r.randint(97,122)))
		
		
	global captcha_text
	captcha_text = h[0]+h[1]+h[2]+h[3]+h[4]
	
	print(captcha_text)
	color = ["pink","white","purple","red","blue","green","gray","yellow","orange"]
	fnt   = ["Verdana","Arial","Papyrus","Calibri","Times New Roman","Courier New","Garamond","Bookman","Comic Sans MS","Impact"]	
	
	
	myFont1 = Font(family=fnt[r.randint(0,9)], size=r.randint(26,36))
	myFont2 = Font(family=fnt[r.randint(0,9)], size=r.randint(26,36))
	myFont3 = Font(family=fnt[r.randint(0,9)], size=r.randint(26,36))
	myFont4 = Font(family=fnt[r.randint(0,9)], size=r.randint(26,36))
	myFont5 = Font(family=fnt[r.randint(0,9)], size=r.randint(26,36))
	
	t1 = c.create_text(40+r.randint(0,10),40+r.randint(0,10),text=h[0],font=myFont1,fill= color[r.randint(0,8)])
	t2 = c.create_text(80+r.randint(0,10),40+r.randint(0,10),text=h[1],font=myFont2,fill= color[r.randint(0,8)])
	t3 = c.create_text(120+r.randint(0,10),40+r.randint(0,10),text=h[2],font=myFont3,fill= color[r.randint(0,8)])
	t4 = c.create_text(160+r.randint(0,10),40+r.randint(0,10),text=h[3],font=myFont4,fill= color[r.randint(0,8)])
	t5 = c.create_text(200+r.randint(0,10),40+r.randint(0,10),text=h[4],font=myFont5,fill= color[r.randint(0,8)])
	
	for i in range(0,10):
		l = c.create_line(r.randint(5,295),r.randint(5,195),r.randint(5,295),r.randint(5,195),fill=color[r.randint(0,8)],width=r.randint(1,4))
	



window =tk.Tk()
window.geometry("300x210")
window.title("Captcha")



bgcolor = ["black"]

e1= ttk.Entry(width=10)
c = tk.Canvas (width=280,height=100,bg=bgcolor[r.randint(0,0)])
b = ttk.Button(text="Create",command=create)
b1 = ttk.Button(text="Submit",command=check)


b.place(x=100,y=120)
b1.place(x=100,y=170)
c.place(x=10,y=10)
e1.place(x=5,y=180)


window.mainloop()
