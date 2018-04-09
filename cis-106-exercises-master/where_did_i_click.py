import tkinter as t

def where():
    main=t.Tk()
    main.bind('<Button 1>',click)
    canvas=t.Canvas(main,width=300,height=300)
    canvas.pack()
    global startX,startY
    
    t.mainloop()

def click(eventorigin):
    startX=eventorigin.x
    startY=eventorigin.y
    print(startX,startY)


where()
