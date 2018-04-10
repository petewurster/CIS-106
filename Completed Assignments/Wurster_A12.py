'''
creates a window which displays a canvas that closely copies the image
in the assignment
'''

import tkinter

#main prog as func
def assignment12():
    #build main window & define canvas size
    main=tkinter.Tk()
    main.wm_title('Pete\'s House')
    canvas=tkinter.Canvas(main,height=300,width=300,background='cyan')
    canvas.pack()
    
    #draw shapes on canvas using tkinter's built-in canvas methods
    canvas.create_rectangle(0,220,300,300,fill='green')
    canvas.create_rectangle(50,110,150,220,fill='yellow')
    canvas.create_rectangle(65,125,85,145,fill='blue')
    canvas.create_rectangle(115,125,135,145,fill='blue')
    canvas.create_rectangle(90,180,110,220,fill='brown')
    canvas.create_rectangle(225,170,250,220,fill='brown')
    canvas.create_oval(200,90,270,190,fill='green')
    canvas.create_oval(235,200,245,210,fill='black')
    canvas.create_polygon(50,110,
                          100,40,
                          150,110,fill='red')
    #enter tk loop
    tkinter.mainloop()
#execute prog
assignment12()
