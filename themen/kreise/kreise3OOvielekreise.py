class Kreis:
    def __init__(self, x, y, durchmesser):
        self.x = x
        self.y = y
        self.durchmesser = durchmesser
        r = 50  # random(255)
        g = random(100, 230)
        b = 0  # random(255)
        self.color = color(r, g, b)

    def falle_runter(self):
        self.y += 1

    def draw(self):
        max_aenderung = 0.2 * self.durchmesser
        # Durch sin(frame_count) ändert sich der Durchmesser im Laufe der Zeit:
        aktueller_durchmesser = self.durchmesser + sin(frame_count / 30) * max_aenderung
        fill(self.color)
        circle(self.x, self.y, aktueller_durchmesser)


# Main
def setup():
    global kreise
    size(200, 200)
    kreise = []
    for nr in range(180):
        k = Kreis(random_int(0, width), random_int(0, height), 16)
        kreise.append(k)


def draw():
    global kreise  # Liste von Kreisen
    background(200)
    for kreis in kreise:  # einzelner kreis aus der Liste
        kreis.falle_runter()
        kreis.draw()
