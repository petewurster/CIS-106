'''
random number 1-100 is selected; user guesses up to 8 times;
hints are given after 1st guess... data-type input validation
left out for sake of simplicity
'''

#main func; sets start values and inits game
def ex03():
    from random import randint
    pcNum=randint(1,100)
    print('You have 8 tries to guess the correct number from 1 to 100.')
    yourNum=int(input('What\'s your guess? '))
    #initiate recursive loop, set max recursion depth to 7
    numGuess(yourNum,pcNum,7)
    
#recursive func processes guess & displays results
def numGuess(you,pc,tri):
    if you==pc:
        print('\nCorrect!\nYou got it on try #',8-tri,'!\n',sep='')
        input('press ENTER to quit')
    #re-prompt w/hints as needed
    else:
        if tri>0:
            print('Too', ('low' if you<pc else 'high'),end='; ')
            you=int(input('guess again. '))
            #call self for retry
            numGuess(you,pc,tri-1)
        #out of recursive loop == game over
        else:
            print('\nOut of guesses!  The number was ',pc,'.\n',sep='')
            input('press ENTER to quit')
        
#run example 3
ex03()
