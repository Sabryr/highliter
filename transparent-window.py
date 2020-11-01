from tkinter import Tk # or(from Tkinter import Tk) on Python 2.x
root = Tk(className='Highlight')
root.geometry("400x200")
root.configure(bg='yellow')
root.wait_visibility(root)
root.wm_attributes('-alpha',0.3)
root.mainloop()

#from tkinter import *

# set window size

#set window color

#gui.mainloop() 
