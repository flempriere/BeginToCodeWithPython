"""
Example 16.1 Simple Drawing Demonstration

Demonstrates the use of drawing commands in pygame
"""

import time

import pygame

pygame.init()

size = (800, 600)
surface = pygame.display.set_mode(size)
pygame.display.set_caption("An awesome game")

red = (255, 0, 0)
start = (0, 0)
end = (255, 0)

pygame.draw.line(surface, red, start, end)
pygame.display.flip()

time.sleep(5)

white = (255, 255, 255)
surface.fill(white)
pygame.display.flip()

time.sleep(5)
