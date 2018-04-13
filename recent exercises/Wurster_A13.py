'''
use GUI to interact with Temperature object; prompt user to set Fahrenheit
temperature via mutator func and display converted temperatures via object's
accessor funcs
'''

import tkinter as t
import temperature

#main prog as func
def assignment_13():
    #declare relevant globals
    global converter,entry,celcius,kelvin

    #create instance of Tepmerature object
    converter=temperature.Temperature()

    #create GUI
    main=t.Tk()
    main.title('Wurster')
    main.geometry('210x100')

    #build entry box
    mainentry=t.Frame(main)

    entrylbl=t.Label(mainentry,text='° Fahrenheit')
    entrylbl.pack(side='right')

    entry=t.Entry(mainentry,width=6)
    '''     use Class accessor to display "__ftemp"     '''
    entry.insert(0,converter.gettemperature())
    entry.pack(side='right')

    #build celcius display area
    maincel=t.Frame(main)

    celcius=t.StringVar()
    celcius.set('= '+format(converter.tocelcius(),'.2f'))
    cel=t.Label(maincel,textvariable=celcius)
    cel.pack(side='left')
    
    clbl=t.Label(maincel,text='° Celcius')
    clbl.pack(side='left')

    #build kelvin display area
    mainkvn=t.Frame(main)

    kelvin=t.StringVar()
    kelvin.set('= '+format(converter.tokelvin(),'.2f'))
    kvn=t.Label(mainkvn,textvariable=kelvin)
    kvn.pack(side='left')
    
    klbl=t.Label(mainkvn,text='° Kelvin.')
    klbl.pack(side='left')

    #set conversion triggers
    action=t.Button(main,text='Convert',command=convert)
    main.bind('<Return>',enterkey)

    #pack & play
    mainentry.pack()
    maincel.pack()
    mainkvn.pack()
    action.pack()
    t.mainloop()

#define conversion funcs
def enterkey(event): convert()

def convert():
    '''     use mutator to set internal Class temp      '''
    converter.settemperature(float(entry.get()))
    '''     use Class accessors to display converted results    '''
    celcius.set('= '+format(converter.tocelcius(),'.2f'))
    kelvin.set('= '+format(converter.tokelvin(),'.2f'))

#execute prog
assignment_13()
