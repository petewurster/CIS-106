def search():
    with open(r'searchme.txt','r') as file:
        for line in file:
            yield line.rstrip('\n')
            #yield data
            

def results():
    for info in search():
        if 'japan' in info:
            print(info)



        

results()
        
























##    with open(r'result.txt','a') as file:
##        while data!='':
##            print (data)
##            file.write(data+'\n')
##            data=search()
