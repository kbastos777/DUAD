first_num = (input("\nPlease enter a number:"))
second_num = (input("\nPlease enter a number:"))
third_num = (input("\nPlease enter a number:"))


def int_only (func):
    def wrapper(*args):
        for arg in args:
            try:
                int(arg)
            except ValueError as err:
                print(f"You have entered an invalid value type, please try again later:{err}")
        func(*args)
        print("\nGood bye!")
    return wrapper        


@int_only
def sum_of_three_numbers(num_one,num_two,num_three):
    return print(f"The sum of {num_one} + {num_two} + {num_three} is: {int(num_one) + int(num_two) + int(num_three)}")


sum_of_three_numbers(first_num,second_num,third_num)