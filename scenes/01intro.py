import time


def scene(en):
    time.sleep(2)

    x, y = en.c.coords(22, 9)

    en.typewrite(en.assets['lamartine'], x, y, 0.015, en.t.gray25)
    time.sleep(2)
    en.typewrite(en.assets['lamartine_t'], x, y, 0.065)

    time.sleep(1)
    en.typewrite(
        '- Alphonse de Lamartine, "Le Papillon"',
        x + 2,
        y + 11,
        0.075,
        en.t.gray40,
    )

    while True:
        key = en.t.inkey().lower()
        if key == 'q':
            return None
        if key == 'e':
            return '01intro'
