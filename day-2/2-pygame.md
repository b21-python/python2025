# Getting started with pygame

We are going to start with the [quick start docs](https://www.pygame.org/docs/) found on the pygame docs front page.  


## Importing pygame and showing the screen

```python
import pygame

pygame.init() # initialize pygame

# Create a game window that is 640 by 480 pixels
screen = pygame.display.set_mode((640,480))
```

Run this code and you should see a blank screen.  You will have to click the red stop button in Thonny to exit.


## Drawing on the screen

Pygame lets you draw multiple things on the screen then once you have drawn everything you tell it to render what you've drawn to the screen.

```python
import pygame

pygame.init() # initialize pygame

# Create a game window that is 640 by 480 pixels
screen = pygame.display.set_mode((640,480))

# Set screen color
screen.fill("orange")

# Draw a circle
pygame.draw.circle(screen, "green", [200, 200], 40)

# Render what you've drawn to the screen
pygame.display.flip()
```

Try changing the color of the screen and the circle to something else.  You can try named colors or make an array of RGB values like `[100, 100, 100]` where the first number is for red, the second for green and the third for blue, the minimum value for each is 0 and the maximum is 255.


## Adding a game loop

Games have a main loop that repeats until the game ends.  This loop allows the game to respond to continue to respond to input for as long as the game is running.


```python
import pygame

pygame.init() # initialize pygame

# Create a game window that is 640 by 480 pixels
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
running = True

while running:
    # Set screen color
    screen.fill("orange")

    # Draw a circle
    pygame.draw.circle(screen, "green", [200, 200], 40)

    # Render what you've drawn to the screen
    pygame.display.flip()

    clock.tick(60) # limit to 60 FPS
```

This looks the same when we run it but it's drawing the same thing up to 60 times a second.


## Listen to events so we can exit the game normally

Pygame listens to events like key presses and the user clicking the x to close the window and saves them so we can react to them

```python
import pygame

pygame.init() # initialize pygame

# Create a game window that is 640 by 480 pixels
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events and react to user closing the window to end the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Set screen color
    screen.fill("orange")

    # Draw a circle
    pygame.draw.circle(screen, "green", [200, 200], 40)

    # Render what you've drawn to the screen
    pygame.display.flip()

    clock.tick(60) # limit to 60 FPS

# Exit game when we leave the game loop
pygame.quit()
```



## Take input to move the circle

Now that the game is listening for events we can react to the player pressing the w, a, s, d keys to move the circle.

```python
import pygame

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

    # Draw a circle
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
```

> NOTE: You can move the circle off of the screen.  How would you limit the movement so the circle cannot go off the screen?