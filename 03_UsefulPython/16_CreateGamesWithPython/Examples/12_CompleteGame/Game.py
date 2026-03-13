"""
Example 16.12a Game

Implements the construct of a complete game including a start menu and scoring
"""

import sys

import pygame
import Sprite


class CrackerChase:
    """
    CrackerChase game

    Runs Cracker Chase. A simple game in which the player must navigate their
    cheese around a picnic rug, capturing crackers while avoiding killer tomatoes

    This class handles the main game loop. It run's as a two-state system
    alternating between a start screen and the gameplay loop.

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
    font : pygame.font.Font
        The game font for text rendering
    start_background_sprite : Sprite
        Sprite representing the background of the game during the
        start screen
    background_sprite : Sprite
        Sprite representing the background of the game
    player_sprite : Sprite
        Sprite representing the cheese controlled by the player
    sprites : list[Sprite]
        collection containing all the game sprites
    score : int
        current game score
    top_score : int
        The highest achieved score this session
    game_running : bool
        Indicates if the game is in the menu, or the main gameplay loop
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
        Load and populate the game sprites and font

        Loads the font, player sprite, background sprites and enemy sprites
        and stores the in the sprites list

        Returns
        -------
        None
        """
        self.font = pygame.font.Font(None, 60)

        self.background_sprite = Sprite.Sprite(
            pygame.image.load("Images/background.png"), self
        )

        self.start_background_sprite = Sprite.Sprite(
            pygame.image.load("Images/start_background.png"), self
        )

        cracker_image = pygame.image.load("Images/cracker.png")
        cracker_captured_sound = pygame.mixer.Sound("Sounds/burp.wav")

        self.sprites = [self.background_sprite]
        for i in range(20):
            cracker_sprite = Sprite.Cracker(
                image=cracker_image, game=self, captured_sound=cracker_captured_sound
            )
            self.sprites.append(cracker_sprite)

        tomato_image = pygame.image.load("Images/Tomato.png")
        tomato_entry_times = (300, 3000, 300)  # start, stop, step

        for entry_delay in range(*tomato_entry_times):
            tomato_sprite = Sprite.Tomato(
                image=tomato_image, game=self, entry_delay=entry_delay
            )
            self.sprites.append(tomato_sprite)

        self.player_sprite = Sprite.Cheese(pygame.image.load("Images/cheese.png"), self)
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
        End the game and return the menu

        Returns
        -------
        None
        """
        self.game_running = False
        if self.score > self.top_score:
            self.top_score = self.score

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
                    init_result[1]
                )
            )

        self.width = 800
        self.height = 600
        self.size = (self.width, self.height)

        self.surface = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Cracker Chase")

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
        Update the game state in response to the player's input

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
                elif e.key == pygame.K_UP:
                    self.player_sprite.startMovingUp()
                elif e.key == pygame.K_DOWN:
                    self.player_sprite.startMovingDown()
                elif e.key == pygame.K_LEFT:
                    self.player_sprite.startMovingLeft()
                elif e.key == pygame.K_RIGHT:
                    self.player_sprite.startMovingRight()
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_UP:
                    self.player_sprite.stopMovingUp()
                elif e.key == pygame.K_DOWN:
                    self.player_sprite.stopMovingDown()
                elif e.key == pygame.K_LEFT:
                    self.player_sprite.stopMovingLeft()
                elif e.key == pygame.K_RIGHT:
                    self.player_sprite.stopMovingRight()

        for sprite in self.sprites:
            sprite.update()

    def draw_game(self):
        """
        Draw the current game state

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
        self.start_background_sprite.draw()
        self.display_message(message="Top Score: {0}".format(self.top_score), y_pos=0)
        self.display_message(message="Welcome to Cracker Chase", y_pos=150)
        self.display_message(message="Steer the cheese to", y_pos=250)
        self.display_message(message="capture the crackers", y_pos=300)
        self.display_message(message="BEWARE THE KILLER TOMATOES", y_pos=350)
        self.display_message(message="Arrow keys to move", y_pos=450)
        self.display_message(message="Press G to play", y_pos=500)
        self.display_message(message="Press Escape to exit", y_pos=550)


if __name__ == "__main__":
    game = CrackerChase()
    game.play_game()
