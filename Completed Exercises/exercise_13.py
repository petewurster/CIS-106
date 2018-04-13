'''
customer spec: demonstrate usage of the car object named "test_car";
        demonstrate proper effect for "accelerate" and "brake" functions;
        use "print" to demonstrate use of all 4 accessor functions
added feature: supplemental UML diagram is displayed in a dialogue window
        rather than as an (MS Word or MS Paint) attachment; uses a GUI to
        generate/manipulate the "test_car"
'''

import ex13
import tkinter as t

#main prog as a func
def cars():

    #declare globals
    global main,year,make,model,title
    main=t.Tk()
    main.wm_title('Car')

    #build entry boxes
    yearlbl=t.Label(main,text='year:')
    year=t.Entry(main,width=10)
    yearlbl.grid(row=1,column=1)
    year.grid(row=1,column=2)

    makelbl=t.Label(main,text='make:')
    make=t.Entry(main,width=10)
    makelbl.grid(row=2,column=1)
    make.grid(row=2,column=2)

    modellbl=t.Label(main,text='model:')
    model=t.Entry(main,width=10)
    modellbl.grid(row=3,column=1)
    model.grid(row=3,column=2)

    #build buttons
    about=t.Button(main,text='UML',command=uml)
    about.grid(row=0,column=0)

    createCar=t.Button(main,text='Create',command=drive)
    createCar.grid(row=3,column=3)

    #enter tkloop
    t.mainloop()

def drive():
    # declare globals
    global test_car,speed
    #Create test_car (allow exceptions to be raised for improper values)
    if year.get().isdigit(): test_car=ex13.Car(int(year.get()),make.get(),model.get())
    else: test_car=ex13.Car(year.get(),make.get(),model.get())

    #add labels onto main window
    lbl=t.Label(main,text='\tSpeed :')
    lbl.grid(row=0,column=2)
    
    speed=t.StringVar()
    speed.set(str(test_car.get_speed()))

    speedlbl=t.Label(main,textvariable=speed)
    speedlbl.grid(row=0,column=3)

    #add speed buttons onto main window
    slower=t.Button(main,text='Slower',command=slow)
    slower.grid(row=1,column=3)

    faster=t.Button(main,text='Faster',command=fast)
    faster.grid(row=1,column=4)

    main.wm_title(str(test_car.get_year())+' '+test_car.get_make())
    
    #print in console to meet customer requirements
    print(test_car)
    print('get_speed value= '+ str(test_car.get_speed()))
    print('get_year value= '+ str(test_car.get_year()))
    print('get_make value= '+ str(test_car.get_make()))
    print('get_model value= '+ str(test_car.get_model()))
    
#functions for speed buttons
def slow():
    test_car.brake(5)
    speed.set(str(test_car.get_speed()))
    print('get_speed value= '+ str(test_car.get_speed()))

def fast():
    test_car.accelerate(5)
    speed.set(str(test_car.get_speed()))
    print('get_speed value= '+ str(test_car.get_speed()))

#display UML on a canvas in a new window
def uml():
    diagram=t.Tk()
    diagram.wm_title('UML diagram')
    c=t.Canvas(diagram,height=360,width=300,background='black')
    c.pack()
    c.create_text(140,25,text='Car',font=('',24),fill='white')
    c.create_line(0,50,300,50,width=3,fill='white')
    c.create_text(55,65,text='__speed',font=('',16),fill='white')
    c.create_text(48,85,text='__year',font=('',16),fill='white')
    c.create_text(52,105,text='__make',font=('',16),fill='white')
    c.create_text(54,125,text='__model',font=('',16),fill='white')
    c.create_line(0,145,300,145,width=2,fill='white')
    c.create_text(139,160,text='__init__(year,make,model)',font=('',16),fill='white')
    c.create_text(51,180,text='__str__',font=('',16),fill='white')
    c.create_text(74,200,text='accelerate( )',font=('',16),fill='white')
    c.create_text(51,220,text='brake( )',font=('',16),fill='white')
    c.create_text(73,240,text='get_speed( )',font=('',16),fill='white')
    c.create_text(65,260,text='get_year( )',font=('',16),fill='white')
    c.create_text(69,280,text='get_make( )',font=('',16),fill='white')
    c.create_text(72,300,text='get_model( )',font=('',16),fill='white')
    #ok button
    ok=t.Button(diagram,text='ok',width=42,command=diagram.destroy)
    ok.pack()

#call main func
cars()
