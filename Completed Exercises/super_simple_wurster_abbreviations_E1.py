'''
customer spec: allow abbreviation look-up from dictionary; include entries for
        TCP, UDP, POP, IMAP & FTP; react to unknown entries; permit user to
        look up terms until they decide to stop
'''

terms={'TCP':'Transmission Control Protocol','UDP':'User Datagram Protocol',
       'POP':'Post Office Protocol','IMAP':'Internet Message Access Protocol',
       'FTP':'File Transfer Protocol'}#define dictionary
item=-1#set as bogus value to prime loop
while item!='STOP':#loop until "stop" or "STOP" is typed
      item=input('====> ').upper()#get input & convert to uppercase
      if item in terms: print('\t',item,'-',terms[item])#if it exists, print it
      else: print('\t Unknown entry!')#it ain't there

      
