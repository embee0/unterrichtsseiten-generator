class Bubble:
    def __init__(self):
        self.reset(random(width), random(height), random(8, 22))

    def reset(self, x_position, y_position, diameter):
        self.x = x_position
        self.y = y_position
        self.diameter = diameter
        self.speed = random(0.4, 1.4)
        self.wobble = random(0.3, 1.0)
        self.phase = random(TWO_PI)

    def update(self):
        self.y -= self.speed
        self.x += sin(frame_count * 0.03 + self.phase) * self.wobble

        if self.y < -self.diameter:
            self.reset(random(width), height + random(10, 60), random(8, 22))

    def draw(self):
        no_fill()
        stroke(220, 245, 255, 170)
        stroke_weight(2)
        circle(self.x, self.y, self.diameter)
        no_stroke()


class Food:
    def __init__(self, x_position, y_position):
        self.x = x_position
        self.y = y_position
        self.size = random(6, 10)
        self.speed = random(1.2, 2.0)
        self.drift = random(-0.35, 0.35)
        self.phase = random(TWO_PI)

    def update(self):
        self.y += self.speed
        self.x += self.drift + sin(frame_count * 0.05 + self.phase) * 0.15

    def draw(self):
        fill(255, 188, 73)
        circle(self.x, self.y, self.size)

    def is_outside(self):
        return self.y > height + self.size


class Fish:
    def __init__(self, x_position, y_position):
        self.x = x_position
        self.base_y = y_position
        self.y = y_position
        self.scale = random(0.7, 1.35)
        self.body_length = 58 * self.scale
        self.body_height = 30 * self.scale
        self.tail_length = 24 * self.scale
        self.speed = random(0.6, 1.8)
        self.dx = self.speed
        self.phase = random(TWO_PI)
        self.body_color = color(random(70, 255), random(90, 230), random(110, 255))
        self.fin_color = color(random(140, 255), random(120, 220), random(40, 180))
        self.eye_size = 4.5 * self.scale

    def update(self, food_list):
        target_food = self.find_nearest_food(food_list)

        if target_food is not None:
            x_distance = target_food.x - self.x
            y_distance = target_food.y - self.y
            if x_distance > 0:
                self.dx += 0.02
            else:
                self.dx -= 0.02
            self.dx = constrain(self.dx, -2.2, 2.2)
            self.base_y += y_distance * 0.015
            self.base_y = constrain(self.base_y, 45, height - 35)

            if (
                dist(self.x, self.y, target_food.x, target_food.y)
                < self.body_length * 0.35
            ):
                food_list.remove(target_food)
        else:
            self.base_y += sin(frame_count * 0.02 + self.phase) * 0.35

        self.x += self.dx
        self.y = self.base_y + sin(frame_count * 0.08 + self.phase) * (8 * self.scale)

        if self.x < 35:
            self.x = 35
            self.dx = self.speed
        elif self.x > width - 35:
            self.x = width - 35
            self.dx = -self.speed

    def find_nearest_food(self, food_list):
        nearest_food = None
        nearest_distance = 10**9

        for food in food_list:
            current_distance = dist(self.x, self.y, food.x, food.y)
            if current_distance < nearest_distance:
                nearest_distance = current_distance
                nearest_food = food

        return nearest_food

    def draw(self):
        direction = 1
        if self.dx < 0:
            direction = -1

        no_stroke()
        fill(self.body_color)
        ellipse(self.x, self.y, self.body_length, self.body_height)

        fill(self.fin_color)
        triangle(
            self.x - direction * (self.body_length * 0.48),
            self.y,
            self.x - direction * (self.body_length * 0.48 + self.tail_length),
            self.y - self.body_height * 0.45,
            self.x - direction * (self.body_length * 0.48 + self.tail_length),
            self.y + self.body_height * 0.45,
        )

        fill(255, 255, 255, 160)
        ellipse(
            self.x + direction * self.body_length * 0.12,
            self.y - self.body_height * 0.12,
            self.body_length * 0.33,
            self.body_height * 0.2,
        )

        fill(255)
        circle(
            self.x + direction * self.body_length * 0.24,
            self.y - self.body_height * 0.12,
            self.eye_size * 1.6,
        )
        fill(22)
        circle(
            self.x + direction * self.body_length * 0.28,
            self.y - self.body_height * 0.12,
            self.eye_size,
        )


def draw_background():
    for row in range(height):
        blend = row / height
        red = 16 + 10 * blend
        green = 95 + 85 * blend
        blue = 165 + 55 * blend
        stroke(red, green, blue)
        line(0, row, width, row)

    no_stroke()
    fill(18, 84, 58, 180)
    rect(0, height - 42, width, 42)

    fill(200, 177, 108)
    rect(0, height - 18, width, 18)


def draw_seaweed():
    stroke(24, 118, 76)
    stroke_weight(5)

    for x_position in range(25, width, 44):
        line(
            x_position,
            height - 18,
            x_position + sin(frame_count * 0.03 + x_position * 0.1) * 10,
            height - 72 - (x_position % 3) * 12,
        )

    no_stroke()


def setup():
    global fishes, bubbles, food_list

    size(520, 320)
    fishes = []
    bubbles = []
    food_list = []

    for _ in range(7):
        fishes.append(Fish(random(50, width - 50), random(70, height - 70)))

    for _ in range(16):
        bubbles.append(Bubble())


def draw():
    draw_background()
    draw_seaweed()

    for bubble in bubbles:
        bubble.update()
        bubble.draw()

    for food in food_list[:]:
        food.update()
        food.draw()
        if food.is_outside():
            food_list.remove(food)

    for fish in fishes:
        fish.update(food_list)
        fish.draw()

    fill(255, 248, 214)
    text_size(14)
    text("Klick ins Aquarium: Futter fallen lassen", 16, 24)


def mouse_pressed():
    food_list.append(Food(mouse_x, mouse_y))
