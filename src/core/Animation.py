import pygame

class Animation(object):

    # Pre-defined: animation list must be a list of sprite objects
    def __init__(self, animation=[]):
        self.animationList = animation
        self.playing = False
        self.loop = False

    def updateAnimationLocation(self, locationX, locationY):
        for frame in self.animationList:
            frame.initialPosition = (locationX, locationY)
            frame.restartPosition()
            frame.updateSprite()

    def updateAnimationSize(self, x, y):
        for frame in self.animationList:
            frame.changeSize(x,y)
            frame.updateSprite()

    def playAnimation(self, sheet, window, loop=False, locationX=0, locationY=0):
        self.updateAnimationLocation(locationX, locationY)

        if loop:
            # Turn on attributes
            self.playing = True
            self.loop = True

            # Run while it is looping
            while self.loop:
                for frame in self.animationList:
                    frame.visible = True
                    frame.drawSprite(window)
                    print(frame.x, frame.y, frame.rectangle)
        else:
            # Turn on/off attributes
            self.playing = True
            self.loop = False

            # Run through animation
            for frame in self.animationList:
                frame.drawSprite(window)
                print(frame.x, frame.y, frame.rectangle)

            # Turn off
            self.playing = False

            for frame in self.animationList:
                frame.visible = False

    def isPlaying(self):
        return self.playing

    def stopAnimation(self):
        self.loop = False

        for frame in self.animationList:
            frame.visible = False