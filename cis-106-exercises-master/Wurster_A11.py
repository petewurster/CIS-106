'''
customer spec: tip calculator with percentage slider; buttons to calculate,
        reset, and quit
added feature: code marked ### (at end of line) is for optional feature to
        include PA sales tax in the calculated total; tax is only levied on
        the amount input by the user; to enable this feature, remove ###
        from left margin
'''

import tkinter as tki

def assignment11():
    main=tki.Tk()
    main.wm_title('Tip Calculator')
    main.geometry('242x166')

    #build/pack entry frame
    fr_entry=tki.Frame(main)
    entry_label=tki.Label(fr_entry,text='Enter bill amount:   $')
    global amount
    amount=tki.Entry(fr_entry,width=8)
    entry_label.pack(side='left')
    amount.pack(side='left')

    #build/pack slide frame
    fr_slide=tki.Frame(main)
    slide_label=tki.Label(fr_slide,text='Tip Amount (%):')
    global slide
    slide=tki.Scale(fr_slide,from_=0,to=50,orient='horizontal',
                    tickinterval=10,length=150)
    global total
    global total_text
    total_text=tki.StringVar()
    total_label=tki.Label(fr_slide,textvariable=total_text)
    slide_label.pack()
    slide.pack()
    total_label.pack()

    #bulid/pack button frame
    fr_button=tki.Frame(main)
    calc_btn=tki.Button(fr_button,text='Calculate Tip',command=calculate)
    reset_btn=tki.Button(fr_button,text='Reset',command=reset)
    quit_btn=tki.Button(fr_button,text='Quit',command=main.destroy)
    calc_btn.pack(side='left')
    reset_btn.pack(side='left')
    quit_btn.pack(side='left')

    #build/pack check box to switch on tax###
    fr_switch=tki.Frame(main)###
    global switch###
    global switch_text###
    switch_text=tki.StringVar()###
    switch=tki.IntVar()###
    tax_switch=tki.Checkbutton(fr_switch,textvariable=switch_text,###
                               variable=switch)###
    tax_switch.pack(side='bottom')###
  
    #pack frames into main window & enter loop
    fr_entry.pack(side='top')
    fr_slide.pack()
    fr_button.pack(side='bottom')
    fr_switch.pack(side='left')###

    #set init values
    reset()
    tki.mainloop()

#changes the "total" to 1.x times the entered amound (x comes from slider)
def calculate():
    total=float(amount.get())*(1+float(slide.get())/100)
    if switch.get()==1: total+=float(amount.get())*.08###
    total=str(format(total,',.2f'))
    total_text.set('Total Amount:  $ '+total)
    switch_text.set('include PA sales tax (8%):  $ '+###
                    str(format(float(amount.get())*.08,',.2f')))###

#reset field, label, and slider position
def reset():
    slide.set(30)
    total_text.set('Total Amount:')
    amount.delete(0,'end')
    switch.set(0)###
    switch_text.set('include PA sales tax (8%) :  ')###

#run main prog
assignment11()
