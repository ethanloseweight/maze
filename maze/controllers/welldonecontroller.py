from views.welldoneview import WellDoneView
from controllers.keycontroller import KeyController


class WellDoneController(KeyController):
    def __init__(self):
        '''
        Inheritance Keyboard actions from the KeyController
        '''
        super().__init__()
        self._view = WellDoneView()

    def run(self, win, player):
        """
            Run Complete View page
        :param win: Game Window
        :param player: Player Name
        :return: None
        """
        self._view.well_done_display(win, player)

