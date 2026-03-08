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
    global kreise
    size(200, 200)
    kreise = []
    kreise.append(Kreis(145, 60, 35))
    kreise.append(Kreis(80, 145, 90))
    kreise.append(Kreis(45, 85, 42))


def draw():
    global kreise
    background(200)
    for kreis in kreise:
        kreis.draw()
