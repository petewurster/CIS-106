import tkinter as t

main=t.Tk()

up=t.Frame(main)

u1=t.Label(up,text='up up')
u2=t.Label(up,text='up dn')
u3=t.Label(up,text='up lf')
u4=t.Label(up,text='up rt')
u5=t.Label(up,text='U')

u1.pack(side='top')
u2.pack(side='bottom')
u3.pack(side='left')
u4.pack(side='right')
u5.pack()

dn=t.Frame(main)

d1=t.Label(dn,text='dn up')
d2=t.Label(dn,text='dn dn')
d3=t.Label(dn,text='dn lf')
d4=t.Label(dn,text='dn rt')
d5=t.Label(dn,text='D')


d1.pack(side='top')
d2.pack(side='bottom')
d3.pack(side='left')
d4.pack(side='right')
d5.pack()

lf=t.Frame(main)

l1=t.Label(lf,text='lf up')
l2=t.Label(lf,text='lf dn')
l3=t.Label(lf,text='lf lf')
l4=t.Label(lf,text='lf rt')
l5=t.Label(lf,text='L')


l1.pack(side='top')
l2.pack(side='bottom')
l3.pack(side='left')
l4.pack(side='right')
l5.pack()

rt=t.Frame(main)

r1=t.Label(rt,text='rt up')
r2=t.Label(rt,text='rt dn')
r3=t.Label(rt,text='rt lf')
r4=t.Label(rt,text='rt rt')
r5=t.Label(rt,text='R')

r1.pack(side='top')
r2.pack(side='bottom')
r3.pack(side='left')
r4.pack(side='right')
r5.pack()


up.pack(side='top')
dn.pack(side='bottom')
lf.pack(side='left')
rt.pack(side='right')

up.pack(side='top')
dn.pack(side='bottom')
lf.pack(side='left')
rt.pack(side='right')

c1=t.Label(main,text='m up')
c2=t.Label(main,text='m dn')
c3=t.Label(main,text='m lf')
c4=t.Label(main,text='m rt')
c5=t.Label(main,text='MAIN')

c1.pack(side='top')
c2.pack(side='bottom')
c3.pack(side='left')
c4.pack(side='right')
c5.pack()









t.mainloop()
