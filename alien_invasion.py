import sys 
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """ Overall class to manage assets and behavior"""
    def __init__(self):
        """Initialize the game,and create game resources"""
        pygame.init()
        self.settiings = Settings()

        self.screen=pygame.display.set_mode(
            (self.settiings.screen_width, self.settiings.screen_height))

        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
    

    def run_game(self):
        """"Start the main loop for the game"""
        while True:
            #watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #Redraw the secreen during each pass through the loop.
            self.screen.fill(self.settiings.bg_color)
            self.ship.blitme()
            # Make the most recently drawn screen visble.
            pygame.display.flip()

if __name__=='__main__':
    #Make a game instance, and run the game.
    ai= AlienInvasion()
    ai.run_game()



            



    