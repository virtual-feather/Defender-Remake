from src.core.Sprite import Sprite

class Enemy(Sprite):

    def __init__(self, x, y, imageFile):
        super().__init__(x, y, imageFile)
        self.moving = False
        self.dead = True
        self.speed = 0
        self.enemyHealth = None