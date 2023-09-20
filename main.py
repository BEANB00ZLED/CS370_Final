import pygame
import tile
from tile import Tile

def main():
    #Initialize pygame module
    pygame.init()
    
    #Set window size
    screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE, pygame.FULLSCREEN)
    
    #Set window name
    pygame.display.set_caption('Carcassonne')
    
    #For if game is running
    running = True
    
    #TEST
    test_tile = Tile(500, 500, 'TileAssets\Tile1_4.png')
    
    #*********
    #Game loop
    #*********
    
    while running:
    
        event_list = pygame.event.get()
    
        #Gets the events that are done
        event_list = pygame.event.get()
        #Check for event if user has made any sort of input
        for event in event_list:
            #Closes winow if X is pressed
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                #Closes window if esc key pressed
                if event.key == pygame.K_ESCAPE:
                    running = False
                
        #Set window color
        screen.fill("black")
        
        test_tile.process(screen, event_list)
        
        #Update the display
        pygame.display.flip()
        
        
if __name__ == "__main__":
    main()
