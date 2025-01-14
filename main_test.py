def is_age(age):
    if isinstance(age, int):
        if age >= 18 and age < 100:
            return True
        else:
            return False
    else:
        return False

def plus_numbers(num1, num2):
    if not isinstance(num1,str) and not isinstance(num2,str):
        return num1+num2
    else:
        return False
    
def return_size_list(sps):
    if isinstance(sps,list):
        return len(sps)
    else:
        return False
    

def is_up_latter(word):
    if word[0] == word[0].upper():
        return True
    else:
        return False