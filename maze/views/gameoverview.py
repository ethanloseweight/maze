import pygame


class GameOverView:

    def __init__(self):
        pass

    @classmethod
    def gameover_display(cls, win):
        '''
            Initialize window and visualize Game Over Page
            :param win: Game Window
        '''
        win.fill((255, 255, 255))

        # Background Image load
        bg_image = pygame.image.load('pictures/gameover.jpg')

        # Display Background Image
        game_over_image = pygame.transform.scale(bg_image, (1000, 800))
        game_over_image_rect = game_over_image.get_rect()
        win.blit(game_over_image, game_over_image_rect)

        # Initialize Text to show on the Window
        game_over_txt = pygame.font.Font(None, 50)

        # Text contents
        text = "Press ESC"

        # Initialize Text
        text_txt_surface = game_over_txt.render(text, True, (0, 0, 0))
        text_txt_rect = text_txt_surface.get_rect()
        text_txt_rect.center = (500, 750)

        # Display Text
        win.blit(text_txt_surface, text_txt_rect)

        pygame.display.flip()
