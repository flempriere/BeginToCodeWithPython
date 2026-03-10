"""
Example 16.8b Sprite

Extends the sprite collection with a target cracker sprite
"""

import random


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


class Cheese(Sprite):
    """
    Player controlled cheese sprite

    Steerable cheese sprite controllable by the player
    """

    def reset(self):
        """
        Reset the player sprite

        Stops the sprite moving and returns it to it's starting position

        Returns
        -------
        None
        """
        self.movingUp = False
        self.movingDown = False
        self.movingLeft = False
        self.movingRight = False

        self.position = [
            (self.game.width - self.image.get_width()) / 2,
            (self.game.height - self.image.get_height()) / 2,
        ]
        self.speed = [5, 5]

    def update(self):
        """
        Update the cheese position

        Notes
        -----
        Ensures the player is restricted to the play screen

        Returns
        -------
        None
        """
        if self.movingUp:
            self.position[1] = self.position[1] - self.speed[1]
        if self.movingDown:
            self.position[1] = self.position[1] + self.speed[1]
        if self.movingLeft:
            self.position[0] = self.position[0] - self.speed[0]
        if self.movingRight:
            self.position[0] = self.position[0] + self.speed[0]

        # bound movement to the game space
        if self.position[0] < 0:
            self.position[0] = 0
        if self.position[1] < 0:
            self.position[1] = 0
        if self.position[0] + self.image.get_width() > self.game.width:
            self.position[0] = self.game.width - self.image.get_width()
        if self.position[1] + self.image.get_height() > self.game.height:
            self.position[1] = self.game.height - self.image.get_height()

    def startMovingUp(self):
        """
        Start the cheese moving up

        Returns
        -------
        None
        """
        self.movingUp = True

    def stopMovingUp(self):
        """
        Stop the cheese moving up

        Returns
        -------
        None
        """
        self.movingUp = False

    def startMovingDown(self):
        """
        Start the cheese moving down

        Returns
        -------
        None
        """
        self.movingDown = True

    def stopMovingDown(self):
        """
        Stop the cheese moving down

        Returns
        -------
        None
        """
        self.movingDown = False

    def startMovingLeft(self):
        """
        Start the cheese moving left

        Returns
        -------
        None
        """
        self.movingLeft = True

    def stopMovingLeft(self):
        """
        Stop the cheese moving left

        Returns
        -------
        None
        """
        self.movingLeft = False

    def startMovingRight(self):
        """
        Start the cheese moving right

        Returns
        -------
        None
        """
        self.movingRight = True

    def stopMovingRight(self):
        """
        Stop the cheese moving right

        Returns
        -------
        None
        """
        self.movingRight = False


class Cracker(Sprite):
    """
    Cracker sprite representing a target for the player

    Moves to random place on the screen once captured
    """

    def reset(self):
        """
        Reset the Cracker to a new random position

        Returns
        -------
        None
        """
        self.position = [
            random.randint(0, self.game.width - self.image.get_width()),
            random.randint(0, self.game.height - self.image.get_height()),
        ]
