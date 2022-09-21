import pygame


class WellDoneView:

    def well_done_display(self, win, player):
        '''
            Initialize window and visualize Game Over Page
        :param win: Game Window
        :param player: Player Name
        '''
        win.fill((255, 255, 255))

        # Background Image Load
        bg_image = pygame.image.load('pictures/victory.jpg')

        # Display Background
        escape_image = pygame.transform.scale(bg_image, (1000, 800))
        escape_image_rect = escape_image.get_rect()
        win.blit(escape_image, escape_image_rect)

        # Player Name textbox
        base_txt = pygame.font.Font(None, 40)

        textbox_surface = base_txt.render(player, True, (255, 255, 255))
        input_rect = pygame.Rect(410, 400, 200, 45)

        pygame.draw.rect(win, (255, 255, 255), input_rect, 4)
        input_rect.w = textbox_surface.get_width()
        win.blit(textbox_surface, (input_rect.x + 5, input_rect.y + 5))

        player_txt_sf = base_txt.render("Type Your Name", True, (255, 255, 255))
        player_txt_rect = player_txt_sf.get_rect()
        player_txt_rect.x = 400
        player_txt_rect.y = 350
        win.blit(player_txt_sf, player_txt_rect)

        pygame.display.flip()


