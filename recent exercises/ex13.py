class Car:
    #create a Car, accept arguments for year, make, model, set speed==0
    def __init__(self,year,make,model):
        self.__speed=0
        if not isinstance(year,int):
            raise TypeError('arg for "year" needs to be an Int')
        else:
            if year<1886 or year>2018:
                raise Exception('valid production years are 1886-2018')
            else: self.__year=year
        if not isinstance(make,str):
            raise TypeError('arg for "make" needs to be a Str')
        else: self.__make=make.title()
        if not isinstance(model,str):
            raise TypeError('arg for "model" needs to be a Str')
        else: self.__model=model.title()

    #create getter funcs
    def get_speed(self): return self.__speed

    def get_year(self): return self.__year

    def get_make(self): return self.__make

    def get_model(self): return self.__model

    #create setter funcs
    def accelerate(self,x):
        self.__speed+=x

    def brake(self,x):
        self.__speed-=x
        if self.__speed<0: self.__speed=0

    #what am i?
    def __str__(self):
        return 'You\'re driving a '+str(self.__year)+' '+\
               str(self.__make)+' '+str(self.__model)+'.'
