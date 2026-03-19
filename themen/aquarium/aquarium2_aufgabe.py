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
    def __init__(self, x_position, y_position, scale, body_color, fin_color):
        self.x = x_position
        self.y = y_position
        # TODO: Speichere scale, body_color und fin_color im Objekt.
        ...

    def draw(self):
        # TODO: Berechne body_length, body_height und tail_length mit self.scale.
        ...

        no_stroke()
        # TODO: Nutze self.body_color und self.fin_color beim Zeichnen.
        ...


def setup():
    global fish
    size(420, 260)
    fish = Fish(210, 135, 1.1, color(255, 190, 73), color(255, 112, 67))


def draw():
    draw_background()
    fish.draw()