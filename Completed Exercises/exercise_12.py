'''
customer spec: create a program that will create a 300x300 "canvas" object
            and draw either a star (ex_1) or a cube (ex_2)
added feature: allow user to define which shape to draw, where on the canvas
            the shape appears, shape size & color
'''

import tkinter as t

#main prog as a function
def shapes():
    #define main window & assign globals 
    main=t.Tk()
    main.wm_title('Select type of shape and click around!')
    main.geometry('375x330')
    global newX,endY,endX,endY,canvas,shape,color
    shape=t.StringVar()
    shape.set(None)
    color=t.StringVar()
    color.set(None)
    
    #define canvas object & associate mouse input
    canvas=t.Canvas(main,width=300,height=300,background='white')
    canvas.bind('<Button 1>',click)
    canvas.bind('<ButtonRelease 1>',release)

    #create/pack selection frame
    left=t.Frame(main)
    rbLine=t.Radiobutton(left,text='line',variable=shape,value='line')
    rbRect=t.Radiobutton(left,text='rect',variable=shape,value='rect')
    rbOval=t.Radiobutton(left,text='oval',variable=shape,value='oval')
    rbStar=t.Radiobutton(left,text='star',variable=shape,value='star')
    clear=t.Button(left,text='Clear',command=cls)
    
    rbLine.pack()
    rbRect.pack()
    rbOval.pack()
    rbStar.pack()
    clear.pack()

    #create/pack colors frame
    colors=t.Frame(main)
    black=t.Radiobutton(colors,bg='black',variable=color,value='black')
    white=t.Radiobutton(colors,bg='white',variable=color,value='white')
    red=t.Radiobutton(colors,bg='red',variable=color,value='red')
    blue=t.Radiobutton(colors,bg='blue',variable=color,value='blue')

    black.pack(side='left')
    white.pack(side='left')
    red.pack(side='left')
    blue.pack(side='left')

    #pack frames into main window & do mainloop
    left.pack(side='left')
    canvas.pack()
    colors.pack()
    t.mainloop()

#clear screer & reset selections
def cls():
    canvas.delete('all')
    color.set(None)
    shape.set(None)

#gather mouse position at time of button press
def click(eventorigin):
    global newX,newY
    newX=eventorigin.x
    newY=eventorigin.y
    '''print(newX,newY)'''
    
#gather mouse position at time of button release
def release(eventorigin):
    endX=eventorigin.x
    endY=eventorigin.y
    '''print(endX,endY)'''
    #call func to draw shapes
    printshape(newX,endX,newY,endY)

#draw appropriate shape
def printshape(newX,endX,newY,endY):
    #measurements for sizing
    distX=endX-newX
    distY=endY-newY

    if shape.get()=='line':
        canvas.create_line(newX,newY,endX,endY,
                           fill=color.get())
        
    if shape.get()=='oval':
        canvas.create_oval(newX,newY,endX,endY,
                           fill=color.get())

    if shape.get()=='rect':
        canvas.create_rectangle(newX,newY,endX,endY,
                                fill=color.get())
        
    if shape.get()=='star':
        canvas.create_polygon(newX+.5*distX,newY,
                              newX+.65*distX,newY+.4*distY,
                              endX,newY+.4*distY,
                              newX+.8*distX,newY+.62*distY,
                              newX+.9*distX,endY,
                              newX+.5*distX,newY+.7*distY,
                              newX+.1*distX,endY,
                              newX+.2*distX,newY+.62*distY,
                              newX,newY+.4*distY,
                              newX+.38*distX,newY+.4*distY,
                              newX+.5*distX,newY,
                              fill=color.get())



    
#main prog as func
shapes()
