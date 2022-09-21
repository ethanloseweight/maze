from models.score import Score


def score_instance():
    return Score("Ian", 100, 15.000, "2021-04-08")


def test_has_attributes():
    """Tests if specific attribute(s) exist"""

    score = score_instance()

    assert hasattr(score, "_name")
    assert hasattr(score, "_score")
    assert hasattr(score, "_play_time")
    assert hasattr(score, "_date")


def test_has_methods():
    """Tests if specific method(s) exist"""

    score = score_instance()

    assert hasattr(score, "to_dict")


def test_to_dict():
    """Tests to_dict method"""

    score = score_instance()

    assert score.to_dict() == {"name": "Ian", "score": 100, "play time": 15.000, "date": "2021-04-08"}
