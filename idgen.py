import math
from decouple import config
from time import time
node = config("NODE", cast=int)
epoch = config("EPOCH", cast=int)

counter = 0

def getTime() -> int:
    t = time()
    return math.floor(t*1000)

def getId() -> int:
    global counter
    id = ((getTime() - epoch) << (63 - 41)) | (node << 63 - 41 - 10) | counter
    counter += 1
    return id