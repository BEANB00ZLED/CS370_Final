import pygame
import button

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
    #Button Creation and testing
    #*********

    def buttonTest():
        print("PRESSEED!!!!!!!!JJJJ")

    buttonTest = button.Button(100, 100, 100, 100, "CLICK ME", click_function=buttonTest, color="white", font_size=30)
    #*********
    #Game loop
    #*********
    while running:

    
        #Gets the events that are done
        event_list = pygame.event.get()
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


        buttonTest.process(screen)

        #Update the display
        pygame.display.flip()


        
if __name__ == "__main__":
    main()
