import os
from utilities.data import BankAccount,SavingsAccount


def main_menu ():
    my_savings_account = SavingsAccount()
    while True:
        try:
                    print("### Welcome to your Bank ### \n\n")
                    print("Option 1:See current balance")
                    print("Option 2:Add funds")
                    print("Option 3:Withdraw money")
                    print("Option 4:Exit\n")
                    option = int(input("Please enter an option:"))

                    if option == 1:
                        os.system("CLS")
                        print(f"Your savings are: {my_savings_account._balance}")
                    elif option == 2:
                        os.system("CLS")
                        my_savings_account._balance = my_savings_account._add_funds(int(input("Please enter the amount of money to add to savings:")))
                    elif option == 3:
                        os.system("CLS")
                        my_savings_account._balance = my_savings_account.balance_check() 
                    elif option == 4:
                        os.system("CLS")
                        print("Good bye!")
                        break
                    else:
                        os.system("CLS")
                        print("##ERROR## Please enter a valid option")
        except ValueError as err:
                print(f"An error occurred in main_menu function due to {err}")    