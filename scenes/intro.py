import core


def scene():
    core.typewrite('papillon', core.c.cx - len('papillon') // 2, core.c.cy)

    key = core.t.inkey()
    if key == 'q':
        return None
    else:
        return 'next'
