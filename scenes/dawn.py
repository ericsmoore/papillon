import time

from engine import Engine


def scene(en: Engine):
    time.sleep(3)

    en.write(en.assets['dawn00'], en.t.italic_gray50, 0.075)
    time.sleep(2.5)
    en.write(en.assets['dawn00'], en.bg, 0.02)

    en.clear_canvas()
    time.sleep(3.5)

    en.write_verse(en.assets['rise'], en.t.italic_gray50, 0.05, 0.10)

    time.sleep(1)

    en.scene_pause()

    en.clear_canvas()
    time.sleep(4)

    en.write(en.assets['dawn01'])
    time.sleep(1)
    en.write(en.assets['dawn01'], en.bg, 0.01)

    en.clear_canvas()
    time.sleep(2)

    en.write(en.assets['dawn02'], en.t.italic_gray50, 0.15)

    time.sleep(1)

    en.scene_pause()

    en.clear_canvas()
    time.sleep(1.5)

    en.write(en.assets['dawn03'])
    time.sleep(1.5)
    en.write(en.assets['dawn03'], en.bg, 0.003)

    en.clear_canvas()
    time.sleep(1)

    en.write(en.assets['dawn04'])

    time.sleep(2)

    en.clear_canvas()
    time.sleep(2)

    en.write(en.assets['dawn05'], en.t.italic_gray40, 0.15)

    time.sleep(1.5)

    en.scene_pause()

    en.clear_canvas()
    time.sleep(4)

    en.write(en.assets['dawn06'])

    time.sleep(2.5)

    en.clear_canvas()
    time.sleep(2)

    en.write('What will you do?', en.t.italic_gray50, 0.15)

    time.sleep(1)

    en.write_choices(['RETURN TO SLEEP - S', 'KEEP AWAKE - W'])

    while True:
        key = en.get_input()
        if key == 'q':
            return None
        elif key == 's':
            time.sleep(0.25)
            en.clear_canvas()

            time.sleep(2)

            en.write(en.assets['dawn-s00'])
            time.sleep(2)
            en.write(en.assets['dawn-s00'], en.bg, 0.003)

            en.clear_canvas()
            time.sleep(3)

            en.write(en.assets['dawn-s01'], en.t.italic_gray40, 0.075)

            time.sleep(1)

            en.scene_pause()
            return 'wander'
        elif key == 'w':
            time.sleep(0.25)
            en.clear_canvas()

            time.sleep(2)

            en.write(en.assets['dawn-w00'])
            time.sleep(2)
            en.write(en.assets['dawn-w00'], en.bg, 0.003)

            en.clear_canvas()
            time.sleep(3)

            en.write(en.assets['dawn-w00'])

            time.sleep(1)

            en.scene_pause()
            return 'path'
