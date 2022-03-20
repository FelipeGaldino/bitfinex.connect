def save_ticker(path_csv,array_data):
    read_csv  = open(f"{path_csv}","a")
    read_csv.write(f"{array_data[0]},{array_data[1]},{array_data[2]},{array_data[3]},{array_data[4]},{array_data[5]},{array_data[6]},{array_data[7]},{array_data[8]},{array_data[9]}\n")
    read_csv.close()
    return

def save_trades(path_csv,array_data):
    read_csv  = open(f"{path_csv}","a")
    read_csv.write(f"{array_data[0]},{array_data[1]},{array_data[2]},{array_data[3]}\n")
    read_csv.close()
    return

def save_tickers(path_csv,array_data):
    read_csv  = open(f"{path_csv}","a")
    read_csv.write(f"{array_data[0]},{array_data[1]},{array_data[2]},{array_data[3]},{array_data[4]},{array_data[5]},{array_data[6]},{array_data[7]},{array_data[8]},{array_data[9]},{array_data[10]}\n")
    read_csv.close()
    return

def save_trades_wb(path_csv,array_data):
    read_csv  = open(f"{path_csv}","a")
    read_csv.write(f"{array_data[0]},{array_data[1]},{array_data[2]},{array_data[3]},{array_data[4]},{array_data[5]}\n")
    read_csv.close()
    return
