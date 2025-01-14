from Cat.Tail import Tail
from Cat.Paws import Paws
from Cat.Head import Head

class Cat:
    def __init__(self,name,color,age):
        self.name = name
        self.color = color
        self.age = age
        self.tail = Tail()
        self.paws = Paws()
        self.head = Head()
        
    def state_show(self,choise):
        print('Имя кошки',self.name)
        print('Цвет кошки',self.color)
        print('Возраст кошки', self.age)
        self.tail.show()
        self.paws.show()
        match choise:
            case 1:
                self.head.voice()
            case 2:
                self.head.eat()
            case 3:
                self.head.bite()
    
    def change_state_tail(self,state):
        self.tail.move_tail = state
    
    def change_state_paws(self,state):
        self.paws.state_paws = state
        
if __name__ == '__main__':
    Murzik = Cat('Murzik','Red',2)
    Murzik.state_show(3)