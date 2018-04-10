'''
customer spec:  get 3 racer names & finish times;
                distribute awards appropritely;
                reject times if<=0 and re-prompt;
added feats:    reject times if improper data type
                logic includes proper ranking during ties
                re-prompt for duplicated names
'''

#main func
def assignment4():
    #init vars as null values to prime validation loops
    name1,name2,name3,time1,time2,time3='','','',0,0,0
    #loop until no data errors and all times are in spec range
    while time3<=0:
        try:
            #acquire racer info; re-prompt as needed
            while time1<=0:
                if name1=='':
                    name1=input('Who is racer #1? ')
                print('How many minutes did it take',name1,end='')
                time1=float(input(' to finish? '))
                testTime(time1)
            while time2<=0:
                if name2=='':
                    name2=input('Who is racer #2? ')
                    name2=dupNameTest(name1,name3,name2)
                print('How many minutes did it take',name2,end='')
                time2=float(input(' to finish? '))
                testTime(time2)
            if name3=='':
                name3=input('Who is racer #3? ')
                name3=dupNameTest(name1,name2,name3)
            print('How many minutes did it take',name3,end='')
            time3=float(input(' to finish? '))
            testTime(time3)
        #handle bad time inputs; prompt user
        except ValueError:
            print('Invalid data type.')
    #calculate awards
    rank1,rank2,rank3=rankWinner(time1,time2,time3)
    #display results
    print(name1,'won a',rank1,'medal!')
    print(name2,'won a',rank2,'medal!')
    print(name3,'won a',rank3,'medal!')

#func ensures unique names so award decisions are clearly understood
def dupNameTest(prevName1,prevName2,newName):
    while newName==prevName1 or newName==prevName2:
        print('A racer cannot have the exact same name as another')
        newName=input('racer, please enter another name: ')
    return newName

#func prompts user if times are out of spec range
def testTime(t):
    if t==0:
        print('Time cannot be zero!')
    elif t<0:
        print('Negative times are not accepted!')
    else: print()

#func distributes awards via logic array, ties handled according to
#standard competition ranking system
def rankWinner(t1,t2,t3):
    if t1==min(t1,t2,t3): r1='Gold'
    elif t1==max(t1,t2,t3): r1='Bronze'
    elif t1>min(t1,t2,t3) and t1<max(t1,t2,t3): r1='Silver'
    if t2==min(t1,t2,t3): r2='Gold'
    elif t2==max(t1,t2,t3): r2='Bronze'
    elif t2>min(t1,t2,t3) and t2<max(t1,t2,t3): r2='Silver'
    if t3==min(t1,t2,t3): r3='Gold'
    elif t3==max(t1,t2,t3): r3='Bronze'
    elif t3>min(t1,t2,t3) and t3<max(t1,t2,t3): r3='Silver'        
    return r1,r2,r3
    
#run prog
assignment4()













'''
original logic assigned awards based on "dense ranking system (aka 1223)";
replaced with simpler logic that handled ties more effectively and also
aligned with "standard competition ranking system  aka (1224)"
'''
#func distributes awards via logic array; tie scenarios marked with ##
##def rankWinner(t1,t2,t3,n1,n2,n3):
##    rank1,rank2,rank3=0,0,0
##    if t1==t2==t3: rank1=n1+', '+n2+', and '+n3+' all tied for a'##
##    if t1<t2 and t1<t3:
##        rank1=n1+' won the'
##        if t2==t3: rank2=n2+' and '+n3+' both tied for a'##
##        if t2<t3: rank2,rank3=n2+' won the',n3+' won the'
##        if t3<t2: rank3,rank2=n2+' won the',n3+' won the'
##    if t2<t1 and t2<t3:
##        rank1=n2+' won the'
##        if t1==t3: rank2=n1+' and '+n3+' both tied for a'##
##        if t1<t3: rank2,rank3=n1+' won the',n3+' won the'
##        if t3<t1: rank3,rank2=n1+' won the',n3+' won the'
##    if t3<t1 and t3<t2:
##        rank1=n3+' won the'
##        if t1==t2: rank2=n1+' and '+n2+' both tied for a'##
##        if t1<t2: rank2,rank3=n1+' won the',n2+' won the'
##        if t2<t1: rank3,rank2=n1+' won the',n2+' won the'
##    if t1==t2 and t1<t3:
##        rank1,rank2=n1+' and '+n2+' both tied for a',n3+' won the'##
##    if t2==t3 and t2<t1:
##        rank1,rank2=n2+' and '+n3+' both tied for a',n1+' won the'##
##    if t1==t3 and t1<t2:
##        rank1,rank2=n1+' and '+n3+' both tied for a',n2+' won the'##
##    return rank1, rank2, rank3
'''
earlier version concatenated the racer name with a string which was re-
assigned to a placement holder to ensure that 1st place was reported 1st
and last place was reported last. reporting sequence was sacrificed for
simpler logic that also ranked in "standard" format. concatenated string
rankings were replaced in favor of re-usable rank variables
'''
##    print(gold,'gold medal!')
##    if slvr!=0:
##        print(slvr,'silver medal!')
##    if brnz!=0:
##        print(brnz,'bronze medal!')





