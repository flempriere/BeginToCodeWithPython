"""
Exercise 12.2 a Game

Implements the game wrapper for Brick Break
"""

import sys

import pygame
import Sprite


class BrickBreak:
    """
    BrickBreak game

    Runs a basic version of the ATARI breakout arcade game.
    In this version the player must contest with an increasing
    number of balls over time. Watch out these ball's don't have
    a fixed speed but are instead guided by gravity

    Attributes
    ----------
    width : int
        width of the game window in pixels
    height : int
        height of the game window in pixels
    size : tuple[int, int]
        The size of the game screen in pixels
    surface : pygame.Surface
        The game window
    background_sprite : RectangularSprite
        The background
    sprites : list[Sprite]
        All the game sprites
    bricks : list[Brick]
        The brick sprites
    player_sprite : Player
        The player sprite
    score : int
        The current score
    top_score : int
        The highest score reached
    font : Font
        The game font
    """

    def display_message(self, message, y_pos):
        """
        Display a message on the screen

        The message is drawn centred on the screen with a black shadow

        Parameters
        ----------
        message : str
            string containing the text to render
        y_pos : int
            vertical position of the text in pixels

        Returns
        -------
        None
        """
        shadow = self.font.render(message, True, (0, 0, 0))
        text = self.font.render(message, True, (0, 0, 255))
        text_position = [self.width / 2 - text.get_width() / 2, y_pos]

        # draw the text twice with a slight offset to create a shadow effect
        self.surface.blit(shadow, text_position)
        text_position[0] += 2
        text_position[1] += 2
        self.surface.blit(text, text_position)

    def initialise_game_assets(self):
        """
        Initialise the game sprites

        Returns
        -------
        None
        """
        self.font = pygame.font.Font(None, 60)

        background_colour = (220, 220, 220)  # grey background
        self.background_sprite = Sprite.RectangularSprite(
            self.size, background_colour, self
        )

        self.sprites: list[Sprite.Sprite] = [self.background_sprite]

        self.bricks = []
        # create the bricks
        brick_size = (100, 30)  # bricks are 20 x 100

        # place the bricks
        brick_start_height = 60
        n_rows = 8

        colours = ((255, 0, 0), (0, 255, 0), (0, 0, 255))  # red, green, blue
        for row, row_pos in enumerate(
            range(
                brick_start_height,
                brick_start_height + brick_size[1] * n_rows,
                brick_size[1],
            )
        ):
            for col_pos in range(0, self.width, brick_size[0]):
                self.sprites.append(
                    Sprite.Brick(
                        size=brick_size,
                        position=[col_pos, row_pos],
                        colour=colours[row % 3],
                        game=self,
                    )
                )
                self.bricks.append(self.sprites[-1])

        self.player_sprite = Sprite.Player(brick_size, (150, 150, 150), self)

        ball_start_time = 0
        max_balls = 5
        ball_entry_delay_in_seconds = 30
        ball_entry_delay_in_frames = ball_entry_delay_in_seconds * 60

        ball_entry_times = (
            ball_start_time,
            ball_start_time + max_balls * ball_entry_delay_in_frames,
            ball_entry_delay_in_frames,
        )

        for entry_time in range(*ball_entry_times):
            self.sprites.append(Sprite.Ball(10, (200, 200, 0), self, entry_time))

        self.sprites.append(self.player_sprite)

    def start_game(self):
        """
        Start running the game

        Returns
        -------
        None
        """
        for sprite in self.sprites:
            sprite.reset()
        self.score = 0
        self.game_running = True

    def end_game(self):
        """
        End the game and return to the menu

        Returns
        -------
        None
        """
        self.game_running = False
        if self.score > self.top_score:
            self.top_score = self.score

    def play_game(self):
        """
        Start the game

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

        self.width = 800
        self.height = 600
        self.size = (self.width, self.height)

        self.surface = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Brick Break")

        self.initialise_game_assets()

        self.score = 0
        self.top_score = 0
        self.end_game()
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            if self.game_running:
                self.update_game()
                self.draw_game()
            else:
                self.update_start()
                self.draw_start()

            pygame.display.flip()

    def update_game(self):
        """
        Update the game

        Runs once per frame

        Returns
        -------
        None
        """
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    return
                elif e.key == pygame.K_LEFT:
                    self.player_sprite.start_moving_left()
                elif e.key == pygame.K_RIGHT:
                    self.player_sprite.start_moving_right()
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_LEFT:
                    self.player_sprite.stop_moving_left()
                elif e.key == pygame.K_RIGHT:
                    self.player_sprite.stop_moving_right()

        for sprite in self.sprites:
            sprite.update()
        # check if we broke all the bricks
        if not (any(map(lambda x: x.is_alive, self.bricks))):
            self.score += 1000  # bonus for fully clearing the game
            self.end_game()

    def draw_game(self):
        """
        Draw the game sprites

        Returns
        -------
        None
        """
        for sprite in self.sprites:
            sprite.draw()
        status = "Score: {0}".format(self.score)
        self.display_message(status, 0)

    def update_start(self):
        """
        Update the start menu

        Polls events to see if the player wants to start the game or quit

        Returns
        -------
        None
        """
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif e.key == pygame.K_g:
                    self.start_game()

    def draw_start(self):
        """
        Draw the start menu

        Returns
        -------
        None
        """
        self.background_sprite.draw()
        self.display_message(message="Top Score: {0}".format(self.top_score), y_pos=0)
        self.display_message(message="Welcome to Brick Breaker", y_pos=150)
        self.display_message(message="Steer the paddle to", y_pos=250)
        self.display_message(message="bounce the ball. Don't drop it!", y_pos=300)
        self.display_message(message="Break all the bricks!", y_pos=350)
        self.display_message(message="Left and Right Arrow keys to move", y_pos=450)
        self.display_message(message="Press G to play", y_pos=500)
        self.display_message(message="Press Escape to exit", y_pos=550)


if __name__ == "__main__":
    game = BrickBreak()
    game.play_game()
