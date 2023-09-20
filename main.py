import pygame
from tile import Tile
import button
from deck import Deck


def main():
    #Initialize pygame module
    pygame.init()
    
    #Set window size
    screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE, pygame.FULLSCREEN)
    
    #Set window name
    pygame.display.set_caption('Carcassonne')
    
    #For if game is running
    running = True

    testDeck = Deck()
    tile_list = []
    #*********
    #Game loop
    #*********
    def processTile():
        drawnTile = testDeck.drawTile()
        print("drawn tile 2", drawnTile)
        tile_list.append(drawnTile)



    buttonTest = button.Button(100, 100, 100, 100, "CLICK ME", click_function=processTile, color="white",
                               hover_color="grey", click_color="red", font_size=30)

    while running:
    
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

        for i in tile_list:
            i.process(screen, event_list)


        buttonTest.process(screen, event_list)

        #Update the display
        pygame.display.flip()

        
if __name__ == "__main__":
    main()
