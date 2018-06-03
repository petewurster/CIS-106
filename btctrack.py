import requests
print('pulling current BTC rates...')
rq=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
current=(rq.json()['bpi']['USD']['rate_float'])

print('\nEnter BTC buys followed by the price-rate at the time\n'
	'of transaction. Use negative $ entries to represent buy\n'
	'transactions. Enter "0" to tally results.\n')

buys=[-1]
buypr=[-1]
while buys[-1]!=0:
    buys.append(float(input(str(len(buys))+'>> $')))
    if buys[-1]!=0: buypr.append(float(input(' @')))
    else: pass
buys.remove(-1)
buypr.remove(-1)
buys.remove(0)

shares=[]
for buy in range(len(buys)):
    shares.append((buys[buy]/buypr[buy])*-1)
    print (buys[buy],buypr[buy],shares[buy])

val=sum(shares)*current
print('\nremaining BTC:',sum(shares))
print('\nNot including the current value of the ',sum(shares),
      '\nBTC in your wallet (valued at $',val,'),',sep='')
print('your banked profits are $' if sum(buys)>-1 else 'your current Losses are $',
      sum(buys),'.',sep='')

input('\n\npress ENTER to exit')
