import pygame
import sys
import random
import asyncio

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

async def main():
    BLUE = (0, 122, 255)
    YELLOW = (255, 223, 0)  

    player_img = pygame.image.load("player.png").convert_alpha()
    player_img = pygame.transform.scale(player_img, (50, 50))

    player_x = 30.0
    player_y = 500.0
    player_dx = 0.0
    player_dy = 0.0

    gravity = 0.25
    jump_speed = -10.0
    on_ground = False

    platforms = [
        pygame.Rect(50, 450, 200, 20),
        pygame.Rect(300, 350, 200, 20),
        pygame.Rect(550, 250, 200, 20),
    ]

    cupcakes = []
    while len(cupcakes) < 10:
        cx = random.randint(50, 750)
        cy = random.randint(50, 500)
        new_cupcake = pygame.Rect(cx, cy, 16, 16)

        overlaps = False
        for platform in platforms:
            if new_cupcake.colliderect(platform):
                overlaps = True
                break
                
        if not overlaps:
            cupcakes.append(new_cupcake)

    running = True
    while running:
        clock.tick(144)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        
        player_dx = 0
        if keys[pygame.K_LEFT]:
            player_dx = -5
        if keys[pygame.K_RIGHT]:
            player_dx = 5

        player_x += player_dx
        player_rect = pygame.Rect(player_x, player_y, 50, 50)

        for platform in platforms:
            if player_rect.colliderect(platform):
                if player_dx > 0:
                    player_rect.right = platform.left
                elif player_dx < 0:
                    player_rect.left = platform.right
                player_x = player_rect.x 

        if player_x < 0:
            player_x = 0
        elif player_x > 750:
            player_x = 750

        if keys[pygame.K_UP] and on_ground:
            player_dy = jump_speed
            on_ground = False

        player_dy += gravity
        player_y += player_dy
        
        player_rect = pygame.Rect(player_x, player_y, 50, 50)
        on_ground = False 

        # Vertical platform collision 
        for platform in platforms:
            if player_rect.colliderect(platform):
                if player_dy > 0:
                    player_rect.bottom = platform.top
                    player_dy = 0
                    on_ground = True
                elif player_dy < 0:
                    player_rect.top = platform.bottom
                    player_dy = 0
                player_y = player_rect.y

        if player_y >= 550:
            player_y = 550
            player_dy = 0
            on_ground = True
        elif player_y < 0:
            player_y = 0
            player_dy = 0

        for cupcake in cupcakes[:]:
            if player_rect.colliderect(cupcake):
                cupcakes.remove(cupcake)

        screen.fill((30, 30, 30))
        
        for platform in platforms:
            pygame.draw.rect(screen, BLUE, platform)

        for cupcake in cupcakes:
            pygame.draw.circle(screen, YELLOW, cupcake.center, 8)

        screen.blit(player_img, (int(player_x), int(player_y)))

        pygame.display.flip()

        await asyncio.sleep(0)

    pygame.quit()

asyncio.run(main())