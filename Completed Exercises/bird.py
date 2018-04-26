"""
Bird Object.

DO NOT MODIFY
"""

class Bird :

  def __init__(self, color_in) :
    self.color = color_in

  def birdcall(self) :
    print("Generic Bird Sound!")

  def getcolor(self) :
    return self.color
