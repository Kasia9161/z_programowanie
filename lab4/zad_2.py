"""
Stworzyć następujące klasy:
Library (klasa opisująca bibliotekę), posiadająca pola:
city; street; zip_code; open_hours (str); phone
Employee (klasa opisująca pracownika biblioteki), posiadająca pola:
first_name; last_name; hire_date; birth_date; city; street; zip_code; phone
Book (klasa opisująca książkę), posiadająca pola
library; publication_date; author_name; author_surname; number_of_pages
Order (klasa opisująca zamówienie), posiadająca pola:
employee; student; books (lista obiektów klasy Book); order_date
Dodatkowo:
Każda klasa ma mieć zaimplementowaną metodę __str__ , która będzie opisywała obiekt oraz ewentualne obiekty
znajdujące się w tym obiekcie (np. obiekt Library w obiekcie Book).
Pola w klasie mają być zdefiniowane jako atrybuty ustawiane podczas tworzenia instancji klasy za pośrednictwem
konstruktora.
Stworzyć 2 biblioteki (2 instancje klasy), 5 książek, 3 pracowników, 3 studentów, oraz 2 zamówienia.
Wyświetlić oba zamówienia ( print )
"""

nl_char = "\n"


class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Biblioteka: adres: {self.street}, {self.zip_code} {self.city}, godziny działania: {self.open_hours}, tel.: {self.phone}"


class Employee:
    def __init__(
        self,
        first_name,
        last_name,
        hire_date,
        birth_date,
        city,
        street,
        zip_code,
        phone,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Pracownik: {self.first_name} {self.last_name}, urodzony: {self.birth_date}, zatrudniony: {self.hire_date}, adres: {self.street}, {self.zip_code} {self.city}, tel.: {self.phone}"


class Book:
    def __init__(
        self, library, publication_date, author_name, author_surname, number_of_pages
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Książka: Biblioteka: {self.library.__str__()}, \nopublikowana: {self.publication_date}, autorstwa: {self.author_name} {self.author_surname}, l. stron: {self.number_of_pages}"


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student: {self.name}, oceny: {self.marks}"


class Order:
    def __init__(self, employee, student, books: list, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'Zamówienie: pracownik: {self.employee.__str__()}, \nstudent: {self.student} w dniu: {self.order_date}, \nzawiera: \n{nl_char.join(map(str, [str(index)+": "+book.__str__() for index, book in enumerate(self.books)]))}.'


biblioteka1 = Library("Gliwice", "Czapli", "44-100", "9.00-16.00", "1111-111-111")
biblioteka2 = Library("Katowice", "Mickiewicza", "44-444", "8.00-15.30", "123-123-123")
book1 = Book(biblioteka1, "20-04-2020", "Adam", "Mickiewicz", 2581)
book2 = Book(biblioteka1, "30-08-2025", "Anna", "Nowak", 12345)
book3 = Book(biblioteka1, "22-05-2222", "Karol", "Kowalski", 987)
book4 = Book(biblioteka2, "12-05-2000", "Jan", "Piątek", 555)
book5 = Book(biblioteka2, "12-06-1987", "Piotr", "Sacała", 963)
pracownik1 = Employee(
    "Jan",
    "Nowak",
    "20-04-2015",
    "12-04-1995",
    "Knurów",
    "Orłów",
    "11-111",
    "111-111-111",
)
pracownik2 = Employee(
    "Ewa",
    "Lipa",
    "20-08-2000",
    "11-01-1972",
    "Kraków",
    "Polna",
    "22-000",
    "222-222-222",
)
pracownik3 = Employee(
    "Filip",
    "Król",
    "14-11-2015",
    "10-02-1980",
    "Katowice",
    "Owocowa",
    "00-000",
    "000-000-000",
)
student1 = Student("Wiktor", [11, 50, 89])
student2 = Student("Kamila", [90, 88, 22])
student3 = Student("Kamil", [20, 33, 40])
zamowienie1 = Order(pracownik1, student1, [book3, book2], "20-10-2022")
zamowienie2 = Order(pracownik3, student3, [book1, book4, book5], "11-09-2022")

print(zamowienie1.__str__())
print("\n")
print(zamowienie2.__str__())
