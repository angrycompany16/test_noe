import pygame
import time

from pygame import draw
from pygame import surface
import Vectors

# initialize and draw window
pygame.init()
width, height = 800, 500
display = pygame.display.set_mode((width, height))

# mouse
dragging = False

# drawing a circle
Green = (0, 255, 0)
Red = (255, 0, 0)
Blue = (0, 0, 255)
radius = 20
pygame.draw.circle(display, Green, (width / 2, height / 2), radius)
pygame.display.update()

# movement
acceleration = Vectors.Vector2D(0, -9.81 * 50)
velocity = Vectors.Vector2D(100, 0)
position = Vectors.Vector2D(width / 2, height / 2)

# timedelta
prevTime = time.time()

# draw a rectangle
margin_top = 20
margin_sides = 40

# box collider

rect = pygame.Rect(margin_sides, margin_top, width - (margin_sides * 2),
                   height - (margin_top * 2))
pygame.draw.rect(display, Red, rect, 1)


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

    # circle collider
    # left, right, top, bottom
    borders = (
        Vectors.Vector2D(position.x - radius, height - position.y),
        Vectors.Vector2D(position.x + radius, height - position.y),
        Vectors.Vector2D(position.x, height - position.y - radius),
        Vectors.Vector2D(position.x, height - position.y + radius)
    )


    pygame.draw.circle(display, Red, (borders[0].x, borders[0].y), 3)
    pygame.draw.circle(display, Red, (borders[1].x, borders[1].y), 3)
    pygame.draw.circle(display, Red, (borders[2].x, borders[2].y), 3)
    pygame.draw.circle(display, Red, (borders[3].x, borders[3].y), 3)

    rect = pygame.Rect(margin_sides, margin_top, width - (margin_sides * 2),
                       height - (margin_top * 2))
    pygame.draw.rect(display, Red, rect, 1)

    # box collider
    # bot-left, bot-right, top-left, top-right
    corners = (
        Vectors.Vector2D(margin_sides, height - margin_top),
        Vectors.Vector2D(width - margin_sides, height - margin_top),
        Vectors.Vector2D(margin_sides, margin_top),
        Vectors.Vector2D(width - margin_sides, margin_top)
    )

    pygame.draw.circle(display, Red, (corners[0].x, corners[0].y), 3)
    pygame.draw.circle(display, Red, (corners[1].x, corners[1].y), 3)
    pygame.draw.circle(display, Red, (corners[2].x, corners[2].y), 3)
    pygame.draw.circle(display, Red, (corners[3].x, corners[3].y), 3)

    if (borders[0].x < corners[0].x):
        position = Vectors.Vector2D(corners[0].x + radius, position.y)
        velocity.x *= -1
    elif(borders[1].x > corners[1].x):
        position = Vectors.Vector2D(corners[1].x - radius, position.y)
        velocity.x *= -1
    elif(borders[2].y < corners[2].y):
        position = Vectors.Vector2D(position.x, height - (corners[2].y +
                                    radius))
        velocity.y *= -1
    elif(borders[3].y > corners[1].y):
        position = Vectors.Vector2D(position.x, height - (corners[1].y -
                                    radius))
        velocity.y *= -1


startPos = Vectors.Vector2D(0, 0)
endPos = Vectors.Vector2D(0, 0)

manualUpdate = pygame.Surface((800, 500))

def CalculateForce(start, end, strength):
    global velocity
    directionVector = end - start
    normalizedVector = directionVector.Normalize()
    velocity = Vectors.Vector2D(normalizedVector.x, - normalizedVector.y) * strength


def OnMouseButtonDown() -> None:
    global startPos
    global dragging

    dragging = True
    startPos = Vectors.Vector2D(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])


def OnMouseButtonUp() -> None:
    global endPos
    global dragging

    dragging = False
    endPos = Vectors.Vector2D(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    CalculateForce(startPos, endPos, 500)


def WhileMouseDrag() -> None:
    pygame.draw.line(display, Red, (startPos.x, startPos.y), (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]), 10)

running = True

while running:
    display.fill((0, 0, 0))
    if(dragging):
        WhileMouseDrag()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            OnMouseButtonDown()
        elif event.type == pygame.MOUSEBUTTONUP:
            OnMouseButtonUp()

    update()
    pygame.display.update()

