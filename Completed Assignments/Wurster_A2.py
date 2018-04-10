'''
prompt user for two points in a plane, calculate Euclidean distance, and
display result, *will loop back for re-prompt if alpha char is input*
'''

#####       FINAL REVISION: (previous version & changes noted below)

#acquire square root function from library
from math import sqrt

#test inputs for appropriate chars & loop to re-prompt if needed
while True:
    try:        
        #acquire user input as floats for conversionless calculation
        print('Please enter coordinates for 1st Point (P1).')
        x1=float(input('P1-coordinate x:'))
        y1=float(input('  \\coordinate y:'))
        print('\nPlease enter coordinates for 2nd Point (P2).')
        x2=float(input('P2-coordinate x:'))
        y2=float(input('  \\coordinate y:'))
        #calculation
        dist=sqrt((x2-x1)**2+(y2-y1)**2)
        #output uses sep to properly place punctuation at end of sentence
        print('\nThe distance between P1 and'
              'P2 is ',format(dist,'.2f'),'.',sep="")
        break #escape from loop

    except ValueError:
        #print error message; return to user prompts
        print('\n\n***  Whoopps, you must have mis-typed something!  ***'
              '\n***  Please try again using numerical characters. ***\n\n') 


#####       ORIGINAL SUBMISSION:
'''
#acquire square root function from library
from math import sqrt

#acquire user input; begin loop to repeat if alpha char is used
while True:
    print('Please enter coordinates for 1st Point (P1).')
    x1=(input('P1-coordinate x:'))
    y1=(input('  \\coordinate y:'))
    print('\nPlease enter coordinates for 2nd Point (P2).')
    x2=(input('P2-coordinate x:'))
    y2=(input('  \\coordinate y:'))

    #test inputs for alpha chars & depart loop if appropriate
    if x1.isalpha()==False and y1.isalpha()==False and x2.isalpha()==False and y2.isalpha()==False:
        break
       
    #prompt user to enter correct data (last statement in loop)
    print('\n\nWhoopps, you must have mis-typed something!'
           '\nPlease try again using numerical characters.\n\n')        

#convert input strings to float for use in calculation
x1=float(x1)
y1=float(y1)
x2=float(x2)
y2=float(y2)
#calculation
dist=sqrt((x2-x1)**2+(y2-y1)**2)

#output uses sep to properly place punctuation at end of sentence
print('\nThe distance between P1 and P2 is ',format(dist,'.2f'),'.',sep="")
'''


#####       AUTHOR'S NOTES:
'''
22 JAN 2018
I know that the loop and the logic were unnecessary and probably not expected
for this assignment, but I was so unhappy after accidentally typing an "r"
into the prompt x1=float(input('.....')) and having it rejected that I felt
like I HAD to do better...

I used my prior experience with TI-82 calculator programming along with the
index of the CIS 106 textbook to research a simple while-loop(p161) and some
string testing methods(p420).  Originally I used .isdigit()==True but changed
to .isalpha()==False due to .isdigit() not liking negatives or decimals.
The final product doesn't kick out all inappropriate input, but its the best
I could figure out as yet.

23 JAN 2018
The try command seems much more advanced than what I've produced here, but
it looks like a promissing solution to my data-type dilemma....

24 JAN 2018
Update!  try is WAY easier than I thought.  I'm sure I haven't mastered its
nuances but it seems to do exactly what I want!  Despite the new code being
only 3 lines shorter I'm much happier with the appearance as well!
'''
