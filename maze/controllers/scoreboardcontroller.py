from views.scoreview import ScoreView
from controllers.keycontroller import KeyController


class ScoreBoardController(KeyController):
    def __init__(self):
        '''
            Inheritance Keyboard actions from the KeyController
        '''
        super().__init__()
        self._view = ScoreView()

    def display_score(self, win, player, time, data):
        """
            Display Score Board View
        :param win: Game Window
        :param player: Player Name
        :param time: Time Record
        :param data: All scores to get rank
        :return: None
        """
        rank = self.get_rank(data, player)
        self._view.display_score(win, player, round(time, 3), rank)

    def display_time_over(self, win, time):
        """
            Display Incomplete Score Board View
        :param win: Game Window
        :param time: Time Record
        :return: None
        """
        self._view.display_time_over(win, round(time, 3))

    def display_incomplete(self, win, time):
        """
            Display Incomplete Score Board View
        :param win: Game Window
        :param time: Time Record
        :return: None
        """
        self._view.display_incomplete(win, round(time, 3))

    def display_user_no_name(self, win, time):
        """
            Display Incomplete Score Board View
        :param win: Game Window
        :param time: Time Record
        :return: None
        """
        self._view.display_no_name(win, round(time, 3))

    def get_rank(self, data, player):
        """
            To get your Rank among players
        :param data: All Scores data
        :param player: Your Name
        :return: Rank
        """
        for idx, key in enumerate(data['scores']):
            if key['name'] == player:
                return idx+1

