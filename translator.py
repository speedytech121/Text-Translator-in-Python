from tkinter import*
from translate import Translator

# translate function
def translate():
    translator=Translator(from_lang=lan1.get(),to_lang=lan2.get())
    translation=translator.translate(var.get())
    var1.set(translation)


# tkinter root window with title
root=Tk()
root.title("DPK Translator")

# creating a frame and grid to hold the content(we can use place also)
mainframe=Frame(root)
mainframe.grid(column=0,row=0,sticky=(N,W,E,S)) #sticky provides the cell direction here it will be centered
mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure(0,weight=1)
mainframe.pack(pady=100,padx=100)


# variables for dropdown language list | using stringvar just because it has many methods like set method which we will use to set the languages 
lan1=StringVar(root)
lan2=StringVar(root)

# choices to show in dropdown menu
choices={'English','Hindi','Gujarati','Spanish','German','Tamil'}
lan1.set('English')
lan2.set('Hindi')

# creating dropdown and arranging in grid
lan1menu=OptionMenu(mainframe,lan1,*choices)
Label(mainframe,text="select a language").grid(row=0,column=1)
lan1menu.grid(row=1,column=1)

lan2menu=OptionMenu(mainframe,lan2,*choices)
Label(mainframe,text="select a language").grid(row=0,column=2)
lan2menu.grid(row=1,column=2)

# Textbox to take user input
Label(mainframe,text="Enter text").grid(row=2,column=0)
var=StringVar()
textbox=Entry(mainframe,textvariable=var).grid(row=2,column=1)

# Textbox to show translated output
Label(mainframe,text="Output").grid(row=2,column=2)
var1=StringVar()
textbox=Entry(mainframe,textvariable=var1).grid(row=2,column=3)

# creating a button to call Translator function
b=Button(mainframe,text='Translate',command=translate)
b.grid(row=4,column=1,columnspan=2)

root.mainloop()