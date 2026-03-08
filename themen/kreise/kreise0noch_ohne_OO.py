def setup():
    size(200, 200)


def draw():
    background(200)
    durchmesser = width / 2
    max_aenderung = 20
    aktueller_durchmesser = durchmesser + sin(frame_count / 30) * max_aenderung
    fill(0, 0, 255)
    circle(width / 2, height / 2, aktueller_durchmesser)
