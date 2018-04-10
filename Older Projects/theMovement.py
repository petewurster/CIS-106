#flavor text
print('Simulate the rise & fall a social action movement!\n'
      'Manage your Funds, build your Legal clout, and keep\n'
      'the Media interested while you continue to attract\n'
      'Supporters.  How much support can you muster?  How\n'
      'many weeks will your movement last!?')
#create vars w/null values so they don't prematurely affect my sub-defs
week,media,legal,funds,actn,score,event=0,0,0,0,'zzzz',0,0
import random

#main prog written as a func
def movement():
    #re-set vars to start values
    week,media,legal,funds,actn,score,amt=1,10,10,10,'zzzz',10000,0
    #loop until a stat falls too low
    while media>0 and legal>0 and funds>0 and score>0:
        random.seed()
        #max value for stats is 20 due to bar graphs displaying in percentage
        if media>20: media=20
        if legal>20: legal=20
        if funds>20: funds=20
        #show stats
        showStat(media,legal,funds,score,week)
        #win condition kicks prog out of loop early
        if media==20 and legal==20 and funds==20:
            break
        #menu is defined as a func to de-clutter main prog
        actn=showMenu()
        week+=1
        #user selects action category, but prog randomly chooses the
        #event in the chosen category
        event=random.randint(1,10)
        print()
        if actn=='m' or actn=='M':
            media,legal,funds,score,amt=mediaStunts(media,legal,funds,score,event)
        elif actn=='l' or actn=='L':
            media,legal,funds,score,amt=legalStatus(media,legal,funds,score,event)
        elif actn=='f' or actn=='F':
            media,legal,funds,score,amt=getMoney(media,legal,funds,score,event)
        #display score
        if actn!='zzzz':
            print('The movement',end=' ')
            if amt>0: print('gained',amt,end=' ')
            else: print('lost',amt,end=' ')
            print('supporters!')
    #end conditions, display why user lost
    if media==20 and legal==20 and funds==20:
        print()
        print('The movement will never be stronger than it is right\n'
              'now, and the corporate fat-cats can see the writing on\n'
              'the wall!\n')
        print('Hold your breath for the next game, where you will\n'
              'act as the charismatic leader in our exciting Cult\n'
              'Simulator!')
    else:
        print('\n\nYour movement has failed because')
        if media<1:
            print('one of the Kardashians had another surgery and\n'
                  'being a human-centipede is now the latest rage!')
        if legal<1:
            print('the court system considers your claims to be\n'
                  'frivolous.  There will be no more appeals.')
        if funds<1:
            print('social justice ain\'t cheap!')
        if score<1:    
            print('it\'s just no longer socially relevant.')
    print()

#these events are all supposed to raise MEDIA but also modify other stats
def mediaStunts(m,l,f,s,e):
    if e==1:
        print('One of your supporters steps forward with a claim\n'
              'that a crooked politician molested her pet snake!\n'
              'Animal lovers are outraged!\n\n'
              '*Media UP!    *Legal DOWN!')
        m+=4
        l-=1
        amt=random.randint(400,600)
        s+=amt
    elif e==2:
        print('You throw an expensive gala.  If not for the hand-\n'
              'ful of celerbity attendees, it woulda been a total\n'
              'failure.\n\n'
              '*Media UP!    *Funds DOWN!')
        m+=5
        f-=2
        amt=random.randint(300,700)
        s+=amt
    elif e==3:
        print('Your Scientologist-outreach campaign is taking\n'
              'Hollywood by storm!  Traditional faith organizations\n'
              'are becoming big donors!\n\n'
              '*Media UP!    *Funds UP!    *Legal DOWN!')
        m+=6
        l-=2
        amt=random.randint(2000,4000)
        s+=amt
        f+=3        
    elif e==9:
        print('Nothing like a good old-fashioned riot!  Its a\n'
              'shame we didn\'t loot enough to cover the bail for\n'
              'our supporters that got arrested.\n\n'
              '*Legal Down!    *Funds Down!    *Media UP!')
        m+=10
        f-=5
        l-=8
        amt=random.randint(10000,20000)
        s+=amt
    elif e==10:
        print('No matter how peaceful you try to keep things,\n\n'
              'there\'s always some lunatic makin bomb threats!\n'
              'Yeah it gets attention, but it scares away too many\n'
              'sympathizers.\n\n'
              'Legal DOWN!    *Media UP!')
        m=20
        l-=10
        amt=0-random.randint(5000,10000)
        s+=amt
    else:
        print('Picketing outside Trump Tower is always a popular\n'
              'idea...  Too bad we get sued every time!\n\n'
              '*Media UP!    *Funds DOWN!    *Legal UP!')
        m+=1
        f-=e/2
        amt=e*random.randint(1000,2000)
        s+=amt
    return m,l,f,s,amt

#these events are all supposed to raise LEGAL but also modify other stats
def legalStatus(m,l,f,s,e):
    if e<=4:
        print('Trump sues your organization for slander.....\n'
              'again.\n\n'
              '*Legal UP!    *Funds DOWN!')
        l+=3
        f-=5
        amt=random.randint(500,1000)
        s+=amt
    elif e==5:
        print('The ACLU just exonerated one of your celebrity\n'
              'supporters.\n\n'
              '*Legal UP!    *Media UP!')
        l+=5
        m+=1
        amt=random.randint(4000,6000)
        s+=amt
    elif e==6:
        print('Subsidy cutbacks have the farmers in an uproar!\n'
              'They\'re no longer contributing, but everybody in the\n'
              'corn belt is mobilizing to join!\n\n'
              '*Funds DOWN!    *Legal UP!')
        l+=1
        f-=5
        amt=random.randint(5,99)
        s+=amt
    elif e==7:
        print('We won over another state in our marijuana legalization\n'
              'campaign!  Donations are rolling in from other localities\n'
              'that want our help!\n\n'
              'Funds UP!    Legal UP!    Media UP!')
        l+=8
        f+=2
        m+=1
        amt=random.randint(10000,30000)
        s+=amt
    elif e==10:
        print('Another popular social welfare program bites the dust!\n'
              'Our supporters don\'t have time to protest because they\n'
              'are taking on second jobs to feed their kids.\n\n'
              '*Legal UP!    *Media UP!')
        l+=1
        m+=2
        amt=0-random.randint(1000,9000)
        s+=amt
    else:
        print('It ain\'t always full of media-swamped congressional\n'
              'hearings... Even a small win is still a win brother!\n\n'
              '*Legal UP!')
        l+=3
        amt=0
    return m,l,f,s,amt

#these events are all supposed to raise FUNDS but also modify other stats
def getMoney(m,l,f,s,e):
    if e==1:
        print('Bake sales seem like a good idea, but people have a\n'
              'hard time taking you serious when it\'s your primary\n'
              'source of revenue.\n\n'
              '*Funds UP!    *Media DOWN!')
        f+=1
        m-=1
        amt=0-random.randint(1000,2000)
        s+=amt
    elif e==2:
        print('A candle-light vigil always strikes a chord with the\n'
              'religious community.  Solid fundraising strategy, amen!\n\n'
              '*Media UP!    *Funds UP!')
        m+=2
        f+=7
        amt=random.randint(1000,2000)
        s+=amt
    elif e==3:
        print('Ever since Warren Buffett decided to use us as a tax\n'
              'write-off, the money just keeps flowing in!\n\n'
              '*Funds UP!')
        f+=12
        amt=0
    elif e==4:
        print('After our latest \'Down with Trump!\' fund raiser, the\n'
              'President banned another news network from covering our\n'
              'movement!\n\n'
              '*Media DOWN!    *Funds UP!')
        f+=2
        m-=5
        amt=0
    elif e==7:
        print('What\'s with these finance officers always embezzling?\n'
              'He got caught, but his heart was in the right place:  He\n'
              'placed big bets in Vegas ',end='')
        amt=random.randint(300,10000)
        if amt%2==0:
            print('and won!  He\'s donating the winnings!\n\n'
                  '*Legal DOWN!    *Funds UP!    *Media UP!')
            f+=7
        else:
            print('and lost it all!\n\n'
                  '*Legal DOWN!    *Funds DOWN!    *Media UP!')
            f-+7
        l-=3
        m+=1
        amt=0-amt
        s+=amt        
    else:
        print('Good thing we can crowdsource our funding through tech\n'
              'companies like Facebook or GoFundMe or whatever.  If only\n'
              'it was a more reilable recruitment tool.\n\n'
              '(*Funds UP!    *Media UP!    *Legal DOWN!')
        f+=3
        m+=1
        l-=1
        amt=random.randint(200,5000)
        s+=amt        
    return m,l,f,s,amt

#display stat bars each segment is 10%
def showStat(m,l,f,s,w):
    print('\n---------------------------------------')
    print('MEDIA [',end='')
    for x in range(1,11):
        y=int(m/2)
        if x<=y: print('#',end='')
        else: print(' ',end='')
    print(']           SUPPORTERS')
    print('LEGAL [',end='')
    for x in range(1,11):
        y=int(l/2)
        if x<=y: print('=',end='')
        else: print(' ',end='')
    print(']           ',format(s,','))
    print('FUNDS [',end='')
    for x in range(1,11):
        y=int(f/2)
        if x<=y: print('$',end='')
        else: print(' ',end='')
    print(']              WEEK',w)
#show menu and limit user input to valid selections
def showMenu():
    while True:
        print('---------------------------------------')
        print('increase       improve         secure')
        print('(M)edia        (L)egal        (F)unding')
        print('coverage       position\n')
        actn=input('How do you wanna help the movement?')
        if actn=='exit': exit()
        elif actn not in 'mlfMLF':
            print('\nThat ain\'t helpin\' the cause brother!\n')
        else: return actn
#run prog
movement()
#pause before exit so user can read ending messages
input('press ENTER to exit')
exit()
