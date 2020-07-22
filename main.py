def on_pin_pressed_p0():
    global button_count
    button_count += 1
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    global button_count
    button_count = 0
    basic.show_number(0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_number(button_count)
input.on_button_pressed(Button.B, on_button_pressed_b)

button_count = 0
button_count = 0
basic.show_number(0)

def on_forever():
    pass
basic.forever(on_forever)
