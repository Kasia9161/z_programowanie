#zadanie 3

def spr_parzysta(x) -> bool:
   if x % 2 == 0:
    return True
   else:
       return False

wynik = spr_parzysta(2)

if (wynik):
    print('Liczba parzysta')
else:
    print('Liczba nieparzysta')
