from engine import Engine
import time


def scene(en: Engine):
    time.sleep(4)

    llen = max(len(line) for line in en.assets['dawn00'].splitlines())

    en.typewrite(
        en.assets['dawn00'],
        en.c.cx - llen // 2,
        en.c.cy - 3,
        0.075,
        en.t.italic_gray50,
    )

    time.sleep(2.5)

    en.typewrite(
        en.assets['dawn00'],
        en.c.cx - llen // 2,
        en.c.cy - 3,
        0.02,
        en.bg,
    )

    time.sleep(3.5)

    lines = en.assets['rise'].splitlines()
    for i, line in enumerate(lines):
        en.typewrite(
            line, en.c.cx - len(line) // 2, en.c.cy - len(lines) // 2 + i - 2
        )
        time.sleep(0.10)

    time.sleep(1)

    en.scene_pause()

    # -------------------------
    x = en.c.cx - 26
    y = en.c.cy - 6

    en.clear_canvas()

    time.sleep(2)

    en.typewrite(en.assets['dawn01'], x, y)

    time.sleep(3)

    # en.clear_canvas()
    en.typewrite(en.assets['dawn01'], x, y, 0.01, en.bg)

    time.sleep(2)

    en.typewrite(
        en.assets['dawn02'],
        en.c.cx - len(en.assets['dawn02']) // 2,
        en.c.cy - 3,
        0.15,
        en.t.italic_gray40,
    )

    time.sleep(0.5)

    en.scene_pause()

    en.clear_canvas()

    time.sleep(1.5)

    en.typewrite(en.assets['dawn03'], x, y)

    time.sleep(2)

    en.typewrite(en.assets['dawn03'], x, y, 0.005, en.bg)

    time.sleep(1)

    lines = en.assets['dawn04'].splitlines()
    for i, line in enumerate(lines):
        en.typewrite(line, x, y + i)
        if line == '\n':
            time.sleep(0.5)
        else:
            time.sleep(0.10)

    time.sleep(2)
    en.clear_canvas()
    time.sleep(2)

    en.typewrite(
        en.assets['dawn05'],
        en.c.cx - len(en.assets['dawn05']) // 2,
        en.c.cy - 3,
        0.15,
        en.t.italic_gray40,
    )

    en.scene_pause()
