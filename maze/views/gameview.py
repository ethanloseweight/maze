
import pygame


class GameView:
    def __init__(self, maze, treasures, player, maze_way, finds, end_point):
        '''
            Tack all positions, and display on the window
        :param maze: maze positions
        :param treasures: treasure positions
        :param player: player position
        :param maze_way: maze way position
        :param finds: treasures player find
        :param end_point: end position
        '''
        self._gameplay = maze
        self._treasures = treasures
        self._player = player
        self._maze_way = maze_way
        self._finds = finds
        self._end_point = end_point

    def init_display(self, win, x, y):
        '''
            Initialize window and visualize all things get positions
        :param win: Basic window will display all
        :param x: x position for player moving
        :param y: y position for player moving
        :param timer: to display time pass
        :return: None
        '''

        # Fill window's color
        win.fill((0, 0, 0))

        # Images load
        blocks = pygame.image.load('pictures/block.png')
        player = pygame.image.load('pictures/player.png')
        treasure = pygame.image.load('pictures/treasure.png')
        pockets = pygame.image.load('pictures/pocket.png')
        endpt = pygame.image.load('pictures/endpt.jpg')

        # Draw Maze color grey, width 30, height 30
        for maze in self._gameplay:
            block_im = pygame.transform.scale(blocks, (30, 30))
            block_im_rect = block_im.get_rect()
            block_im_rect.x = maze[0]
            block_im_rect.y = maze[1]
            win.blit(block_im, block_im_rect)

        # Draw Maze way color white, width 30, height 30
        for maze_way in self._maze_way:
            pygame.draw.rect(win, (255, 255, 255), (maze_way[0], maze_way[1], 30, 30))

        # Draw Treasures color green, width 20, height 20
        for golds in self._treasures:
            treasure_im = pygame.transform.scale(treasure, (30, 30))
            treasure_im_rect = treasure_im.get_rect()
            treasure_im_rect.x = golds[0]
            treasure_im_rect.y = golds[1]
            win.blit(treasure_im, treasure_im_rect)

        # Over-draw when player find treasures, same color with way, same size with treasures
        point = 0
        for finds in self._finds:
            if finds in self._treasures:
                pygame.draw.rect(win, (255, 255, 255), (finds[0], finds[1], 30, 30))

                # Display items when player get the treasure
                pocket_im = pygame.transform.scale(pockets, (30, 30))
                pocket_im_rect = pocket_im.get_rect()
                pocket_im_rect.x = 550 + point
                pocket_im_rect.y = 10
                win.blit(pocket_im, pocket_im_rect)
                point += 40

        # Draw End Point, color blue, width 30, height 30
        endpt_im = pygame.transform.scale(endpt, (30, 30))
        endpt_im_rect = endpt_im.get_rect()
        endpt_im_rect.x = self._end_point[0][0]
        endpt_im_rect.y = self._end_point[0][1]
        win.blit(endpt_im, endpt_im_rect)

        # Draw Player color red, width 30, height 30
        player_im = pygame.transform.scale(player, (30, 30))
        player_im_rect = player_im.get_rect()
        player_im_rect.x = x + self._player[0][0]
        player_im_rect.y = y + self._player[0][1]
        win.blit(player_im, player_im_rect)

        # Update display
        pygame.display.update()

    @staticmethod
    def display_timer(window, timer):
        # Fill window's background color
        # window.fill((0, 0, 0))

        # Timer Text
        txt = pygame.font.Font(None, 32)
        txt_sf = txt.render('Timer : ', True, (255, 255, 255))
        txt_rect = txt_sf.get_rect()
        txt_rect.center = (410, 20)
        window.blit(txt_sf, txt_rect)

        txt1 = pygame.font.Font(None, 32)
        txt1_sf = txt1.render(str(timer), True, (255, 255, 255))
        txt1_rect = txt1_sf.get_rect()
        txt1_rect.center = (500, 20)
        window.blit(txt1_sf, txt1_rect)

        pygame.display.update()

    @staticmethod
    def display_alert_timer(window, timer):
        # Fill window's background color
        # window.fill((0, 0, 0))

        # Timer Alert Text
        txt = pygame.font.Font(None, 32)
        txt_sf = txt.render('Timer : ', True, (204, 0, 0))
        txt_rect = txt_sf.get_rect()
        txt_rect.center = (410, 20)
        window.blit(txt_sf, txt_rect)

        txt1 = pygame.font.Font(None, 32)
        txt1_sf = txt1.render(str(timer), True, (204, 0, 0))
        txt1_rect = txt1_sf.get_rect()
        txt1_rect.center = (500, 20)
        window.blit(txt1_sf, txt1_rect)

        pygame.display.update()



