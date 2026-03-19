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

    def position(self):
        return self.x, self.y

    def draw(self):
        no_stroke()
        fill(110, 220, 255)
        circle(self.x, self.y, self.radius * 2)


class Drohne:
    def __init__(self, x_position, y_position, speed):
        self.x = x_position
        self.y = y_position
        self.speed = speed
        # TODO: Gib jeder Drohne eine zufaellige Farbe.
        # color(...) erzeugt einen Farbwert, den du in self.body_color
        # speichern und spaeter mit fill(...) benutzen kannst.
        ...

    def verfolgen(self, ziel_x, ziel_y):
        if ziel_x > self.x:
            self.x += self.speed
        elif ziel_x < self.x:
            self.x -= self.speed

        if ziel_y > self.y:
            self.y += self.speed
        elif ziel_y < self.y:
            self.y -= self.speed

    def abstand(self, ziel_x, ziel_y):
        return dist(self.x, self.y, ziel_x, ziel_y)

    def draw(self):
        no_stroke()
        fill(self.body_color)
        rect(self.x - 13, self.y - 13, 26, 26, 6)


def setup():
    global agent, drohnen, links, rechts, oben, unten, game_over
    size(520, 320)
    agent = Agent(390, 180, 2.5)
    links = False
    rechts = False
    oben = False
    unten = False
    game_over = False

    drohnen = []
    # TODO: Erzeuge mehrere Drohnen mit verschiedenen Startpositionen
    # und fuege sie der Liste hinzu.
    ...


def draw():
    global game_over

    draw_background()

    if not game_over:
        agent.steuern()
        agent_x, agent_y = agent.position()

        # TODO: Lasse alle Drohnen verfolgen und pruefe die Kollision in einer Schleife.
        ...

    agent.draw()

    for drohne in drohnen:
        drohne.draw()

    if game_over:
        fill(255)
        text_size(28)
        text("Game Over", 190, 50)


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
