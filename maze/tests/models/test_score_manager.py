from models.score import Score
from models.score_manager import ScoreManager


def score_instance():
    score = Score("Ian", 100, 15.000, "2021-04-08")
    return score


def manager_instance():
    return ScoreManager()


def test_has_attributes():
    manager = manager_instance()

    assert hasattr(manager, "_scores")


def test_has_methods():
    manager = manager_instance()

    assert hasattr(manager, "add_score")
    assert hasattr(manager, "serialize")
    assert hasattr(manager, "to_json")
    assert hasattr(manager, "load_from_json")


def test_add_score():
    score = score_instance()
    manager = manager_instance()
    manager.add_score(score)

    assert manager._scores == {"Ian": score}


def test_serialize():
    score = score_instance()
    manager = manager_instance()
    manager.add_score(score)

    assert manager.serialize() == {"scores": [{"name": "Ian", "score": 100, "play time": 15.000, "date": "2021-04-08"}]}

