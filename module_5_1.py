class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for i in range(1, new_floor + 1):
            if self.number_of_floors > new_floor > 1:
                print(i)
            else:
                print("Такого этажа не существует")
                break


House_1 = House('ЖК Горский', 18)
House_2 = House('Домик в деревне', 2)
House_3 = House('ТК "Северный"', 4)

House_1.go_to(5)
House_2.go_to(10)
House_3.go_to(3)
