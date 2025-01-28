def sum_numbers_in_list (num_list):
    total = 0
    for index , record in enumerate(num_list):
        total = total + num_list[index] 
    return total


def return_sorted_phrase (input_phrase):
    sorted_word_list = []
    for string in range(len(list(input_phrase))-1, -1,-1):
        sorted_word_list.append(input_phrase[string]) 
    return ''.join(sorted_word_list)

def print_upper_case_letters_quantity (phrase):
    counter = 0
    for string in phrase:
        if string.isupper():
            counter = counter + 1
    return counter


def print_lower_case_letters_quantity (phrase):
    counter = 0
    for string in phrase:
        if string.islower():
            counter = counter + 1
    return counter


def return_alphabetic_sorted_list(words):
    new_list = words.split("-")
    new_list.sort()
    return "-".join(str(element) for element in new_list)


def create_prime_number_list (input_list):
    prime_number_list = []
    for index , record in enumerate(input_list):
        divisible_numbers = 0
        for number in range(1,record+1,1):
            if record % number == 0:
                divisible_numbers = divisible_numbers + 1
        if divisible_numbers == 2:
            prime_number_list.insert(index,record)
            divisible_numbers = 0
    return prime_number_list