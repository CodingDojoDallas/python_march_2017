class Animal(object):
    def __init__(self, name):                   # Initialize an animal with set health and give name
        self.name = name
        self.health = 100
    def walk(self):                             # Walking and running drains the animal's health
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print "Current health:", self.health

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)         # Inherit the parent class initialization
        self.health = 150
    def pet(self):                              # Exclusive pet method for Dogs that heals
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)      # Inherit the parent class initialization
        self.health = 170
    def fly(self):                              # Exclusive fly method for Dragons that decreases health
        self.health -= 10
        return self
    def displayHealth(self):
        print "This is a dragon!"
        super(Dragon, self).displayHealth()     # Inherit the parent class displayHealth


animal = Animal("animal")
animal.walk().walk().walk().run().run().displayHealth()

dog = Dog("Dog")
dog.walk().walk().walk().run().run().pet().displayHealth()

dragon = Dragon("Dragon")
dragon.walk().walk().walk().run().run().fly().fly().displayHealth()
