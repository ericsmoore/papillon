from engine import Engine
import time


def scene(en: Engine):
    time.sleep(3)

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
    en.clear_canvas()

    time.sleep(3.5)

    lines = en.assets['rise'].splitlines()
    for i, line in enumerate(lines):
        en.typewrite(
            line,
            en.c.cx - len(line) // 2,
            en.c.cy - len(lines) // 2 + i - 2,
            0.05,
            en.t.italic_gray50,
        )
        time.sleep(0.10)

    time.sleep(1)

    en.scene_pause()

    # -------------------------
    x = en.c.cx - 26
    y = en.c.cy - 6

    en.clear_canvas()

    time.sleep(4)

    en.typewrite(en.assets['dawn01'], x, y)

    time.sleep(1)

    en.typewrite(en.assets['dawn01'], x, y, 0.01, en.bg)
    en.clear_canvas()

    time.sleep(2)

    en.typewrite(
        en.assets['dawn02'],
        en.c.cx - len(en.assets['dawn02']) // 2,
        en.c.cy - 3,
        0.15,
        en.t.italic_gray50,
    )

    time.sleep(1)

    en.scene_pause()
    en.clear_canvas()

    time.sleep(1.5)

    en.typewrite(en.assets['dawn03'], x, y)

    time.sleep(1.5)

    en.typewrite(en.assets['dawn03'], x, y, 0.003, en.bg)
    en.clear_canvas()

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

    time.sleep(1.5)

    en.scene_pause()

    en.clear_canvas()

    time.sleep(4)

    lines = en.assets['dawn06'].splitlines()
    for i, line in enumerate(lines):
        en.typewrite(line, x, y + i)
        time.sleep(1)

    time.sleep(2.5)
    en.clear_canvas()
    time.sleep(2)

    line = 'What will you do?'
    en.typewrite(line, en.c.cx - len(line) // 2, y, 0.15, en.t.italic_gray50)

    time.sleep(1)

    opts = ['RETURN TO SLEEP - S', 'KEEP AWAKE - W']

    oy = 2 * en.c.h // 3

    def xpos(o, i):
        return i * (en.c.w // 3) - len(o) // 2

    c1 = en.c.coords(xpos(opts[0], 1), oy)
    en.typewrite(opts[0], c1[0], c1[1], 0.05, en.t.italic_gray30)

    time.sleep(0.5)

    c2 = en.c.coords(xpos(opts[1], 2), oy)
    en.typewrite(opts[1], c2[0], c2[1], 0.05, en.t.italic_gray30)

    while True:
        key = en.get_input()
        if key == 'q':
            return None
        elif key == 's':
            time.sleep(0.25)
            en.clear_canvas()

            time.sleep(2)

            lines = en.assets['dawn-s00'].splitlines()
            for i, line in enumerate(lines):
                en.typewrite(line, x, y + i)
                if line == '\n':
                    time.sleep(0.5)
                else:
                    time.sleep(0.10)

            time.sleep(2)

            for i, line in enumerate(lines):
                en.typewrite(line, x, y + i, 0.003, en.bg)

            en.clear_canvas()
            time.sleep(3)

            en.typewrite(en.assets['dawn-s01'], x, y, 0.075, en.t.italic_gray40)

            time.sleep(1)

            en.scene_pause()
            return '03-wander'
        elif key == 'w':
            time.sleep(0.25)
            en.clear_canvas()

            time.sleep(2)

            lines = en.assets['dawn-w00'].splitlines()
            for i, line in enumerate(lines):
                en.typewrite(line, x, y + i)
                if line == '\n':
                    time.sleep(0.5)
                else:
                    time.sleep(0.10)

            time.sleep(2)

            for i, line in enumerate(lines):
                en.typewrite(line, x, y + i, 0.003, en.bg)

            en.clear_canvas()
            time.sleep(3)

            lines = en.assets['dawn-w01'].splitlines()
            for i, line in enumerate(lines):
                en.typewrite(line, x, y + i)
                if line == '\n':
                    time.sleep(0.5)
                else:
                    time.sleep(0.10)

            time.sleep(1)

            en.scene_pause()
            return '03-path'
