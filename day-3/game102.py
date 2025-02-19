import pygame
import random

pygame.init() # initialize pygame

# Create a game window that is 640 by 480 pixels
screen = pygame.display.set_mode((640,960))
h_center = screen.get_width() / 2
clock = pygame.time.Clock()
running = True

def cropAlpha(surface):
    final_size = surface.get_bounding_rect()
    cropped = pygame.Surface((final_size.width, final_size.height), pygame.SRCALPHA, 32)
    cropped.blit(surface, (0,0), final_size)
    cropped = cropped.convert_alpha()
    return cropped

def prepareTraffic(sprite):
    rotated_sprite = pygame.transform.rotate(sprite, 180)
    return cropAlpha(rotated_sprite)

# Load Player
player = cropAlpha(pygame.image.load('sprites/car.png'))

# Line parameters
line_speed = 5
line_length = 20
line_width = 5
line_space = 60

# List of line start positions
lines = []
for i in range(0, screen.get_height() + 1, 80):
    lines.append(i)


# Load Vehicles
vehicles = [
    prepareTraffic(pygame.image.load('sprites/Ambulance.png')),
    prepareTraffic(pygame.image.load('sprites/Audi.png')),
    prepareTraffic(pygame.image.load('sprites/Black_viper.png')),
    prepareTraffic(pygame.image.load('sprites/Car.png')),
    prepareTraffic(pygame.image.load('sprites/Mini_truck.png')),
    prepareTraffic(pygame.image.load('sprites/Mini_van.png')),
    prepareTraffic(pygame.image.load('sprites/Police.png')),
    prepareTraffic(pygame.image.load('sprites/truck.png'))
]

traffic_speed = 2 * line_speed
spawn_rate = 1000 #ms
spawn_timer = spawn_rate

# Create Lanes
lanes = [
    {'pos': 180, 'traffic':[{'v_pos': -100, 'car_id': 0}] },
    {'pos': 370, 'traffic':[] },
]

# create a variable to store player position so we can modify it based on keyboard input
player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

while running:
    # poll for events and react to user closing the window to end the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Set screen color
    screen.fill("green")

    # Draw Road                        X   Y  Width  Height
    pygame.draw.rect(screen, "grey", (140, 0, 360,   screen.get_height()))
    
    for i in range(len(lines)):
        pygame.draw.line(screen, "white", [h_center, lines[i]], [h_center, lines[i] + line_length], line_width)
        # Move line
        lines[i] += line_speed
        # If off bottom of screen move above top of screen
        if lines[i] >= screen.get_height():
            lines[i] = -(line_space)
 
    # Draw player
    player_box = screen.blit(player, player_pos)

 
    # Spawn Traffic
    if spawn_timer <= 0:
        spawn_timer = spawn_rate
        spawn = random.randrange(0, len(vehicles))
        lane = spawn % len(lanes)
        car = spawn % len(vehicles)
        lanes[lane]['traffic'].append({'v_pos':-(player.get_height()), 'car_id':car})

    
    # Draw Traffic
    for lane in lanes:
        for vehicle in lane['traffic']:
            vehicle_box = screen.blit(vehicles[vehicle['car_id']], [lane['pos'], vehicle['v_pos']])
            if player_box.colliderect(vehicle_box):
                print(player_box)
                print(vehicle_box)
                running = False
            vehicle['v_pos'] += traffic_speed
        lane['traffic'] = [vehicle for vehicle in lane['traffic'] if vehicle['v_pos'] < screen.get_height()]
    

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

    spawn_timer -= clock.tick(60) # limit to 60 FPS

print("you died")
running = True
while running:
    # poll for events and react to user closing the window to end the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Exit game when we leave the game loop
pygame.quit()