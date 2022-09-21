import pytest
from models.maze import Maze


@pytest.fixture
def maze1():
    return Maze()


def test_has_attribute(maze1):
    """Tests if specific attribute(s) exist"""

    assert hasattr(maze1, 'maze_position')
    assert hasattr(maze1, 'way_position')
    assert hasattr(maze1, 'player')
    assert hasattr(maze1, 'end_point')


def test_has_methods(maze1):
    """Tests if specific method(s) exist"""

    assert hasattr(maze1, 'create_position_easy_mode')
    assert hasattr(maze1, 'load_from_easy_mode_file')
    assert hasattr(maze1, 'find_random_spot_easy_mode')


def test_load_from_easy_mode_file(maze1):
    """Tests load_from_file method"""

    structure = maze1.load_from_easy_mode_file()
    for i in structure:
        assert type(i) == type(str())


def test_find_random_spot(maze1):
    """Tests find_random_spot method"""

    random_spots = maze1.find_random_spot_easy_mode()
    assert len(random_spots) == 4
