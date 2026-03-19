DEMO_ROUTE = [
    (0.84, 0.22),
    (0.18, 0.3),
    (0.74, 0.82),
    (0.28, 0.72),
    (0.9, 0.5),
]


class Agent:
    def __init__(self, x_position, y_position, speed, body_color):
        self.x = x_position
        self.y = y_position
        self.speed = speed
        self.body_color = body_color
        self.radius = 16
        self.demo_target_index = 0

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
        self.y = constrain(self.y, self.radius + 24, height - self.radius)

    def demo_steuern(self):
        route_point_x, route_point_y = DEMO_ROUTE[self.demo_target_index]
        target_x = width * route_point_x
        target_y = height * route_point_y
        self.x += (target_x - self.x) * 0.018
        self.y += (target_y - self.y) * 0.018
        if dist(self.x, self.y, target_x, target_y) < 18:
            self.demo_target_index = (self.demo_target_index + 1) % len(DEMO_ROUTE)

    def position(self):
        return self.x, self.y

    def draw(self):
        glow_size = self.radius * 3.4 + sin(frame_count * 0.12) * 3
        fill(90, 210, 255, 40)
        circle(self.x, self.y, glow_size)
        no_stroke()
        fill(self.body_color)
        circle(self.x, self.y, self.radius * 2)

        fill(255, 255, 255, 45)
        arc(self.x, self.y, self.radius * 3.4, self.radius * 3.4, -PI * 0.2, PI * 1.2)

        fill(255, 240)
        circle(self.x - 4, self.y - 4, 9)
        circle(self.x + 4, self.y - 4, 9)
        fill(18)
        circle(self.x - 4, self.y - 4, 4)
        circle(self.x + 4, self.y - 4, 4)


class Drohne:
    def __init__(self, x_position, y_position, speed, body_color):
        self.x = x_position
        self.y = y_position
        self.speed = speed
        self.body_color = body_color
        self.size = 26
        self.phase = random(TWO_PI)

    def verfolgen(self, target_x, target_y):
        if target_x > self.x:
            self.x += self.speed
        elif target_x < self.x:
            self.x -= self.speed

        if target_y > self.y:
            self.y += self.speed
        elif target_y < self.y:
            self.y -= self.speed

    def abstand(self, other_x, other_y):
        return dist(self.x, self.y, other_x, other_y)

    def draw(self):
        halo_size = self.size * 1.8 + sin(frame_count * 0.14 + self.phase) * 2
        fill(255, 110, 110, 34)
        circle(self.x, self.y, halo_size)
        no_stroke()
        fill(self.body_color)
        rect(self.x - self.size / 2, self.y - self.size / 2, self.size, self.size, 6)

        fill(255, 210)
        circle(self.x - 6, self.y - 4, 6)
        circle(self.x + 6, self.y - 4, 6)
        stroke(255, 130)
        stroke_weight(2)
        line(self.x - 16, self.y - 16, self.x - 7, self.y - 7)
        line(self.x + 16, self.y - 16, self.x + 7, self.y - 7)
        line(self.x - 16, self.y + 16, self.x - 7, self.y + 7)
        line(self.x + 16, self.y + 16, self.x + 7, self.y + 7)
        no_stroke()

        fill(255, 70, 70, 120)
        circle(self.x, self.y + 2, 5)


def create_drones():
    center_x = width / 2
    center_y = height / 2
    return [
        Drohne(center_x - 42, center_y - 28, 0.18, color(255, 95, 95)),
        Drohne(center_x + 34, center_y - 18, 0.25, color(255, 162, 72)),
        Drohne(center_x - 24, center_y + 34, 0.27, color(255, 220, 82)),
        Drohne(center_x + 44, center_y + 22, 0.36, color(145, 255, 170)),
    ]


def reset_game():
    global agent, drones, game_over, survived_frames
    global demo_mode, demo_switch_frame, game_over_frame

    agent = Agent(width * 0.84, height / 2, 2.5, color(110, 220, 255))
    drones = create_drones()
    game_over = False
    game_over_frame = None
    survived_frames = 0
    demo_mode = True
    demo_switch_frame = frame_count


def controls_active():
    return links or rechts or oben or unten


def update_controls(current_key, current_key_code, is_pressed):
    global links, rechts, oben, unten

    if current_key == "a" or current_key == "A" or current_key_code == 65:
        links = is_pressed
        return True
    if current_key == "d" or current_key == "D" or current_key_code == 68:
        rechts = is_pressed
        return True
    if current_key == "w" or current_key == "W" or current_key_code == 87:
        oben = is_pressed
        return True
    if current_key == "s" or current_key == "S" or current_key_code == 83:
        unten = is_pressed
        return True

    return False


def draw_background():
    background(14, 18, 30)
    no_stroke()
    fill(24, 30, 48)
    rect(18, 18, width - 36, height - 36, 14)
    no_fill()
    stroke(72, 90, 128)
    stroke_weight(2)
    rect(18, 18, width - 36, height - 36, 14)
    no_stroke()


def draw_hud():
    fill(235, 245, 255)
    text_size(15)
    text("WASD: Agent bewegen", 18, 26)
    text(f"Zeit: {survived_frames // 60} s", width - 100, 26)

    if demo_mode:
        fill(255, 214, 120)
        text("Demo-Modus: Taste drücken zum Übernehmen", 18, 48)

    if game_over:
        fill(10, 16, 30, 210)
        rect(90, 120, width - 180, 110, 16)
        fill(255, 210, 210)
        text_size(24)
        text("Game Over", width / 2 - 62, 160)
        fill(240)
        text_size(15)
        text("Neustart läuft automatisch ...", width / 2 - 98, 194)


def setup():
    global links, rechts, oben, unten

    size(560, 360)
    text_font(create_font("Helvetica", 16))
    links = False
    rechts = False
    oben = False
    unten = False
    reset_game()


def draw():
    global demo_mode, game_over, survived_frames, game_over_frame

    draw_background()

    if game_over and game_over_frame is not None and frame_count - game_over_frame > 90:
        reset_game()

    if not game_over:
        if controls_active():
            demo_mode = False

        if demo_mode:
            agent.demo_steuern()
        else:
            agent.steuern()

        agent_x, agent_y = agent.position()

        for drone in drones:
            drone.verfolgen(agent_x, agent_y)
            if drone.abstand(agent_x, agent_y) < 18:
                game_over = True
                game_over_frame = frame_count

        survived_frames += 1

    agent.draw()

    for drone in drones:
        drone.draw()

    draw_hud()


def key_pressed():
    global demo_mode

    if update_controls(key, key_code, True):
        demo_mode = False

def key_released():
    update_controls(key, key_code, False)