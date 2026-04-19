import core


def scene():
    core.typewrite('next scene', core.c.cx - len('papillon') // 2, core.c.cy)

    key = core.t.inkey()
    if key:
        return None
