from controllers.gamecontroller import GameController
from controllers.gameovercontroller import GameOverController
from controllers.welcomecontroller import WelcomeController
from controllers.welldonecontroller import WellDoneController
from controllers.scoreboardcontroller import ScoreBoardController
from models.maze import Maze
from models.player import Player
from models.score_manager import ScoreManager
from models.score import Score
import pygame
import pygame.locals
import os
import time
from pygame import mixer
from datetime import date


class AppController:

    def __init__(self):
        """
            Arg:
                game_window: initialize game window
                player_name: get player name
                timer: get game play time
        """
        self._game_window = pygame.display.set_mode((1000, 800))
        self._player_name = ''
        self._timer = 0

    def easy_game_run(self):
        running = True
        # Setting Window
        clock = pygame.time.Clock()

        # Creating All positions(Maze, Way, Player)
        game = Maze()
        game.create_position_easy_mode()
        treasures = game.find_random_spot_easy_mode()
        backpack = Player()

        # Starting Maze Game
        game_start = GameController(game.maze_position, treasures,
                                    game.player, backpack, game.way_position, game.end_point)
        # Game Score
        game_score = ScoreManager()

        # Today
        today = date.today()

        while running:
            # Recode Game Starting Time
            start_time = time.time()

            while running is True:

                clock.tick(20)

                # Easy Game Mode Actions
                for event_game in pygame.event.get():
                    if event_game.type == pygame.locals.QUIT or game_start.escape_key_action() is True:
                        running = False

                # Key actions from keyboard and changing and moving player's position
                if game_start.left_key_action() is True:
                    if game_start.player_go_left() is True:
                        game_start.x -= 30
                elif game_start.right_key_actions() is True:
                    if game_start.player_go_right() is True:
                        game_start.x += 30
                elif game_start.up_key_action() is True:
                    if game_start.player_go_up() is True:
                        game_start.y -= 30
                elif game_start.down_key_action() is True:
                    if game_start.player_go_down() is True:
                        game_start.y += 30

                # Start Game
                self._timer = time.time() - start_time
                if 0 <= self._timer < 7:
                    game_start.get_display(self._game_window, round(self._timer, 3))

                # Find Treasures
                game_start.find_treasures()

                if 7 <= self._timer < 10:
                    game_start.get_display2(self._game_window, round(self._timer, 3))

                if self._timer >= 10:
                    self.game_time_out_run()
                    running = False

                # If user do not find all treasures and go to end point(exit), Game Over,
                # else If user find all treasures and go to end point(exit), Finish Game.
                if game_start.get_end_point() is True:
                    # check the file is existed the current directory
                    if os.path.isfile('scores.json'):
                        game_score.load_from_json('scores.json')

                    # Record Game End Time
                    end_time = time.time()

                    # Calculate score and play time
                    score = len(backpack) * 10
                    play_time = round(end_time - start_time, 3)
                    # Check backpack and Run each page
                    if len(backpack) != 4:
                        self.game_incomplete_run()
                        running = False
                    elif len(backpack) == 4:
                        self.game_complete_run()
                        # Add data into score manager as json file
                        player_name = self._player_name.replace('\r', '')
                        data = Score(player_name, score, play_time, str(today))
                        game_score.add_score(data)
                        game_score.to_json('scores.json')
                        self.game_scoreboard()
                        running = False

    def hard_game_run(self):
        running = True
        # Setting Window
        clock = pygame.time.Clock()

        # Creating All positions(Maze, Way, Player)
        game = Maze()
        game.create_position_hard_mode()
        treasures = game.find_random_spot_hard_mode()
        backpack = Player()

        # Starting Maze Game
        game_start = GameController(game.maze_position, treasures,
                                    game.player, backpack, game.way_position, game.end_point)
        # Game Score
        game_score = ScoreManager()

        # Today
        today = date.today()

        while running:
            # Recode Game Starting Time
            start_time = time.time()

            while running is True:

                clock.tick(20)

                # Hard Game Mode Actions
                for event_game in pygame.event.get():
                    if event_game.type == pygame.locals.QUIT or game_start.escape_key_action() is True:
                        running = False

                # Key actions from keyboard and changing and moving player's position
                if game_start.left_key_action() is True:
                    if game_start.player_go_left() is True:
                        game_start.x -= 30
                elif game_start.right_key_actions() is True:
                    if game_start.player_go_right() is True:
                        game_start.x += 30
                elif game_start.up_key_action() is True:
                    if game_start.player_go_up() is True:
                        game_start.y -= 30
                elif game_start.down_key_action() is True:
                    if game_start.player_go_down() is True:
                        game_start.y += 30

                # Start Game
                self._timer = time.time() - start_time
                if 0 <= self._timer < 17:
                    game_start.get_display(self._game_window, round(self._timer, 3))

                # Find Treasures
                game_start.find_treasures()

                if 17 <= self._timer < 20:
                    game_start.get_display2(self._game_window, round(self._timer, 3))

                if self._timer >= 20:
                    self.game_time_out_run()
                    running = False

                # If user do not find all treasures and go to end point(exit), Game Over,
                # else If user find all treasures and go to end point(exit), Finish Game.
                if game_start.get_end_point() is True:
                    # check the file is existed the current directory
                    if os.path.isfile('scores.json'):
                        game_score.load_from_json('scores.json')

                    # Record Game End Time
                    end_time = time.time()

                    # Calculate score and play time
                    score = len(backpack) * 10
                    play_time = round(end_time - start_time, 3)
                    # Check backpack and Run each page
                    if len(backpack) != 10:
                        self.game_incomplete_run()
                        running = False
                    elif len(backpack) == 10:
                        self.game_complete_run()

                        # Add data into score manager as json file
                        player_name = self._player_name.replace('\r', '')
                        data = Score(player_name, score, play_time, str(today))
                        game_score.add_score(data)
                        game_score.to_json('scores.json')
                        self.game_scoreboard()
                        running = False

    def game_time_out_run(self):
        running_game_incomplete = True

        # Game Over page
        game_over = GameOverController()

        # Game Over Page running
        while running_game_incomplete:
            # Game Over Page Actions
            for event_game_over in pygame.event.get():
                if event_game_over.type == pygame.locals.QUIT or game_over.escape_key_action() is True:
                    running_game_incomplete = False
                    self.game_time_out()

            # Running Game Over page
            game_over.run(self._game_window)

    def game_incomplete_run(self):
        running_game_incomplete = True

        # Game Over page
        game_over = GameOverController()

        # Game Over Page running
        while running_game_incomplete:
            # Game Over Page Actions
            for event_game_over in pygame.event.get():
                if event_game_over.type == pygame.locals.QUIT or game_over.escape_key_action() is True:
                    running_game_incomplete = False
                    self.game_incomplete()

            # Running Game Over page
            game_over.run(self._game_window)

    def game_complete_run(self):
        clock = pygame.time.Clock()
        running_game_complete = True

        # Complete page
        game_complete = WellDoneController()

        # The Complete Page running when the player complete the game
        while running_game_complete:
            # Complete Game Page Actions
            for event_well_done in pygame.event.get():
                if event_well_done.type == pygame.locals.QUIT or game_complete.escape_key_action() is True:
                    running_game_complete = False
                # Key actions, input player name
                if event_well_done.type == pygame.locals.KEYDOWN:
                    # Add typing sound
                    keyboard_sound = mixer.Sound('bgm/keyboard.MP3')
                    keyboard_sound.play()
                    # Enter player name and press Enter key
                    if game_complete.enter_key_action() is True:
                        running_game_complete = False

                    if game_complete.backspace_key_action() is True:
                        self._player_name = self._player_name[:-1]
                    else:
                        # Name path is less then 13 and all input from keyboard
                        if len(self._player_name) < 13:
                            self._player_name += event_well_done.unicode
                        else:
                            self._player_name = self._player_name

            # Running Complete Page to enter your name
            game_complete.run(self._game_window, self._player_name)
            clock.tick(20)

    def game_scoreboard(self):

        clock = pygame.time.Clock()

        # ScoreBoard
        game_score_board = ScoreBoardController()
        get_rank = ScoreManager()
        scoreboard_running = True

        while scoreboard_running:
            # Score Board Actions
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT or game_score_board.escape_key_action() is True:
                    self._player_name = ""
                    scoreboard_running = False

            if len(self._player_name) > 1:
                # Running Score Board Not Complete
                get_rank.load_from_json('scores.json')
                data = get_rank.serialize()
                player_name = self._player_name.replace('\r', '')
                game_score_board.display_score(self._game_window, player_name, self._timer, data)

            else:
                # Running Score Board to show your score
                game_score_board.display_user_no_name(self._game_window, self._timer)

            clock.tick(60)

    def game_incomplete(self):

        # ScoreBoard
        game_score_board = ScoreBoardController()
        scoreboard_running = True

        while scoreboard_running:
            # Score Board Actions
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT or game_score_board.escape_key_action() is True:
                    scoreboard_running = False
                game_score_board.display_incomplete(self._game_window, self._timer)

    def game_time_out(self):
        # ScoreBoard
        game_score_board = ScoreBoardController()
        scoreboard_running = True

        while scoreboard_running:
            # Score Board Actions
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT or game_score_board.escape_key_action() is True:
                    scoreboard_running = False
                game_score_board.display_time_over(self._game_window, self._timer)

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()

        # Welcome page running
        running_wel = True
        click = False

        # Welcome page
        welcome_game = WelcomeController()

        # Starting bgm
        mixer.music.load('bgm/Among Us Theme.MP3')
        mixer.music.play(-1)

        while running_wel:
            # Welcome page Actions
            for event in pygame.event.get():
                # Escape Welcome page
                if event.type == pygame.locals.QUIT or welcome_game.escape_key_action() is True:
                    running_wel = False
                # Mouse button action
                if event.type == pygame.locals.MOUSEBUTTONDOWN:
                    click = True

            # Get Mouse Position
            mx, my = pygame.mouse.get_pos()

            # Get Each Button Rect
            button_easy = pygame.Rect(250, 620, 200, 70)
            button_hard = pygame.Rect(530, 620, 200, 70)

            # Button Click Event to run Game Mode
            if button_easy.collidepoint(mx, my):
                if click:
                    # Add game starting sound
                    start_sound = mixer.Sound('bgm/start.MP3')
                    start_sound.play()
                    self.easy_game_run()
            if button_hard.collidepoint(mx, my):
                if click:
                    # Add game starting sound
                    start_sound = mixer.Sound('bgm/start.MP3')
                    start_sound.play()
                    self.hard_game_run()

            # Running Welcome page and Draw Buttons
            welcome_game.run(self._game_window)
            welcome_game.draw_button1(self._game_window, button_easy)
            welcome_game.draw_button2(self._game_window, button_hard)

            click = False
            clock.tick(60)
