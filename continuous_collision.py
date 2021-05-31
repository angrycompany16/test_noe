import pygame
import time

from pygame import draw
from pygame import surface
import Vectors

# initialize and draw window
pygame.init()
width, height = 800, 500
display = pygame.display.set_mode((width, height))

# drawing a circle
Green = (0, 255, 0)
Red = (255, 0, 0)
Blue = (0, 0, 255)
radius = 20
pygame.draw.circle(display, Green, (width / 2, height / 2), radius)

# movement
acceleration = Vectors.Vector2D(0, -9.81 * 50)
velocity = Vectors.Vector2D(100, 0)
position = Vectors.Vector2D(width / 2, height / 2)

# making an edge to collide with
point1 = (300, 450)
point2 = (700, 400)

# timedelta
prevTime = time.time()


def update() -> None:
    global prevTime
    global velocity
    global position
    now = time.time()
    dt = (now - prevTime)
    prevTime = now

    velocity += acceleration * dt
    position += velocity * dt    
    pygame.draw.circle(display, Green, (position.x, height - position.y),
                       radius)
    pygame.draw.line(display, Red, point1, point2, 5)


running = True

while running:
    display.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update()
    pygame.display.update()

