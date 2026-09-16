import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player = pygame.image.load("player.png").convert_alpha()
player = pygame.transform.scale(player, (50, 50))

# Movement & Physics Variables
player_x = 50
player_y = 300
player_dy = 0

player_dy = 0
gravity = 0.5
jump_speed = -10
on_ground = True


running = True
while running:
    clock.tick(144)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))

    screen.blit(player, (player_x, player_y))
    
    pygame.display.flip()

    keys = pygame.key.get_pressed()
    
    #Horizontal Movement
    if keys[pygame.K_LEFT]:
        player_x -= 5

    if keys[pygame.K_RIGHT]:
        player_x += 5

    #Vertical Movement
    if keys[pygame.K_UP] and on_ground:
        player_dy = jump_speed
        on_ground = False


    if not on_ground:
        player_dy += gravity
    
    # Apply vertical velocity to position
    player_y += player_dy

    #Ground Check
    if player_y >= 300:
        player_y = 300
        player_dy = 0
        on_ground = True


pygame.quit()