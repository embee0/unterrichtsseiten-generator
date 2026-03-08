class Kreis:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        diameter = sin(frame_count / 60) * 20 + 80
        fill(0, 0, 255)
        circle(self.x, self.y, diameter)


# Main


def setup():
    global k1
    size(200, 200)
    k1 = Kreis(100, 100)


def draw():
    global k1
    background(200)
    k1.draw()
