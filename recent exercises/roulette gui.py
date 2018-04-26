import tkinter as t
import random

def rungame(x):
    global cash
    cash=x

    main=t.Tk()

    c=t.Canvas(main,height=300,width=300)
    c.grid(row=0,column=0)

    s123=t.Button(main,bg='white')
    s123.grid(row=2,column=1)

    r1=t.Button(main,text='1',bg='red')
    r1.grid(row=2,column=2)

    sp12=t.Button(main,bg='white')
    sp12.grid(row=2,column=3)

    
    b2=t.Button(main,text='2',bg='black',fg='white')
    b2.grid(row=2,column=4)





    t.mainloop()



rungame(500)
