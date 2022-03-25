import websocket
import json
import ssl
import time

from save_data import save_tickers

class WebsocketConnect:
    
    def __init__(self,params,update_connect,ticker_path): 
        self.params         = params
        self.update_connect = update_connect
        self.ticker_path    = ticker_path
        
    def connect(self):

        # OPEN SOCKET
        def on_open(ws):
            print('Opened Connection')
            ws.send(json.dumps(self.params))         
        # CLOSE SOCKET
        def on_close(ws):
            print('Closed Connection')
            ws.keep_running = False
            ws.close()
        # ERROR SOCKET
        def on_error(ws, err):
            print("Got a an error: ", err)
        # RECEIVE TICK
        def on_message(ws, message):
            # EVENTS
            if '{'in message:
                print(f"\nWEBSOCKET EVENT : {message}\n")
                return
            # HB
            if 'hb'in message:
                return
            # GO TICK
            if '['in message:
                
                self.update_connect -= 1
                
                replace_msg = message.replace("[", "")
                replace_msg = replace_msg.replace("]", "")
                split_msg   = replace_msg.split(",")
                
                if len(split_msg) == 11:
                    print(f"--------------- TICKER ------------")
                    print(f"CHANNEL_ID            : {split_msg[0]}")
                    print(f"BID                   : {split_msg[1]}")
                    print(f"BID_SIZE              : {split_msg[2]}")
                    print(f"ASK                   : {split_msg[3]}")
                    print(f"ASK_SIZE              : {split_msg[4]}")
                    print(f"DAILY_CHANGE          : {split_msg[5]}")
                    print(f"DAILY_CHANGE_RELATIVE : {split_msg[6]}")
                    print(f"LAST_PRICE            : {split_msg[7]}")
                    print(f"VOLUME                : {split_msg[8]}")
                    print(f"HIGH                  : {split_msg[9]}")
                    print(f"LOW                   : {split_msg[10]}\n")
                    
                    save_tickers(self.ticker_path,split_msg)
                
                if self.update_connect == 0:
                    on_close(ws) 

        # RUN
        ws = websocket.WebSocketApp('wss://api-pub.bitfinex.com/ws/2', on_open = on_open, on_close = on_close, on_message = on_message,on_error=on_error)
        ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

update_connect = 10
params         = { "event": "subscribe", "channel": "ticker", "symbol": "tBTCUSD"}

timestamp = time.time()

ticker_path = f"data/websocket_ticker_{timestamp}.csv"
ticker_csv  = open(f"{ticker_path}","a")
ticker_csv.write(f"channel_id,bid,bid_size,ask,ask_size,daily_change,daily_change_relative,last_price,volume,high,low\n")
ticker_csv.close()

while True :
    WebsocketConnect(params,update_connect,ticker_path).connect()
    print("Renew Connect")