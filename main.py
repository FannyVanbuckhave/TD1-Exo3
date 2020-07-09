def on_button_pressed_a():
    global nb
    if nb <= 10:
        basic.show_number(nb)
        nb += nb + 1
input.on_button_pressed(Button.A, on_button_pressed_a)

nb = 0
nb = 1

def on_forever():
    pass
basic.forever(on_forever)
