from controllers.keycontroller import KeyController
from views.gameview import GameView
import pygame
from pygame import mixer


class GameController(KeyController):

    def __init__(self, maze, treasures, player, backpack, maze_way, end_point):
        '''

        :param maze: maze position
        :param treasures: treasure position
        :param player: player position
        :param backpack: storage for treasures
        :param maze_way: maze way position
        :param end_point: maze end position
        '''
        self._x = 0
        self._y = 0

        self._maze = maze
        self._treasures = treasures
        self._player = player
        self._backpack = backpack
        self._find = list()
        self._end_point = end_point
        self._view = GameView(maze, treasures, player, maze_way, self._find, end_point)

    # Getter x for moving player
    @property
    def x(self):
        return self._x

    # Setter x for moving player
    @x.setter
    def x(self, x):
        self._x = x

    # Getter y for moving player
    @property
    def y(self):
        return self._y

    # Setter y for moving player
    @y.setter
    def y(self, y):
        self._y = y

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, count):
        self._count = count

    def get_display(self, game_window, timer):
        '''
            Display game window with all positions
        :param game_window: Basic Window
        :param timer: Timer
        :return:
        '''

        self._view.init_display(game_window, self.x, self.y)
        self._view.display_timer(game_window, timer)

    def get_display2(self, game_window, timer):
        '''
            Display game window with all positions
        :param game_window: Basic Window
        :param timer: Timer
        :return:
        '''

        self._view.init_display(game_window, self.x, self.y)
        self._view.display_alert_timer(game_window, timer)

    def find_treasures(self):
        '''
            When player find the treasure, store in the backpack
        :return: None
        '''
        self._player_position = ((self._player[0][0] + self._x), (self._player[0][1] + self._y))

        # Compare between player position and treasure position player find
        for find in self._treasures:
            if self._player_position == find:
                # If treasure player find is not in backpack, store in the backpack
                if find not in self._backpack.backpack:
                    self._backpack.pickup(find)
                    self._find.append(find)
                    self.count = len(self._backpack)
                    # Adding coin sound
                    coin_sound = mixer.Sound('bgm/coin.MP3')
                    coin_sound.play()

    def get_end_point(self):
        # When player get end point(Exit)
        for end_point in self._end_point:
            if end_point[0] <= self._player_position[0] < (end_point[0]+30):
                if end_point[1] <= self._player_position[1] < (end_point[1]+30):
                    return True

    def player_go_left(self):
        # Check the maze for going left wall if there is no wall, return True
        player_mv = (self._player_position[0] - 30, self._player_position[1])
        if player_mv not in self._maze:
            return True

    def player_go_right(self):
        # Check the maze for going right wall if there is no wall, return True
        player_mv = (self._player_position[0] + 30, self._player_position[1])
        if player_mv not in self._maze:
            return True

    def player_go_up(self):
        # Check the maze for going up wall if there is no wall, return True
        player_mv = (self._player_position[0], self._player_position[1] - 30)
        if player_mv not in self._maze:
            return True

    def player_go_down(self):
        # Check the maze for going down wall if there is no wall, return True
        player_mv = (self._player_position[0], self._player_position[1] + 30)
        if player_mv not in self._maze:
            return True
