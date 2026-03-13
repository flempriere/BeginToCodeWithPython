"""
Exercise 16.2b Sprite

Provides a basic sprite implementation for a rectangular brick and a circular
ball
"""

import abc
import random

import pygame


class Sprite(abc.ABC):
    """
    Abstract representation of a sprite

    Provides a common interface for simple shape-based sprites

    Subclasses are expected to override the draw method to draw the sprite

    Attributes
    ----------
    image : Surface
        The surface the sprite is drawn on
    position : list[int, int]
        The position of the sprite's top left corner
    game : BrickBreaker
        The instance of Brick Breaker
    """

    def __init__(self, size, game):
        """
        Create a new `Sprite`

        Parameters
        ----------
        size : tuple[int, int]
            size of the sprite in pixels, (width, height)
        game : BrickBreak
            the game instance
        """
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.position = [0, 0]
        self.game = game

        self.reset()

    @property
    def top_edge(self):
        """
        top_edge : int | float
            y coordinate of the line defining the sprites top edge
        """
        return self.position[1]

    @property
    def bottom_edge(self):
        """
        bottom_edge : int | float
            y coordinate of the line defining the sprites bottom edge
        """
        return self.position[1] + self.image.get_height()

    @property
    def left_edge(self):
        """
        left_edge : int | float
            x coordinate of the line defining the sprites left edge
        """
        return self.position[0]

    @property
    def right_edge(self):
        """
        right_edge : int | float
            x coordinate of the line defining the sprites top edge
        """
        return self.position[0] + self.image.get_width()

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

    @abc.abstractmethod
    def draw(self):
        """
        Draw the sprite on the screen

        The sprite is drawn at it's current position

        Returns
        -------
        None
        """
        pass

    def reset(self):
        """
        Reset the sprite

        Called at the start of the game and on Sprite creation

        Returns
        -------
        None
        """
        pass

    def intersects_with(self, target):
        """
        Check if this sprite intersects the target sprite

        Uses a rectangular bounding box to compare for intersection.
        This is a simpler calculation but can overestimate intersection
        for non-rectangular sprites

        Parameters
        ----------
        target : Sprite
            sprite to compare for intersection

        Returns
        -------
        bool
            `True` if the sprites intersect, else `False`

        """

        if self.right_edge < target.left_edge:  # To the left of the target sprite
            return False
        if self.bottom_edge < target.top_edge:  # Below the target sprite
            return False
        if self.left_edge > target.right_edge:  # To the right of the target sprite
            return False
        if self.top_edge > target.bottom_edge:  # Above the target sprite
            return False
        # Passes all the exclusion principles, so must intersect
        return True


class RectangularSprite(Sprite):
    """
    Generic Sprite for a Sprite that displays a filled rectangle
    """

    def __init__(self, size, colour, game):
        """
        Create a new `RectangularSprite`

        The entire dimension of the sprite is coloured by the
        provided colour parameter

        Parameters
        ----------
        size : tuple[int, int]
            size of the sprite in pixels, (width, height)
        colour : tuple[int, int, int]
            colour of the sprite as an RBG tuple
        game : BrickBreak
            the game instance
        """
        super().__init__(size, game)
        self.image.fill(colour)

    def draw(self):
        """
        Draws the Sprite as rectangle

        The sprite position is taken as the upper left corner

        Returns
        -------
        None
        """
        self.game.surface.blit(self.image, self.position)


class Brick(RectangularSprite):
    """
    Represents a static brick the player will try to break

    Attributes
    ----------
    is_alive : bool
        Indicates if the brick has been broken or not
    """

    def __init__(self, size, position, colour, game):
        super().__init__(size, colour, game)
        self.position = position

    def update(self):
        pass

    def draw(self):
        """
        Draw's the brick on the screen

        Only runs if the brick is alive

        Returns
        -------
        None
        """
        if not self.is_alive:
            return
        super().draw()
        # add border effect
        border_width = 5
        pygame.draw.rect(
            self.game.surface,
            (0, 0, 0),
            (
                self.position[0],
                self.position[1],
                self.image.get_width(),
                self.image.get_height(),
            ),
            border_width,
        )

    def reset(self):
        """
        Resets the brick

        The brick is marked as alive if it had previously
        been destroyed

        Returns
        -------
        None
        """
        self.is_alive = True


class Player(RectangularSprite):
    """
    Represents the player paddle that can move side to side

    Attributes
    ----------
    moving_left : bool
        Indicates the player is moving left
    moving_right : bool
        Indicates the player is moving right
    speed : int
        Magnitude of the velocity the player can move at
    """

    def reset(self):
        """
        Resets the player

        The player is placed stationary in the middle of the
        bottom eighth of the screen

        Returns
        -------
        None
        """
        self.moving_left = False
        self.moving_right = False

        self.position = [
            (self.game.width - self.image.get_width()) / 2,
            (self.game.height - self.image.get_height()) * (7.0 / 8.0),
        ]

        self.speed = 10  # pixels per frame

    def update(self):
        """
        Update the player position if they are moving

        Returns
        -------
        None
        """
        if self.moving_left:
            self.position[0] -= self.speed
        if self.moving_right:
            self.position[0] += self.speed

        # bound movement to the game space

        if self.left_edge < 0:
            self.position[0] = 0
        if self.right_edge > self.game.width:
            self.position[0] = self.game.width - self.image.get_width()

    def start_moving_left(self):
        """
        Make the player start moving left

        Returns
        -------
        None
        """
        self.moving_left = True

    def stop_moving_left(self):
        """
        Make the player stop moving left

        Returns
        -------
        None
        """
        self.moving_left = False

    def start_moving_right(self):
        """
        Make the player start moving right

        Returns
        -------
        None
        """
        self.moving_right = True

    def stop_moving_right(self):
        """
        Make the player stop moving right

        Returns
        -------
        None
        """
        self.moving_right = False


class Ball(Sprite):
    """
    Sprite representing a ball the player must bounce

    Attributes
    ----------
    entry_delay : int
        Number of frames before the sprite should become active
    elasticity : float
        magnitude of velocity that is lost on a collision
    gravity : float
        acceleration per frame due to gravity
    speed : tuple[float, float]
        velocity of the ball
    """

    def __init__(self, radius, colour, game, entry_delay):
        """
        Create a new `Ball` instance

        Parameters
        ----------
        radius : int
            radius of the ball
        colour : tuple[int, int, int]
            RGB tuple describing the colour of the ball
        game : BrickBreaker
            the game
        entry_delay : int
            number of frames from the start of the game until the
            ball should become active
        """
        size = (2 * radius, 2 * radius)
        super().__init__(size, game)
        pygame.draw.circle(self.image, colour, (radius, radius), radius)
        self.entry_delay = entry_delay

    def reset(self):
        """
        Reset the ball.

        The ball is placed randomly close to the
        centre of the screen using a gaussian distribution
        with an initial velocity towards the player

        Also sets the other kinematic properties

        Returns
        -------
        None
        """
        self.entry_count = 0
        self.elasticity = 0.9
        self.gravity = 0.1
        self.position = [
            random.gauss(self.game.width / 2, (self.game.width / 10)),
            self.game.height / 2,
        ]
        self.speed = [(self.game.player_sprite.position[0] - self.position[0]) / 50, 0]

    def update(self):
        """
        Update the ball's position and velocity

        Checks if the ball has collided with any of the bricks
        or the player. Bricks are then destroyed. The ball
        reflects off any surfaces it contacts
        """
        self.entry_count += 1
        if not self.is_active():
            return

        self.speed[1] += self.gravity
        self.position[0] += self.speed[0]

        # check for x-axis collisions
        if self.intersects_with(self.game.player_sprite):
            self.horizontal_bounce(self.game.player_sprite, 1.2)

        # check for collisions with the boxes
        for brick in self.game.bricks:
            if brick.is_alive and self.intersects_with(brick):
                self.horizontal_bounce(brick, 1.0)
                brick.is_alive = False
                self.game.score += 100

        self.position[1] += self.speed[1]

        # check for y-axis collisions
        if self.intersects_with(self.game.player_sprite):
            self.vertical_bounce(self.game.player_sprite, 1.2)

        # check for collisions with the boxes
        for brick in self.game.bricks:
            if brick.is_alive and self.intersects_with(brick):
                self.vertical_bounce(brick, 1.0)
                brick.is_alive = False

        # bounce off the side walls and roof
        if self.left_edge < 0:
            self.position[0] = 0
            self.reflect(axis=0)

        if self.right_edge > self.game.width:
            self.position[0] = self.game.width - self.image.get_width()
            self.reflect(axis=0)

        if self.top_edge < 0:
            self.position[1] = 0
            self.reflect()

        # if falls below bottom we lose
        if self.top_edge > self.game.width:
            self.game.end_game()

    def draw(self):
        if not self.is_active():
            return
        self.game.surface.blit(self.image, self.position)

    def is_active(self):
        """
        Indicates the the ball is active

        Returns
        -------
        bool
            `True` if the ball is actively moving, else `False`
        """
        return self.entry_count >= self.entry_delay

    def reflect(self, boost_factor=1.0, axis=1):
        """
        Reflect the ball off a given axis

        The velocity of the component is
        negated and the elasticity factor is applied

        Parameters
        ----------
        boost_factor : float
            multiplicative boost to apply to speed after a bounce
        axis : int
            axis to reflect off, 0 for horizontal, 1 for vertical (default = 1)

        Returns
        -------
        None
        """
        self.speed[axis] *= -self.elasticity * boost_factor

    def horizontal_bounce(self, target, boost_factor):
        """
        Bounce the ball horizontally off a target sprite

        Performs a reflection and ensures that the ball's
        updated position is valid

        Parameters
        ----------
        target : Sprite
            sprite to bounce the ball off
        boost_factor : float
            multiplicative speed boost from the bounce
        """
        if self.speed[0] < 0:
            self.position[0] = target.right_edge
        else:  # hit the left edge
            self.position[0] = target.left_edge - self.image.get_width()

        self.reflect(boost_factor, axis=0)

    def vertical_bounce(self, target, boost_factor):
        """
        Bounce the ball vertically off a target sprite

        Performs a reflection and ensures that the ball's
        updated position is valid

        Parameters
        ----------
        target : Sprite
            sprite to bounce the ball off
        boost_factor : float
            multiplicative speed boost from the bounce
        """
        if self.speed[1] < 0:
            self.position[1] = target.bottom_edge
        else:
            self.position[1] = target.top_edge - self.image.get_height()
        self.reflect(boost_factor, axis=1)
