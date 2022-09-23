#OOP moment
class PlayerCharacter: #init must be used to initialize an object, with (self, <parameter>)
    def __init__(self, name, age, school) -> None: #self is a default parameter that lets us refer to something
        self.name = name #we havent created yet, so self is a placeholder for everything to the left
        self.age = age 
        self.school = school
    def run(self): #of the method , remember that the name parameter here is a variable for the function
        print("run") # in relation to argument we put, such as Cindy or Tom
        return "done" #so that we can print(player1.run())


#Hover over PlayerCharacter to see what are the possible parameters you can put in
player1 = PlayerCharacter("Cindy", 14, "CLS") #We instantiate player1 with arguments for name, age, school parameters
player2 = PlayerCharacter("Tom", 15, "SXI") 
print(player1.name) #we use the self.name method
print(player1.age) #the .age is not actually a method, it's accessing the attribute 
print(player2.school) # you can access run with a call syntax
player1.run()
print(player2.name)
print(player2.run())
print(player1)
print(player2) #player 1 and player 2 have different memory values

#Objects can have attributes that we can create
player2.attack = 50
print(player2.attack) #Output = 50, cannot work for player 1 as they have different memory values

