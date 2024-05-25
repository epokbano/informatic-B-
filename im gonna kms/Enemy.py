from MyConstants import WINDOW_WIDTH, WINDOW_HEIGHT, INTERFACE_WIDTH, ENEMY_WIDTH, PLAYER_WIDTH



class Enemy:
    def __init__(self, xPos, yPos, shootingFrequency, speed):
        self.xPos = xPos   
        self.yPos = yPos
        self.width = ENEMY_WIDTH
        self.shootingFrequency = shootingFrequency
        self.speed = speed



    def draw(self, canvas):
        canvas.create_rectangle(self.xPos, self.yPos, self.xPos + self.width, self.yPos + self.width, fill='red')

    def update(self):
        self.doMovement()
        ## shoot 



    def doMovement(self):
        if self.speed > 0:   ## prawa kolizja
            if (self.rightBoundPos() + self.speed >= WINDOW_WIDTH): 
                self.xPos = WINDOW_WIDTH - self.width ##clip to wall
                self.speed = -self.speed
            else:
                self.xPos += self.speed

        else:           ## lewa kolizja
            if (self.xPos + self.speed <= INTERFACE_WIDTH): 
                self.xPos = INTERFACE_WIDTH
                self.speed = -self.speed
            else:
                self.xPos += self.speed

    def rightBoundPos(self):
        return self.xPos + self.width
    
    