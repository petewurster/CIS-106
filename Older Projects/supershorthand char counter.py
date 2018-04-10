string=input('String to analyze: ')
print('total letters: ',len(string))
print(type(sum(c.isdigit() for c in string)))
