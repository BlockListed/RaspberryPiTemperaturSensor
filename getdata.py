from board import D4
from adafruit_dht import DHT22

def getData():
    d = DHT22(D4)
    data = (d.temperature, d.humidity)
    d.exit()
    return data