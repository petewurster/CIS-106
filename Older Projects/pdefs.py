'''
this prog holds all the defs that i wrote to for my RPG...  it also
imports any modules/functions that i needed to make it happen
'''

#import pete's most used
from random import random, seed     #need for random
from msvcrt import getch            #need for keyinput


#create random integer from 1 --> r
def rnd(r):
    seed()
    return int(random()*r)+1

#return keystroke as string char if within bounds of menu 
def keyp(menu):
    while True:
        select=getch()
        try:
            select=bytes.decode(select)
            if select in menu:
                return select
        except ValueError:
            pass    #arrow keys and some others

#save game to selected file
def psave(slot,stat):
    if slot=='1':
        save1=open('C:\\Users\\Hat\\AppData\\Local\\Programs\\Python\\Python36\\save1.txt','w')
        for line in range(len(stat)):
            save1.write(str(stat[line])+'\n')
        save1.close()
    if slot=='2':
        save2=open('C:\\Users\\Hat\\AppData\\Local\\Programs\\Python\\Python36\\save2.txt','w')
        for line in range(len(stat)):
            save2.write(str(stat[line])+'\n')
        save2.close()
    if slot=='3':
        save3=open('C:\\Users\\Hat\\AppData\\Local\\Programs\\Python\\Python36\\save3.txt','w')
        for line in range(len(stat)):
            save3.write(str(stat[line])+'\n')
        save3.close()

#load file into game
def pload(slot):
    stat=''
    if slot=='1':
        load1=open('C:\\Users\\Hat\\AppData\\Local\\Programs\\Python\\Python36\\save1.txt','r')
        for x in range (6):
            stat=stat+(load1.readline())
        load1.close()
    if slot=='2':
        load2=open('C:\\Users\\Hat\\AppData\\Local\\Programs\\Python\\Python36\\save2.txt','r')
        for x in range (6):
            stat=stat+(load2.readline())
        load2.close()
    if slot=='3':
        load3=open('C:\\Users\\Hat\\AppData\\Local\\Programs\\Python\\Python36\\save3.txt','r')
        for x in range (6):
            stat=stat+(load3.readline())
        load3.close()
    stat=stat.splitlines()
    for item in range(len(stat)):   stat[item]=int(stat[item])
    return stat



















            


        
