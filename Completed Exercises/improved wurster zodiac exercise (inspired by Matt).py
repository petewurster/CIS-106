#loops until valid user entry
def ex3():
    dd,mm=0,0
    #create dict for reference iterations
    zod={'Aquarius':21,'Pisces':51,'Aries':80,'Taurus':111,'Gemini':142,
         'Cancer':173,'Leo':204,'Virgo':235,'Libra':267,'Scorpio':297,
         'Sagittarius':327,'Capricorn':356}
    while True:
        print ('Using format MM/DD, please enter')
        date=input ('your birthday? ')
# i need to add more parameters, this only tests if date.split()==valid
        try:
            date=date.split('/')
            mm,dd=int(date[0]),int(date[1])
            break
        except: print('\nPlease be sure to use the proper format!\n')
    #run funcs to do the work
    jdate=jdatecalc(mm,dd)
    sign=zodloop(zod,jdate)    
    print ('Your zodiac sign is',sign)
    input()

#convert date to julian calender
def jdatecalc(a,b):
    jdate=0
    for x in range (1,a):
        if x==4 or x==6 or x==9 or x==11:
            jdate+=30
        elif x==2: jdate+=28
        else: jdate+=31
    jdate+=b
    return jdate

#iterate through dict, assign proper sign
def zodloop(a,j):
    sign='Capricorn'
    for key in a.keys():
        if j>=int(a.get(key)): sign=key
    return sign

#run exercise 3
ex3()
