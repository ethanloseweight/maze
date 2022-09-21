from views.welcomeview import WelcomeView
from controllers.keycontroller import KeyController


class WelcomeController(KeyController):
    def __init__(self):
        '''
        Inheritance Keyboard actions from the KeyController
        '''
        super().__init__()
        self._view = WelcomeView()

    def run(self, win):
        """
            Display Welcome View
        :param win: Game Window
        :return: None
        """
        # Running welcome page and making sure to display on the window
        self._view.welcome_display(win)

    def draw_button1(self, win, rect):
        """
            Draw Easy Mode Button
        :param win: Game Window
        :param rect: Easy Mode Button Image Rect(x, y, width, height)
        :return: None
        """
        # Draw Easy Mode Button
        self._view.draw_button1(win, rect)

    def draw_button2(self, win, rect):
        """
            Draw Hard Mode Button
        :param win: Game Window
        :param rect: Hard Mode Button Image Rect(x, y, width, height)
        :return: None
        """
        # Draw Hard Mode Button
        self._view.draw_button2(win, rect)
