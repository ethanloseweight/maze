import pytest
from models.player import Player
from models.maze import Maze


@pytest.fixture
def player1():
    return Player()


@pytest.fixture
def item():
    return 'item'


def test_has_attribute(player1):
    """Tests if specific attribute(s) exist"""

    assert hasattr(player1, 'backpack')


def test_has_method(player1):
    """Tests if specific method(s) exist"""

    assert hasattr(player1, 'pickup')


def test_attribute_type(player1):
    """Tests type of attribute(s)"""

    assert type(player1.backpack) == type(list())


def test_pickup(player1):
    """Tests pickup method"""

    maze1 = Maze()
    maze1.load_from_easy_mode_file()

    player1.pickup('item')
    assert player1.backpack == ['item']
