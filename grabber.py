#!/usr/bin/python3

##
## run the code for about 2/3 days
##

import requests
import time

wait_time = 30
f_name = input("dataset name:")
f = open(f_name,"a")
keys = ["price_usd","24h_volume_usd","market_cap_usd","available_supply","total_supply","percent_change_1h","percent_change_24h","percent_change_7d"]
vals = [0]*len(keys)

print("Collecting data...")
print("price_usd, 24h_volume_usd, market_cap_usd, available_supply ,total_supply, percent_change_1h ,percent_change_24h ,percent_change_7d")

while True:
  try:
    data = requests.get("https://api.coinmarketcap.com/v1/ticker/bitcoin/", timeout=10).json()[0]
    bstamp = requests.get("https://www.bitstamp.net/api/v2/ticker/btcusd/", timeout=10).json() 
    bkc = requests.get("https://poloniex.com/public?command=returnTicker", timeout=10).json()
    log = ''
  
    for d in data.keys():
       if d in keys:
         indx = keys.index(d)
         vals[indx] = data[d]
    for val in vals:
         f.write(val+",")
         log = log + val + ', '
      
    print("Data: " + log)
    

    f.write("{},{},".format(bstamp["volume"],bstamp["vwap"]))
    f.write("{},{},{}".format(float(int(float(bkc["USDT_BTC"]["highestBid"])*100)/100),float(int(float(bkc["USDT_BTC"]["lowestAsk"])*100)/100),float(int(float(bkc["USDT_BTC"]["last"])*100)/100)))
    f.write("\n")
    f.flush()
    time.sleep(wait_time)
  except requests.exceptions.RequestException as e:
    print e
    print("Trying again...")
    time.sleep(wait_time)
