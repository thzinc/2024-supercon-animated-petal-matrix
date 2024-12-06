import asyncio
import random

MAX_CYCLE = 0x100

rows = [0, 0, 0, 0, 0, 0, 0, 0]


def set_center_row(r, cycle, color_value):
    global rows
    if cycle < color_value:
        rows[r] |= 0b10000000
    else:
        rows[r] &= 0b01111111


center = (0xFF, 0xFF, 0xFF)


async def render_rows():
    global center
    global rows
    cycle = 0
    while True:
        cycle = (cycle + 0x10) % MAX_CYCLE

        (red, green, blue) = center
        set_center_row(2, cycle, red)
        set_center_row(3, cycle, green)
        set_center_row(1, cycle, blue)

        for row in range(1, 9):
            r = row - 1
            cols = rows[r]
            petal_bus.writeto_mem(PETAL_ADDRESS, row, bytes([cols]))

        await asyncio.sleep(0)


BLEND_STEPS = 10
BLEND_STEP_SLEEP = 0.1


async def colors():
    global center
    color_transitions = [
        (0xFF, 0x00, 0x00),
        (0x00, 0xFF, 0x00),
        (0x00, 0x00, 0xFF),
        (0x00, 0x00, 0x00),
        (0x44, 0x00, 0x00),
        (0x00, 0x44, 0x00),
        (0x00, 0x00, 0x44),
    ]
    while True:
        prev_color = center
        for next_color in color_transitions:
            (r1, g1, b1) = prev_color
            (r2, g2, b2) = next_color
            for pct in range(0, BLEND_STEPS + 1):
                ratio = pct / BLEND_STEPS
                r = int((r1 * (1 - ratio) + r2 * ratio))
                g = int((g1 * (1 - ratio) + g2 * ratio))
                b = int((b1 * (1 - ratio) + b2 * ratio))
                center = (r, g, b)
                await asyncio.sleep(BLEND_STEP_SLEEP)

            prev_color = next_color


BURST_MASK = 0b1111111000
bursting_rows = [0, 0, 0, 0, 0, 0, 0, 0]


async def render_burst(row):
    global rows
    global bursting_rows
    r = row - 1

    if bursting_rows[r]:
        return

    bursting_rows[r] = True
    cols = 0b111
    while cols < 0b10000000000000:
        c = (cols & BURST_MASK) >> 3
        rows[r] = c
        cols = cols << 1
        await asyncio.sleep(0.1)
    bursting_rows[r] = False


async def bursts():
    while True:
        row = random.randrange(1, 9)
        asyncio.create_task(render_burst(row))

        sleep = random.uniform(0.2, 1.0)
        await asyncio.sleep(sleep)


async def main():
    asyncio.create_task(render_rows())
    asyncio.create_task(colors())
    asyncio.create_task(bursts())

    while True:
        await asyncio.sleep(5)


while True:
    try:
        asyncio.run(main())
    except Exception as e:
        print(e)
