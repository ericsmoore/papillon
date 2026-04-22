import time
import engine as en
from scenes import scenes


def main():
    with (
        en.t.cbreak(),
        en.t.hidden_cursor(),
        en.t.fullscreen(),
        en.t.window_title('papillon'),
    ):
        en.initialize()

        scene = 'intro'
        while True:
            scene = scenes[scene]()
            if not scene:
                en.clear_canvas()
                time.sleep(0.5)
                break
            en.clear_canvas()


if __name__ == '__main__':
    main()
