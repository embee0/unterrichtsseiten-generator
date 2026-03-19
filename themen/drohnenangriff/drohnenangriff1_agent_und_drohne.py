def draw_background():
    background(18, 24, 42)


class Agent:
    def __init__(self, x_position, y_position):
        self.x = x_position
        self.y = y_position

    def draw(self):
        no_stroke()
        fill(110, 220, 255)
        circle(self.x, self.y, 32)


class Drohne:
    def __init__(self, x_position, y_position):
        self.x = x_position
        self.y = y_position

    def draw(self):
        no_stroke()
        fill(255, 112, 112)
        rect(self.x - 13, self.y - 13, 26, 26, 6)


def setup():
    global agent, drohne
    size(520, 320)
    agent = Agent(390, 180)
    drohne = Drohne(130, 110)


def draw():
    draw_background()
    agent.draw()
    drohne.draw()
