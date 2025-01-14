from console import Console
from words import Words
class Viselica:
    def __init__(self):
        self.console = Console()
        self.words = Words()
        self.guess_word = ''
        self.count_chance = 10
        self.exit = True
        self.win = False
        self.show_word =''
        self.view_word = []
    
    def logic_game(self):
        if len(self.console.get_enter) == 1:
            if self.console.get_enter in self.guess_word:
                index = self.get_index_letters()
                for i in index:
                    self.view_word[i] = self.console.get_enter
            else:
                self.console.error_letter()
        elif len(self.console.get_enter) == len(self.guess_word):
            if self.console.get_enter != self.guess_word:
                self.console.error_word()
            else:
                self.win = True
        else:
            self.console.error_enter()
        if '*' not in self.view_word:
            self.exit = False
            self.win = True
    
    def get_index_letters(self):
        list_index = []
        for i,v in enumerate(self.guess_word):
            if v == self.console.get_enter:
                list_index.append(i)
        return list_index
        
    def add_show_word(self):
        self.show_word = ''.join(self.view_word)
                
    
    def game_play(self):
        self.request_word()
        for i in range(len(self.guess_word)):
            self.view_word.append('*')
        
        while self.exit:
            if self.count_chance !=0 and self.guess_word != self.console.get_enter:
                self.add_show_word()
                self.console.show(self.count_chance,self.show_word,len(self.guess_word))
                self.console.input_value()
                self.logic_game()
                self.count_chance -= 1
            else:
                self.exit = False
        
        if self.win:
            self.console.you_win(self.guess_word)
        else:
            self.console.you_lose(self.guess_word)
            
    
    def request_word(self):
        self.guess_word = self.words.get_word().lower()
        

if __name__ == '__main__':
    game = Viselica()
    game.game_play()