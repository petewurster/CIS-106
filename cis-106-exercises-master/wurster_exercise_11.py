import tkinter

def exercise11():
    main=tkinter.Tk()
    main.wm_title("Distance Conversion Tool")
    
    #build entry frame
    fr_entry_box=tkinter.Frame(main)
    e_label=tkinter.Label(fr_entry_box, text= "Distance:")
    global entry
    entry=tkinter.Entry(fr_entry_box, width= 10)
    e_label.pack(side= "left")
    e_box.pack(side= "left")
    
    #build radio frame
    fr_radio=tkinter.Frame(main)
    global convert
    convert=tkinter.IntVar()
    convert.set(0)
    rb_mile=tkinter.Radiobutton(fr_radio, text= "Miles to Kilometers",
                                variable= convert, value= 1)
    rb_kilo=tkinter.Radiobutton(fr_radio, text= "Kilometers to Miles",
                                variable= convert, value= 2)
    rb_mile.pack()
    rb_kilo.pack()
    
    #build button frame
    fr_button_tkinter.Frame(main)
    btn_convert=tkinter.Button(fr_button, text= "Convert",
                            command= do_conversion)
    btn_quit=tkinter.Button(fr_button, text="Quit",
                            command= main.destroy)
    btn_convert.pack(side= "left")
    btn_quit.pack(side= "left")
    
    #pack main window & enter loop
    fr_entrybox.pack()
    fr_radio.pack()
    fr_button.pack()
    tkinter.mainloop()

def do_conversion():
    which=convert.get()
    
    if which==1:
        result=float(entry.get())/0.6214
        tkinter.messagebox.showinfo("Miles to Kilometers",result)
        
    if which==2:
        result=float(entry.get())*.6214
        tkinter.messagebox.showinfo("Kilometers to Miles",result)


exercise11()
    
