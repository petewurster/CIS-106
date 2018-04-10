'''
take user input month and date>1000, check for leap year
and display # of days per given month
'''

#main prog as a func
def assignment3():
    #acquire func to get current date & set init vars
    from datetime import datetime
    mm,yyyy,leapY,days=0,0,False,31
    monthStr={1:'January', 2:'February', 3:'March', 4:'April', 5:'May',
              6:'June', 7:'July', 8:'August', 9:'September', 10:'October',
              11:'November', 12:'December'}
    #loop until dates are within range of customer specs...
    while mm<1 or mm>12 or yyyy<1001:
        print('\nEnter a month & year some time AFTER the year 1000.')
        date=input('  (use MM/YYYY format):')
        #ensure user input==valid results; prompt user to re-input as needed
        try:
            date=date.split('/')
            mm,yyyy=int(date[0]),int(date[1])
            if mm<1 or mm>12: print('\nInvalid month!')
            if yyyy<1001: print('\nInvalid year!')
        except: print('\nPlease be sure to use the MM/YYYY format!\n')
    #run leap year test
    leapY=isLeap(yyyy)
    #determine #/days for user's selected month
    if mm==4 or mm==6 or mm==9 or mm==11: days=30 
    elif mm==2:
        days=28
        if leapY==True: days+=1
    print()
    #display result using proper grammar w/respect to past & future tense
    if yyyy>=datetime.now().year:
        print('There will be',days,'days in',monthStr.get(mm),yyyy,end='')
        if leapY==True:
            if mm==2: print(' because ', end='')
            else: print('; ',end='')
            print('it will be a leap year!')
    else:
        print('There were',days,'days in',monthStr.get(mm),yyyy,end='')
        if leapY==True:
            if mm==2: print(' because ', end='')
            else: print('; ',end='')
            print('it was a leap year!')
    if leapY!=True:
        print()

#func that tests for leap year (written as func to practice passing args/vars)
def isLeap(yyyy):
    if yyyy%4==0 and yyyy%100!=0 or yyyy%100==0 and yyyy%400==0:
        leapY=True
        return leapY

#run prog & pause display for user to view before exiting
assignment3()
input('\n---------------press ENTER to quit---------------')
exit()
