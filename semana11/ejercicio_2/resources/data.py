import os


class Bus:
    
    passenger_list = []
    def __init__(self):
        self.max_passengers = 5
    def AddPasengers (self,person,passenger_list):
        try:
            if len(passenger_list) < self.max_passengers:
                os.system("CLS")
                print("Passenger was sucessfully added")
                self.passenger_list.append(person)
            else:
                os.system("CLS")
                print("This bus run out of spaces for now, please try to free up some spaces")
        except Exception as ex:
                print(f"An error ocurred in AddPasengers method due to {ex}")


    def DispatchPassengers (self):
        try:
            dispatched_passengers = int(input("Please enter the number of passengers to be dispatched:"))
            counter = 0
            if dispatched_passengers > len(self.passenger_list):
                os.system("CLS")
                print("Dispatch passenger number is larger than the amount of passengers on board")
            else:
                while counter < dispatched_passengers:
                    self.passenger_list.pop(0)
                    counter = counter + 1
                os.system("CLS")
                print("Passenger(s) were sucessfully removed!")
                print(f"There are now {len(self.passenger_list)} passenger(s) on board")
        except IndexError as err:
            os.system("CLS")
            print(f"An error ocurred in DispatchPassengers method due to: {err}")
            print(f"There are now {len(self.passenger_list)} passenger(s) on board")
