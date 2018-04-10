def hurrtotal(total):
    with open("hurricanes.txt","r") as textFile:
        with open("hurr.csv","w")as csv:
            for line in textFile:
                if line.rstrip().isdigit():
                    if total!=0:
                        csv.write(str(total)+'\n')
                        total=0
                    csv.write(line.rstrip()+',')
                else: total+=int(line.rstrip()[4:])
            csv.write(str(total))
hurrtotal(0)




    

