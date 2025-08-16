import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage tame assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resource"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
    
    def _check_events(self):
        """Respond to keypress and mouse events."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            #Moving the ship
            elif event.type == pygame.KEYDOWN:
                #Moving right
                if event.key == pygame.K_RIGHT:
                    #Move the ship to the right.
                    self.ship.moving_right = True
                
                #Moving left
                elif event.key == pygame.K_LEFT:
                    #Move the ship to the left
                    self.ship.moving_left = True

            #Stop moving the ship
            elif event.type == pygame.KEYUP:
                #Stop moving right
                if event.key == pygame.K_RIGHT:
                    #Stop to right
                    self.ship.moving_right = False
                
                elif event.key == pygame.K_LEFT:
                    #Stop to left
                    self.ship.moving_left = False
                
                    
            
                
    
    def _update_screen(self):
        """Update images on the screen, and flip to the now screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    #Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game() 