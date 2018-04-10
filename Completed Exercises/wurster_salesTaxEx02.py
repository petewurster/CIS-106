"""
Create a program that prompts the user to enter the amount of a purchase.
"""

while True:
    try:
        cost=float(input('What is the item\'s cost? $'))


        stTax,coTax= .062*cost, .03*cost
        cost+= stTax+coTax
        print('\nState sales tax @6.2% is $',format(stTax,',.2f'),sep='')
        print('County sales tax @3% is $',format(coTax,',.2f'),sep='')                                     
        print('Total sales tax is $',format(stTax+coTax,',.2f'),sep='')
        print('\nYour final price is $',format(cost,',.2f'),sep='')
        break
    except ValueError:
        print('\n\n\n\n\n\n\n WRONG INPUT')




        
        
