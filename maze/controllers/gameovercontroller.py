import pygame
from pygame import mixer
from views.gameoverview import GameOverView
from controllers.keycontroller import KeyController


class GameOverController(KeyController):
    def __init__(self):
        '''
            Inheritance Keyboard actions from the KeyController
        '''
        super().__init__()
        self._view = GameOverView()

    def run(self, win):
        """
            Display Game Over View
        :param win: Game Window
        :return: None
        """
        self._view.gameover_display(win)
        # Add Game Over sound
        gameover_sound = mixer.Sound('bgm/gameover.MP3')
        gameover_sound.play()