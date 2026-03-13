"""
Example 16.3 Draw Image

Demonstrates drawing an image with pygame
"""

import time

import pygame


def do_image_demo():
    """
    Demonstrate loading and drawing an image using pygame

    Returns
    -------
    None
    """
    init_result = pygame.init()
    if init_result[1] != 0:
        print(
            "pygame failed to load {0} elements. Please verify installation".format(
                init_result[1]
            )
        )

    width = 800
    height = 600
    size = (width, height)

    surface = pygame.display.set_mode(size)
    pygame.display.set_caption("Image Example")

    white = (255, 255, 255)
    surface.fill(white)

    cheeseImage = pygame.image.load("cheese.png")
    cheesePos = (0, 0)
    surface.blit(cheeseImage, cheesePos)
    pygame.display.flip()


if __name__ == "__main__":
    do_image_demo()
    time.sleep(10)
