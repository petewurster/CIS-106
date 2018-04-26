'''
Create a subclass of the Bird object (bird.py) named Owl

Include one initializer in this class that accepts a String argument
Name the parameter color_in and use its value to initialize the superclass.
No other functions should be called in the initializer.
No fields should be created in the initializer.

Override the superclass's birdCall method so when called, it prints "Hoot!"

Do not include any other, additional functions.
'''

from bird import Bird

class Owl(Bird):
    def __init__(self,color_in):
        #validate for "color"
        if isinstance(color_in,str): Bird.__init__(self,color_in)
        else: raise TypeError('Color parameter requires "str" Data-Type')
    #override superclass "birdcall"
    def birdcall(self): print('Hoot!')




































#Wurster_ex_14
