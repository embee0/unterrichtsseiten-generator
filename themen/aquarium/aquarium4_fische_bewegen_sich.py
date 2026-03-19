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
    def __init__(self, x_position, y_position, scale, body_color, fin_color, speed):
        self.x = x_position
        self.base_y = y_position
        self.y = y_position
        self.scale = scale
        self.body_color = body_color
        self.fin_color = fin_color
        self.speed = speed
        self.dx = speed

    def move(self):
        self.x += self.dx

        if self.x < 48:
            self.x = 48
            self.dx = self.speed
        elif self.x > width - 48:
            self.x = width - 48
            self.dx = -self.speed

        self.y = self.base_y + sin(frame_count * 0.08) * (7 * self.scale)

    def draw(self):
        direction = 1
        if self.dx < 0:
            direction = -1
        body_length = 84 * self.scale
        body_height = 42 * self.scale
        tail_length = 28 * self.scale

        no_stroke()
        fill(self.body_color)
        ellipse(self.x, self.y, body_length, body_height)

        fill(self.fin_color)
        triangle(
            self.x - direction * body_length * 0.48,
            self.y,
            self.x - direction * (body_length * 0.48 + tail_length),
            self.y - body_height * 0.45,
            self.x - direction * (body_length * 0.48 + tail_length),
            self.y + body_height * 0.45,
        )

        fill(255)
        circle(
            self.x + direction * body_length * 0.26,
            self.y - body_height * 0.12,
            11 * self.scale,
        )
        fill(15)
        circle(
            self.x + direction * body_length * 0.28,
            self.y - body_height * 0.12,
            5 * self.scale,
        )


def create_random_fish():
    return Fish(
        random(70, width - 70),
        random(70, height - 55),
        random(0.7, 1.25),
        color(random(90, 255), random(120, 230), random(80, 180)),
        color(random(220, 255), random(110, 180), random(50, 120)),
        random(0.8, 1.8),
    )


def setup():
    global fishes
    size(420, 260)
    fishes = []

    for _ in range(7):
        fishes.append(create_random_fish())


def draw():
    draw_background()

    for fish in fishes:
        fish.move()
        fish.draw()
