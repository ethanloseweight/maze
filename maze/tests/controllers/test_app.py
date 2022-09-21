import pytest
from controllers.app import AppController


@pytest.fixture
def app1():
    return AppController()


def test_has_method(app1):
    """Tests if specific method(s) exist"""
    assert hasattr(app1, 'run')


