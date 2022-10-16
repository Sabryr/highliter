from tkinter import Tk # or(from Tkinter import Tk) on Python 2.x
root = Tk(className='Type-with-me')
root.geometry("200x0")
root.configure(bg='green')
root.wait_visibility(root)
root.wm_attributes('-alpha',0.5)
root.mainloop()

#from tkinter import *

# set window size

#set window color

#gui.mainloop() 
