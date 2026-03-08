def draw_background():
    for row in range(height):
        blend = row / height
        stroke(18, 110 + 60 * blend, 170 + 40 * blend)
        line(0, row, width, row)

    no_stroke()
    fill(19, 100, 70, 170)
    rect(0, height - 38, width, 38)

    fill(204, 182, 112)
    rect(0, height - 14, width, 14)


class Fish:
    def __init__(self, x_position, y_position):
        # TODO: Speichere x_position und y_position im Objekt.
        ...

    def draw(self):
        # TODO: Zeichne hier den Fisch aus Ellipse, Dreieck und Auge.
        ...


def setup():
    global fish
    size(420, 260)
    fish = Fish(width / 2, height / 2)


def draw():
    draw_background()
    fish.draw()