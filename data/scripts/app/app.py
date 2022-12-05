import pygame # Game module Pygame

# My module
from data.scripts.app.app_settings import *

class App:
    
    def __init__(self) -> None:
        pygame.init() # Initialization PyGame
        self.screen = pygame.display.set_mode((SIZE[0], SIZE[1])) 
        pygame.display.set_caption(NAME) # Set name screen
        self.clock = pygame.time.Clock() # In-game clock
        self.dt = 0
        
    def loop(self) -> None:
        
        # -*-*-  Input Block -*-*-
        for event in pygame.event.get():                                            # Main events in PyGame
            if event.type == pygame.QUIT:                                           # If you want to close the program...
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:                                # If mouse button down...
                pass

            if event.type == pygame.KEYDOWN:                                        # If key button down...
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
            
        # If pressed ...
        # keys=pygame.key.get_pressed()
        # if keys[pygame.K_LSHIFT]:
        # -*-*-              -*-*-
        
        
        # -*-*- Physics Block -*-*-
        
        # -*-*-               -*-*-
        
        
        # -*-*- Rendering Block -*-*-
        
        # -*-*-                 -*-*-
        
        # -*-*- Update Block -*-*-
        pygame.display.update()                                                    # Update display
        self.dt = self.clock.tick(FPS)                                             # return time between frames
        # -*-*-              -*-*-