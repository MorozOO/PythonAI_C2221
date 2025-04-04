class Human:
    def __init__(self,name="Human"):
        self.name = name

class Auto:
    def __init__(self,brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def print_passengers_names(self):
        if self.passengers !=[]:
            print(f"Names of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"There are no passengers is {self.brand}")

nick = Human("Nick")
kate = Human("Kate")
car = Auto("Mercedes")
car.add_passenger(nick)
car.add_passenger(kate)
car.print_passengers_names()

# Створити 5 об`єктів класу Human
# Створити об'єк класу Auto
# Посати всіх людей в машину