import pygame
import button
from Meeples import Meeples

def main():
    #Initialize pygame module
    pygame.init()
    
    #Set window size
    screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE, pygame.FULLSCREEN)
    
    #Set window name
    pygame.display.set_caption('Carcassonne')
    
    #meeple = Meeples(100, 100, 50, 50, 'red')
    meeple_list = [] #List to store  meeples
    current_color = None # Initialize current_color to None
    dragging_meeple = None # Initialize a varibale to keep track of the meeple being dragged 
    
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
        #for event in pygame.event.get():
        for event in event_list:
            #Closes winow if X is pressed
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                #Closes window if esc key pressed
                if event.key == pygame.K_ESCAPE:
                    running = False
                #added for meeple
                elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                    current_color = event.key - pygame.K_1 + 1
                
        #Set window color
        screen.fill("black")

        # Initialize a flag to check if a meeple was deleted during this frame
        deleted_meeple = False
        
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and current_color is not None:
                    # Check if the mouse click is inside an existing meeple's rectangle
                    for meeple in meeple_list:
                        if meeple.rect.collidepoint(event.pos):
                            dragging_meeple = meeple
                            break
                    else:
                        # If not inside an existing meeple, create a new one
                        new_meeple = Meeples(event.pos[0], event.pos[1], 50, 50, current_color)
                        meeple_list.append(new_meeple)
                elif event.button == 3:
                    #check if a  meeple was already delted in this fram
                    if not deleted_meeple:
                        for meeple in meeple_list.copy(): # Use a copy to avoid modifying the original list while iterating
                            if meeple.rect.collidepoint(event.pos):
                                meeple_list.remove(meeple)
                                deleted_meeple = True # Set the flag to indicate a meeple was deleted
                        if deleted_meeple:
                            break   # Break out of the loop after deleting one meeple

    

        #Draw meeples here
        for meeple in meeple_list:
            meeple.process(screen, event_list, meeple_list)

        #Update the display
        pygame.display.flip()

        # Check if we are dragging an existing meeple and update its position
        if dragging_meeple is not None:
            if pygame.mouse.get_pressed()[0]:  # Left mouse button is still pressed
                mouse_x, mouse_y = pygame.mouse.get_pos()
                dragging_meeple.rect.topleft = (mouse_x, mouse_y)
            else:
                dragging_meeple = None  # Stop dragging when left mouse button is released



        
if __name__ == "__main__":
    main()
