class Kreis:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        background(200)
        diameter = sin(frame_count / 60) * 50 + width / 2
        fill(0, 0, 255)
        ellipse(self.x, self.y, diameter, diameter)

# Main
def setup():
    global k1
    size(400, 400)
    k1 = Kreis(200, 200)

def draw():
    global k1
    k1.draw()
    