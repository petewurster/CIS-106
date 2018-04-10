import tkinter as t

def where():
    main=t.Tk()
    canvas=t.Canvas(main,width=300,height=300)
    canvas.bind('<Button 1>',click)
    canvas.pack()
    
    t.mainloop()

def click(eventorigin):
    print(eventorigin.x,eventorigin.y)

where()
