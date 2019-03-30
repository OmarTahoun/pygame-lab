import pygame as pg #import the module pygame

pg.init() #initialize the module to start working with it
window = pg.display.set_mode((800,600)) #Makinga window with the size 800 * 600
pg.display.set_caption("Move the rectangle")

width, height = pg.display.get_surface().get_size() # Storing the width and height of our screen to make sure that our player doesn't go off the screen


class player():
    """This is the player object,  it stores the attributes of our player (Width, Height, velocity)""" # It's better to go OOP with games.

    def __init__(self, x, y, height, width,velocity): #the costructor to our player object
        self.x = x  # X location
        self.y = y  # Y location
        self.w = width  # Width
        self.h = height # Height
        self.v = velocity   # Velocity to move by

    def draw(self): # The function to show or draw our player
        window.fill((0,0,0))    # clearing the screen from any previous frames
        pg.draw.rect(window, (255, 153, 0), (self.x, self.y, self.w, self.h)) # drawing our player as a rectangle
        pg.display.update() # updating the screen

    def move(self, pressed_keys):   # The function that allows the player to move around
        if pressed_keys[pg.K_LEFT] and self.x > 0:              # moving to the Left, making sure not to go off screen
            self.x -= self.v

        if pressed_keys[pg.K_RIGHT] and self.x < width-self.w:  # moving to the Right, making sure not to go off screen
            self.x += self.v

        if pressed_keys[pg.K_UP] and self.y > 0:                # moving Up, making sure not to go off screen
            self.y -= self.v

        if pressed_keys[pg.K_DOWN] and self.y < height-self.h:  # moving Down, making sure not to go off screen
            self.y += self.v


my_player = player(50, 50, 50, 50, 10)  # Creating our player object

running = True #set the running flag that will be used for the game loop

while (running):    # Our Game loop
    pg.time.delay(30) # Setting the frame rate

    for event in pg.event.get():    # checking if the user has quit the game
        if event.type == pg.QUIT:
            running = False

    pressed_keys = pg.key.get_pressed() # getting the pressed keys
    my_player.move(pressed_keys)    # updating the player location
    my_player.draw()                # Drawing the player at the new location

pg.quit()   # quitting the game
