from src.core.Base import Base
from src.core.HelperFunctions import *
from pygame.locals import *
import random

# Test class houses the FUNCTIONALITY of the game with the assets
# defined in Base

# Test-Case: Defender
class Test(Base):
    # GAME FUNCTIONALITY FUNCTIONS #
    def toggleGame(self, restart=False):
        if restart:
            # Restart all game variables
            self.level = 0
            self.player.setShipAttributes(visible=False)
            self.shipUI.visible = False
            self.player.killCount = 0
            self.enemyKills.changeText('Enemies Defeated: '+str(self.player.killCount))
            self.player.lives = 3

            # Restart all enemies
            for enemy in self.enemyList:
                enemy.dead = True
                enemy.moving = False
                enemy.visible = False
                enemy.restartPosition()
        else:
            # Start the game
            if testKeyPressed(K_SPACE):
                self.level = 1
                self.levelText.changeText('Level: ' + str(self.level))

            self.player.setShipAttributes(visible=True)
            self.shipUI.visible = True

    def toggleInstructions(self):
        if testKeyPressed(K_b) and self.level == 999:
            self.level = 0
        elif testKeyPressed(K_i) and self.level == 0:
            self.level = 999

    # Restart some things and go to next level
    def nextLevel(self):
        # Update the level
        self.level = self.level + 1
        self.levelText.changeText('Level: '+str(self.level))

        # Restart all enemies
        for enemy in self.enemyList:
            enemy.dead = True
            enemy.moving = False
            enemy.visible = False
            enemy.restartPosition()

    # Define keyboard input for player movement
    def playerMovement(self):
        # Move Up
        if testKeyPressed(K_w):
            self.player.moving = True
            self.player.direction = 'U'

        # Move Down
        elif testKeyPressed(K_s):
            self.player.moving = True
            self.player.direction = 'D'

        # Debugging
        elif testKeyPressed(K_q):
            print("\nPlayer info: "+str(self.player.x), str(self.player.y), str(self.player.rectangle))
            print("Animation Location: "+str(self.explosion.animationList[0].x), str(self.explosion.animationList[0].y),
                  self.explosion.animationList[0].visible)
            print("Player Image: "+str(self.player.image),
                  "Animation Image: "+str(self.explosion.animationList[0].image))
            self.player.lives = self.player.lives - 1

        # Player is not moving
        else:
            self.player.moving = False

        # Update the movement
        self.player.moveBoundToLayout(2)
        self.player.laser.updateMissile(self.player, 12, 15)

    # Define keyboard input for Missiles
    def missileMovement(self):
        # If Missile is off-screen
        if self.player.laser.x > 730:
            self.player.laser.visible = False
            self.player.laser.x = self.player.x
            self.player.laser.numOnScreen = 0
            self.player.laser.updateSprite()

        # If Missile is ready to shoot
        elif testKeyPressed(K_SPACE) and (self.player.laser.numOnScreen < 1) and self.player.visible:
            self.player.laser.numOnScreen = 1
            self.player.laser.visible = True

        # Shoot Missile
        if self.player.laser.visible:
            self.player.laser.moveSprite(15, 0)

    # Spawn in enemies onto the screen
    # enemyList - Will be implemented to add in certain enemies
    def spawnEnemies(self, speedList, enemyList=None):
        # Select and enemy in the enemy list
        for enemy in enemyList:
            # If the enemy is off-screen, kill it and take a player life
            if enemy.x < -40:
                enemy.visible = False
                enemy.moving = False
                enemy.y = random.randint(110, 440)
                enemy.dead = True
                self.player.lives = self.player.lives - 1

            # If the enemy died, restart the enemy attributes
            if enemy.dead:
                enemy.x = 740
                enemy.y = random.randint(110, 440)
                enemy.moving = False
                enemy.dead = False

            # Make the enemy visible again
            elif not enemy.visible:
                enemy.visible = True

            # If not moving, select speed from list
            if not enemy.moving:
                enemy.speed = speedList[random.randint(0, len(speedList)-1)]
                enemy.moving = True
            else:
                enemy.moveSprite(-enemy.speed, 0)

    def collisionCheck(self):
        # Collisions regarding Enemies
        for enemy in self.enemyList:

            # Check if it's being hit
            if testSpriteOverlap(enemy, self.player.laser) and enemy.visible and self.player.laser.visible:
                # Kill the enemy
                enemy.visible = False
                enemy.dead = True

                # Animate explosion
                # self.explosion.playAnimation(self.explosionSheet, self.window, False, self.player.laser.x, self.player.laser.y)

                # Update the player's kill
                self.player.laser.x = 740
                self.player.killCount = self.player.killCount + 1
                self.enemyKills.changeText('Enemies Defeated: '+str(self.player.killCount))

                # Update the highScore if needed
                if self.window.highScore < self.player.killCount:
                    self.window.highScore = self.window.highScore + 1
                    self.highScoreCount.changeText('High Score: '+str(self.window.highScore))

            # Check if player is being hit
            if testSpriteOverlap(enemy, self.player) and enemy.visible:
                self.player.lives = self.player.lives - 1

                # Kill enemy
                enemy.dead = True
                enemy.visible = False

            # Check if it's the player's last life
            if self.player.lives == 0:
                self.toggleGame(restart=True)


    # DRAW LEVELS
    def drawLives(self):
        # Determine the current number of lives
        numOfLives = self.player.lives

        # Draw the lives
        for i in range(0, numOfLives):
            self.playerHealth[i].drawSprite(self.window)

    def drawUserUI(self):
        # Draw ann UI stuff in-game
        self.playerGameUI.drawSprite(self.window)
        self.playerGameUIVL1.drawSprite(self.window)
        self.playerGameUIVL2.drawSprite(self.window)
        self.playerGameUIHL.drawSprite(self.window)
        self.shipUI.drawSprite(self.window)
        self.levelText.displayFont(self.window, (565, 5), WHITE)
        self.gameTitle.displayFont(self.window, (210, 20), GREY)
        self.enemyKills.displayFont(self.window, (565, 75), WHITE)
        self.highScoreCount.displayFont(self.window, (320, 80), WHITE)

        # Draw the lives
        self.drawLives()

    def drawPlayerStuff(self):
        self.player.laser.drawSprite(self.window)
        self.player.drawSprite(self.window)

    def drawEnemies(self):
        for enemy in self.enemyList:
            enemy.drawSprite(self.window)

    def drawInstructions(self):
        backgroundWrap(self.space1, self.space2, -2)

        # Draw Backgrounds
        self.space1.drawSprite(self.window)
        self.space2.drawSprite(self.window)

        self.instructions1.displayFont(self.window, (70, 160), WHITE)
        self.instructions2.displayFont(self.window, (70, 200), WHITE)
        self.instructions3.displayFont(self.window, (70, 240), WHITE)
        self.instructions4.displayFont(self.window, (70, 280), WHITE)

    def drawLvl0(self):
        backgroundWrap(self.space1, self.space2, -2)

        # Draw Backgrounds
        self.space1.drawSprite(self.window)
        self.space2.drawSprite(self.window)

        # Draw Menu UI
        self.gameTitle.displayFont(self.window, (210, 50), GREY)
        self.tempInstruction.displayFont(self.window, (240, 400), WHITE)
        self.tempStartScreen.displayFont(self.window, (260, 360), WHITE)

    def drawLvl1(self):
        backgroundWrap(self.space1, self.space2, -2)

        # Draw Backgrounds
        self.space1.drawSprite(self.window)
        self.space2.drawSprite(self.window)

        # Draw Player and Laser
        self.drawPlayerStuff()

        # Draw Player UI
        self.drawUserUI()

        # Draw Enemies
        self.drawEnemies()

    # BRING FUNCTIONALITY AND DRAW TOGETHER #
    def Instructions(self):
        self.drawInstructions()

        self.toggleInstructions()

    def Level0(self):
        # Draw the level
        self.drawLvl0()

        # Start the game (Currently Space to start)
        self.toggleGame()
        self.toggleInstructions()

    def Level1(self):
        # Draw the level
        self.drawLvl1()

        # Import game functionality
        self.playerMovement()
        self.missileMovement()
        self.spawnEnemies([1, 2.5, 1.5, 3], self.enemyList)
        self.collisionCheck()  # CONTAINS LOSE CONDITION

        # Win condition
        if self.player.killCount == 10:
            self.nextLevel()

    def Level2(self):
        # Draw the level
        self.drawLvl1()

        # Import game functionality
        self.playerMovement()
        self.missileMovement()
        self.spawnEnemies([2.5, 2.3, 3, 3.2], self.enemyList)
        self.collisionCheck()   # CONTAINS LOSE CONDITION

        """
        # Win Condition
        if self.player.killCount == 30:
            self.nextLevel()
        """

    # Function that gets sent to the game loop
    def update(self):
        # Update the game based on the current level
        if self.level == 0:
            self.Level0()
        elif self.level == 1:
            self.Level1()
        elif self.level == 2:
            self.Level2()
        elif self.level == 999:
            self.Instructions()

# Instantiate and run
if __name__ == '__main__':
    Test().run()