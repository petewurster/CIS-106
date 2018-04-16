'''
Wurster
'''

class Temperature:
    #create a Temperature conversion object
    def __init__(self): self.__ftemp=1.0

    #create setter func
    def settemperature(self,ftempin):
        #reject invalid entries
        try: self.__ftemp=float(ftempin)
        except Exception as error: print('\t',error) 

    #create getter funcs
    def gettemperature(self): return self.__ftemp
    def tocelcius(self): return (self.__ftemp-32)*(5/9)
    def tokelvin(self): return (self.__ftemp+459.67)*(5/9)
