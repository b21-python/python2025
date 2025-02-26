import pygame
from math import pi

pygame.init() # initialize pygame

# Create a game window that is 640 by 480 pixels
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
running = True

# create a variable to store player position so we can modify it based on keyboard input
player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

while running:
    # poll for events and react to user closing the window to end the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Set screen color
    screen.fill("orange")

    # Draw a line
    pygame.draw.line(screen, "blue", [0,0], (640,480), 6)

    # Draw a rectangle
    pygame.draw.rect(screen, "pink", (20, 40, 25,100))

    # Draw a polygon
    pygame.draw.polygon(screen, (100,120,0), [(600,400), (600, 300), (300, 350), (300, 375)])

    # Draw a circle
    pygame.draw.circle(screen, (255,0,200), (320,240), 100)

    # Draw an ellipse
    pygame.draw.ellipse(screen, (0,200,255), (0,400, 300, 80))

    # Draw arcs
    pygame.draw.arc(screen, (25,125,225), (0,0,400,100), 0, pi, 4)

    # Draw the player
    pygame.draw.circle(screen, "green", player_pos, 40)

    # update player position based on keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 10
    if keys[pygame.K_s]:
        player_pos.y += 10
    if keys[pygame.K_a]:
        player_pos.x -= 10
    if keys[pygame.K_d]:
        player_pos.x += 10

    # Render what you've drawn to the screen
    pygame.display.flip()

    clock.tick(60) # limit to 60 FPS

# Exit game when we leave the game loop
pygame.quit()