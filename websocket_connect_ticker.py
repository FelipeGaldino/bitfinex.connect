import websocket
import json
import ssl

class WebsocketConnect:
    
    def __init__(self,params): 
        self.params = params
        
    def connect(self):

        # OPEN SOCKET
        def on_open(ws):
            print('Opened Connection')
            params = self.params
            ws.send(json.dumps(params))         
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
                    print(f"HIGH                  : {split_msg[9]}\n")

        # RUN
        ws = websocket.WebSocketApp('wss://api.bitfinex.com/ws/2', on_open = on_open, on_close = on_close, on_message = on_message,on_error=on_error)
        ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
        
params = { "event": "subscribe", "channel": "ticker", "symbol": "tBTCUSD"}
WebsocketConnect(params).connect()