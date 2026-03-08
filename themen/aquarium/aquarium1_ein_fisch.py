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
        self.x = x_position
        self.y = y_position

    def draw(self):
        no_stroke()
        fill(255, 141, 76)
        ellipse(self.x, self.y, 84, 42)

        triangle(
            self.x - 40,
            self.y,
            self.x - 68,
            self.y - 18,
            self.x - 68,
            self.y + 18,
        )

        fill(255)
        circle(self.x + 22, self.y - 6, 11)
        fill(15)
        circle(self.x + 24, self.y - 6, 5)


def setup():
    global fish
    size(420, 260)
    fish = Fish(width / 2, height / 2)


def draw():
    draw_background()
    fish.draw()
