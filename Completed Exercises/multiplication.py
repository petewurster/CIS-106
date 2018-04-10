#prime validation loops
r,c='',''
#loop to acquire func parameters
while r.isdigit()==False: r=input('Rows? ')
while c.isdigit()==False: c=input('Cols? ')

#main func creates multiplication table
def timesTable(lyst,rows,cols):
    #create rows
    for row in range(0,rows):
        lyst.append([])
        #fill rows & display table
        for col in range(0,cols):
            lyst[row].append((row+1)*(col+1))
            if lyst[row][col]<10: print(end=' ')
            if lyst[row][col]<100: print(end=' ')
            print(lyst[row][col],end=' ')
        print()
    return lyst

#pass empty list & parameters into main func
timesTable([],int(r),int(c))
   
    
