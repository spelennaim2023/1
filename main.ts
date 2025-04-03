input.onButtonPressed(Button.A, function on_button_pressed_a() {
    music.play(music.stringPlayable("- - C5 - - - - - ", 120), music.PlaybackMode.UntilDone)
    basic.showLeds(`
        . # . # .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        `)
    basic.pause(2000)
    basic.showLeds(`
        . # . # .
        . # . # .
        . . . . .
        . . . . .
        . # # # .
        `)
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    basic.showLeds(`
        . # . # .
        . # . # .
        . . . . .
        . # . # .
        # . # . #
        `)
    music.play(music.stringPlayable("- - G B - - - - ", 120), music.PlaybackMode.InBackground)
    basic.pause(200)
    basic.showIcon(IconNames.Confused)
    basic.pause(200)
    basic.showLeds(`
        . # . # .
        . # . # .
        . . . . .
        . # . # .
        # . # . #
        `)
    music.stopAllSounds()
    basic.pause(5000)
    basic.showLeds(`
        . # . # .
        . # . # .
        . . . . .
        . . . . .
        . # # # .
        `)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    music.play(music.stringPlayable("- - C C C C - - ", 120), music.PlaybackMode.UntilDone)
    basic.showLeds(`
        . # . # .
        . # . # .
        . . . . .
        . # # # .
        # . . . #
        `)
    basic.pause(2000)
    basic.showLeds(`
        . # . # .
        . # . # .
        . . . . .
        . . . . .
        . # # # .
        `)
})
