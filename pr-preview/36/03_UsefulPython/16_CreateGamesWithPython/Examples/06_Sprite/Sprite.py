"""
Example 16.6 Sprite

Introduces a generic base sprite
"""

import pygame


class Sprite:
    """
    Base class for a game Sprite

    Attributes
    ----------
    image : pygame.Surface
        The sprite image
    game : CrackerChase
        The current game instance
    """

    def __init__(self, image, game):
        """
        Create a new `Sprite`

        Parameters
        ----------
        image : pygame.Surface
            image to draw
        game : CrackerChase
            the game instance
        """
        self.image = image
        self.position = [0, 0]  # list so it's mutable
        self.game = game
        self.reset()

    def update(self):
        """
        Update the sprite

        Called in the game loop to update the status of the sprite. Does
        nothing in the superclass

        Returns
        -------
        None
        """
        pass

    def draw(self):
        """
        Draw the sprite on the screen

        The sprite is drawn at it's current position

        Returns
        -------
        None
        """
        self.game.surface.blit(self.image, self.position)

    def reset(self):
        """
        Reset the sprite

        Called at the start of the game

        Returns
        -------
        None
        """
        pass


class CrackerChase:
    """
    CrackerChase game

    Runs a simple game loop to display a background sprite

    Attributes
    ----------
    size : tuple[int, int]
        The size of the game screen in pixels
    surface : pygame.Surface
        The game window
    background_sprite : Sprite
        Sprite representing the background of the game
    """

    def play_game(self):
        """
        Load the game and start the game loop

        Returns
        -------
        None
        """
        init_result = pygame.init()
        if init_result[1] != 0:
            print(
                "Failed to initialise {0} elements, verify pygame installation".format(
                    init_result
                )
            )

        width = 800
        height = 600
        self.size = (width, height)

        self.surface = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Cracker Chase")
        self.background_sprite = Sprite(pygame.image.load("background.png"), self)

        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return
            self.background_sprite.draw()
            pygame.display.flip()


if __name__ == "__main__":
    game = CrackerChase()
    game.play_game()
