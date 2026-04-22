import engine
from scenes import scenes


def main():
    engine.a = engine.load_assets()
    with (
        engine.t.cbreak(),
        engine.t.hidden_cursor(),
        engine.t.fullscreen(),
        engine.t.window_title('papillon'),
    ):
        engine.initialize()

        scene = 'intro'
        while True:
            scene = scenes[scene]()
            if not scene:
                engine.clear_canvas()
                engine.time.sleep(0.5)
                break
            engine.clear_canvas()


if __name__ == '__main__':
    main()
