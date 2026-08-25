import pygame

pygame.init()

screen = pygame.display.set_mode((500, 300))
clock = pygame.time.Clock()

steering_angle = 0
MAX_ANGLE = 45      # degrees
STEER_SPEED = 2     # degrees per frame
CENTER_SPEED = 1    # return-to-center speed

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        steering_angle -= STEER_SPEED
    elif keys[pygame.K_RIGHT]:
        steering_angle += STEER_SPEED
    else:
        # Auto-center
        if steering_angle > 0:
            steering_angle -= CENTER_SPEED
        elif steering_angle < 0:
            steering_angle += CENTER_SPEED

    steering_angle = max(-MAX_ANGLE, min(MAX_ANGLE, steering_angle))

    screen.fill((30, 30, 30))

    font = pygame.font.SysFont(None, 40)
    text = font.render(f"Steering: {steering_angle:.1f}°", True, (255, 255, 255))
    screen.blit(text, (50, 120))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()