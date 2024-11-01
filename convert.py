from PIL import Image
from struct import pack
import sys
import math

led_by_pixel = [
    [
        None,
        None,
        (2, 7),
        (1, 5),
        (1, 5),
        (1, 6),
        (1, 7),
        None,
        None,
    ],
    [
        None,
        (2, 6),
        (2, 6),
        (1, 4),
        (8, 3),
        (8, 4),
        (8, 5),
        (8, 6),
        None,
    ],
    [
        (3, 7),
        (2, 5),
        (1, 3),
        (8, 2),
        (8, 2),
        (7, 2),
        (7, 3),
        (7, 3),
        (8, 7),
    ],
    [
        (3, 6),
        (2, 4),
        (1, 2),
        (8, 1),
        (7, 1),
        (6, 1),
        (6, 2),
        (7, 4),
        (7, 4),
    ],
    [
        (3, 5),
        (2, 3),
        (2, 2),
        (1, 1),
        None,
        (5, 1),
        (6, 2),
        (6, 3),
        (7, 5),
    ],
    [
        (3, 4),
        (3, 4),
        (2, 2),
        (2, 1),
        (3, 1),
        (4, 1),
        (5, 2),
        (6, 4),
        (7, 6),
    ],
    [
        (4, 7),
        (3, 3),
        (3, 3),
        (3, 2),
        (4, 2),
        (4, 2),
        (5, 3),
        (6, 5),
        (7, 7),
    ],
    [
        None,
        (4, 6),
        (4, 5),
        (4, 4),
        (4, 3),
        (5, 4),
        (6, 6),
        (6, 6),
        None,
    ],
    [
        None,
        None,
        (5, 7),
        (5, 6),
        (5, 5),
        (5, 5),
        (6, 7),
        None,
        None,
    ],
]

[_, filename] = sys.argv[0:2]
img = Image.open(filename)

x_shift = 1
if len(sys.argv) == 3:
    x_shift = int(sys.argv[2])

frames = []
frame_count = 1
if img.width > 9:
    frame_count = math.ceil(img.width / x_shift)

print(f"Generating {frame_count} frames")

height = min(9, img.height)
x_offset = 0
for f in range(frame_count):
    leds = []

    x_next = min(x_offset + 9, img.width)
    for x in range(x_offset, x_next):
        for y in range(height):
            pix = img.getpixel((x, y))

            x_rel = x - x_offset
            led = led_by_pixel[x_rel][8 - y]

            if led and not pix:
                leds.append(led)

    x_offset += x_shift

    rows = [
        0b0000000,
        0b0000000,
        0b0000000,
        0b0000000,
        0b0000000,
        0b0000000,
        0b0000000,
        0b0000000,
    ]
    for row, col in set(leds):
        r = row - 1
        mask = 1 << (col - 1)
        rows[r] |= mask

    str = pack("BBBBBBBB", *rows)
    frames.append(str)

print(frames)
