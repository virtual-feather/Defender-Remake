import pygame

class Sprite(object):

    def __init__(self, x, y, imageFile, load=True):
        self.x = x
        self.y = y
        self.initialPosition = (x, y)
        if load:
            self.image = pygame.image.load(imageFile)
        else:
            self.image = imageFile
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rectangle = self.image.get_rect(topleft=(x, y))

        # Attributes needed for collision
        self.leftSide = self.x
        self.rightSide = self.x + self.width
        self.topSide = self.y
        self.bottomSide = self.y + self.height
        self.visible = True

    def restartPosition(self):
        self.x = self.initialPosition[0]
        self.y = self.initialPosition[1]
        self.updateSprite()

    def drawSprite(self, screen):
        if self.visible:
            screen.window.blit(self.image, self.rectangle)

    def moveSprite(self, newX, newY):
        self.x += newX
        self.y += newY

        # Update remaining attributes
        self.updateSprite()

    def changeSize(self, x, y):
        self.image = pygame.transform.scale(self.image, (x,y))

        # Update remaining attributes
        self.updateSprite()

    def rotateImage(self, degree):
        self.image = pygame.transform.rotate(self.image, degree)

        # Update remaining attributes
        self.updateSprite()

    def updateSprite(self):
        self.x = self.x
        self.y = self.y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rectangle = self.image.get_rect(topleft=(self.x, self.y))
        self.leftSide = self.x
        self.rightSide = self.x + self.width
        self.topSide = self.y
        self.bottomSide = self.y + self.height

    def flipVertical(self):
        self.image = pygame.transform.flip(self.image, 1, 0)

    def flipHorizontal(self):
        self.image = pygame.transform.flip(self.image, 0, 1)
