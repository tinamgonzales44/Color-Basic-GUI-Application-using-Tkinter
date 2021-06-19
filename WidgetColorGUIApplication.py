#Color Window

from tkinter import * #imports all of the tkinter module
window = Tk() #call tkinter function to create a tkinter window // create GUI window // window is the named given to the GUI: name is needed for attributes

window.title("Hello Python") #Title of the Message Window // Will appear on the Top // title widget
window.geometry('850x700+600+200') #Defines the width, height and coordinates of the top left corner of the frame as below in pixels | (width x height + XPOS + YPOS) //geometry widget
window.configure(bg='#856ff8', highlightbackground='#3E4149') #Defines bg=background | highlightbackground=Defines background of the whole window //configuration widget


window.mainloop() #event listening loop // it waits for other events such as radio buttons et al // will close on x // main loop widget // needed for the GUI to pop-up

""" 
Sources: 

https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python

https://pythonexamples.org/python-tkinter-window-background-color/#2

https://www.geeksforgeeks.org/how-to-change-the-tkinter-label-text

"""

