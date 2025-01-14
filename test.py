# from main_test import is_age, plus_numbers, return_size_list

# def test_is_age_more_18():
#     age = 20
#     result = is_age(age)
#     assert result

# def test_is_age_less_18():
#     age = 17
#     result = is_age(age)
#     assert not result

# def test_is_age_equals_18():
#     age = 18
#     result = is_age(age)
#     assert result

# def test_is_age_equals_1():
#     age = -1
#     result = is_age(age)
#     assert result != True
    
# def test_is_age_text():
#     age = 'yes'
#     result = is_age(age)
#     assert result == False

# def test_is_age_more_100():
#     age = 101
#     result = is_age(age)
#     assert result == False
    
# def test_plus_numbers():
#     a = 5
#     b = 12
#     result = plus_numbers(a, b)
#     assert result == a + b
    
# def test_plus_numbers_zero():
#     a = 0
#     b = 0
#     result = plus_numbers(a, b)
#     assert result == a + b
    
# def test_return_size_list():
#     my_list = [1, 2, 3, 4, 5]
#     result = return_size_list(my_list)
#     assert result == len(my_list)

from main_test import is_age,plus_numbers,return_size_list,is_up_latter
import pytest

test_ages_negative = [17,100,-1,0,'hello']
test_ages_positive = [18,35,99]
test_words = ['Hello','World','Cat']

test_nums_positive = [[2, 5], [100, 45], [4.5, 7.8], [67.9, 101.5]]
test_nums_negative = [['hello', 25], [35, 'world'], ['tails', 'dollar']]

@pytest.mark.parametrize('age',test_ages_negative)
def test_is_age_negative(age):
    assert not is_age(age)
    
@pytest.mark.parametrize('age',test_ages_positive)
def test_is_age_positive(age):
    assert is_age(age)
    
@pytest.mark.parametrize('word',test_words)
def test_is_up_latter(word):
    assert is_up_latter(word)
    
@pytest.mark.parametrize('num1, num2', test_nums_positive)
def test_plus_numbers_positive(num1, num2):
    assert plus_numbers(num1, num2)
    
@pytest.mark.parametrize('num1, num2', test_nums_negative)
def test_plus_numbers_negative(num1, num2):
    assert not plus_numbers(num1, num2)