'''
customer spec: European-style Roulette; validate user choice;
        display detailed results; enable re-play
extra feature: enable betting with proper payouts for various bets; to emulate
        the feeling of a real casino, this game encourages the user to play
        again by NOT offering a "play again" option, but instead automatically
        prompting the user for another bet... to quit playing, the user must
        place a bet of $0
'''

#main prog as func
def midterm(cash):
    bet=getbet(cash)
    #loops to play again via recursion as long as player is placing a bet>0
    if bet!=0:
        chip=placechip()
        print('\nYou bet on ',
              detcolor(chip)+' ' if type(chip)==int
              else '',chip,sep='',end=', ')
        result=spinwheel(randint(4,12))
        #display result
        print ('\t...it landed on the ',end='')
        print(detcolor(result),' ',result,'!',sep='',end=' ')
        #add or subtract appropriate amount
        cash+=payout(result,bet,chip)
        print()
        midterm(cash)

def payout(result,bet,chip):
    win=False
    #street
    if str(chip).startswith('street')==True:
        num=result
        if num<10:
            num='0'+str(result)
        if str(num) in chip:
            win=True
            payout=11
    #columns
    for x in range(1,4):
        if str(chip).endswith('mn '+str(x))==True:
            #loops to -3 from result to determine column of result
            while result>0:
                result-=3
            if result==-2 and chip=='column 1' or result==-1 and\
               chip=='column 2' or result==0 and chip=='column 3':
                win=True
                payout=2
    #basket
    if chip=='basket' and result>=0 and result<=3:
        win=True
        payout=6    
    #odds/evens
    try:
        if chip=='even' and result%2==0 or chip=='odd' and result%2!=0:
            win=True
            payout=1
    except: pass
    #red/black
    if chip==detcolor(result):
        win=True
        payout=1
    #high/low
    if chip=='high' and result>18 or chip=='low' and result<19 and result!=0:
        win=True
        payout=1
    #singles
    if result==chip:
        win=True
        payout=35
    #pay the winner
    if win==True:
        print('You won $',bet*payout,'!',sep='')
        return bet*payout
    #player loses
    else:
        print('The house wins again!')
        return 0-bet

def placechip():
    #bet options in a list for easier comparison of string values
    options=['high','low','odd','even','red','black','column','basket','street',\
             '0','1','2','3','4','5','6','7','8','9','10','11','12','13',\
             '14','15','16','17','18','19','20','21','22','23','24','25',\
             '26','27','28','29','30','31','32','33','34','35','36']
    print()
    print('bets: ',end='')
    for item in range(9):
        print (options[item],end='  ')
    print()
    chip=input('Choose a special bet or enter a number (0-36): ')
    #validate chip placement
    while chip not in options:
        chip=input('Choose a special bet or enter a number (0-36): ')
    #if chip is placed as a "single" convert to int
    try: chip=(int(chip))
    except: pass
    #chip is placed on a column
    if chip=='column':
        print('\n  column #1 includes: 1 4 7 10 13 16 19 22 25 28 31 34')
        print('  column #2 includes: 2 5 8 11 14 17 20 23 26 29 32 35')
        print('  column #3 includes: 3 6 9 12 15 18 21 24 27 30 33 36\n')
        x=0
        while int(x)<1 or int(x)>3:
            x=input('Please choose column 1, 2, or 3: ')
            while x.isdigit()==False:
                x=input('Please choose column 1, 2, or 3: ')
        chip+=' '+x
    #chip is placed on a street
    if chip=='street':
        streets=['1 2 3','4 5 6','7 8 9','10 11 12','13 14 15','16 17 18',\
                 '19 20 21','22 23 24','25 26 27','28 29 30','31 32 33','34 35 36']
        for x in range(1,37):
            print(x if x>9 else ' '+str(x),end=' ')
            if x%3==0:
                print()
        print('\nInclude a space between your selections.')
        while x not in streets:
            x=input('Please choose street: ')
        if x=='1 2 3': x='01 02 03'
        if x=='4 5 6': x='04 05 06'
        if x=='7 8 9': x='07 08 09'
        chip+=' '+x
    #return final chip designation
    return chip

def spinwheel(bounces):
    last=-1
    print('watch the ball bounce...')
    #show user where the ball bounces while wheel is spinning
    for x in range(bounces):
        result=randint(0,36)
        #prevent consecutive bouncing in the same slot
        if result==last:
            result-=35
            result=abs(result)
        last=result
        print(result,end='   ')
    print()
    return result

#determine color
def detcolor(x):
    if x==0: return 'green'
    if x%2==0 and x<11 or x%2==0 and x>18 and x<29 or x%2!=0 and x>10\
       and x<19 or x%2!=0 and x>28: return 'black'
    else: return'red'

#get users bet amount
def getbet(cash):
    bet=''
    print('****Let\'s play Roulette!!!****\n'
          '   (\"0\" will exit the game)\n')
    print('You have',cash,'dollars.')
    while bet.isdigit()==False:
        bet=input('How much do you want to bet? $')
        #validate for alpha chars
        if bet.isdigit()==False:
            print('You must enter a number!',end=' ')
        else:
            bet=int(bet)
            if bet==0: print('\nCome play again soon!')
            if bet<=cash: return bet
            #validate for insufficient funds
            if bet>cash:
                print('That\'s more than you have!',end=' ')
                bet=''
                
#acquire needed module
from random import randint

#run main prog    
midterm(5000)



