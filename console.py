class Console:
    def __init__(self):
        self.enter = ''
    
    def show(self,chance_count,word, len_word):
        print(f'Осталось {chance_count} попыток')
        print(f'Слово из {len_word} букв: {word}')

    def error_enter(self):
        print('Вводите слово или только одну букву!')
    
    def error_word(self):
        print('Вы ввели неправильное слово!')
    
    def error_letter(self):
        print('Такой буквы нет!')
       
    def you_win(self,word):
        print(f'Ты угадал слово {word}!!!')
    
    def you_lose(self,word):
        print(f'Ты проиграл! загаданное слово {word}')
        
    def input_value(self):
        self.enter = input('Введите слово или букву:').lower()
    
    @property
    def get_enter(self):
        return self.enter