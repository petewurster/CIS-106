
import tkinter as tki



def assignment11():
    global main
    main=tki.Tk()
    main.wm_title('Tip Calculator')
    main.geometry('242x150')

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
  
    #pack frames into main window & enter loop
    fr_entry.pack(side='top')
    fr_slide.pack()
    fr_button.pack(side='bottom')
    reset()
   
    tki.mainloop()

#changes the "total" to 1.x times the entered amound (x comes from slider)
def calculate():
    total=float(amount.get())*(1+float(slide.get())/100)
    total=str(format(total,',.2f'))
    total_text.set('Total Amount:  $ '+total)

#reset field, label, and slider position
def reset():
    slide.set(30)
    total_text.set('Total Amount:')
    amount.delete(0,'end')      ##########


    #build/pack entry frame
##    fr_entry=tki.Frame(main)
##    entry_label=tki.Label(fr_entry,text='Enter bill amount:   $')
##    global amount
##    amount=tki.Entry(fr_entry,width=8)
##    entry_label.pack(side='left')
##    amount.pack(side='left')
##
##    fr_entry.pack(side='top')

    ##fr_entry=tki.Frame(main)
    ##amount=tki.Entry(fr_entry,width=8)

assignment11()
