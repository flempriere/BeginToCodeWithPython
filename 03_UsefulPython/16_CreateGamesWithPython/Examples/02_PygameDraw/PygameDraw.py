"""
Example 16.2 Pygame Drawing Functions

Demonstrates the use of pygame's drawing functionality to create
some artwork
"""

import random

import pygame


class DrawDemo:
    """
    Draws an image of randomly coloured and positioned lines and dots
    """

    @staticmethod
    def do_draw_demo():
        """
        Create a demonstration display
        """
        init_result = pygame.init()
        if init_result[1] != 0:
            print("Failed to initialise all elements, check pygame installation")

        width = 800
        height = 600
        size = (width, height)

        def get_random_coordinates():
            """
            Generates a random (X,Y) coordinate tuple

            Returns
            -------
            tuple[int, int]
                X,Y coordinates
            """
            X = random.randint(0, width - 1)
            Y = random.randint(0, height - 1)

            return (X, Y)

        def get_random_colour():
            """
            Generate a random (R,G,B) colour tuple

            Returns
            -------
            tuple[int, int, int]
                R,G,B colour tuple
            """
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)

            return (red, green, blue)

        surface = pygame.display.set_mode(size)
        pygame.display.set_caption("Drawing Example")

        red = (255, 0, 0)  # noqa: F841
        green = (0, 255, 0)  # noqa: F841
        blue = (0, 0, 255)  # noqa: F841
        black = (0, 0, 0)  # noqa: F841
        yellow = (255, 255, 0)  # noqa: F841
        magenta = (255, 0, 255)  # noqa: F841
        cyan = (0, 255, 255)  # noqa: F841
        white = (255, 255, 255)
        gray = (128, 128, 128)  # noqa: F841

        surface.fill(white)

        for count in range(100):
            start = get_random_coordinates()
            stop = get_random_coordinates()
            colour = get_random_colour()
            pygame.draw.line(surface, colour, start, stop)

        for count in range(100):
            pos = get_random_coordinates()
            colour = get_random_colour()
            radius = random.randint(5, 50)
            pygame.draw.circle(surface, colour, pos, radius)

        pygame.display.flip()


DrawDemo.do_draw_demo()
