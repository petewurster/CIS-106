'''
customer spec: allow abbreviation look-up from dictionary; include entries for
        TCP, UDP, POP, IMAP & FTP; react to unknown entries; permit user to
        look up terms until they decide to stop
added feat: import serialized dictionary; permit user to add and delete dictionary
        entries; save dictionary for future use
'''
#import dictionary if available
import pickle
try:
      with open(r'dictionary.dat','rb') as file: terms=pickle.load(file)
#otherwise build init dictionary
except: terms={'TCP':'Transmission Control Protocol','UDP':'User Datagram Protocol',
               'POP':'Post Office Protocol','IMAP':'Internet Message Access Protocol',
               'FTP':'File Transfer Protocol'}

#main prog as func
def ex10(terms):
    while True:
        item=input('====> ').upper()
        if item=='EXIT': break
        #show keys
        elif item=='SEE ALL': print(terms.keys())
        elif item in terms: print(item,'-',terms[item])
        #delete entries
        elif item.startswith('DELETE '):
            for key in terms:
                if item=='DELETE '+key:
                    print('\tYou sure you want to delete ',item[7:],'?',sep='')
                    if input('\t\t("y" for yes) ').upper()=='Y':
                        terms.pop(key)
                        break
        #create new entries
        else:
            print('\tUnknown entry! Create new entry?')
            if input('\t\t("y" for yes) ').upper()=='Y':
                print('What does',item,'stand for?')
                terms[item]=input('new entry> ')
    #since user is done, autosave dictionary and exit prog
    with open(r'dictionary.dat','wb') as file:
        pickle.dump(terms,file)

#prompt user & start main func with initial KVp
print('Enter an abbreviation to look up in the dictionary!\n'
      '(To delete, type "delete" followed by a space and the key you want to delete.\n'
      'Type "see all" to view the keys or "exit" to quit.)')
ex10(terms)
