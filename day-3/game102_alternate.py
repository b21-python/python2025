import pygame
import random

pygame.init() # initialize pygame

# Create a game window that is 640 by 480 pixels
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
running = True

def cropAlpha(surface):
    final_size = surface.get_bounding_rect()
    cropped = pygame.Surface((final_size.width, final_size.height), pygame.SRCALPHA, 32)
    cropped.blit(surface, (0,0), final_size)
    cropped = cropped.convert_alpha()
    return cropped

# Load Player
player = cropAlpha(pygame.transform.scale(pygame.image.load('sprites/taxi.png'), [100,100]))

# Traffic
traffic = [
    pygame.transform.rotate(pygame.transform.scale(pygame.image.load('sprites/Ambulance.png'), [100, 100]), 180),
    pygame.transform.rotate(pygame.transform.scale(pygame.image.load('sprites/Audi.png'), [100, 100]), 180),
    pygame.transform.rotate(pygame.transform.scale(pygame.image.load('sprites/Black_viper.png'), [100, 100]), 180),
    pygame.transform.rotate(pygame.transform.scale(pygame.image.load('sprites/Car.png'), [100, 100]), 180),
    pygame.transform.rotate(pygame.transform.scale(pygame.image.load('sprites/Mini_truck.png'), [100, 100]), 180),
    pygame.transform.rotate(pygame.transform.scale(pygame.image.load('sprites/Mini_van.png'), [100, 100]), 180),
    pygame.transform.rotate(pygame.transform.scale(pygame.image.load('sprites/Police.png'), [100, 100]), 180),
    pygame.transform.rotate(pygame.transform.scale(pygame.image.load('sprites/truck.png'), [100, 100]), 180)
]


traffic = list(map(cropAlpha, traffic))

line_speed = 5
traffic_speed = 2 * line_speed
spawn_rate = 1000 #ms
spawn_timer = spawn_rate
lanes = [
    {'pos': 165, 'vehicles':[] },
    {'pos': 255, 'vehicles':[] },
    {'pos': 345, 'vehicles':[] },
    {'pos': 435, 'vehicles':[] },
]


#lines
line_length = 20
line_width = 5
line_space = 60
lines = []
for i in range(0, screen.get_height() + 1, 80):
    lines.append(i)
    

h_center = screen.get_width()/2

# create a variable to store player position so we can modify it based on keyboard input
player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

while running:
    # poll for events and react to user closing the window to end the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Set screen color
    screen.fill("green")
    
    pygame.draw.rect(screen, "grey", (140, 0, 360, 480))
    
    for i in range(len(lines)):
        pygame.draw.line(screen, "white", [h_center, lines[i]], [h_center, lines[i] + line_length], line_width)
        lines[i] += line_speed
        if lines[i] >= screen.get_height():
            lines[i] = -(line_space)
            

    # Draw player
    player_box = screen.blit(player, player_pos)
    
    # Draw traffic
    if spawn_timer <= 0:
        spawn_timer = spawn_rate
        spawn = random.randrange(0, 100)
        lane = spawn % 4
        car = spawn % len(traffic)
        lanes[lane]['vehicles'].append({'v_pos':-100, 'car_id':car})

        
    for lane in lanes:
        for vehicle in lane['vehicles']:
            vehicle_box = screen.blit(traffic[vehicle['car_id']], [lane['pos'], vehicle['v_pos']])
            if player_box.colliderect(vehicle_box):
                running = False
            vehicle['v_pos'] += traffic_speed
        lane['vehicles'] = [vehicle for vehicle in lane['vehicles'] if vehicle['v_pos'] < screen.get_height()]
    

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

running = True
while running:
    # poll for events and react to user closing the window to end the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Exit game when we leave the game loop
pygame.quit()