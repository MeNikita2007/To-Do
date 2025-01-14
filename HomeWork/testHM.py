import unittest
# from mainHM import Nums,Chislo

# class Test_Nums(unittest.TestCase):
#     test_obj = Nums([3,4,12,18,6])
    
#     def test_summ(self):
#         self.assertEqual(self.test_obj.summ(),sum(self.test_obj.list_nums))
    
#     def test_mid_areph(self):
#         self.assertEqual(self.test_obj.mid_areph(), sum(self.test_obj.list_nums)/len(self.test_obj.list_nums))
    
#     def test_max_in_list(self):
#         self.assertEqual(self.test_obj.max_in_list(), max(self.test_obj.list_nums))
    
#     def test_min_in_list(self):
#         self.assertEqual(self.test_obj.min_in_list(), min(self.test_obj.list_nums))

# class Test_Chislo(unittest.TestCase):
#     test_obj = Chislo(123)
    
#     def test_oct(self):
#         self.assertEqual(self.test_obj.num_in_oct(), oct(self.test_obj.num)[2:])
    
#     def test_hex(self):
#         self.assertEqual(self.test_obj.num_in_hex(), hex(self.test_obj.num)[2:])
    
#     def test_bin(self):
#         self.assertEqual(self.test_obj.num_in_bin(), bin(self.test_obj.num)[2:])
        
#     def test_get_set(self):
#         self.test_obj.num = tmp = 42
#         self.assertEqual(self.test_obj.num, tmp)
        
# if __name__ == '__main__':
#     unittest.main()


from HomeWork.mainHM import Valid_Form

class Test_Valid_form(unittest.TestCase):
    test_form = Valid_Form('Ivan', 23, 'Ivan23', '123ivan*?23')
    
    def test_check_age(self):
        self.assertTrue(self.test_form.check_age())