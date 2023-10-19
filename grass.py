from pico2d import load_image


class Grass:
    def __init__(self, y_move=0):
        self.x, self.y = 400,30 + y_move
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass
