def pcGuess(num,mod,trys):
    print ('is it ',num,'?',sep='')
    print ('\t\t(h)igher\t(l)ower\t\t(y)es')
    ans=input('? ')
    mod=int(round(mod/2,0))
    if ans=='y':
        print('I got it on try #',8-trys,'!',sep='')
        input('press ENTER to quit')
        exit()
    elif ans=='h':
        num=num+mod
        if num==99 and trys==1: num=100
    elif ans=='l':
        num=num-mod
    if trys>0:
        pcGuess(num,mod,trys-1)

print('Think of a number from 1 to 100.  I\n'
      'will guess your number within 8 trys\n')
input('\npress ENTER to begin')
print('\n')
    
pcGuess(50,50,7)
