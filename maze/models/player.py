
class Player:
    def __init__(self):
        '''
            This is backpack that stores treasures when player find it
        '''
        self.backpack = []

    def pickup(self, item):
        '''
            Store action, when player find treasure
        '''
        self.backpack.append(item)

    def __len__(self):
        return len(self.backpack)
