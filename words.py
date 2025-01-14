import random
class Words:
    def __init__(self):
        self.list_words = ['Будильник', 'Зарядка', 'Акварель', 'Травма', 'Оригами', 'Пульс', 'Спорт', 'Канатоходец', 'Магнитофон', 'Халат']
    
    def get_word(self):
        return random.choice(self.list_words)
    
    
|---------|
|    |    |
|    O    |
|   /|\   |
|   / \   |
|         |