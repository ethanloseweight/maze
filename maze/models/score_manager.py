from models.score import Score
import json


class ScoreManager:
    """ Simple class to represent a score group """
    def __init__(self):
        """ Initialize private attribute
        Arg:
            scores (dict) : a group of the players with name and score
        """
        self._scores = dict()

    def add_score(self, score):
        """
        Add score in the dictionary
        """
        self._scores[score.name] = score

    @property
    def scores(self):
        """
        :return a list representation of this object
        """
        return list(self._scores.values())

    def serialize(self):
        """
        Arg:
            score_dict_list(list): a list of all scores
            score_dict(dictionary): a dictionary of scores

        return: a dictionary representation of this object
        """
        score_dict_list = list()
        score_dict = dict()

        # Add each score in the list as dictionary type
        for score in self.scores:
            score_dict_list.append(score.to_dict())
        # Sort by play time, the shortest time is higher
        new_sorted_list = sorted(score_dict_list, key=lambda i: (-i['score'], i['play time']))

        # Add all list in the dictionary as scores: [ data list ]
        score_dict['scores'] = new_sorted_list

        return score_dict

    def to_json(self, json_file):
        """
            Store all data as json file
        """
        with open(json_file, 'w') as j_file:
            json.dump(self.serialize(), j_file)

    def load_from_json(self, json_file):
        """
            Load json file and add data to the score's dictionary
        """
        with open(json_file, 'r') as j_file:
            data = json.load(j_file)
            for item in data['scores']:
                new_score = Score(name=item["name"], score=item["score"], play_time=item["play time"], date=item["date"])
                self.add_score(new_score)

