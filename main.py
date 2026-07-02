import time
from engine import Engine
from blessed import Terminal
from scenes import scenes


def main():
    t = Terminal()

    with (
        t.cbreak(),
        t.hidden_cursor(),
        t.fullscreen(),
        t.window_title('papillon'),
    ):
        en = Engine(t)

        scene = '00-title'
        while True:
            scene = scenes[scene](en)
            if not scene:
                en.clear_canvas()
                time.sleep(0.5)
                break
            en.clear_canvas()


if __name__ == '__main__':
    main()
