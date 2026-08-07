import time

from engine import Engine


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

    en.write_choices(['ENTER - E', 'QUIT - Q'])

    while True:
        key = en.get_input()
        if key == 'q':
            return None
        elif key == 'e':
            return 'epigraph'
