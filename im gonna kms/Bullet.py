from MyConstants import WINDOW_WIDTH, WINDOW_HEIGHT, INTERFACE_WIDTH, ENEMY_WIDTH, PLAYER_WIDTH, BULLETSPEED, BULLET_WIDTH, BULLET_HEIGHT
from Player import Player



class Bullet:
    
    def __init__(self, xPos, yPos, shootingFrequency, speed):
        self.xPos = PLAYER_WIDTH/2 
        self.yPos = Player.xPos
        self.width = BULLET_WIDTH
        self.height = BULLET_HEIGHT
        self.shootingFrequency = shootingFrequency
        self.speed = BULLETSPEED



    def draw(self, canvas):
        canvas.create_rectangle(self.xPos, self.yPos, self.xPos + BULLET_WIDTH, self.yPos + BULLET_HEIGHT, fill='white')

    def update(self):
        self.doMovement()
        self.BulletDissapear()

    def doMovement(self):
        self.yPos += -self.speed
    
    def BulletDissapear(self):
        # if self.xPos < 0:
        return