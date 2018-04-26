#Imports the Owl object
from owl import Owl

"""
Demonstrates an Owl Object.

Complete the Owl class in owl.py

DO NOT MODIFY ANY CODE IN THIS FILE.
If the Owl class is implemented correctly,
this program will run without errors.

"""

def main() :
  test_bird = Owl("brown")

  print("The color of this owl is", test_bird.getcolor())

  test_bird.birdcall()	
	
main()


