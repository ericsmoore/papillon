import time
import engine as en


def scene():
    x, y = en.c.coords(en.c.w - 30, 0)
    en.fade(en.assets['trail_1'], x, y, 0.15, 5, 40)

    x, y = en.c.coords(82, 26)
    en.fade(en.assets['trail_2'], x, y, 0.15, 5, 50)

    x, y = en.c.coords(0, en.c.h - 8)
    en.fade(en.assets['trail_3'], x, y, 0.1, 5, 60)

    en.fade(en.assets['butterfly'], en.c.x, en.c.y, 0.1, 5, 70)
    time.sleep(1)

    en.typewrite(
        en.assets['title'], en.c.cx - 21 // 2 - 1, en.c.y + en.c.h // 3, 0.05
    )
    time.sleep(1)

    opts = ['ENTER - E', 'QUIT - Q']

    y = 2 * en.c.h // 3

    def x(o, i):
        return i * (en.c.w // 3) - len(o) // 2

    c1 = en.c.coords(x(opts[0], 1), y)
    en.typewrite(opts[0], c1[0], c1[1], 0.05, en.t.gray30)

    time.sleep(0.5)

    c2 = en.c.coords(x(opts[1], 2), y)
    en.typewrite(opts[1], c2[0], c2[1], 0.05, en.t.gray30)

    while True:
        key = en.t.inkey().lower()
        if key == 'q':
            return None
        if key == 'e':
            return 'intro'
