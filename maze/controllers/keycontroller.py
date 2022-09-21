import pygame
import pygame.locals


class KeyController:

    def __init__(self):
        pass

    @classmethod
    def right_key_actions(cls):
        '''
            Left moving action when 'a' is pressed from the keyboard
        :return: Boolean
        '''
        keys = pygame.key.get_pressed()
        if keys[pygame.locals.K_RIGHT] or keys[pygame.locals.K_KP_6]:
            return True

    @classmethod
    def left_key_action(cls):
        '''
            Right moving action when 'd' is pressed from the keyboard
        :return: Boolean
        '''
        keys = pygame.key.get_pressed()
        if keys[pygame.locals.K_LEFT] or keys[pygame.locals.K_KP_4]:
            return True

    @classmethod
    def up_key_action(cls):
        '''
            Up moving action when 'w' is pressed from the keyboard
        :return: Boolean
        '''
        keys = pygame.key.get_pressed()
        if keys[pygame.locals.K_UP] or keys[pygame.locals.K_KP_8]:
            return True

    @classmethod
    def down_key_action(cls):
        '''
            Down moving action when 's' is pressed from the keyboard
        :return: Boolean
        '''
        keys = pygame.key.get_pressed()
        if keys[pygame.locals.K_DOWN] or keys[pygame.locals.K_KP_2]:
            return True

    @classmethod
    def backspace_key_action(cls):
        '''
            Backspace key to remove letters
        :return: Boolean
        '''
        keys = pygame.key.get_pressed()
        if keys[pygame.locals.K_BACKSPACE]:
            return True

    @classmethod
    def escape_key_action(cls):
        '''
            ESC key to escape Game
        :return: Boolean
        '''
        keys = pygame.key.get_pressed()
        if keys[pygame.locals.K_ESCAPE]:
            return True

    @classmethod
    def enter_key_action(cls):
        '''
            Enter keys and Space key to escape Game
        :return: Boolean
        '''
        keys = pygame.key.get_pressed()
        if keys[pygame.locals.K_RETURN] or keys[pygame.locals.K_KP_ENTER] or keys[pygame.locals.K_SPACE]:
            return True
