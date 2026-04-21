import pygame

class Ball:
    def __init__(self, width, height):
        self.radius = 20
        self.x = width // 2
        self.y = height // 2
        self.speed = 20

        self.width = width
        self.height = height

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            if self.x - self.speed - self.radius >= 0:
                self.x -= self.speed

        if keys[pygame.K_RIGHT]:
            if self.x + self.speed + self.radius <= self.width:
                self.x += self.speed

        if keys[pygame.K_UP]:
            if self.y - self.speed - self.radius >= 0:
                self.y -= self.speed

        if keys[pygame.K_DOWN]:
            if self.y + self.speed + self.radius <= self.height:
                self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 50, 50))