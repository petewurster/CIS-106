'''
customer spec: extract data from .txt source file and convert to .csv file
'''

#main prog as func
def assignment9():
    #access live files
    with open(r'randomaddresses.txt','r') as txt:
        with open(r'excel_addresses.csv','w') as csv:
            #read first line in source file to prime loop
            line=txt.readline().rstrip()
            #loop until no more lines in source file
            while line!='':
                #if line contains zip, parse line appropriately
                if line[-5:].isdigit():
                    #seperate city from state & zip; keep spaces in city name
                    line=line.split(',')
                    #parse state & zip; append to line & remove redundancy
                    line=line+line[1].split()
                    del(line[1])
                    #iterate through parsed line
                    for item in line:
                        #write to csv; advance cursor when appropriate
                        csv.write(item+',' if not item.isdigit() else item+'\n')
                #write street address line to csv
                else: csv.write(line+',')
                #acquire next line from source to continue loop
                line=txt.readline().rstrip()
#run main prog
assignment9()
