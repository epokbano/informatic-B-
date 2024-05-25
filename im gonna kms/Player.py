from MyConstants import WINDOW_WIDTH, WINDOW_HEIGHT, INTERFACE_WIDTH, ENEMY_WIDTH, PLAYER_WIDTH






class Player:
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
        self.speed = 5
        self.currentSpeed = 0
        
        self.BulletCount = 1
        self.BulletSpread = False
        self.PlayerHP = 3
        self.ShootingFrequency = 1 ## to be determined
        self.width = PLAYER_WIDTH
        self.moveLimit = [False, False]

 
    def draw(self, canvas):
        canvas.create_rectangle(self.xPos, self.yPos, self.xPos + PLAYER_WIDTH, self.yPos + PLAYER_WIDTH, fill='blue')

    def update(self):
        self.doMovement()
        return
        ## shoot 

    def initiatePlayerMovementSetup(self, root):
        root.bind("<KeyPress-A>", self.onKeyPress)
        root.bind("<KeyPress-a>", self.onKeyPress)
        root.bind("<KeyPress-D>", self.onKeyPress)
        root.bind("<KeyPress-d>", self.onKeyPress)

        root.bind("<KeyRelease-A>", self.onKeyRelease)
        root.bind("<KeyRelease-a>", self.onKeyRelease)
        root.bind("<KeyRelease-D>", self.onKeyRelease)
        root.bind("<KeyRelease-d>", self.onKeyRelease)

    def onKeyPress(self, event):

        keysym = event.keysym.lower()  # Convert to lowercase
        if keysym == 'a':
            if self.moveLimit[0] == False:
                self.moveLimit[0] = True
                self.currentSpeed -= self.speed
                print("A pressed")
        if keysym == 'd':
            if self.moveLimit[1] == False:
                self.moveLimit[1] = True
                self.currentSpeed += self.speed
                print("D pressed")

    def onKeyRelease(self, event):
        keysym = event.keysym.lower()
        if event.keysym == 'a':
            self.moveLimit[0] = False
            self.currentSpeed += self.speed
            print("A released")
        if event.keysym == 'd':
            self.moveLimit[1] = False
            self.currentSpeed -= self.speed
            print("D released")
        
    def doMovement(self):
        print("Current speed:", self.currentSpeed)
        if self.currentSpeed >= 0:   ## prawa kolizja
            if (self.rightBoundPos() + self.currentSpeed >= WINDOW_WIDTH): 
                self.xPos = WINDOW_WIDTH - self.width
                self.currentSpeed = 0  ##clip to wall
                print("Clipping right")
            else:
                self.xPos += self.currentSpeed

        elif self.currentSpeed <= 0 :          ## lewa kolizja
            if (self.xPos + self.currentSpeed <= INTERFACE_WIDTH):
                print("Clipping left")
                self.xPos = INTERFACE_WIDTH
                self.currentSpeed = 0 
            else:
                self.xPos += self.currentSpeed

    def rightBoundPos(self):
        return self.xPos + self.width
    