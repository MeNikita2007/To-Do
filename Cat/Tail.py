class Tail:
    def __init__(self):
        self.__move_tail = False
        
    @property
    def move_tail(self):
        return self.__move_tail
    @move_tail.setter
    def move_tail(self, value):
        self.__move_tail = value
        
    def show(self):
        if self.move_tail:
            print('Машет хвостом')
        else:
            print('Махать хвостом запрещено!')