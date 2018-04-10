"""
This program calculates the volume of a rectangular swimming pool.
"""

#dimensions in Meters
poolLength = 6
poolWidth = 3
poolDepth = 2

"""
My original solution:
poolVolCubeFt=poolLength*poolWidth*poolDepth*35.31
print(poolVolCubeFt)
"""

#calculation
poolVol=poolLength*poolWidth*poolDepth

#output with M->Ft conversion done in-line
print('for a pool with length:',poolLength,', width:',poolWidth,
      ', and depth:',poolDepth,' Meters...','\npool volume is ',
      poolVol,' cubic Meters...\nwhich converts to ',poolVol*35.31,
      ' cubic Feet',sep="")
