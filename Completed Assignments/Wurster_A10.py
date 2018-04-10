'''
customer spec: convert user input to Morse code; add single space between
        "letters" and double space between words
added feat: also convert FROM Morse code; automatically recognize Morse input
        that matches customer specified spacing format; include int'l Morse
        numerals
'''

#main prog as function
def assignment10(string):
    #reformat & parse source string; insert placeholders so spaces not lost from
    #source during .split(); use 20 commas to avoid conflict with user input
    string=string.replace(' ',' ,,,,,,,,,,,,,,,,,,,, ').split()
    #name var to store conversion
    convertedString=[]
    #process data by segments
    for item in string:
        #re-inserts spaces removed during string tokenization
        if item==',,,,,,,,,,,,,,,,,,,,':
            convertedString.append(' ')
            continue
        #get appropriate code
        code=getCode(item.lower())
        #handle Morse data segment
        if item in code: convertedString.append(code[item])
        #process non-Morse string segment
        else:
            for char in item:
                char=char.lower()
                if char in code: convertedString.append(code[char]+' ')
                else: convertedString.append(char)
                #include parentheses around "." & "-" to avoid confusion
                #during mixed-data conversions
                if char=='.' or char=='-':
                    del convertedString[-1]
                    convertedString.append('(.)' if char=='.' else '(-)')
                    
    #display final conversion
    for item in convertedString: print(item,end='')
    #re-prompt for another conversion
    if string!=['exit']: assignment10(input('\n\n====> '))

#assign code to convert m-->a or a-->m as appropriate for each data segment
def getCode(segment):
    alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
           'r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8',
           '9','0']
    morse=['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---',
           '-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-',
           '...-','.--','-..-','-.--','--..','.----','..---','...--',
           '....-','.....','-....','--...','---..','----.','-----']
    if segment in morse: return dict(zip(morse,alpha))
    else: return dict(zip(alpha,morse))

#call main func primed with user input
print('Type something to convert TO or FROM Morse code! (For best results\n'
      'include space between Morse entries.  Type "exit" to quit.)')
assignment10(input('====> '))
