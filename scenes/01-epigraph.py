from engine import Engine
import time


def scene(en: Engine):
    time.sleep(3)

    x, y = en.c.coords(22, 7)

    en.typewrite(en.assets['lamartine'], x, y, 0.015, en.t.gray25)
    time.sleep(2)
    en.typewrite(en.assets['lamartine_t'], x, y, 0.065)

    time.sleep(1)
    en.typewrite(
        '- Alphonse de Lamartine, "Le Papillon"',
        x + 2,
        y + 11,
        0.075,
        en.t.gray50,
    )

    time.sleep(1.5)

    opt = 'PRESS ANY KEY'

    x, y = en.c.coords(en.c.w // 2 - len(opt) // 2, en.c.h - 4)
    en.typewrite(opt, x, y, 0.05, en.t.italic_gray30)

    en.clear_input()
    while (True):
        key = en.t.inkey().lower()
        if key == 'q':
            return None
        else:
            return '02-wake'
