#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  1 18:47:35 2022

@author: priyankadas
"""

from tkinter import *
import random

root = Tk()

root.title("Your lucky friend")
root.geometry("500x500")


list1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
label1 = Label(root)
print(list1[2:4])

def friend():
    a = random.randint(0, 52)
    
    b = random.randint(0, 52)
    
    c = random.randint(0, 52)
    
    d = random.randint(0, 52)
    
    e = random.randint(0, 52)
    
    label1["text"] = "Your random wordle guess : " + list1[a]+list1[b]+list1[c]+list1[d]+list1[e] 

btn = Button(root, text = "What will be your random wordle guess today?", command = friend)
btn.place(relx = 0.5, rely = 0.6, anchor = CENTER)
label1.place(relx = 0.5, rely = 0.4, anchor = CENTER)  
root.mainloop()