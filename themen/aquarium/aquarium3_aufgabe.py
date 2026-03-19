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
        self.scale = scale
        self.body_color = body_color
        self.fin_color = fin_color

    def draw(self):
        body_length = 84 * self.scale
        body_height = 42 * self.scale
        tail_length = 28 * self.scale

        no_stroke()
        fill(self.body_color)
        ellipse(self.x, self.y, body_length, body_height)

        fill(self.fin_color)
        triangle(
            self.x - body_length * 0.48,
            self.y,
            self.x - body_length * 0.48 - tail_length,
            self.y - body_height * 0.45,
            self.x - body_length * 0.48 - tail_length,
            self.y + body_height * 0.45,
        )

        fill(255)
        circle(
            self.x + body_length * 0.26, self.y - body_height * 0.12, 11 * self.scale
        )
        fill(15)
        circle(self.x + body_length * 0.28, self.y - body_height * 0.12, 5 * self.scale)


def create_random_fish():
    # TODO: Ersetze die festen Werte durch random(...), damit nicht alle Fische gleich aussehen.
    return Fish(
        width / 2,
        height / 2,
        1.0,
        color(255, 190, 73),
        color(255, 112, 67),
    )


def setup():
    global fishes
    size(420, 260)
    fishes = []

    # TODO: Erzeuge mehrere Fische und fuege sie mit append(...) zur Liste hinzu.
    ...


def draw():
    draw_background()

    # TODO: Gehe mit einer Schleife durch fishes und zeichne jeden Fisch.
    ...