#!/usr/bin/python
from __future__ import print_function

import sys
import socket
import json
import datetime
import time

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("test-exch-PMPPLUSPLUS", 25000))
    return s.makefile('rw', 1)

def write(exchange, obj):
    json.dump(obj, exchange)
    exchange.write("\n")

def read(exchange):
    return json.loads(exchange.readline())


def main():
    timeid = str(datetime.datetime.now()).split(" ")[1].replace(":","").split(".")[0]
    exchange = connect()
    print(timeid)
    write(exchange, {"type": "hello", "team": "PMPPLUSPLUS"})
    print("the exchange replied" , read(exchange),file=sys.stderr)
    write(exchange, {"type": "add", "order_id": timeid , "symbol": 'BOND', "dir": "BUY", "price": 997, "size": 1})
    while True: 
        hello_from_exchange = read(exchange)
        print("The exchange replied:", hello_from_exchange, file=sys.stderr)
        time.sleep(3)
	
if __name__ == "__main__":
    main()
