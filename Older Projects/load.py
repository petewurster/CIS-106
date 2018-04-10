import pdefs
print('Load which game?    (1)     (2)     (3)     e(x)it')
slot=pdefs.keyp('123x')
if slot=='x':
    exit()
     
stat=pdefs.pload(slot)
print(stat)
input('\n\n\n                 press Enter to exit')
