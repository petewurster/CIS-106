'''
customer spec: GUI to convert miles to kilometers; include "quit" button;
        use 0.6214 as the conversion factor
added feat: permit two-way conversion; permit user to set output decimal position
'''

import tkinter as tki
import tkinter.messagebox

#conversion prog
def exercise11():
    #init window
    main=tki.Tk()
    main.wm_title('Let\'s Convert!')
    main.geometry('240x140')
    main.resizable(0,0)
    
    #build/pack entry frame
    fr_entry_box=tki.Frame(main)
    e_label=tki.Label(fr_entry_box, text='Distance :    ')
    global entry
    entry=tki.Entry(fr_entry_box, width=10)
    e_label.pack(side='left')
    entry.pack(side='left')
    
    #build/pack radio frame
    fr_radio=tki.Frame(main)
    global convert
    convert=tki.IntVar()
    convert.set(0)
    rb_mile=tki.Radiobutton(fr_radio,text='miles to kilometers',
                                variable=convert,value= 1)
    rb_kilo=tki.Radiobutton(fr_radio,text='kilometers to miles',
                                variable=convert,value= 2)
    rb_mile.pack()
    rb_kilo.pack()
    
    #build/pack button frame
    fr_button=tki.Frame(main)
    btn_convert=tki.Button(fr_button,text='     Convert     ',
                            command= do_conversion)
    btn_quit=tki.Button(fr_button,text='Quit',
                            command= main.destroy)
    space=tki.Label(fr_button,text='   ')
    btn_quit.pack(side='right')
    space.pack(side='right')
    btn_convert.pack(side='right')

    #build scale
    global scale
    scale=tki.Scale(main,from_=0,to=10,orient='horizontal')
    scale.set(3)
 
    #pack main window & enter loop
    fr_entry_box.pack()
    fr_radio.pack()
    fr_button.pack()
    dp=tki.Label(main,text='\t(decimal pos)')
    dp.pack(side='left')
    scale.pack(side='left')
    tki.mainloop()

#do conversion & display results in message box
def do_conversion():
    whichway=convert.get()
    result=float(entry.get())
    start=result
    
    if whichway==1:
        result/=0.6214
        tki.messagebox.showinfo((str(round(start,scale.get()))+' miles ='),
        (round(result,scale.get()),'kilometers'))
    if whichway==2:
        result*=.6214
        tki.messagebox.showinfo((str(round(start,scale.get()))+' km ='),
                                (round(result,scale.get()),'miles'))

#let's convert!
exercise11()
    
