#!/usr/bin/python
import pygame
#from gi.repository import Gtk


class TestGame:
    def __init__(self):
        # Set up a clock for managing the frame rate.
        self.clock = pygame.time.Clock()

        self.recty = 0;
        self.rectx = 0;

        self.x = -100
        self.y = 100

        self.vx = 10
        self.vy = 0

        self.paused = False
        self.direction = 1

        self.createArray(4)

        self.circlex = 0.0
        self.circley = 0.0;

        self.font = pygame.font.Font(pygame.font.get_default_font(), 20)

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
                    if event.key == pygame.K_LEFT:
                        self.direction = -1
                    elif event.key == pygame.K_RIGHT:
                        self.direction = 1

            # Move the ball
            if not self.paused:
                self.x += self.vx * self.direction
                if self.direction == 1 and self.x > screen.get_width() + 100:
                    self.x = -100
                elif self.direction == -1 and self.x < -100:
                    self.x = screen.get_width() + 100
                self.y += self.vy
                if self.y > screen.get_height() - 100:
                    self.y = screen.get_height() - 100
                    self.vy = -self.vy

                self.vy += 5

            # Clear Display
            screen.fill((150, 150, 150))  # 255 for white

            
            # Draw the ball
            #pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 100)

            self.recty = 0;
            self.rectx = 0;

            self.w = screen.get_width(); self.h = screen.get_height();

            self.xplus = (self.w - self.h) / 2

            self.recth = self.rectw = ((self.h) / self.rowLength)

            self.circlex += ((self.xplus + (self.rectw * (2 + 0.5))) - self.circlex) * 0.2

            self.circley += (((self.recth * (0 + 0.5))) - self.circley) * 0.2

            

            for i in range(self.rowLength):
                self.rectx += 14
                for j in range(self.rowLength):
                    pygame.draw.rect(screen, (220, 220, 220), pygame.Rect((self.rectw * i) + self.xplus, self.recth * j, self.rectw - 2, self.recth - 2))
                    self.recty += 14

            pygame.draw.circle(screen, (255, 0, 0), (int(self.circlex), int(self.circley)), self.rectw / 3)
            # Flip Display
            pygame.display.flip()

            # Try to stay at 30 FPS
            self.clock.tick(30)

    def createArray(self, rows):
        self.rowLength = rows
        self.array = [rows*[0] for t in range(rows)]
        self.textArray = [rows*[0] for t in range(rows)]
        for i in range(rows):
            for j in range (rows):
                self.array[i][j] = i + j 
                self.textArray[i][j] = "hello"
        print self.array
        print self.textArray
# This function is called when the game is run directly from the command line:
# ./TestGame.py
def main():
    pygame.init()
    pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    game = TestGame()
    game.run()

if __name__ == '__main__':
    main()
