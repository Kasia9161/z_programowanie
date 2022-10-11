#zadanie 2d

def co_drugi(d):
    for i in d:
        if i.__index__() % 2 ==1:
            print(i)

co_drugi(range(10))
