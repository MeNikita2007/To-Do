# class Nums:
#     def __init__(self,list_nums):
#         self.list_nums = list_nums
    
#     def summ(self):
#         return sum(self.list_nums)
    
#     def mid_areph(self):
#         return sum(self.list_nums)/len(self.list_nums)
    
#     def max_in_list(self):
#         return max(self.list_nums)
        
#     def min_in_list(self):
#         return min(self.list_nums)
    

# class Chislo:
#     def __init__(self,num):
#         self.__num = num
    
#     @property
#     def num(self):
#         return self.__num
    
#     @num.setter
#     def num(self,num):
#         self.__num = num
    
#     def num_in_oct(self):
#         return oct(self.num)[2:]
    
#     def num_in_hex(self):
#         return hex(self.num)[2:]
    
#     def num_in_bin(self):
#         return bin(self.num)[2:]


class Valid_Form:
    def __init__(self,name,age,login,password):
        self.name = name
        self.age = age
        self.login = login
        self.password = password
    def check_age(self):
        if self.age >= 18 and self.age <100:
            return True
        else:
            return False
        
    def valid(self):
        list_symbols = ['.',',','!','?','/','*','-']
        count_name = 0
        count_login = 0
        count_password = 0
        for i in list_symbols:
            if i in self.name:
                count_name += 1
            if i in self.login:
                count_login +=1
            if i in self.password:
                count_password+=1
        if count_name == 0 and count_login == 0 and count_password >= 1:
            return True
        else:
            return False