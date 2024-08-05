import sys
import pygame
from settings import Settings

class AlienInvasion:
    """Overall class to manage the game assets and behaviour."""

    def __init__(self):
        """Initialise the game and create game resources."""
        # pygame.init() function initializes the background settings 
        pygame.init
        # set control for the frame rate
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Create a display window - tuple referring to the pixel dimensions
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        # Set the background colour
        self.bg_colour = (230, 230, 230)

    # A method to control the game
    def run_game(self):
        """Start the main loop for the game."""
        # Event loop - an event is user's action in the game (keyboard/mouse)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_colour)

        # Make the most recently drawn screen visible
        pygame.display.flip()
        # Create an instance of the class Clock and make the clock tick at the end of the while loop
        self.clock.tick(60)
    
if __name__ == '__main__':
    # Create a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()

