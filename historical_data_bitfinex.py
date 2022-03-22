import json
import time
import requests

from datetime import datetime

from save_data import save_trades

start_timestamp = 1647874639000 # 2013 - 1357052239000
end_timestamp   = 1647961039000 # 2014 - 1388588239000
last_timestamp  = None

url = 'https://api.bitfinex.com/v2/trades/tBTCUSD/hist/'

start_data  = datetime.fromtimestamp(start_timestamp/1000)
end_data    = datetime.fromtimestamp(end_timestamp/1000)
trades_path = f"data/historical_init_{start_data}_end_{end_data}.csv"
trades_csv  = open(f"{trades_path}","a")
trades_csv.write(f"id,mts,amount,price\n")
trades_csv.close()

while start_timestamp <= end_timestamp and start_timestamp != last_timestamp:
    
    data = datetime.fromtimestamp(start_timestamp/1000)
    print("Requesting : "+str(data))
    
    parameters = {'start': start_timestamp, 'limit': 10000, 'sort': 1}
    response   = requests.get(url, params=parameters)
    
    last_timestamp = start_timestamp
    
    if response != 200:

        trades = json.loads(response.content)

        # ERROR
        if len(trades) <= 1:
            print("trades",trades)

        if len(trades) > 1:
            id, start_timestamp, amount, price = trades[1]
            data = datetime.fromtimestamp(start_timestamp/1000)
            print(f"id : {id}, start_timestamp : {data}, amount : {amount}, price : {price}, size {len(trades)}")
                
            id, start_timestamp, amount, price = trades[-1]
            data = datetime.fromtimestamp(start_timestamp/1000)
            print(f"id : {id}, end_timestamp : {data}, amount : {amount}, price : {price}, \n")
            
            for i in range(len(trades)):
                save_trades(trades_path,trades[i])
        
    time.sleep(2)
