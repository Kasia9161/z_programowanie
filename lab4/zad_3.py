"""
Stworzyć następujące klasy:
Property (klasa opisująca posiadłość/nieruchomość), posiadająca pola:
area; rooms (int); price; address
House (klasa dziedzicząca klasę Property , która opisuje dom), posiadająca pola:
plot (rozmiar działki, int)
Flat (klasa dziedzicząca klasę Property , która opisuje mieszkanie), posiadająca pola:
floor
Dodatkowo:
Każda z klas dziedziczących ma mieć zaimplementowaną metodę __str__ , która będzie opisywała obiekt.
Pola w klasie mają być zdefiniowane jako atrybuty ustawiane podczas tworzenia instancji klasy za pośrednictwem
konstruktora.
Stworzyć po jednym obiekcie klasy House oraz Flat, a następnie je wyświetlić.
"""


class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    @property
    def area(self):
        return self._area

    @property
    def rooms(self):
        return self._rooms

    @property
    def price(self):
        return self._price

    @property
    def address(self):
        return self._address

    @area.setter
    def area(self, wartosc):
        self._area = wartosc

    @rooms.setter
    def rooms(self, wartosc):
        self._rooms = wartosc

    @price.setter
    def price(self, wartosc):
        self._price = wartosc

    @address.setter
    def address(self, wartosc):
        self._address = wartosc

    def __str__(self) -> str:
        return f"Area: {self.area}, pokoje: {self.rooms}, cena: {self.price}, adres: {self.address}"


class House(Property):
    def __init__(self, area, rooms: int, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self._plot = plot

    @property
    def plot(self) -> int:
        return self._plot

    @plot.setter
    def plot(self, plot: int):
        self._plot = plot

    def __str__(self) -> str:
        return super().__str__() + f", Plot: {self.plot}"


class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address)
        self._floor = floor

    @property
    def floor(self) -> None:
        return self._floor

    @floor.setter
    def plot(self, floor):
        self._floor = floor

    def __str__(self) -> str:
        return super().__str__() + f", Piętro: {self.floor}"


dom = House(120, 7, 1500000, "ul. Polna", 200)
mieszkanie = Flat(60, 2, 150000, "ul. Mikołowska", 5)
print("Dom: " + dom.__str__())
print("Mieszkanie: " + mieszkanie.__str__())
