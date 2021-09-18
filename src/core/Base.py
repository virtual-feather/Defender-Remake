from src.core.Ship import Ship
from src.core.Sprite import Sprite
from src.core.Window import Window
from src.core.Enemy import Enemy
from src.core.Text import Text
from src.core.HelperFunctions import *
from src.core.Animation import Animation
from src.core.SpriteSheet import SpriteSheet
import pygame, sys, os.path
from pygame.locals import *

# Base class houses all the assets that will be used
class Base(object):

    def __init__(self):
        # Set up game-specific variables
        self.level = 0
        self.window = Window(720, 480, "Defender")
        self.player = Ship(100, 240, os.path.join('../../assets/sprite', 'airship.png'),
                           os.path.join('../../assets/sprite', 'ship_beam.png'))
        self.enemyList = [
            Enemy(740, 0, os.path.join('../../assets/sprite', 'airship.png')),
            Enemy(740, 0, os.path.join('../../assets/sprite', 'airship.png')),
            Enemy(740, 0, os.path.join('../../assets/sprite', 'airship.png'))
        ]

        # Explosion Sprite
        self.explosionSheet = SpriteSheet(os.path.join('../../assets/sprite', 'explosion.png'))
        self.explosion = Animation([
            # Top Row in sheet
            Sprite(0, 0, self.explosionSheet.imageAt((0, 100, 0, 100)), load=False),
            Sprite(0, 0, self.explosionSheet.imageAt((100, 200, 0, 100)), load=False),
            Sprite(0, 0, self.explosionSheet.imageAt((200, 300, 0, 100)), load=False),
            Sprite(0, 0, self.explosionSheet.imageAt((300, 400, 0, 100)), load=False),
            Sprite(0, 0, self.explosionSheet.imageAt((400, 500, 0, 100)), load=False),
            Sprite(0, 0, self.explosionSheet.imageAt((500, 600, 0, 100)), load=False)

        ])

        # Background dump
        self.space1 = Sprite(0, 0, os.path.join('../../assets/ui', 'space.png'))
        self.space2 = Sprite(720, 0, os.path.join('../../assets/ui', 'space.png'))

        # UI Stuff
        self.shipUI = Sprite(10, 25, os.path.join('../../assets/sprite', 'airship.png'))
        self.playerGameUI = Sprite(0, 0, os.path.join('../../assets/ui', 'playerUI.png'))
        self.playerGameUIHL = Sprite(0, 35, os.path.join('../../assets/ui', 'line.png'))
        self.playerGameUIVL1 = Sprite(100, 0, os.path.join('../../assets/ui', 'line.png'))
        self.playerGameUIVL2 = Sprite(490, 0, os.path.join('../../assets/ui', 'line.png'))
        self.playerHealth = [
            Sprite(120, 15, os.path.join('../../assets/sprite', 'heart.png')),
            Sprite(120, 40, os.path.join('../../assets/sprite', 'heart.png')),
            Sprite(120, 65, os.path.join('../../assets/sprite', 'heart.png'))
        ]
        self.levelText = Text('Level: '+str(self.level), 25)
        self.gameTitle = Text('DEFENDER', 80)
        self.enemyKills = Text('Enemies Defeated: '+str(self.player.killCount), 20)
        self.highScoreCount = Text('High Score: '+str(self.window.highScore), 20)
        self.tempStartScreen = Text('Press Space to Start!', 30)
        self.tempInstruction = Text("Press 'I' for Instructions!", 30)

        # Instruction UI Stuff
        self.instructions1 = Text("Press 'W' to move up and 'S' to move down.", 40)
        self.instructions2 = Text("Press 'Space' to shoot the laser. If the enemy", 40)
        self.instructions3 = Text("goes off screen or hits you, you lose a life.", 40)
        self.instructions4 = Text("Press 'b' to go back to the main menu.", 40)

        # Update those variables to be game-ready
        self.player.setShipAttributes(visible=False)
        self.player.changeSize(50,28)
        self.player.laser.updateMissile(self.player, 12, 15)

        # Change heart size
        for heart in self.playerHealth:
            heart.changeSize(15, 15)

        # Change individual enemy variables
        for enemy in self.enemyList:
            enemy.changeSize(50, 28)
            enemy.visible = False
            enemy.flipVertical()

        # Update animation frame variables
        for frame in self.explosion.animationList:
            frame.visible = False

        # Update UI Variables
        self.shipUI.visible = False
        self.shipUI.changeSize(75, 40)
        self.playerGameUI.changeSize(720, 104)
        self.playerGameUIHL.changeSize(720, 150)
        self.playerGameUIVL1.rotateImage(90)
        self.playerGameUIVL2.rotateImage(90)
        self.playerGameUIVL1.changeSize(150, 100)
        self.playerGameUIVL2.changeSize(150, 100)

    # Defined in Test examples
    def update(self):
        pass

    # Main game loop
    def run(self):
        # Create game variables
        gameRunning = True

        while gameRunning:
            # Run the update
            self.update()

            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    gameRunning = False
                if event.type == pygame.KEYDOWN:
                    keysPressed.append(event.key)
                if event.type == pygame.KEYUP:
                    keysPressed.remove(event.key)

            pygame.display.update()
            self.window.setFPS(60)

        pygame.quit()
        sys.exit()