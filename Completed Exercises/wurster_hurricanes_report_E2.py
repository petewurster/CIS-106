'''
customer spec: convert source .txt file into a .csv file
'''

#main prog as func
def exercise9(count):
    #open source file
    with open(r'hurricanes.txt','r') as txt:
        #open conversion output file
        with open(r'hurricane.csv','w') as csv:
            #read first line from source to prime loop
            line=txt.readline().rstrip()
            #loop until no more data to read
            while line!='':
                #when a year date is encountered...
                if line.isdigit():
                    #write sum of prev year & advance cursor in csv file
                    if count!=-1: csv.write(str(sum(count))+'\n')
                    #write new year entry to csv file
                    csv.write(line+',')
                    #clear previous year totals
                    count=[]
                #append yearly total when monthly entry is encountered
                else: count.append(int(line[4:]))
                #read next line to advance loop
                line=txt.readline().rstrip()
            #write total for last year processed to csv file
            csv.write(str(sum(count)))
            
#run prog with init condition so that 'count' is not written in 1st iteration
exercise9(-1)
