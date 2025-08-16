import sys
import pygame

class AlienInvasion:
    """Overall class to manage tame assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resource"""

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien invasion")


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            #Whatch for keborad and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Make the most recentl draw screen visible
            pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()