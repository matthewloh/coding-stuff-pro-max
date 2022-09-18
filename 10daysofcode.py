def add(*num):
    sum = 0
    for x in num:
        sum += x
    return sum
    

# print(add(1, 2, 3, 4 ,5, 10))

def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
calculate(2, add=3 , multiply=5)

class Car:
    def __init__(self, **kwargs) -> None:
        self.make = kwargs["make"] # .get() method for tuples are able to return None compared to [] that causes a crash
        self.model = kwargs["model"]

car = Car(make= "Big Car", model = "Really Big Car")
print(car.make)