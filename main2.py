import time

# def timer(function):
#     t = time.time()
#     result = function()
#     print(f'Time of function`s work {time.time()-t}')

# def timer(function):
#     def tmp(*args, **kwargs):
#         t = time.time()
#         res = function(*args, **kwargs)
#         print(f'Time of function`s work {time.time()-t}')
#         return res
#     return tmp
    
# @timer
# def numbers():
#     tmp = []
#     for i in range(115001):
#         tmp.append(i)

# def add_list(num):
#     tmp_list = []
#     for i in range(num):
#         tmp_list.append(i*3)
#     return tmp_list
        
# numbers()

# print(add_list(100))



# NUmber 2
# def admin(function):
#     def tmp(*args,kwargs):
#         user_list = ['user','admin','moderator']
#         if args[0] in user_list:
#             res = function(*args,kwargs)
#             return res
#         else:
#             print(f'Пользователь {args.str()} не имеет доступ')
#     return tmp

# @admin
# def only_admin(user):
#     print(f'Hello {user}')

# only_admin('Vasya')



# NUmber 3
# def otchet(function):
#     def tmp(*args,kwargs):
#         stat_org = {
#             "ИП":"Отчет для ИП",
#             "ООО":"Отчет для ООО",
#             "ГОС":"Отчет для гос.организации"
#         }
#         if stat_org.get(args[0]):
#             res = function(stat_org[args[0]])
#             return res
#         else:
#             print(f'Статуса {args[0]} нет')
#     return tmp

# def numbers(function):
#     def tmp(*args,kwargs):
#         stat_org = {
#             "ИП":"1",
#             "ООО":"2",
#             "ГОС":"3"
#         }
#         if stat_org.get(args[0]):
#             res = function(stat_org[args[0]])
#             return res
#         else:
#             print(f'Статуса {args[0]} нет')
#     return tmp

# @otchet
# def send_otchet(org):
#     print(org)
    
# send_otchet("ИП")

# @numbers
# def send_otchet(org):
#     print(org)

# send_otchet("ИП")



# NUmber 4
# def correct_nums(function):
#     def tmp(*args,kwargs):
#         if (args[0]-args[1]) < 0:
#             res = function(args[1],args[0])
#             return res
#         else:
#             result = function(*args,kwargs)
#             return result
#     return tmp

# @correct_nums
# def minus_nums(num1, num2):
#     return num1 - num2

# # print(minus_nums(1,7))
# print(minus_nums(8,4))



# NUmber 5
def correct_words(function):
    def tmp(*args, **kwargs):
        if len(args[0]) < 8 and len(args[1]) < 8:
            result = function(*args,**kwargs)
            return result
        else:
            print(f"Error: length of {args[0] if len(args[0]) > 8 else args[1]} should not exceed 7 characters.")
    return tmp

@correct_words
def print_words(word1, word2):
    print(word1 + " " + word2)

print_words("Hello", "world")
print_words("Beautiful", "world")