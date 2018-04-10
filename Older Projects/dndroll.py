import pdefs #pete's def's


#roll stats until acceptable to save
slot='r'
while slot=='r':
    stat=[]
    #roll 4 dice, sum highest 3::do 6 times & display results
    for x in range (6):
        roll=[pdefs.rnd(6), pdefs.rnd(6), pdefs.rnd(6), pdefs.rnd(6)]
        print(roll)
        roll.sort()
        del(roll[0])
        stat.append(sum(roll))
    print(stat)
    #prompt user to where to save
    print('\n\nSave to which slot?       (1)    (2)    (3)    (r)e-roll stats')
    slot=pdefs.keyp('123r')

#save stats to selected file; overwrite existing file data
pdefs.psave(slot,stat)

