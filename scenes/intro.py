import engine as en
from engine import typewrite


def scene():
    c = en.c.coords(en.c.w - 30, 0)
    en.fade(en.a['trail_1'], c[0], c[1], 0.07, 5, 40)

    c = en.c.coords(82, 26)
    en.fade(en.a['trail_2'], c[0], c[1], 0.07, 5, 50)

    c = en.c.coords(0, en.c.h - 8)
    en.fade(en.a['trail_3'], c[0], c[1], 0.07, 5, 60)

    en.fade(en.a['butterfly'], en.c.x, en.c.y, 0.05, 5, 70)
    en.time.sleep(1)

    typewrite(en.a['title'], en.c.cx - 21 // 2, en.c.y + en.c.h // 3, 0.05)
    en.time.sleep(1)

    opts = ['ENTER - E', 'QUIT - Q']

    y = 2 * en.c.h // 3

    def x(o, i):
        return i * (en.c.w // 3) - len(o) // 2

    c1 = en.c.coords(x(opts[0], 1), y)
    typewrite(opts[0], c1[0], c1[1], 0.05, en.t.gray40)

    en.time.sleep(0.5)

    c2 = en.c.coords(x(opts[1], 2), y)
    typewrite(opts[1], c2[0], c2[1], 0.05, en.t.gray40)

    while True:
        key = en.t.inkey().lower()
        if key == 'q':
            return None
        if key == 'e':
            return 'intro'
