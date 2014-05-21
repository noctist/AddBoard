#!/usr/bin/python
import pygame
import random
#from gi.repository import Gtk

defaultPanelColor = (220, 220, 220)
prospectivePanelColor = (220, 200, 200)
prospectiveGoalPanelColor = (255, 240, 240)
goalPanelColor = (255, 250, 250)
movesColor = (255, 180, 180)
circleColor = (255, 100, 100)
levelColor = (90, 90, 90)
scoreColor = (255, 150, 150)

left = 0
right = 1
up = 2
down = 3
class TestGame:
    
    def __init__(self):
        # Set up a clock for managing the frame rate.
        self.clock = pygame.time.Clock()

        self.controllable = 1;

        self.movesLeft = 0;

        self.goToNextLevel = 0;

        self.screenAlpha = 255;

        self.recty = 0;
        self.rectx = 0;

        self.rectw = 50;
        self.recth = 50

        self.x = -100
        self.y = 100

        self.vx = 10
        self.vy = 0

        self.paused = False
        self.direction = 1

        self.fontSmall = pygame.font.Font(pygame.font.get_default_font(), 10)
        self.fontMedium = pygame.font.Font(pygame.font.get_default_font(), 20)
        self.fontLarge = pygame.font.Font(pygame.font.get_default_font(), 30)

        self.textArray = [3*[0] for t in range(25)]
        for i in range(25):
            self.textArray[i][0] = self.fontSmall.render(str(i + 1), 1, (120, 120, 120), (220, 220, 220))
            self.textArray[i][1] = self.fontMedium.render(str(i + 1), 1, (120, 120, 120), (220, 220, 220))
            self.textArray[i][2] = self.fontLarge.render(str(i + 1), 1, (120, 120, 120), (220, 220, 220))
            self.textArray[i][0].set_alpha(0)
            self.textArray[i][0].set_colorkey((220, 220, 220))
            self.textArray[i][1].set_alpha(0)
            self.textArray[i][1].set_colorkey((220, 220, 220))
            self.textArray[i][2].set_alpha(0)
            self.textArray[i][2].set_colorkey((220, 220, 220))

        #This value represents the current level in the game
        self.level = 0;

        self.score = 0;

        #Creates the first level in the game. This method adds 1 to the level, and creates a new array of squares for the player to navigate
        self.nextLevel();

        #self.createArray(4)

        #The X and Y positions of the circle representing the player
        self.circlex = 0.0
        self.circley = 0.0;

        #The X and Y indices representing the player's position on the board
        self.indexx = 0;
        self.indexy = 0;



        print "initialized TestGame"
        

    def set_paused(self, paused):
        self.paused = paused

    # Called to save the state of the game to the Journal.
    def write_file(self, file_path):
        pass

    # Called to load the state of the game from the Journal.
    def read_file(self, file_path):
        pass

    # The main game loop.
    def run(self):
        self.running = True

        screen = pygame.display.get_surface()

        while self.running:
            # Pump GTK messages.
            #while Gtk.events_pending():
                #Gtk.main_iteration()

            # Pump PyGame messages.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.VIDEORESIZE:
                    pygame.display.set_mode(event.size, pygame.RESIZABLE)
                elif event.type == pygame.KEYDOWN:
                    if self.goToNextLevel == 0:
                        if event.key == pygame.K_LEFT and self.indexx > 0:
                            # Move left
                            i = self.array[self.indexx - 1][self.indexy]
                            #if self.indexy == self.rowLength / 2 and self.indexx > self.rowLength / 2 and self.indexx - i <= self.rowLength / 2:
                                #self.goToNextLevel = 1
                            self.movesLeft -= 1
                            self.indexx -= i
                        elif event.key == pygame.K_RIGHT and self.indexx < self.rowLength - 1:
                            # Move right
                            i = self.array[self.indexx + 1][self.indexy]
                            #if self.indexy == self.rowLength / 2 and self.indexx < self.rowLength / 2 and self.indexx + i >= self.rowLength / 2:
                                #self.goToNextLevel = 1
                            self.movesLeft -= 1
                            self.indexx += i
                        elif event.key == pygame.K_UP and self.indexy > 0:
                            # Move up
                            i = self.array[self.indexx][self.indexy - 1]
                            #if self.indexx == self.rowLength / 2 and self.indexy > self.rowLength / 2 and self.indexy - i <= self.rowLength / 2:
                                #self.goToNextLevel = 1
                            self.movesLeft -= 1
                            self.indexy -= i
                        elif event.key == pygame.K_DOWN and self.indexy < self.rowLength - 1:
                            # Move down
                            i = self.array[self.indexx][self.indexy + 1]
                            #if self.indexx == self.rowLength / 2 and self.indexy < self.rowLength / 2 and self.indexy + i >= self.rowLength / 2:
                                #self.goToNextLevel = 1
                            self.indexy += i
                            self.movesLeft -= 1
                        if self.indexx == self.rowLength / 2 and self.indexy == self.rowLength / 2:
                            self.goToNextLevel = 1
                            self.indexx = self.indexy = self.rowLength / 2
                        self.renderMoves()

            if self.goToNextLevel == 1:
                self.screenAlpha -= 5
                
                if self.screenAlpha <= 0:
                    self.score += self.movesLeft;
                    self.nextLevel()
            else:
                self.screenAlpha += 15
                if self.movesLeft == 0:
                    self.level -= 1
                    self.score -= 1
                    if self.score < 0:
                        self.score = 0
                    self.goToNextLevel = 1



            if self.screenAlpha < 0:
                self.screenAlpha = 0;
            elif self.screenAlpha > 255:
                self.screenAlpha = 255

            screen.set_alpha(self.screenAlpha)

            # Make sure the index values aren't out of the range of the array
            if self.indexx < 0:
                self.indexx = 0
            elif self.indexx > self.rowLength - 1:
                self.indexx = self.rowLength - 1;
            if self.indexy < 0:
                self.indexy = 0
            elif self.indexy > self.rowLength - 1:
                self.indexy = self.rowLength - 1;
            # Clear Display
            screen.fill((240, 240, 240))  # 255 for white

            
            # Draw the ball
            #pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 100)

            self.recty = 0;
            self.rectx = 0;

            self.w = screen.get_width(); self.h = screen.get_height();

            self.xplus = (self.w - self.h) / 2

            self.recth = self.rectw = ((self.h) / self.rowLength)

            self.circlex += ((self.xplus + (self.rectw * (self.indexx + 0.5))) - self.circlex) * 0.2

            self.circley += (((self.recth * (self.indexy + 0.5))) - self.circley) * 0.2

            
            textIndex = 2;
            if (self.rectw < 25):
                textIndex = 0
            elif (self.rectw < 50):
                textIndex = 1
            for i in range(self.rowLength):
                self.rectx += 14
                for j in range(self.rowLength):
                    
                    col = defaultPanelColor
                    center = 0
                    if i == self.rowLength /2 and j == self.rowLength / 2:
                        col = goalPanelColor
                        center = 1
                    if i == self.indexx:
                        if j < self.indexy and (j == self.indexy - self.array[i][self.indexy - 1] or (j == 0 and self.indexy - self.array[i][self.indexy - 1] < 0)):
                            if center:
                                col = prospectiveGoalPanelColor
                            else:
                                col = prospectivePanelColor
                        elif j > self.indexy and (j == self.indexy + self.array[i][self.indexy + 1] or (j == self.rowLength - 1 and self.indexy + self.array[i][self.indexy + 1] >= self.rowLength)):
                            if center:
                                col = prospectiveGoalPanelColor
                            else:
                                col = prospectivePanelColor
                    elif j == self.indexy:
                        if i < self.indexx and (i == self.indexx - self.array[self.indexx - 1][j] or (i == 0 and self.indexx - self.array[self.indexx - 1][j] < 0)):
                            if center:
                                col = prospectiveGoalPanelColor
                            else:
                                col = prospectivePanelColor
                        elif i > self.indexx and (i == self.indexx + self.array[self.indexx + 1][j] or (i == self.rowLength - 1 and self.indexx + self.array[self.indexx + 1][j] >= self.rowLength)):
                            if center:
                                col = prospectiveGoalPanelColor
                            else:
                                col = prospectivePanelColor

                    # Draw the board rectangles to the screen
                    pygame.draw.rect(screen,  col, pygame.Rect((self.rectw * i) + self.xplus, self.recth * j, self.rectw - 2, self.recth - 2))
                    alp = 50;
                    if self.goToNextLevel:
                        alp = 0
                    elif abs(i - self.indexx) + abs(j - self.indexy) <= 1:
                        alp = 255
                    arrayNum = self.array[i][j] - 1
                    

                    a = self.textArray[arrayNum][textIndex].get_alpha();
                    if a < alp:
                        a = alp
                    self.textArray[arrayNum][textIndex].set_alpha(alp)

                    screen.blit(self.textArray[arrayNum][textIndex], (self.xplus + ((self.rectw * i) + ((self.rectw - self.textArray[arrayNum][textIndex].get_width()) / 2)), (self.recth * j) + ((self.recth - self.textArray[arrayNum][textIndex].get_height()) / 2)))
                    self.recty += 14
            if not self.goToNextLevel:   
                pygame.draw.rect(screen, (120, 120, 120), pygame.Rect((self.rectw * self.indexx) + self.xplus, self.recth * self.indexy, self.rectw - 2, self.recth - 2))
            pygame.draw.circle(screen, circleColor, (int(self.circlex), int(self.circley)), self.rectw / 3)
            screen.blit(self.movesSurface, (int(self.circlex - (self.movesSurface.get_width() / 2)), int(self.circley - (self.movesSurface.get_height() / 2))))
            screen.blit(self.levelSurface, (24, 24))
            screen.blit(self.scoreSurface, (screen.get_width() - self.scoreSurface.get_width() - 24, 24))
            # Flip Display
            pygame.display.flip()

            # Try to stay at 30 FPS
            self.clock.tick(30)


    def nextLevel(self):
        self.level += 1
        row = (self.level) + 3;
        self.movesLeft = row + 1;
        if (row%2) == 0:
            row += 1
        else:
            self.movesLeft -= 2
        self.controllable = 1;
        self.goToNextLevel = 0;
        self.renderMoves()
        self.renderLevel()
        self.renderScore()
        print "Going to level with " + str(row) + " rows"
        self.createArray(row)

    def renderMoves(self):
        font = self.fontLarge;
        if ((self.rectw / 3) * 2 < 25):
            font = self.fontSmall
        elif ((self.rectw / 3) * 2 < 50):
            font = self.fontLarge
        self.movesSurface = font.render(str(self.movesLeft), 1, (movesColor), circleColor )
        self.movesSurface.set_colorkey(circleColor)

    def renderLevel(self):
        self.levelSurface = self.fontLarge.render("Level " + str(self.level), 1, levelColor, (255,255,255))
        self.levelSurface.set_colorkey((255,255,255))

    def renderScore(self):
        self.scoreSurface = self.fontLarge.render(str(self.score) + " points", 1, scoreColor, (255, 255, 255))
        self.scoreSurface.set_colorkey((255, 255, 255))

    def createArray(self, rows):
        self.indexx = self.indexy = 0
        self.rowLength = rows
        self.array = [rows*[0] for t in range(rows)]
        #self.textArray = [3*[0] for t in range((rows / 2) + 1)]

        cent = rows / 2
        direction = random.randrange(0, 3)
        modNum = 4
        for i in range(rows):
            for j in range (rows):
                direction += 1
                val = 1
                if j == cent and i == cent :
                    val = random.randrange(1, (rows / 2))
                elif direction%modNum == left or direction%modNum == right:
                    val = (cent - i) + 1
                elif direction&modNum == up or direction%modNum == down:
                    val = (cent - j) + 1
                else: 
                    val = random.randrange(1, (rows / 2))

                if (val <= 0):
                    val = random.randrange(1, (rows / 2))
                #self.array[i][j] = random.randrange(1, (rows / 2) + 1)
                self.array[i][j] = val
        

# This function is called when the game is run directly from the command line:
# ./TestGame.py
def main():
    pygame.init()
    pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    game = TestGame()
    game.run()

if __name__ == '__main__':
    main()
