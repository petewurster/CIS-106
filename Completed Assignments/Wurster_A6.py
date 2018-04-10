'''
customer spec: prompt user for start balance; validate user;
    input; read transaction files; calculate final balance
'''

#main prog as func
def assignment06(startBal):
    messages=[]
    #validate numerical input    
    while startBal==None:
        try: startBal=(float(input('Enter the start balance: ')))
        except ValueError: print('ERROR: Please enter a numerical value!')
    #displays results as values are pulled from files    
    print('\nWith a starting balance of $',format(startBal,',.2f'),'...',sep='')
    print('\t  credits totaling $',end='')
    #credit deposits to balance
    workingBal,messages=getTransaction(r'Deposits.txt',messages)
    newBal=startBal+workingBal
    print('       and debits totaling $',end='')
    #debit deposits from balance
    workingBal,messages=getTransaction(r'Withdrawals.txt',messages)
    newBal=newBal-workingBal
    print(' your final balance is now $',format(newBal,',.2f'),'.',sep='')
    print('\n',messages[0],'\n',messages[1])


#read & sum transactions
def getTransaction(filename,messages):
    workingBal=0
    #access specified file
    try:
        with open(filename,'r') as trans:
            #read 1st line to prime loop
            line=trans.readline()
            #loop until encountering blank line
            while line!='':
                #gather transaction amounts as floats & sum
                line=float(line)
                workingBal+=line
                line=trans.readline()
            #update message log
            messages.append(str(filename)+' read successfully!')
            print (format(workingBal,'.2f'),';',sep='')
    #handle exceptions & update message log
    except FileNotFoundError:
        messages.append(str(filename)+' encountered an error!')
        print ('* 0.00',sep='')
    return workingBal,messages

#prime start balance and run main prog
assignment06(None)

