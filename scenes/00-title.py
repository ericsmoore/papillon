from engine import Engine
import time


def scene(en: Engine):
    time.sleep(1.5)
    x, y = en.c.coords(en.c.w - 30, 0)
    en.fade(en.assets['trail_1'], x, y, 0.15, 5, 10, 40)

    x, y = en.c.coords(82, 26)
    en.fade(en.assets['trail_2'], x, y, 0.15, 5, 10, 50)

    x, y = en.c.coords(0, en.c.h - 8)
    en.fade(en.assets['trail_3'], x, y, 0.1, 5, 10, 60)

    en.fade(en.assets['butterfly'], en.c.x, en.c.y, 0.1, 5, 10, 70)
    time.sleep(2)

    en.typewrite(
        en.assets['title'], en.c.cx - 21 // 2 - 1, en.c.y + en.c.h // 3, 0.075
    )
    time.sleep(2)

    opts = ['ENTER - E', 'QUIT - Q']

    y = 2 * en.c.h // 3

    def xpos(o, i):
        return i * (en.c.w // 3) - len(o) // 2

    c1 = en.c.coords(xpos(opts[0], 1), y)
    en.typewrite(opts[0], c1[0], c1[1], 0.05, en.t.italic_gray30)

    time.sleep(0.5)

    c2 = en.c.coords(xpos(opts[1], 2), y)
    en.typewrite(opts[1], c2[0], c2[1], 0.05, en.t.italic_gray30)

    en.clear_input()
    while True:
        key = en.t.inkey().lower()
        if key == 'q':
            return None
        if key == 'e':
            return '01-epigraph'
