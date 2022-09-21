from views.gameview import GameView
from models.maze import Maze
from models.player import Player


def gameview():
    game = Maze()
    position = game.create_position_easy_mode()
    treasures = game.find_random_spot_easy_mode()
    backpack = Player()
    gameview = GameView(game.maze_position, treasures, game.player, backpack, game.way_position, game.end_point)
    return gameview


def test_has_attributes():
    game_view = gameview()

    assert hasattr(game_view, '_gameplay')
    assert hasattr(game_view, '_treasures')
    assert hasattr(game_view, '_player')
    assert hasattr(game_view, '_maze_way')
    assert hasattr(game_view, '_finds')
    assert hasattr(game_view, '_end_point')


def test_has_methods():
    game_view = gameview()

    assert hasattr(game_view, 'init_display')

