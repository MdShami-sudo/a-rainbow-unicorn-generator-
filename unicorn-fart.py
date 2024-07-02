import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
RAINBOW_COLORS = [(255, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (143, 0, 255)]

unicorn_image = pygame.image.load('unicorn.png')  
unicorn_image = pygame.transform.scale(unicorn_image, (200, 200))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rainbow Unicorn Generator")

class GlitterParticle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = random.choice(RAINBOW_COLORS)
        self.size = random.randint(5, 10)
        self.speed_y = random.uniform(1, 3)
        self.lifetime = random.randint(30, 50)
    
    def update(self):
        self.y += self.speed_y
        self.lifetime -= 1
    
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)

def main():
    clock = pygame.time.Clock()
    particles = []
    unicorn_x, unicorn_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
    
    running = True
    while running:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        for _ in range(5):
            particles.append(GlitterParticle(unicorn_x + 100, unicorn_y + 100))
        
        particles = [p for p in particles if p.lifetime > 0]
        for particle in particles:
            particle.update()
            particle.draw(screen)
        
        screen.blit(unicorn_image, (unicorn_x, unicorn_y))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()
