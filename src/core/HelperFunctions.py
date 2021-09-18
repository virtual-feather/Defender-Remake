# User input testing
keysPressed = []
def testKeyPressed(key):
    return key in keysPressed

# Overlap detection
def testSpriteOverlap(sprite1,sprite2):
    noOverlap = ((sprite1.rightSide <= sprite2.leftSide) or
                 (sprite2.rightSide <= sprite1.leftSide) or
                 (sprite1.bottomSide <= sprite2.topSide) or
                 (sprite2.bottomSide <= sprite1.topSide))
    return not noOverlap

# Creates a moving background (for games like Galaga) - 2 Background Sprites needed
def backgroundWrap(background,background2,speed):
    if background.x >= -720:
        background.moveSprite(speed,0)
        background2.moveSprite(speed,0)
    else:
        background.x = 0
        background2.x = 720
        background.moveSprite(speed,0)
        background2.moveSprite(speed,0)

    background.updateSprite()
    background2.updateSprite()

###########
# Colors! #
###########

WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
GREY = (160,160,160)
FUCHSIA = (255, 0, 255)
GRAY = (128, 128, 128)
LIME = (0, 128, 0)
MAROON = (128, 0, 0)
NAVYBLUE = (0, 0, 128)
OLIVE = (128, 128, 0)
PURPLE = (128, 0, 128)
TEAL = (0,128,128)