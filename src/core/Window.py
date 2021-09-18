import pygame

# Create a blank game window
class Window:
    pygame.display.init()

    def __init__(self, x, y, caption):
        self.x = x
        self.y = y

        displayFlags = pygame.DOUBLEBUF

        self.window = pygame.display.set_mode([x, y], displayFlags)
        self.caption = pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()

        # Keep track of the high score in the current running of the game
        self.highScore = 0

    def setFPS(self, num):
        self.clock.tick(num)
