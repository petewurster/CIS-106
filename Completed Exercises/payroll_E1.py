'''
customer spec: enter employee data; calculate employee weekly pay;
        display total weekly expenses
added feats: permit input of differing wages for each employee;
        apply overtime calc to comply with Fair Labor Standards Act;
        exception handling; modular design permits importation      
'''

#main prog as func
def exercise07():
    #build multi-level list
    payroll=[]
    payroll.append(getnames(0))
    payroll=getwages(payroll)
    payroll=gethours(payroll)
    print('You owe:')
    payroll.append([])
    #defines payroll index level 3 via calc 
    for name in range(len(payroll[0])):
        salary=0
        try:
            #perform salary calcs
            wage=float(payroll[1][name])
            hour=float(payroll[2][name])
            if wage<0:wage=0
            if hour<0:hour=0            
            if hour>40:
                salary=(hour-40)*(1.5*wage)
                hour=40
            payroll[3].append(salary+hour*wage)
            #display individual salary
            print('\t',payroll[0][name],'\t$',format(payroll[3][name],'8,.2f'),sep='')
        except ValueError:
            payroll[3].append(0)
            #display error msg
            print('\t',payroll[0][name],'\tERROR: re-check input!',sep='')
    #display final results
    print('\nPayroll expenses this week: $',format(sum(payroll[3]),'8,.2f'),sep='')
    #return included for modular use
    return payroll

#defines payroll index level 1 via input loop
def getwages(payroll):
    payroll.append([])
    print('How much do you pay him/her per hour')
    for name in range(len(payroll[0])):
        payroll[1].append(input(payroll[0][name]+'? '))
    return payroll

#defines payroll index level 2 via input loop
def gethours(payroll):
    payroll.append([])
    print('How many hours did he/she work')
    for name in range(len(payroll[0])):
        payroll[2].append(input(payroll[0][name]+'? '))
    return payroll

#defines payroll index level 0 via input loop
def getnames(n):
    print('Enter your employee\'s names (enter "done" when finished)')
    names=[]
    names.append(input('  :'))
    while names[n]!='done':
        n+=1
        names.append(input('  :'))
    names.remove('done')
    return names

#run prog
exercise07()
