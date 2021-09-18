import pygame
from src.core.Sprite import Sprite

class Ship(Sprite):
    # Laser class
    class __Laser(Sprite):
        def __init__(self, x, y, imageFile):
            super().__init__(x, y, imageFile)
            self.numOnScreen = 0
            self.visible = False

        # Return missile to its starting position
        def updateMissile(self, sprite, offsetX=0, offsetY=0):
            if not self.visible:
                self.x = sprite.x + offsetX
                self.y = sprite.y + offsetY

            self.updateSprite()

    def __init__(self, x, y, shipImage, laserImage):
        # Parent Constructor
        super().__init__(x, y, shipImage)
        self.moving = False
        self.direction = ''
        self.killCount = 0

        # Ship-specific requirements
        self.laser = self.__Laser(x, y, laserImage)
        self.shooting = False
        self.hp = 100
        self.lives = 3

    # updateHP(amt): Update the player's hp. If amount being subtracted is
    #                greater than the current HP, HP will automatically be 0
    def updateHP(self, amt):
        if self.hp + amt > 0:
            self.hp = self.hp + amt
        else:
            self.hp = 0

    # updateLives(amt): Update the player's life. If amount being subtracted is
    #                   greater than the current HP, HP will automatically be 0
    def updateLives(self, amt):
        if self.lives + amt > 0:
            self.lives = self.lives + amt
        else:
            self.lives = 0

    # setShipAttributes(): Set specific elements of the ship's attributes
    #                      if so needed.
    def setShipAttributes(self, hp=0, lives=0, visible = True):
        self.hp = self.hp + hp
        self.lives = self.lives + lives
        self.visible = visible

    # Bound player to game layout
    def moveBoundToLayout(self,speed):
        if self.moving and self.direction == "U" and (self.y >= 106):
            self.moveSprite(0,-speed)
        elif self.moving and self.direction == "D" and (self.y <= 444):
            self.moveSprite(0,speed)
