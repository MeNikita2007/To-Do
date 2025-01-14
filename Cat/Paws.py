class Paws:
    def __init__(self):
        self.__state_paws = False
        
    @property
    def state_paws(self):
        return self.__state_paws
    @state_paws.setter
    def state_paws(self, value):
        self.__state_paws = value
        
    def show(self):
        if self.state_paws:
            print('Выпускает когти')
        else:
            print('Выпускать когти запрещено!')