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
    global main,converter,entry,celcius,kelvin

    #create instance of Tepmerature object
    converter=temperature.Temperature()

    #create GUI
    main=t.Tk()
    main.title('Wurster')
    main.geometry('210x115')

    #build entry box
    mainentry=t.Frame(main)

    entrylbl=t.Label(mainentry,text='° Fahrenheit')
    entrylbl.pack(side='right')
    
    entry=t.Entry(mainentry,width=6)
    #use Class accessor to display "__ftemp"
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

    #set triggers
    action=t.Button(main,text='Convert',command=convert)
    console=t.Button(main,text='switch to CLI',command=cli)
    quitter=t.Button(main,text='Quit',command=exit)
    main.bind('<Return>',enterkey)

    #pack & play
    mainentry.pack()
    maincel.pack()
    mainkvn.pack()
    action.pack()
    console.pack(side='right')
    quitter.pack(side='right')
    t.mainloop()

#use command line to interact w/Temperature object
def cli():
    #close GUI window to minimize user distraction
    main.destroy()

    #create new Temperature object & loop for more conversions
    cliTemp=temperature.Temperature()
    
    x=''
    while x.lower()!='gui':
        #use Class accessors to display converted results
        print('\tWhen °F = ',format(cliTemp.gettemperature(),'.2f'),'...'
              ' °C = ',format(cliTemp.tocelcius(),'.2f'),' and °K = ',
              format(cliTemp.tokelvin(),'.2f'),sep='')

        #prompt user
        if x=='': print('\n["exit" quits; "gui" restarts GUI]'
                        '\nEnter a temperature to convert:')
        x=input('\n°Fahrenheit==> ')
        
        #quit program
        if x.lower()=='exit': exit()
        
        #use mutator to set internal Class temp
        cliTemp.settemperature(x)
        
    #re-launch GUI
    del cliTemp
    assignment_13()

#define conversion funcs
def enterkey(event): convert()

def convert():
#   use mutator to set internal Class temp
    converter.settemperature(entry.get())
#   use Class accessors to display converted results
    celcius.set('= '+format(converter.tocelcius(),'.2f'))
    kelvin.set('= '+format(converter.tokelvin(),'.2f'))

#execute prog
assignment_13()
