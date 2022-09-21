class Score:
    """ Simple class to represent a score in a game """

    def __init__(self, name, score, play_time: float, date):
        """ Initializes private attributes

        Args:
            name (str): name of the player
            score (int): score of the player
            play_time (int): play time of the player
            date (str): date of the play
        """
        self._name = name
        self._score = score
        self._play_time = play_time
        self._date = date

    @property
    def name(self):
        return self._name

    @property
    def score(self):
        return self._score

    @property
    def play_time(self):
        return self._play_time

    @property
    def date(self):
        return self._date

    def to_dict(self):
        """
            return: a dictionary of attributes
        """
        return {
            "name": self._name,
            "score": self._score,
            "play time": self._play_time,
            "date": self._date
        }