import time
import tkinter as tk
from Enemy import Enemy
from MyConstants import WINDOW_WIDTH, WINDOW_HEIGHT, INTERFACE_WIDTH, ENEMY_WIDTH
from Player import Player
FPS_CAP = 60


class GameWindow:
    def __init__(self, master, width, height):
        self.master = master
        self.width = width
        self.height = height
        self.canvas = tk.Canvas(master, width=width, height=height, bg="BLACK")
        self.canvas.pack()
        self.master.protocol("WM_DELETE_WINDOW", self.stop_game)
        self.enemyList = []
        self.playerObject = None
        
        
        
    def stop_game(self):
        self.running = False
        self.master.destroy()

    def tick(self):
        for i in self.enemyList:
            i.update()
        self.playerObject.update()
        


    def render(self):
        if self.canvas:
            self.canvas.delete("all")
            self.canvas.create_rectangle(0,0, INTERFACE_WIDTH, WINDOW_HEIGHT, outline= "#FF00FF", fill="grey12")
            
            self.playerObject.draw(self.canvas)

            for i in self.enemyList:
                if i.xPos >= INTERFACE_WIDTH and i.xPos <= WINDOW_WIDTH:
                    i.draw(self.canvas)
                else:
                    self.canvas.delete("all")
                    print("ERROR")
            

    def run(self):
        running = True
        clock = time.time()

        while running:
            # Calculate delta time (dt)
            dt = time.time() - clock
            clock = time.time()

            # Update game logic
            self.tick()

            # Draw
            self.render()

            # Cap the frame rate (for demonstration purposes)
            if dt < 1/FPS_CAP:
                time.sleep(1/FPS_CAP - dt)


            self.master.update()

        print("Game loop exited")

    def addEnemy(self, enemy):
        self.enemyList.append(enemy)

    def initiatePlayer(self):
        self.playerObject = Player(500, 500)


    

############################# MAIN #############################
# Create the Tkinter window
if __name__ == "__main__":
    print("Start of App")
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Space Invaders made in Poland")
    # root.bind("<KeyPress>", onKeyPress)
    # root.bind("<KeyRelease>", onKeyRelease)

    # Run the game
    game = GameWindow(root, WINDOW_WIDTH, WINDOW_HEIGHT)

    game.initiatePlayer()
    game.playerObject.initiatePlayerMovementSetup(root)
    game.addEnemy(Enemy(300, 100, 1, 2))
    game.run()


    root.mainloop()

