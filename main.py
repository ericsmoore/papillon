import core
from scenes import scenes


def main():
    core.a = core.load_assets()
    with (
        core.t.cbreak(),
        core.t.hidden_cursor(),
        core.t.fullscreen(),
        core.t.window_title('papillon'),
    ):
        core.initialize()

        scene = 'intro'
        while True:
            scene = scenes[scene]()
            if not scene:
                core.time.sleep(0.5)
                break
            core.clear_canvas()


if __name__ == '__main__':
    main()
