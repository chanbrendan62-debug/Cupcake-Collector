import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player_image = pygame.image.load("player.png").convert_alpha()
player_rect = player_image.get_rect(center=(400, 300))
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key states
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_rect.x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_rect.x += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_rect.y -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_rect.y += speed

    screen.fill((0, 0, 0))
    screen.blit(player_image, player_rect)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()