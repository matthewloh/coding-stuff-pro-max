import re


class PlayerCharacter:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    def run(self):
        return self

player1 = PlayerCharacter("Kabo", 40)
print(player1.run())
b = player1.run()
print(b.run())
c = b 
print(c.run())

#testing return self, return self is a method you call