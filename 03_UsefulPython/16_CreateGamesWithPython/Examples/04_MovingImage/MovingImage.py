"""
Example 16.4 Moving Image

Demonstrates using `blit` to make an image move in pygame
"""

import time

import pygame


def show_moving_image():
    """
    Demonstrate a moving image in pygame

    Returns
    -------
    None
    """
    init_result = pygame.init()
    if init_result[1] != 0:
        print(
            "Failed to initialise {0} elements, verify pygame installation".format(
                init_result[1]
            )
        )

    def setup_pygame_window(caption):
        """
        Setup a pygame window with the specified caption

        Parameters
        ----------
        caption : str
            caption for the window

        Returns
        -------
        Surface
            the window
        """
        width = 800
        height = 600
        size = (width, height)
        surface = pygame.display.set_mode(size)
        pygame.display.set_caption(caption)

        return surface

    surface = setup_pygame_window("Moving Image Example")
    cheeseImage = pygame.image.load("cheese.png")

    cheeseX = 40
    cheeseY = 60

    clock = pygame.time.Clock()

    for i in range(1, 100):
        clock.tick(30)  # pause the game to 30 frames per second
        surface.fill((255, 255, 255))
        cheeseX = cheeseX + 1
        cheeseY = cheeseY + 1
        cheesePos = (cheeseX, cheeseY)
        surface.blit(cheeseImage, cheesePos)
        pygame.display.flip()


if __name__ == "__main__":
    show_moving_image()
    time.sleep(10)
