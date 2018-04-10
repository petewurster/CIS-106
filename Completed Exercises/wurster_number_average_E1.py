'''
prompt user input for 2 numbers & calc average (round up)
customer spec: 1st==1-50
               2nd==51-100
               re-prompt for entries outside of range
added feats:   re-prompt for invalid data type
'''
#main prog function
def avg_of2():
    #set initial conditions
    n1_50,n51_100=0,0
    #loop until no data errors AND 2nd number is in range
    while n51_100<51 or n51_100>100:
        try:
            #loop until 1st number is in range
            while n1_50<1 or n1_50>50:
                n1_50=float(input('Enter a number from 1-50: '))
                inRange(1,50,n1_50)
            n51_100=float(input('Enter a number from 51-100: '))
            inRange(51,100,n51_100)
        #handle improper user input
        except ValueError:
            print ('Invalid data type.  Please try again.')
    #display the average of 1st & 2nd number
    print('The average of ',n1_50,' and ',n51_100,' is ',
          format((n1_50+n51_100)/2,'.2f'),'.',sep='')

#create range test func
def inRange(a,z,num):
    if num<a or num>z:
        print('Number not in range.  Please pay attention to the prompt.')
    else: print()

#start program
avg_of2()
