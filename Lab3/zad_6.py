# zadanie 6


def listy(pierwsza: list, druga: list) -> list:
    koncowa = pierwsza + druga
    koncowa = set(koncowa)
    koncowa = (wynik**3 for wynik in koncowa)
    for wynik in koncowa:
        print(wynik)
    return koncowa
