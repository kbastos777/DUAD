import pytest
from my_module.pytest_short_list import bubble_sort_len

def test_short_list_len():
    #Arrange
    input_list = [5,3,2]
    #Act
    result = bubble_sort_len(input_list)
    #Assert
    assert result == 3


def test_long_list_len():
    #Arrange
    input_list = [5,3,2,1,2,3,4,2,3,4,2,2,3,2,1,2,2,2,3,42,23,3,3,4,2,2,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,43,43,2,5,4,42,24,32,32,32,3,3,3,3,3,44,3,2,34,34,32,3,3,32,43,2,432,32,34,234,324,324,24,32,432,4,324,32,4,324,324,32,4,324,32,4,35,3,432,4,324,32,3,4,3,2,343,5,43,5,6,74,76,56,76,5,4,54,67,5,5,43,43,43,6]
    #Act
    result = bubble_sort_len(input_list)
    #Assert
    assert result > 100


def test_empty_list_len():
    #Arrange
    input_list = []
    #Act
    result = bubble_sort_len(input_list)
    #Assert
    assert result == 0


def test_non_listed_parameters():
    #Arrange
    number = 1
    #Act
    with pytest.raises(TypeError):
        bubble_sort_len(number)