import pygame
from tile import Tile
import button
from deck import Deck
from grid import Grid
from meeple import Meeple


def main():
    #Initialize pygame module
    pygame.init()
    
    #Set window size
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    
    #Set window name
    pygame.display.set_caption('Carcassonne')
    #Set window icon
    pygame.display.set_icon(pygame.image.load('MiscAssets/CarcasonneLogoTransparentBackground.png'))
    
    #For if game is running
    running = True

    game_deck = Deck()
    tile_list = []
    meeple_list = []
    grid = Grid()
    def processTile():
        drawn_tile = game_deck.drawTile()
        tile_list.insert(0, drawn_tile)

    #Create our button for drawing the deck
    draw_button = button.Button((screen.get_width() / 2) - 200, screen.get_height() - 150, 400, 100, "Draw Tile (72)", click_function=processTile, color="white",
                               hover_color="grey", click_color="red", font_size=30)
    
    #Creating the tile that starts in play
    starting_tile = Tile((screen.get_width() / 2.0) -50, (screen.get_height() / 2.0) - 150, "TileAssets/Tile8_4.png")
    tile_list.insert(0, starting_tile)
    
    #*********
    #Game loop
    #*********
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
                #Press 1 for purple meeple
                elif event.key == pygame.K_1:  
                    meeple_list.insert(0, Meeple(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], (128, 0, 128)))
                #Press 2 for magenta meeple
                elif event.key == pygame.K_2:
                    meeple_list.insert(0, Meeple(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], (255, 0, 255)))
                #Press 3 for blue meeple
                elif event.key == pygame.K_3:
                    meeple_list.insert(0, Meeple(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], (0, 0, 255)))
                #Press 4 for orange meeple
                elif event.key == pygame.K_4:
                    meeple_list.insert(0, Meeple(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], (255, 140, 0)))
                    
                    
        #Set window color
        screen.fill("black")
        grid.drawGrid(1050, 10, surface=screen)
        for i in tile_list:
            if i is not None:
                i.process(screen, event_list)
        for i in meeple_list:
            if i.show:
                i.process(screen, event_list)
            else:
                meeple_list.remove(i)
        draw_button.process(screen, event_list)

        #Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
