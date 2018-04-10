'''
customer specs: allow user to enter "paper", "rock", or "scissors";
    choose randomly for computer; print results based on value
    returned by whoWon(); prompt user to replay
'''
## For AI RPS simulation, comment out top half of prog and UNcomment
## bottom half.  Simulation demonstrates the theory stated in this
## video:    https://www.youtube.com/watch?v=rudzYPHuewc

## Basic theory is that in RPS... winners tend to make same choice
## as prev game; losers tend to select something other that what
## they lost with in last game

## In this sim, the "user" demonstrates the natural tendencies observed
## in the study, and the "computer" represents a player trying to exploit
## those tendencies...  THERE IS NO CHEATING DONE IN-CODE; the AI only
## considers its own previous choice and how well it did in the last game

#'''
#main prog as func
def assignment5():
    from gamefunctions import getRPS,whoWon,getUserRPS
    #acquire selections
    comp,user=getRPS(),getUserRPS()
    #compare selections
    result=whoWon(comp,user)
    #show results 
    print('\nThe computer chose ',comp,'.',sep='',end=' ')
    if result=='tie': print('It\'s a tie!\n')
    else: print('The',result,'wins!\n')


#runs main prog until user quits
while input('press ENTER to play Rock, Paper, Scissors\n'
            'or type "quit" to quit ')!='quit':
    assignment5()

#'''
##--------------------------------------------------------------------##

'''
#game theory AI simulation
def assignment5_AI(result,comp,user,times,history):
    from gamefunctions import getRPS_AI,getUserRPS_AI,whoWon,trackData
    comp=getRPS_AI(result,comp)
    user=getUserRPS_AI(result,user)
    result=whoWon(comp,user)
    #display results
    print('comp=',comp,'\tuser=',user,'\twinner=',result,sep='')
    #data tracking
    history=trackData(result,comp,user,history)
    #simulation recursion
    if times>0:
        assignment5_AI(result,comp,user,times-1,history)

#prime the simulator
times=int(input('How many times do you wanna run\n the simulation? '))-1
history=[[0,0,0],[0,0,0],[0,0,0]]

#run sim
assignment5_AI('tie','rock','rock',times,history)

#results summary
print()
print('      COMP          USER      [comp  user  Tie]')
print('  [R,  P,  S]   [R,  P,  S]   [win   win  Tie]')
print(history)
''' 
    

