from struct import unpack
import images
import time

while True:
    selected_images = [images.HELLO_WORLD, images.DEMO]
    for image in selected_images:
        for frame in image:
            rows = unpack("BBBBBBBB", frame)
            for r in range(8):
                row = r + 1
                cols = frame[r]
                petal_bus.writeto_mem(PETAL_ADDRESS, row, bytes([cols]))
            time.sleep_ms(100)
