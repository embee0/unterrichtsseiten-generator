def setup():
    global k1
    size(200, 200)
    k1 = Kreis(100, 100)


class Kreis:
    def __init__(self, x, y):
        # TODO: Speichere x und y im Objekt.
        ...

    def draw(self):
        # TODO: Berechne einen Durchmesser und zeichne den Kreis an self.x und self.y.
        ...


def draw():
    global k1
    background(200)
    k1.draw()
