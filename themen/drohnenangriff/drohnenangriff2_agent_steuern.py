def draw_background():
    background(18, 24, 42)


class Agent:
    def __init__(self, x_position, y_position, speed):
        self.x = x_position
        self.y = y_position
        self.speed = speed
        self.radius = 16

    def steuern(self):
        if links:
            self.x -= self.speed
        if rechts:
            self.x += self.speed
        if oben:
            self.y -= self.speed
        if unten:
            self.y += self.speed

        self.x = constrain(self.x, self.radius, width - self.radius)
        self.y = constrain(self.y, self.radius, height - self.radius)

    def draw(self):
        no_stroke()
        fill(110, 220, 255)
        circle(self.x, self.y, self.radius * 2)


class Drohne:
    def __init__(self, x_position, y_position):
        self.x = x_position
        self.y = y_position

    def draw(self):
        no_stroke()
        fill(255, 112, 112)
        rect(self.x - 13, self.y - 13, 26, 26, 6)


def setup():
    global agent, drohne, links, rechts, oben, unten
    size(520, 320)
    agent = Agent(390, 180, 3.2)
    drohne = Drohne(130, 110)
    links = False
    rechts = False
    oben = False
    unten = False


def draw():
    draw_background()
    agent.steuern()
    agent.draw()
    drohne.draw()


def key_pressed():
    global links, rechts, oben, unten
    if key == "a" or key == "A" or key_code == 65:
        links = True
    elif key == "d" or key == "D" or key_code == 68:
        rechts = True
    elif key == "w" or key == "W" or key_code == 87:
        oben = True
    elif key == "s" or key == "S" or key_code == 83:
        unten = True


def key_released():
    global links, rechts, oben, unten
    if key == "a" or key == "A" or key_code == 65:
        links = False
    elif key == "d" or key == "D" or key_code == 68:
        rechts = False
    elif key == "w" or key == "W" or key_code == 87:
        oben = False
    elif key == "s" or key == "S" or key_code == 83:
        unten = False
