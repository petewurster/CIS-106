'''
customer spec: read numbers from file and calculate total;
    display smallest & largest numbers in the set
'''
#main prog as func
def readNums(fileName,nums):
    #access file
    with open(fileName) as file:
        #read 1st line to prime loop
        line=file.readline()
        #loop until encountering blank line
        while line!='':
            #gather remaining data and package into list as integers
            line=int(line)
            nums.append(line)
            #read next line
            line=file.readline()
            
    #display results
    print(nums)
    print('The sum of the',len(nums),'#s, is',sum(nums))
    print('Smallest #:',min(nums))
    print('Largest #:',max(nums))

#run the prog
readNums(r'numbers.txt',[])
