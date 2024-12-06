import os

class BankAccount():
    _balance = 2000


    def _add_funds(self,amount):
        return self._balance + amount


    def _withdraw_funds(self,amount):
        return self._balance - amount
    


class SavingsAccount(BankAccount):
    __min_balance = 500
    def balance_check(self):
        try:
            if self._balance < self.__min_balance:
                print(f"#ERROR#: The balance is below the minimum\n\n\n")
            else:
                self._balance = self._withdraw_funds(int(input("Please enter the amount of money to withdraw:")))
            return self._balance
        except ValueError as err:
            os.system("CLS")
            print(f"An error occurred in balance_check function due to:{err}")




