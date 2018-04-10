'''
analyze user-input string and display analysis
'''

#main prog as func
def countChars(x):
    #values set to zero to begin tallying
    up,low,dig,sym,sp=0,0,0,0,0
    #iterate across string 'x'
    for char in x:
        #test charachters and tally appropriately
        if char.isalpha():
            if char.isupper(): up+=1
            else: low+=1
        if char.isdigit(): dig+=1
        if not char.isalnum() and not char.isspace(): sym+=1
        if char.isspace(): sp+=1
    #display results
    print('\nstring length:',len(x))
    print('letters: ',up+low,'\t(uppercase:',up,'\tlowercase:',low,')',sep='')
    print('numbers:',dig)
    print('symbols:',sym)
    print(' spaces:',sp)

#calls function assigning user input directly to 'x'
countChars(input('Type the string to be analyzed: '))

    

