"""
Example 16.12b Sprite

Crackers now update the player score when caught, while tomatoes end the
game if they catch the player
"""

import random


class Sprite:
    """
    Base class for a game Sprite

    Attributes
    ----------
    image : pygame.Surface
        The sprite image
    position : list[int, int]
        The position of the sprite, in pixels, determined by the pixel
        position of the top left corner of the sprite
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
        max_x = self.position[0] + self.image.get_width()
        max_y = self.position[1] + self.image.get_height()

        target_max_x = target.position[0] + target.image.get_width()
        target_max_y = target.position[1] + target.image.get_height()

        if max_x < target.position[0]:  # To the left of the target sprite
            return False
        if max_y < target.position[1]:  # Below the target sprite
            return False
        if self.position[0] > target_max_x:  # To the right of the target sprite
            return False
        if self.position[1] > target_max_y:  # Above the target sprite
            return False
        # Passes all the exclusion principles, so must intersect
        return True


class Cheese(Sprite):
    """
    Player controlled cheese sprite

    Steerable cheese sprite controllable by the player

    Attributes
    ----------
    speed : tuple[int, int]
        The velocity of the sprite in pixels per frame
    movingUp : bool
        Indicates the sprite is moving up
    movingDown : bool
        Indicates the sprite is moving down
    movingLeft : bool
        Indicates the sprite is moving left
    movingRight : bool
        Indicates the sprite is moving right
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
            self.position[1] -= self.speed[1]
        if self.movingDown:
            self.position[1] += self.speed[1]
        if self.movingLeft:
            self.position[0] -= self.speed[0]
        if self.movingRight:
            self.position[0] += self.speed[0]

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
    and updates the player's score

    Attributes
    ----------
    captured_sound : Pygame.mixer.Sound
        Sound effect played when this sprite is captured by a player
    """

    def __init__(self, image, game, captured_sound):
        """
        Create a new `Cracker`

        Parameters
        ----------
        image : pygame.Surface
            image to draw
        game : CrackerChase
            the game instance
        captured_sound : pygame.mixer.Sound
            sound to play when captured by the player
        """
        super().__init__(image, game)
        self.captured_sound = captured_sound

    def update(self):
        """
        Checks if the Cracker intersects the player sprite

        Resets the Cracker sprite when intersected

        Returns
        -------
        None
        """
        if self.intersects_with(self.game.player_sprite):
            self.captured_sound.play()
            self.reset()
            self.game.score += 10

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


class Tomato(Sprite):
    """
    Tomato Sprite that chases down the Player

    Enters the game after an optional delay and accelerates towards the player

    Attributes
    ----------
    entry_delay : int
        number of frames before the sprite should appear in the game
    entry_count : int
        number of frames since the sprite was last reset, must exceed `entry_delay` for the sprite to start moving
    speed : list[float]
        the current speed of the sprite in pixels per frame (x,y)
    acceleration : list[float]
        the magnitude of acceleration in pixels per frame per frame (x, y)
    friction : float
        friction co-efficient, controls how much speed is reduced by each frame

    """

    def __init__(self, image, game, entry_delay):
        """
        Create a new `Tomato` sprite

        Parameters
        ----------
        image : pygame.Surface
            image to draw
        game : CrackerChase
            the game instance
        entry_delay : int
            number of frames before the sprite should appear
        """
        super().__init__(image, game)
        self.entry_delay = entry_delay

    def update(self):
        """
        Update the Tomato Sprite's velocity and position

        The sprite is only updated if the game has lasted longer than
        the sprite's entry delay

        Returns
        -------
        None
        """
        self.entry_count += 1
        if self.entry_count < self.entry_delay:
            return
        # calculate speed
        if self.game.player_sprite.position[0] > self.position[0]:
            self.speed[0] += self.acceleration[0]
        else:
            self.speed[0] -= self.acceleration[0]

        if self.game.player_sprite.position[1] > self.position[1]:
            self.speed[1] += self.acceleration[1]
        else:
            self.speed[1] -= self.acceleration[1]

        # apply friction
        self.speed[0] *= self.friction
        self.speed[1] *= self.friction

        # update the position
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]

        # check if has caught the player
        if self.intersects_with(self.game.player_sprite):
            self.game.end_game()

    def reset(self):
        """
        Reset the Tomato sprite

        The sprite's position is reset and the initial velocity is set to 0.
        Also sets the friction and acceleration values to a predefined
        internal value

        Returns
        -------
        None
        """
        self.entry_count = 0
        self.friction = 0.99
        self.acceleration = [0.2, 0.2]
        self.speed = [0.0, 0.0]
        self.position = [-100.0, -100.0]
