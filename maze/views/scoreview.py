import pygame


class ScoreView:

    def display_score(self, win, player, time, rank):
        '''
            Initialize window and visualize Game Over Page
        :param win: Game Window
        :param player: Player name
        :param time: Time Record
        :param rank: Rank
        '''
        win.fill((255, 255, 255))

        # Background Image Load
        bg_image = pygame.image.load('pictures/victory.jpg')

        # Display Background
        escape_image = pygame.transform.scale(bg_image, (1000, 800))
        escape_image_rect = escape_image.get_rect()
        win.blit(escape_image, escape_image_rect)

        # Initialize Text to show on the Window
        complete_txt = pygame.font.Font(None, 55)

        # To display text: Player Name, Time Record, Rank
        player_txt_sf = complete_txt.render("Player Name: " + player, True, (255, 255, 255))
        player_txt_rect = player_txt_sf.get_rect()
        player_txt_rect.center = (500, 390)

        time_txt_sf = complete_txt.render("Time Record: " + str(time), True, (255, 255, 255))
        time_txt_rect = time_txt_sf.get_rect()
        time_txt_rect.center = (500, 440)

        rank_txt_sf = complete_txt.render("Your Rank: " + str(rank), True, (204, 0, 0))
        rank_txt_rect = rank_txt_sf.get_rect()
        rank_txt_rect.center = (500, 490)

        txt_txt_sf = complete_txt.render("Press ESC to escape", True, (255, 255, 255))
        txt_txt_rect = txt_txt_sf.get_rect()
        txt_txt_rect.center = (495, 570)

        # Display Text
        win.blit(player_txt_sf, player_txt_rect)
        win.blit(time_txt_sf, time_txt_rect)
        win.blit(rank_txt_sf, rank_txt_rect)
        win.blit(txt_txt_sf, txt_txt_rect)

        pygame.display.flip()

    def display_time_over(self, win, time):
        '''
            Initialize window and visualize Game Over Page
        :param win: Game Window
        :param time: Time Record
        '''
        win.fill((255, 255, 255))

        # Background Image Load
        bg_image = pygame.image.load('pictures/escape_bg.png')

        # Display Background
        escape_image = pygame.transform.scale(bg_image, (1000, 800))
        escape_image_rect = escape_image.get_rect()
        win.blit(escape_image, escape_image_rect)

        # Initialize Text to show on the Window
        complete_txt = pygame.font.Font(None, 55)

        # To display text: Player Name, Time Record, Rank
        player_txt_sf = complete_txt.render("Time's up! You are too SLOW!!", True, (204, 0, 0))
        player_txt_rect = player_txt_sf.get_rect()
        player_txt_rect.center = (500, 350)

        time_txt_sf = complete_txt.render("Time Record: " + str(time), True, (0, 0, 0))
        time_txt_rect = time_txt_sf.get_rect()
        time_txt_rect.center = (500, 420)

        again_txt_sf = complete_txt.render("Move faster!!! Press ESC", True, (0, 0, 0))
        again_txt_rect = again_txt_sf.get_rect()
        again_txt_rect.center = (500, 500)

        # Display Text
        win.blit(player_txt_sf, player_txt_rect)
        win.blit(time_txt_sf, time_txt_rect)
        win.blit(again_txt_sf, again_txt_rect)

        pygame.display.flip()

    def display_incomplete(self, win, time):
        '''
            Initialize window and visualize Game Over Page
        :param win: Game Window
        :param time: Time Record
        '''
        win.fill((255, 255, 255))

        # Background Image Load
        bg_image = pygame.image.load('pictures/escape_bg.png')

        # Display Background
        escape_image = pygame.transform.scale(bg_image, (1000, 800))
        escape_image_rect = escape_image.get_rect()
        win.blit(escape_image, escape_image_rect)

        # Initialize Text to show on the Window
        complete_txt = pygame.font.Font(None, 55)

        # To display text: Player Name, Time Record, Rank
        player_txt_sf = complete_txt.render("Trying to Cheat?", True, (204, 0, 0))
        player_txt_rect = player_txt_sf.get_rect()
        player_txt_rect.center = (500, 350)

        time_txt_sf = complete_txt.render("Time Record: " + str(time), True, (0, 0, 0))
        time_txt_rect = time_txt_sf.get_rect()
        time_txt_rect.center = (500, 420)

        again_txt_sf = complete_txt.render("Collect ALL the items, Press ESC", True, (0, 0, 0))
        again_txt_rect = again_txt_sf.get_rect()
        again_txt_rect.center = (500, 500)

        # Display Text
        win.blit(player_txt_sf, player_txt_rect)
        win.blit(time_txt_sf, time_txt_rect)
        win.blit(again_txt_sf, again_txt_rect)

        pygame.display.flip()

    def display_no_name(self, win, time):
        '''
            Initialize window and visualize Game Over Page
        :param win: Game Window
        :param time: Time Record
        '''
        win.fill((255, 255, 255))

        # Background Image Load
        bg_image = pygame.image.load('pictures/victory.jpg')

        # Display Background
        escape_image = pygame.transform.scale(bg_image, (1000, 800))
        escape_image_rect = escape_image.get_rect()
        win.blit(escape_image, escape_image_rect)

        # Initialize Text to show on the Window
        complete_txt = pygame.font.Font(None, 55)

        # To display text: Player Name, Time Record, Rank
        player_txt_sf = complete_txt.render("no name? are you the imposter?!", True, (204, 0, 0))
        player_txt_rect = player_txt_sf.get_rect()
        player_txt_rect.center = (500, 350)

        time_txt_sf = complete_txt.render("Time Record: " + str(time), True, (255, 255, 255))
        time_txt_rect = time_txt_sf.get_rect()
        time_txt_rect.center = (500, 420)

        again_txt_sf = complete_txt.render("Leave your name to get ranked. Press ESC", True, (255, 255, 255))
        again_txt_rect = again_txt_sf.get_rect()
        again_txt_rect.center = (500, 500)

        # Display Text
        win.blit(player_txt_sf, player_txt_rect)
        win.blit(time_txt_sf, time_txt_rect)
        win.blit(again_txt_sf, again_txt_rect)

        pygame.display.flip()
