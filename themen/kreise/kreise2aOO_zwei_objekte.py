class Kreis:
    def __init__(self, x, y, durchmesser):
        self.x = x
        self.y = y
        self.durchmesser = durchmesser

    def draw(self):
        max_aenderung = 0.2 * self.durchmesser
        aktueller_durchmesser = self.durchmesser + sin(frame_count / 30) * max_aenderung
        fill(0, 0, 255)
        circle(self.x, self.y, aktueller_durchmesser)


# Main


def setup():
    global k1, k2
    size(200, 200)
    k1 = Kreis(145, 60, 35)
    k2 = Kreis(80, 145, 90)


def draw():
    global k1, k2
    background(200)
    k1.draw()
    k2.draw()
