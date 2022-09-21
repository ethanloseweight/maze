import pygame


class WelcomeView:

    def welcome_display(self, win):
        '''
            Initialize window and visualize Welcome Page
        :param win: Game Window
        '''
        win.fill((255, 255, 255))

        # Background Image
        bg = pygame.image.load('pictures/bg.png')
        b_image = pygame.transform.scale(bg, (1000, 800))
        image_rect = b_image.get_rect()
        win.blit(b_image, image_rect)

        # Initialize Text to show on the Window
        welcome_txt = pygame.font.Font(None, 50)
        time_limit_txt = pygame.font.Font(None, 25)

        # Text contents
        text2 = "Select Game Mode, or ESC to exit"
        text3 = "10 Sec Limit"
        text4 = "20 Sec Limit"

        # Initialize Text
        text2_txt_surface = welcome_txt.render(text2, True, (255, 255, 255))
        text2_txt_rect = text2_txt_surface.get_rect()
        text2_txt_rect.center = (500, 750)

        text3_txt_surface = time_limit_txt.render(text3, True, (204, 0, 0))
        text3_txt_rect = text3_txt_surface.get_rect()
        text3_txt_rect.center = (340, 700)

        text4_txt_surface = time_limit_txt.render(text4, True, (204, 0, 0))
        text4_txt_rect = text4_txt_surface.get_rect()
        text4_txt_rect.center = (630, 700)

        # Display Text
        win.blit(text2_txt_surface, text2_txt_rect)
        win.blit(text3_txt_surface, text3_txt_rect)
        win.blit(text4_txt_surface, text4_txt_rect)

        pygame.display.flip()

    def draw_button1(self, win, rect):
        '''
            Display Button on the page
        :param win: Game Window
        :param rect: Image Rect(x, y, width, Height)
        :return: None
        '''
        # Draw Easy Button
        bt1 = pygame.image.load('pictures/bt_easy.png')
        bt1_image = pygame.transform.scale(bt1, (rect.w, rect.h))
        bt1_rect = bt1_image.get_rect()
        bt1_rect.x = rect.x
        bt1_rect.y = rect.y
        win.blit(bt1_image, bt1_rect)

        # Show Button
        pygame.display.update()

    def draw_button2(self, win, rect):
        '''
            Display Button on the page
        :param win: Game Window
        :param rect: Image Rect(x, y, width, Height)
        :return: None
        '''
        # Draw Hard Button
        bt2 = pygame.image.load('pictures/bt_hard.png')
        bt2_image = pygame.transform.scale(bt2, (rect.w, rect.h))
        bt2_rect = bt2_image.get_rect()
        bt2_rect.x = rect.x
        bt2_rect.y = rect.y
        win.blit(bt2_image, bt2_rect)

        # Show Button
        pygame.display.update()