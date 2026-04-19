import signal
import time

from blessed import Terminal

t = Terminal()

W = 96
H = 32


def check_size():
    min_h = H + 2
    min_w = W + 4

    print(f"\033[8;{min_h};{min_w}t")  # auto-resizes (some emulators)
    time.sleep(0.25)

    if t.height >= min_h and t.width >= min_w:
        return

    print("Please resize to 100x34")

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
    print(t.clear() + t.home())

    x = (t.width - W) // 2
    y = (t.height - H) // 2

    top = "┌" + (W - 2) * "─" + "┐"
    bottom = "└" + (W - 2) * "─" + "┘"
    middle = "│" + (W - 2) * " " + "│"

    print(t.move_xy(x, y) + top)

    for i in range(1, H - 1):
        print(t.move_xy(x, y + i) + middle)

    print(t.move_xy(x, y + H - 1) + bottom, end="", flush=True)


def type(text, x, y, delay):
    with t.location(x, y):
        for c in text:
            print(c, end='', flush = True)
            time.sleep(delay)

def main():
    with t.cbreak(), t.hidden_cursor(), t.fullscreen():
        check_size()
        draw_border()

        # time.sleep(1)

        # text = 'papillon'
        # type('papillon', W//2 - len(text)//2, H//2, 0.05)

        # time.sleep(1)

        # for r in range(H-2):
        #     with t.location(3, 2 + r):
        #         print(' ' * (W-2), end = '', flush = True)

        while True:
            key = t.inkey(timeout=0.1)
            if key == "q":
                break


if __name__ == "__main__":
    main()
