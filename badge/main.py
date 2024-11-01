from struct import unpack
from images import HELLO_WORLD
import time

while True:
    for frame in HELLO_WORLD:
        rows = unpack("BBBBBBBB", frame)
        for r in range(8):
            row = r + 1
            cols = frame[r]
            petal_bus.writeto_mem(PETAL_ADDRESS, row, bytes([cols]))
        time.sleep_ms(100)
