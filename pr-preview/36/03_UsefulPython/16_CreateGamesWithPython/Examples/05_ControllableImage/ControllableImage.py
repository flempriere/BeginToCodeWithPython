"""
Example 16.5 Controllable Image

Demonstrates responding to pygame events to steer the image of cheese around
a screen
"""

import pygame


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
    init_result = pygame.init()
    if init_result[1] != 0:
        print(
            "Failed to initialise {0} elements, verify pygame installation".format(
                init_result[1]
            )
        )

    width = 800
    height = 600
    size = (width, height)
    surface = pygame.display.set_mode(size)
    pygame.display.set_caption(caption)

    return surface


def show_moving_image():
    """
    Demonstrate a moving image in pygame

    Returns
    -------
    None
    """
    surface = setup_pygame_window("Controllable Image")
    image = pygame.image.load("cheese.png")

    cheeseX = 40
    cheeseY = 60
    cheeseSpeed = 2
    cheeseMovingUp = False
    cheeseMovingDown = False

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                if e.key == pygame.K_UP:
                    cheeseMovingUp = True
                elif e.key == pygame.K_DOWN:
                    cheeseMovingDown = True
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_UP:
                    cheeseMovingUp = False
                elif e.key == pygame.K_DOWN:
                    cheeseMovingDown = False
        if cheeseMovingDown:
            cheeseY = cheeseY + cheeseSpeed
        if cheeseMovingUp:
            cheeseY = cheeseY - cheeseSpeed

        cheesePos = (cheeseX, cheeseY)
        surface.fill((255, 255, 255))
        surface.blit(image, cheesePos)
        pygame.display.flip()


if __name__ == "__main__":
    show_moving_image()
