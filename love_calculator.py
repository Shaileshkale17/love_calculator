#import tkinter
from tkinter import *

# import random module
import random

root = Tk()
# root.geometry("400x240")
root.geometry("742x350")
root.title('love calculator')


def calculatoe_love():
    st = '0123456789'
    digit = 2
    temp = "".join(random.sample(st, digit))
    result.config(text=temp)


heading = Label(root, text='love calculator - how much is he/she into you')
heading.pack()
# slot / input for the first name 
slot1 = Label(root, text="enter your name:")
slot1.pack()
name1 = Entry(root, border=5)
name1.pack()
# slot / input for the partner name 
slot1 = Label(root, text="enter your name:")
slot1.pack()
name1 = Entry(root, border=5)
name1.pack()

bt = Button(root, text="calculate", height=1,
            width=7, command=calculatoe_love)
bt.pack()

result = Label(root, text='Love percentage between both of you:')
result.pack()
root.mainloop()
