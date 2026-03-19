def draw_background():
    background(18, 24, 42)


class Agent:
    def __init__(self, x_position, y_position):
        # TODO: Speichere x_position und y_position im Objekt.
        ...

    def draw(self):
        # TODO: Zeichne den Agenten als Kreis.
        ...


class Drohne:
    def __init__(self, x_position, y_position):
        # TODO: Speichere x_position und y_position im Objekt.
        ...

    def draw(self):
        # TODO: Zeichne die Drohne als Quadrat oder Rechteck.
        ...


def setup():
    global agent, drohne
    size(520, 320)
    agent = Agent(390, 180)
    drohne = Drohne(130, 110)


def draw():
    draw_background()
    agent.draw()
    drohne.draw()
