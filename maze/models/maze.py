import random


class Maze:
    def __init__(self):
        '''
            Initialize maze, maze way, player, end point storages
        '''
        self.maze_position = list()
        self.way_position = list()
        self.player = list()
        self.end_point = list()

    def create_position_easy_mode(self):
        '''
            Create each position and calculate positions from the maze file
        :return:
        '''
        _initial_structure = Maze.load_from_easy_mode_file()
        for y in range(len(_initial_structure)):
            for x in range(len(_initial_structure[y])):
                ch = _initial_structure[y][x]

                # Calculate each position
                screen_x = 25 + (30 * x)
                screen_y = 100 + (30 * y)

                # if character is x, it should be in maze position list
                if ch == 'x':
                    self.maze_position.append((screen_x, screen_y))

                # if character is the other, it should be in way position list
                elif ch == ' ' or 'P' or 'E':
                    self.way_position.append((screen_x, screen_y))

                    # if character is P, it should be in player list
                    if ch == 'P':
                        self.player.append((screen_x, screen_y))

                    # if character is E, it should be in end point list
                    elif ch == 'E':
                        self.end_point.append((screen_x, screen_y))

    def create_position_hard_mode(self):
        '''
            Create each position and calculate positions from the maze file
        :return:
        '''
        _initial_structure = Maze.load_from_hard_mode_file()
        for y in range(len(_initial_structure)):
            for x in range(len(_initial_structure[y])):
                ch = _initial_structure[y][x]

                # Calculate each position
                screen_x = 25 + (30 * x)
                screen_y = 100 + (30 * y)

                # if character is x, it should be in maze position list
                if ch == 'x':
                    self.maze_position.append((screen_x, screen_y))

                # if character is the other, it should be in way position list
                elif ch == ' ' or 'P' or 'E':
                    self.way_position.append((screen_x, screen_y))

                    # if character is P, it should be in player list
                    if ch == 'P':
                        self.player.append((screen_x, screen_y))

                    # if character is E, it should be in end point list
                    elif ch == 'E':
                        self.end_point.append((screen_x, screen_y))

    @classmethod
    def load_from_easy_mode_file(cls):
        '''
            load a file named 'map.txt', remove \n and store in a list
        :return: the first structure of the maze from the file as a list
        '''
        filename = 'map_easy.txt'
        _structure = list()
        with open(filename, "r") as f:
            _map = f.readlines()
            # remove \n each lines
            for line in _map:
                _structure.append(line.strip('\n'))
        return _structure

    @classmethod
    def find_random_spot_easy_mode(cls):
        '''
            Find random spots on the load for putting treasures
        :return: Random spots
        '''
        _empty_spot = list()
        _random_spots = list()

        # Finding Random spots from the map.txt file
        _initial_structure = cls.load_from_easy_mode_file()

        for y in range(len(_initial_structure)):
            for x in range(len(_initial_structure[y])):
                each_spot = _initial_structure[y][x]
                # Making an empty position and append to the empty spot list
                if each_spot == ' ':
                    screen_x = 25 + (30 * x)
                    screen_y = 100 + (30 * y)
                    _empty_spot.append((screen_x, screen_y))

        # Make sure which empty spots are using
        for i in range(len(_empty_spot)):
            random_four_number = random.randint(0, len(_empty_spot)-1)
            # Check the position is not duplicate
            if _empty_spot[random_four_number] not in _random_spots:
                _random_spots.append(_empty_spot[random_four_number])

                # If random spots is 4, then finishing the find spots loop
                if len(_random_spots) == 4:
                    break
        return _random_spots

    @classmethod
    def load_from_hard_mode_file(cls):
        '''
            load a file named 'map.txt', remove \n and store in a list
        :return: the first structure of the maze from the file as a list
        '''
        filename = 'map_hard.txt'
        _structure = list()
        with open(filename, "r") as f:
            _map = f.readlines()
            # remove \n each lines
            for line in _map:
                _structure.append(line.strip('\n'))
        return _structure

    @classmethod
    def find_random_spot_hard_mode(cls):
        '''
            Find random spots on the load for putting treasures
        :return: Random spots
        '''
        _empty_spot = list()
        _random_spots = list()

        # Finding Random spots from the map_hard.txt file
        _initial_structure = cls.load_from_hard_mode_file()

        for y in range(len(_initial_structure)):
            for x in range(len(_initial_structure[y])):
                each_spot = _initial_structure[y][x]
                # Making an empty position and append to the empty spot list
                if each_spot == ' ':
                    screen_x = 25 + (30 * x)
                    screen_y = 100 + (30 * y)
                    _empty_spot.append((screen_x, screen_y))

        # Make sure which empty spots are using
        for i in range(len(_empty_spot)):
            random_four_number = random.randint(0, len(_empty_spot)-1)
            # Check the position is not duplicate
            if _empty_spot[random_four_number] not in _random_spots:
                _random_spots.append(_empty_spot[random_four_number])

                # If random spots is 10, then finishing the find spots loop
                if len(_random_spots) == 10:
                    break
        return _random_spots
