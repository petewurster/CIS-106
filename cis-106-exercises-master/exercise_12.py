import tkinter as t

def star():
    main=t.Tk()
    main.wm_title('star')
    main.bind('<Button 1>',click)
    canvas=t.Canvas(main,width=300,height=300,background='grey94')
    canvas.pack()

    global startX,startY
    

    
    t.mainloop()

def click(eventorigin):
    startX=eventorigin.x
    startY=eventorigin.y
    print(startX,startY)


star()
