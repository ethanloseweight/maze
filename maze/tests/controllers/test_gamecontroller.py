from controllers.gamecontroller import GameController
from models.maze import Maze
from models.player import Player


def game_controller():
    game = Maze()
    position = game.create_position_easy_mode()
    treasures = game.find_random_spot_easy_mode()
    backpack = Player()
    game_controller = GameController(game.maze_position, treasures, game.player, backpack, game.way_position, game.end_point)
    return game_controller


def test_has_attributes():
    """Tests if specific attribute(s) exist"""

    game_control = game_controller()

    assert hasattr(game_control, '_maze')
    assert hasattr(game_control, '_treasures')
    assert hasattr(game_control, '_view')
    assert hasattr(game_control, '_backpack')
    assert hasattr(game_control, '_find')
    assert hasattr(game_control, '_end_point')
    assert hasattr(game_control, '_player')


def test_has_methods():
    """Tests if specific method(s) exist"""

    game_control = game_controller()

    assert hasattr(game_control, 'get_display')
    assert hasattr(game_control, 'find_treasures')
    assert hasattr(game_control, 'get_end_point')
