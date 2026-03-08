class Kreis:
    def __init__(self, x, y, durchmesser):
        self.x = x
        self.y = y
        self.durchmesser = durchmesser
        self.farbe = color(50, random(100, 230), 0)

    def falle_runter(self):
        self.y += 1

    def draw(self):
        max_aenderung = 0.2 * self.durchmesser
        aktueller_durchmesser = self.durchmesser + sin(frame_count / 30) * max_aenderung
        fill(self.farbe)
        circle(self.x, self.y, aktueller_durchmesser)


# Main


def setup():
    global kreise
    size(200, 200)
    kreise = []
    for nr in range(40):
        kreise.append(Kreis(random_int(0, width), random_int(0, height), 16))


def draw():
    global kreise
    background(200)
    for kreis in kreise:
        kreis.falle_runter()
        kreis.draw()
