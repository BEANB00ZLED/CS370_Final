import pygame

def main():
    #Initialize pygame module
    pygame.init()
    
    #Set window size
    screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE, pygame.FULLSCREEN)
    
    #Set window name
    pygame.display.set_caption('Carcassonne')
    
    #For if game is running
    running = True
    
    #*********
    #Game loop
    #*********
    
    while running:
    
        #Check for event if user has made any sort of input
        for event in pygame.event.get():
            #Closes winow if X is pressed
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                #Closes window if esc key pressed
                if event.key == pygame.K_ESCAPE:
                    running = False
                
        #Set window color
        screen.fill("black")
        
        #Update the display
        pygame.display.flip()
        
        
if __name__ == "__main__":
    main()
