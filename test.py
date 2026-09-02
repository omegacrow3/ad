import pygame

pygame.init()

screen = pygame.display.set_mode((512, 512))
pygame.display.set_caption("Collision Text")

clock = pygame.time.Clock()

# Font
font = pygame.font.Font(None, 30)

# Player
player = pygame.Rect(100, 250, 50, 50)

# Object
object_rect = pygame.Rect(300, 250, 50, 50)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    # Draw background
    screen.fill((30, 30, 30))

    # Draw player and object
    pygame.draw.rect(screen, (0, 150, 255), player)
    pygame.draw.rect(screen, (255, 100, 0), object_rect)

    # Collision check
    if player.colliderect(object_rect):
        text = font.render('''You collided with the object!
        you are the goat''', True, (255, 255, 255))
        screen.blit(text, (100, 100))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
