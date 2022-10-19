'''
Stworzyć klasę Student , która posiada 2 parametry (name i marks) oraz jedną metodę is_passed, która zwraca wartość
logiczną, pozytywną gdy średnia ocen jest > 50 w przeciwnym przypadku negatywną. Następnie należy stworzyć 2 przykładowe
obiekty klasy, tak aby dla pierwszego obiektu metoda zwracała true , a dla drugiego false .
'''

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        return sum(self.marks) / len(self.marks) > 50

student1 = Student('Anna', [55, 70, 80])
print(student1.is_passed())

student2 = Student("Adam", [20, 33, 50])
print(student2.is_passed())