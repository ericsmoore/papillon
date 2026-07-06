import signal
import time
import termios
import sys
from pathlib import Path

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


class Engine:
    def check_size(self):
        t = self.t
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

    def set_theme(self, fg, bg):
        self.default = getattr(self.t, f'{fg}_on_{bg}')
        self.fg = getattr(self.t, fg)
        self.bg = getattr(self.t, bg)
        print(self.t.clear + self.t.home + self.default)
        for row in range(self.t.height):
            with self.t.location(0, 0 + row):
                print(' ' * self.t.width, end='')

    def draw_border(self):
        t = self.t
        c = self.c

        print(t.home() + t.gray40)

        top = '┌' + (c.w) * '─' + '┐'
        bottom = '└' + (c.w) * '─' + '┘'
        middle = '│' + (c.w) * ' ' + '│'

        print(t.move_xy(c.x - 1, c.y - 1) + top)
        for i in range(c.h):
            print(t.move_xy(c.x - 1, c.y + i) + middle)
        print(t.move_xy(c.x - 1, c.y + c.h) + bottom, end='', flush=True)

    def typewrite(self, text, x, y, delay=0.05, col=None):
        t = self.t
        col = col or t.gray80

        lines = text.splitlines()
        for line in range(len(lines)):
            with t.location(x, y + line):
                print(col, end='', flush=True)
                for ch in lines[line]:
                    print(ch, end='', flush=True)
                    if ch in ',.?!:;':
                        time.sleep(delay * 2.5)
                    elif not ch.isspace():
                        time.sleep(delay)

    def fade(self, text, x, y, delay=0.25, step=10, min=10, max=80):
        t = self.t
        shades = []
        for i in range(min, max, step):
            shades.append(getattr(t, f'gray{i}'))

        lines = text.splitlines()
        for s in shades:
            for line in range(len(lines)):
                with t.location(x, y + line):
                    print(s + lines[line], end='', flush=True)
            time.sleep(delay)

    def clear_canvas(self):
        c = self.c
        t = self.t

        for r in range(c.h):
            with t.location(c.x, c.y + r):
                print(' ' * c.w, end='', flush=True)

    def clear_input(self):
        try:
            termios.tcflush(sys.stdin, termios.TCIFLUSH)
        except termios.error:
            pass
        with self.t.cbreak():
            while self.t.inkey(timeout=0):
                pass

    def scene_pause(self):
        ellip = '. . .'

        ex, ey = self.c.coords(self.c.w // 2 - len(ellip) // 2, self.c.h - 2)
        self.typewrite(ellip, ex, ey, 0.04, self.t.italic_gray40)

        self.clear_input()
        while True:
            key = self.t.inkey().lower()
            if key:
                break

    def load_assets(self):
        assets = {
            p.stem: p.read_text() for p in Path('scenes/assets').rglob('*.txt')
        }

        return assets

    def __init__(self, term):
        self.t = term
        self.check_size()
        self.c = Canvas(
            (self.t.width - W) // 2 + 1, (self.t.height - H) // 2 + 1
        )
        self.assets = self.load_assets()
        self.set_theme("lightgray", "gray4")
        self.draw_border()
