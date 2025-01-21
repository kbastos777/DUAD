from my_module_test.pytest_ejercicios_semana6 import sum_numbers_in_list,return_sorted_phrase,print_upper_case_letters_quantity,print_lower_case_letters_quantity,return_alphabetic_sorted_list,create_prime_number_list


#Exercise #3
#=========================================================#
def test_exercise_three_sum_numbers_in_list():
    #Arrange
    input_list = [100,6,11]
    #Act
    result = sum_numbers_in_list(input_list)
    #Assert
    assert result > 0


def test_exercise_three_sum_numbers_in_list_second():
    #Arrange
    input_list = [2,55,6]
    #Act
    result = sum_numbers_in_list(input_list)
    #Assert
    assert result > 0


def test_exercise_three_3_sum_numbers_in_list_third():
    #Arrange
    input_list = [800,1,3]
    #Act
    result = sum_numbers_in_list(input_list)
    #Assert
    assert result > 0
#=========================================================#


#Exercise #4
#=========================================================#
def test_exercise_four_return_sorted_phrase():
    #Arrange
    phrase = "odnum aloH"
    #Act
    result = return_sorted_phrase(phrase)
    #Assert
    assert result == print("Hola Mundo")


def test_exercise_four_return_sorted_phrase_second():
    #Arrange
    phrase = "etirovaf ym si if icS"
    #Act
    result = return_sorted_phrase(phrase)
    #Assert
    assert result == print("Sci fi is my favorite")


def test_exercise_four_return_sorted_phrase_third():
    #Arrange
    phrase = " sraW ratS"
    #Act
    result = return_sorted_phrase(phrase)
    #Assert
    assert result == print("Star Wars")

#=========================================================#


#Exercise #5
#=========================================================#

#===UPPER CASE==#

def test_exercise_five_print_upper_case_letters_quantity():
    #Arrange
    phrase = "Star Trek"
    #Act
    result = print_upper_case_letters_quantity(phrase)
    #Assert
    assert result == 2


def test_exercise_five_print_upper_case_letters_quantity_second():
    #Arrange
    phrase = "SofTwarE EngineeRing"
    #Act
    result = print_upper_case_letters_quantity(phrase)
    #Assert
    assert result == 5


def test_exercise_five_print_upper_case_letters_quantity_third():
    #Arrange
    phrase = "HarrY Potter"
    #Act
    result = print_upper_case_letters_quantity(phrase)
    #Assert
    assert result == 3


#===LOWER CASE==#

def test_exercise_five_print_lower_case_letters_quantity():
    #Arrange
    phrase = "Star Trek"
    #Act
    result = print_lower_case_letters_quantity(phrase)
    #Assert
    assert result == 6


def test_exercise_five_print_lower_case_letters_quantity_second():
    #Arrange
    phrase = "SofTwarE EngineeRing"
    #Act
    result = print_lower_case_letters_quantity(phrase)
    #Assert
    assert result == 14


def test_exercise_five_print_lower_case_letters_quantity_third():
    #Arrange
    phrase = "HarrY Potter"
    #Act
    result = print_lower_case_letters_quantity(phrase)
    #Assert
    assert result == 8
#=========================================================#


#Exercise #6
#=========================================================#

def test_exercise_six_return_list():
    #Arrange
    phrase = "perro-gato-elefante-tigre"
    #Act
    input_list = return_alphabetic_sorted_list(phrase)
    input_list.sort()
    result = "-".join(str(element) for element in input_list)
    #Assert
    assert result == "elefante-gato-perro-tigre"


def test_exercise_six_return_list_second():
    #Arrange
    phrase = "planeta-galaxia-nave-nebulosa"
    #Act
    input_list = return_alphabetic_sorted_list(phrase)
    input_list.sort()
    result = "-".join(str(element) for element in input_list)
    #Assert
    assert result == "galaxia-nave-nebulosa-planeta"


def test_exercise_six_return_list_third():
    #Arrange
    phrase = "ceviche-limon-mango-aguacate"
    #Act
    input_list = return_alphabetic_sorted_list(phrase)
    input_list.sort()
    result = "-".join(str(element) for element in input_list)
    #Assert
    assert result == "aguacate-ceviche-limon-mango"
#=========================================================#


#Exercise #7
#=========================================================#

def test_exercise_seven_create_prime_number_list():
    #Arrange
    input_list = [1,2,4,5,6,7,9]
    #Act
    result = create_prime_number_list(input_list)
    #Assert
    assert result == [2,5,7]


def test_exercise_seven_create_prime_number_list_second():
    #Arrange
    input_list = [17,18,19,20,21,22]
    #Act
    result = create_prime_number_list(input_list)
    #Assert
    assert result == [17,19]


def test_exercise_seven_create_prime_number_list_third():
    #Arrange
    input_list = [60,61,62,63,64,65]
    #Act
    result = create_prime_number_list(input_list)
    #Assert
    assert result == [61]
#=========================================================#