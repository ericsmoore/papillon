import re
import signal
import time
from blessed import Terminal

t = Terminal()
c = None  # Canvas
assets = None  # Assets

W, H = 96, 32


class Canvas:
    def __init__(self, x, y, w=W - 2, h=H - 2):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.cx = self.x + self.w // 2
        self.cy = self.y + self.h // 2

    def coords(self, cx, cy):
        return self.x + cx, self.y + cy


def check_size():
    min_h = H + 2
    min_w = W + 4

    print(f'\033[8;{min_h};{min_w}t')  # auto-resizes (some emulators)
    time.sleep(0.25)

    if t.height >= min_h and t.width >= min_w:
        return

    print('Please resize to 100x34')

    resized = False

    def on_resize(*args):
        nonlocal resized
        resized = True

    signal.signal(signal.SIGWINCH, on_resize)

    with t.cbreak():
        while True:
            if resized:
                resized = False
                if t.height >= min_h and t.width >= min_w:
                    return
            t.inkey(timeout=0.1)


def draw_border():
    print(t.home())

    top = '┌' + (c.w) * '─' + '┐'
    bottom = '└' + (c.w) * '─' + '┘'
    middle = '│' + (c.w) * ' ' + '│'

    print(t.move_xy(c.x - 1, c.y - 1) + top)
    for i in range(c.h):
        print(t.move_xy(c.x - 1, c.y + i) + middle)
    print(t.move_xy(c.x - 1, c.y + c.h) + bottom, end='', flush=True)


def typewrite(text, x, y, delay=0.05, col=''):
    lines = text.splitlines()
    for line in range(len(lines)):
        with t.location(x, y + line):
            print(col, end='', flush=True)
            for ch in lines[line]:
                print(ch, end='', flush=True)
                if not ch.isspace():
                    time.sleep(delay)


def fade(text, x, y, delay=0.25, step=10, max=70):
    shades = []
    for i in range(10, max, step):
        shades.append(getattr(t, f'gray{i}'))
    lines = text.splitlines()
    for s in shades:
        for line in range(len(lines)):
            with t.location(x, y + line):
                print(s + lines[line], end='', flush=True)
        time.sleep(delay)


def clear_canvas():
    for r in range(c.h):
        with t.location(c.x, c.y + r):
            print(' ' * c.w, end='', flush=True)


def load_assets():
    parts = re.split(
        r'^\[(\w+)\]$', open('scenes/assets.txt').read(), flags=re.MULTILINE
    )
    return {
        parts[i]: parts[i + 1].strip('\n') for i in range(1, len(parts) - 1, 2)
    }


def initialize():
    global c, assets
    check_size()
    c = Canvas((t.width - W) // 2 + 1, (t.height - H) // 2 + 1)
    assets = load_assets()
    print(t.clear + t.home)
    draw_border()
