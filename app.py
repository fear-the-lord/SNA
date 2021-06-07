# Import the necessary dependencies
from tkinter import *
import os

root = Tk()
root.configure(background = "#002984")

def function1(): 
	os.system("python user_defined_network.py")

def function2(): 
	os.system("python manual_network.py")

def function3(): 
	root.destroy()

root.title("STRUCTURAL BALANCE IDENTIFICATOR")
Label(root, text="STRUCTURAL BALANCE IDENTIFICATOR",font=("times new roman",20),fg="black",bg="#c5cae9",height=2).grid(row=2,rowspan=2,columnspan=5,sticky=N+E+W+S,padx=5,pady=10)
Button(root,text="USER INPUT",font=("times new roman",20),bg="#ff7961",fg='white',command=function1).grid(row=5,columnspan=5,sticky=W+E+N+S,padx=5,pady=5)
Button(root,text="MANUAL",font=("times new roman",20),bg="#ff7961",fg='white',command=function2).grid(row=7,columnspan=5,sticky=W+E+N+S,padx=5,pady=5)
Button(root,text="EXIT",font=("times new roman",20),bg="#ff7961",fg='white',command=function3).grid(row=9,columnspan=5,sticky=W+E+N+S,padx=5,pady=5)

root.mainloop()