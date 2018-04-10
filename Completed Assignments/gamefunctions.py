'''
defines game functions for rock, paper, scissors prog (Wurster_A5)

customer spec: random number from 1-3 for computer choice;
    return appropriate strings for getRPS and whoWon; re-prompt
    user when entry is unacceptable
'''

#func gets random computer selection
def getRPS():
    from random import randint
    x=randint(1,3)
    comp='rock'
    if x==2: comp='paper'
    if x==3: comp='scissors'
    return comp

#func prompts user for selection
def getUserRPS():
    user=input('\nChoose rock, paper or scissors: ')
    #reprompr as needed; accept "scissor" OR "scissors"
    while user not in ('rock','paper','scissor','scissors'):
        print('Invalid entry. ',end='')
        user=input('Choose rock, paper or scissors: ')
    #maintain uniform string length for scissor(s)
    if user.startswith('s'): user='scissors'
    return user

#func compares string length to determine winner
#USED IN BOTH VERSIONS OF THE PROGRAM!!
def whoWon(comp,user):
    if comp==user: return 'tie'
    if len(comp)==4 and len(user)==8: return 'computer'
    if len(user)==4 and len(comp)==8: return 'user'
    if len(comp)>len(user): return 'computer'
    if len(comp)<len(user): return 'user'

##--------------------------------------------------------------------##
'''
These funcs ONLY needed for game theory simulation
'''

#computer selection
def getRPS_AI(result,comp):
    from random import randint
    #AI selects randomly if prev match tied
    if result=='tie':
        x=randint(1,3)
        comp='rock'
        if x==2: comp='paper'
        if x==3: comp='scissors'
        return comp
    #AI selects to exploit game theory
    else:
        if comp=='rock': return 'scissors'
        if comp=='paper': return 'rock'
        if comp=='scissors': return 'paper'

#user selection mimics game theory
def getUserRPS_AI(result,user):
    from random import randint
    #user keeps prev selection if they won
    if result=='user': return user
    #user selects randomly if prev match tied
    elif result=='tie':
        x=randint(1,3)
        user='rock'
        if x==2: user='paper'
        if x==3: user='scissors'
        return user
    #user changes selection if they prev lost
    else:
        x=randint(1,2)
        if x==1:
            if user=='rock': return 'scissors'
            if user=='paper': return 'rock'
            if user=='scissors': return 'paper'
        if x==2:
            if user=='rock': return 'paper'
            if user=='paper': return 'scissors'
            if user=='scissors': return 'rock'

#data tracking matrix
def trackData(result,comp,user,history):
    if comp=='rock': history[0][0]+=1
    if comp=='paper': history[0][1]+=1
    if comp=='scissors': history[0][2]+=1
    if user=='rock': history[1][0]+=1
    if user=='paper': history[1][1]+=1
    if user=='scissors': history[1][2]+=1
    if result=='computer': history[2][0]+=1
    if result=='user': history[2][1]+=1
    if result=='tie': history[2][2]+=1
    return history
