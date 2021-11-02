import subprocess, sys
def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

from tkinter import*
from tkinter import filedialog
import os
 
def openFile():
    filepath=filedialog.askopenfilename(initialdir="/",
                                        title="Open File okay?",
                                        filetypes=(("text file","*.txt"),
                                        ("all files","*.*"))) 
    open_file(filepath)
    
window = Tk()
button =Button(text="Open",command=openFile)
button.pack()
window.mainloop()                                     
