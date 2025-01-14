from main import Todo
import pytest

class Test_Todo:
    test_object = Todo()
    test_data = [['test1','8:00'],['test2','9:00'],['test3','10:00'],['test4','11:00'],['test5','12:00']]
    test_complete = False
    test_transfer = False
    
    #Тестирование функции добавления задания
    #с использованием параметризации
    #и одновременное добавление всех 5 заданий 
    #из переменной test_data
    @pytest.mark.parametrize('issue,time',test_data)
    def test_add_issue(self,issue,time):
        self.test_object.add_issue(issue,time,
                                   self.test_complete,self.test_transfer)
        assert self.test_object.issue.get(issue) and self.test_object.issue.get(issue)[0] == time
    #Тест функции удаления задания,проверка что issue удалено 
    def test_delete_issue(self):
        self.test_object.delete_issue(self.test_data[-1][0])
        assert not self.test_object.issue.get(self.test_data[-1][0])
    #Тестирование функции изменения статуса Выполнено/Не выполнено
    def test_change_issue(self):
        self.test_object.change_issue(self.test_data[0][0])
        assert self.test_object.issue.get(self.test_data[0][0])[1] == True
    #Тестирование функции изменения статуса Перенесено/Не перенесено
    def test_change_transfer(self):
        self.test_object.change_transfer(self.test_data[1][0],'16:00')
        assert self.test_object.issue.get(self.test_data[1][0])[2] == True
    
    #Тест функции , возвращающей колличество дел
    def test_get_count(self):
        assert self.test_object.get_count() == len(self.test_object.issue)
    
    #Тест счетчика невыполненных дел
    def test_count_no_complete(self):
        test_complete = 0
        for value in self.test_object.issue.values():
            if value[1] == False:
                test_complete += 1
        assert test_complete == self.test_object.count_no_complete
    
    #Тест счетчика перенесенных дел
    def test_count_no_transfer(self):
        test_transfer = 0
        for value in self.test_object.issue.values():
            if value[2] == True:
                test_transfer += 1
        assert test_transfer == self.test_object.count_transfer  