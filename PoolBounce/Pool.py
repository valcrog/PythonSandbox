import pygame
import math

# Traditional pool tables have a 2:1 ratio, so we'll use that for our simulation
WIDTH = 800
HEIGHT = 400
FRICTION = 0.995  # Friction coefficient. A coefficient of 1 means no friction

class Ball:
    def __init__(self, x, y, velX, velY, radius=5, color='white'):
        self.x = x
        self.y = y
        self.velX = velX
        self.velY = velY
        self.radius = radius
        self.color = color

    def render(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.velX
        self.y += self.velY
        self.velX *= FRICTION
        self.velY *= FRICTION
        self.check_collision()

    def check_collision(self):
        if self.x + self.radius >= WIDTH or self.x - self.radius <= 0:
            self.velX = -self.velX
            self.x = WIDTH - self.radius if self.x + self.radius >= WIDTH else self.radius
        if self.y + self.radius >= HEIGHT or self.y - self.radius <= 0:
            self.velY = -self.velY
            self.y = HEIGHT - self.radius if self.y + self.radius >= HEIGHT else self.radius

    def check_ball_collision(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        distance = math.sqrt(dx**2 + dy**2)

        if distance < self.radius + other.radius:
            # Calculate the angle of collision
            angle = math.atan2(dy, dx)
            sin_angle = math.sin(angle)
            cos_angle = math.cos(angle)

            # Rotate ball velocities
            self_velX = self.velX * cos_angle + self.velY * sin_angle
            other_velX = other.velX * cos_angle + other.velY * sin_angle
            other_velY = other.velY * cos_angle - other.velX * sin_angle

            # Update velocities after collision
            self_velX, other_velX = other_velX, self_velX

            # Rotate velocities back
            self.velX = self_velX * cos_angle - self.velY * sin_angle
            self.velY = self.velY * cos_angle + self.velX * sin_angle
            other.velX = other_velX * cos_angle - other.velY * sin_angle
            other.velY = other_velY * cos_angle + other_velX * sin_angle

            # Separate the balls to avoid sticking
            overlap = 0.5 * (self.radius + other.radius - distance + 1)
            self.x += math.cos(angle) * overlap
            self.y += math.sin(angle) * overlap
            other.x -= math.cos(angle) * overlap
            other.y -= math.sin(angle) * overlap

class Pool:
    def __init__(self, balls, color):
        self.balls = balls
        self.color = color

    def render(self, screen):
        screen.fill(self.color)  # Green color for the pool table
        for ball in self.balls:
            ball.render(screen)

    def move(self):
        for i, ball in enumerate(self.balls):
            ball.move()
            for j in range(i + 1, len(self.balls)):
                ball.check_ball_collision(self.balls[j])

    def update(self, screen):
        self.move()
        self.render(screen)