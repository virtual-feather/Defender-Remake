import pygame

# Handles the importing of Sprite Sheets
class SpriteSheet(object):

    def __init__(self, fileName):
        try:
            self.sheet = pygame.image.load(fileName).convert()
        except pygame.error as e:
            print("Error importing a sheet")
            raise SystemExit(e)

    def imageAt(self, rectangle, colorKey=None):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        #image.blit(self.sheet, (0,0), rect)

        if colorKey is not None:
            if colorKey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    def imagesAt(self, rects, colorKey = None):
        return [self.imageAt(rect, colorKey) for rect in rects]
