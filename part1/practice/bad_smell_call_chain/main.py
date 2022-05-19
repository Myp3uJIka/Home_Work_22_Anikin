# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов


class Person:
    def __init__(self):
        self.room = 42
        self.city_population = 100500

    def get_person_room(self):
        return self.room

    def get_city_population(self):
        return self.city_population

# сделать экземпляр класса person и вызвать новые методы.


person = Person()
print(person.get_person_room())
print(person.get_city_population())