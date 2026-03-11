"""
Example 16.9a Game

Contains the main game loop class for our cracker chasing game, adds
a collection for handling sprite updates
"""

import pygame
import Sprite


class CrackerChase:
    """
    CrackerChase game

    Runs a simple game loop to display a background sprite

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
    background_sprite : Sprite
        Sprite representing the background of the game
    player_sprite : Sprite
        Sprite representing the cheese controlled by the player
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

        self.width = 800
        self.height = 600
        self.size = (self.width, self.height)

        self.surface = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Cracker Chase")

        self.background_sprite = Sprite.Sprite(
            pygame.image.load("Images/background.png"), self
        )
        self.player_sprite = Sprite.Cheese(pygame.image.load("Images/cheese.png"), self)

        cracker_image = pygame.image.load("Images/cracker.png")

        self.sprites = [self.background_sprite]
        for i in range(20):
            cracker_sprite = Sprite.Cracker(image=cracker_image, game=self)
            self.sprites.append(cracker_sprite)
        self.sprites.append(self.player_sprite)

        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        pygame.quit()
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
            for sprite in self.sprites:
                sprite.draw()
            pygame.display.flip()


if __name__ == "__main__":
    game = CrackerChase()
    game.play_game()
