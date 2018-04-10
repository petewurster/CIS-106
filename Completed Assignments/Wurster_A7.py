'''
customer spec: gather yearly rainfall data; output high/low/average
        monthly rainfall; reject negative data entries
added feature: display multiple months in case months tie for highest
        or lowest rainfall
'''

#main prog as func
def assignment07():
    #assign strings to list for user-friendly prompt
    months=['Jan','Feb','March','April','May','June','July',
            'Aug','Sept','Oct','Nov','Dec']
    records=[]
    print('Enter inches of rainfall for each month as prompted.\n')
    #loop for 12 entries; validate input
    for m in months:
        data=-1
        while data<0:
            try:
                data=float(input(m+': '))
                #cause deliberate exception to streamline exception handling
                if data<0: raise ValueError         
                records.append(data)
            #handle negative entries & alpha entries
            except ValueError:
                print('Invalid input for ',end='')
    #display results
    print('\nAverage monthly rainfall:',format(sum(records)/12,'.2f'),'in')
    print('\tYearly rainfall:',format(sum(records),'.2f'),'in')
    print('Month(s) with most rain: ',end='')
    #iterate across records/months in parallel & display max rainfall month(s)
    for value in range(len(records)):
        if records[value]==max(records):
            print(months[value],end=' ')
    print('\nMonth(s) with least rain: ',end='')
    #iterate across records/months in parallel & display min rainfall month(s)
    for value in range(len(records)):
        if records[value]==min(records):
            print(months[value],end=' ')

#run prog
assignment07()

























































































