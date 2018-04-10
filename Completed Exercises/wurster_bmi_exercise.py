"""
Body Mass Index Calculator
"""

def bmiCalc():
    #create dictionary as BMI database
    ptBMIdata={}
    print('      -------BMI Evaluation-------')
    ptNum=int(input('How many patients will be evaluated? '))
    #gather patient information
    for x in range(ptNum):
        ptID=int(input('\nEnter patient\'s 4-digit ID:'))  
        hgt=float(input('Patient\'s height (inches):'))
        wgt=float(input('Patient\'s weight (pounds):'))
        #calculate BMI for current patient
        bmi=round((wgt*703)/(hgt*hgt),2)
        #store data in BMI database
        ptBMIdata[ptID]=bmi
    #recall patient data and display BMI for all patients in database
    keys=ptBMIdata.keys()
    print()
    for x in keys:
        ptID=x
        bmi=ptBMIdata.get(ptID)
        print('BMI for patient #',ptID,' is ',bmi,sep='')
        if bmi<18.5:
            print('.....this patient is underweight.\n')
        elif bmi>=18.5 and bmi<=25:
            print('.....this patnent is an ideal weight.\n')
        else:
            print('.....this patient is overweight.\n')
    return ptBMIdata

bmiCalc()

