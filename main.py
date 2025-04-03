def on_button_pressed_a():
    music.play(music.string_playable("- - C5 - - - - - ", 120),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_leds("""
        . # . # .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        """)
    basic.pause(2000)
    basic.show_leds("""
        . # . # .
        . # . # .
        . . . . .
        . . . . .
        . # # # .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.show_leds("""
        . # . # .
        . # . # .
        . . . . .
        . # . # .
        # . # . #
        """)
    music.play(music.string_playable("- - G B - - - - ", 120),
        music.PlaybackMode.IN_BACKGROUND)
    basic.pause(200)
    basic.show_icon(IconNames.CONFUSED)
    basic.pause(200)
    basic.show_leds("""
        . # . # .
        . # . # .
        . . . . .
        . # . # .
        # . # . #
        """)
    music.stop_all_sounds()
    basic.pause(5000)
    basic.show_leds("""
        . # . # .
        . # . # .
        . . . . .
        . . . . .
        . # # # .
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    music.play(music.string_playable("- - C C C C - - ", 120),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_leds("""
        . # . # .
        . # . # .
        . . . . .
        . # # # .
        # . . . #
        """)
    basic.pause(2000)
    basic.show_leds("""
        . # . # .
        . # . # .
        . . . . .
        . . . . .
        . # # # .
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)
