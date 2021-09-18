import pygame

# Game Text
class Text:
    pygame.font.init()
    allFonts = pygame.font.get_fonts()

    def __init__(self, contentString: str, fontSize: float):
        self.visible = True
        self.content = contentString
        self.font = pygame.font.SysFont('Times.ttc', fontSize)
        self.text = ""

    def displayFont(self, screen, positionTuple, colorTuple):
        if self.visible:
            self.text = self.font.render(self.content, True, colorTuple)
            screen.window.blit(self.text, (positionTuple[0], positionTuple[1]))

    def changeText(self, newString):
        self.content = newString
