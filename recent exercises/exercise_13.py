import ex13
import tkinter as t

#main prog as a func
def cars():
    global main
    main=t.Tk()
    main.wm_title('Test Drive')

    #declare globals
    global year,make,model,speed

    #build entry boxes
    yearlbl=t.Label(main,text='year:')
    year=t.Entry(main,width=10)
    yearlbl.grid(row=0)
    year.grid(row=0,column=1)

    makelbl=t.Label(main,text='make:')
    make=t.Entry(main,width=10)
    makelbl.grid(row=1)
    make.grid(row=1,column=1)

    modellbl=t.Label(main,text='model:')
    model=t.Entry(main,width=10)
    modellbl.grid(row=2,column=0)
    model.grid(row=2, column=1)

    about=t.Button(main,text='see UML',command=uml)
    about.grid(column=7)

    createCar=t.Button(main,text='Let\'s Drive',command=drive)
    createCar.grid(row=3,column=1)





    











    t.mainloop()
def drive():
    if year.get().isdigit(): test_car=ex13.Car(int(year.get()),make.get(),model.get())
    else: test_car=ex13.Car(year.get(),make.get(),model.get())
    new=t.Tk()
    lbl=t.Label(new,text='Speed:')
    lbl.grid(row=0,column=2)
    global aaa
    aaa=test_car.get_speed
    aaa=t.StringVar
    print(str(test_car.get_make))
    speedlbl=t.Label(new,textvariable=aaa)
    speedlbl.grid(row=1,column=2)
    

    
    print(test_car)

def uml():
    diagram=t.Tk()
    diagram.wm_title('UML diagram')
    canvas=t.Canvas(diagram,height=400,width=300,background='black')
    canvas.pack()
    
    ok=t.Button(diagram,text='          ok          ',command=diagram.destroy)
    ok.pack()

    

    

#call main func
cars()



