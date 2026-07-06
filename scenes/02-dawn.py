from engine import Engine
import time


def scene(en: Engine):
    time.sleep(4)

    l1 = 'Rise, you! Rise,'
    x1, y1 = en.c.cx - len(l1) // 2, en.c.cy - 3
    l2 = 'for The Butterfly.'
    x2, y2 = en.c.cx - len(l2) // 2, en.c.cy - 2

    en.typewrite(l1, x1, y1, 0.075, en.t.italic_gray50)
    time.sleep(1)
    en.typewrite(l2, x2, y2, 0.075, en.t.italic_gray50)

    time.sleep(2.5)

    en.typewrite(l1, x1, y1, 0.02, en.t.black)
    en.typewrite(l2, x2, y2, 0.02, en.t.black)

    time.sleep(3.5)

    lines = en.assets['rise'].splitlines()
    for i, line in enumerate(lines):
        en.typewrite(line, en.c.cx - len(line) // 2, en.c.cy - len(lines) // 2 + i - 2, 0.075)
        time.sleep(0.10)

    time.sleep(2)

    ellip = '. . .'

    x, y = en.c.coords(en.c.w // 2 - len(ellip) // 2, en.c.h - 2)
    en.typewrite(ellip, x, y, 0.05, en.t.italic_gray40)

    en.clear_input()
    while True:
        key = en.t.inkey().lower()
        if key:
            break

    # -------------------------


