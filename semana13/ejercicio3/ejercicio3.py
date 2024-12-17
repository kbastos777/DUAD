from datetime import date


class User:
    date_of_birth : date


    def __init__(self, date_of_birth):
            self.date_of_birth = date_of_birth


    @property
    def age(self):
        today = date.today()
        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )


def verify_age(func):
    def wrapper(user):
        if user.age < 18:
            raise ValueError("This user is not at least 18 years old")
        func(user)
    return wrapper


@verify_age
def create_user(user):
    print("\nUser successfully created!")


year = int(input("\nPlease enter the year of birth:"))
month = int(input("\nPlease enter the month of birth:"))
day = int(input("\nPlease enter the day of birth:"))


new_user = User(date(year,month,day))
create_user(new_user)
