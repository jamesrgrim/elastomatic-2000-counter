input.onPinPressed(TouchPin.P0, function () {
    button_count += 1
})
input.onButtonPressed(Button.A, function () {
    button_count = 0
    basic.pause(1000)
    basic.showNumber(0)
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(button_count)
})
let button_count = 0
button_count = 0
basic.showNumber(0)
basic.forever(function () {
	
})
