
# PROBLEMA DE USAR REST É QUE A CHAMADA VEM A CADA 10 SEGUNDOS E NESSE MEIO TEMPO 
# PODE OCORRER DE VIR UM VOLUME POSITIVO EM 5 SEGUNDOS ALTERAR O PRECO PARA CIMA
# E NO DE 10 SEGUNDOS VIR UM VOLUME NEGATIVO, CAUSANDO ASSIM UMA INCONPATIBILIDADE
# NO ANDAMENTO DO VOLUME
 
import time
import json
import requests

from save_data import save_ticker,save_tickers,save_trades

def tickers_get(url):
    get_tickers = requests.get(url) 
    if get_tickers != 200:
        response = json.loads(get_tickers.content)
        tickers  = response[0]
        return tickers
    
def ticker_get(url):
    get_ticker = requests.get(url) 
    if get_ticker != 200:
        ticker = json.loads(get_ticker.content)
        return ticker

def trades_get(url):
    get_trades = requests.get(url) 
    if get_trades != 200:
        response = json.loads(get_trades.content)
        trades   = response[0]
        return trades

ticker_url  = 'https://api-pub.bitfinex.com/v2/ticker/tBTCUSD'
tickers_url = 'https://api-pub.bitfinex.com/v2/tickers?symbols=tBTCUSD'
trades_url  = 'https://api-pub.bitfinex.com/v2/trades/tBTCUSD/hist'

timestamp = time.time()

ticker_path  = f"data/rest_ticker_{timestamp}.csv"
tickers_path = f"data/rest_tickers_{timestamp}.csv"
trades_path  = f"data/rest_trades_{timestamp}.csv"

ticker_csv  = open(f"{ticker_path}","a")
ticker_csv.write(f"bid,bid_size,ask,ask_size,daily_change,daily_change_relative,last_price,volume,high,low\n")
ticker_csv.close()

tickers_csv  = open(f"{tickers_path}","a")
tickers_csv.write(f"symbol,bid,bid_size,ask,ask_size,daily_change,daily_change_relative,last_price,volume,high,low\n")
tickers_csv.close()

trades_csv  = open(f"{trades_path}","a")
trades_csv.write(f"id,mts,amount,price\n")
trades_csv.close()

while True:

    # TICKER
    ticker = ticker_get(ticker_url)
    print(f"--------------- TICKER ------------")
    print(f"BID                   : {ticker[0]}")
    print(f"BID_SIZE              : {ticker[1]}")
    print(f"ASK                   : {ticker[2]}")
    print(f"ASK_SIZE              : {ticker[3]}")
    print(f"DAILY_CHANGE          : {ticker[4]}")
    print(f"DAILY_CHANGE_RELATIVE : {ticker[5]}")
    print(f"LAST_PRICE            : {ticker[6]}")
    print(f"VOLUME                : {ticker[7]}")
    print(f"HIGH                  : {ticker[8]}")
    print(f"LOW                   : {ticker[9]}\n")
    
    save_ticker(ticker_path,ticker)

    # TICKERS
    tickers = tickers_get(tickers_url)
    print(f"--------------- TICKERS ------------")
    print(f"SYMBOL                : {tickers[0]}")
    print(f"BID                   : {tickers[1]}")
    print(f"BID_SIZE              : {tickers[2]}")
    print(f"ASK                   : {tickers[3]}")
    print(f"ASK_SIZE              : {tickers[4]}")
    print(f"DAILY_CHANGE          : {tickers[5]}")
    print(f"DAILY_CHANGE_RELATIVE : {tickers[6]}")
    print(f"LAST_PRICE            : {tickers[7]}")
    print(f"VOLUME                : {tickers[8]}")
    print(f"HIGH                  : {tickers[9]}")
    print(f"LOW                   : {tickers[10]}\n")
    
    save_tickers(tickers_path,tickers)

    # TICKER
    trades = trades_get(trades_url)
    print(f"--------------- TRADES ------------")
    print(f"ID       : {trades[0]}")
    print(f"MTS      : {trades[1]}")
    print(f"AMOUNT   : {trades[2]}")
    print(f"PRICE    : {trades[3]}\n")
    
    save_trades(trades_path,trades)

    time.sleep(10)
    