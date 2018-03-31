##              (p)ete's (inp)ut module

'''------------- grinp():
"prompt" user & loop to (g)et (r)ight (inp)ut from user based on validation
reqs; passes selected arguements to isvalid(); displays "msg" as required'''
def grinp(prompt,msg=None,ok='anso',fi=None,hi=None,lo=None,mu=None):
    validInput=input(prompt)
    while not isvalid(validInput,ok,fi,hi,lo,mu):
        if msg!=None: print(msg)
        validInput=(input(prompt))
    return validInput


'''------------- isvalid():
checks "test" input to meet validation reqs as called via optional arguments;
returns False when proscribed validation specs are encountered'''
def isvalid(test,ok='anso',fi=None,hi=None,lo=None,mu=None):
    #test for float & int conversion
    if fi=='f':
        try: test=float(tested)
        except: return False
    if fi=='i':
        try: test=int(float(tested))
        except: return False
    #without menu:
    if mu==None:
        #test for proscribed chars
        for ch in str(test):
            if ch.isalpha() and 'a' not in ok or ch.isdigit() and 'n' not in\
               ok or ch.isspace() and 's' not in ok or not ch.isalnum() and not\
               ch.isspace() and 'o' not in ok: return False
        #check for hi and lo values
        try: return lo<=float(test)<=hi
        except:pass
    #with menu:
    else:
        if type(mu)==str and str(test).upper()!=mu.upper(): return False
        if test not in mu: return False
    #only one way this returns True!!!
    return True
