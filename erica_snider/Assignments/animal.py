class Animal(object):
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print "Name:", self.name
        print "Health:", self.health

animal = Animal('animal')
animal.walk().walk().walk().run().run().displayHealth()


# Now, create another class called Dog that inherits everything that the Animal does and has,
# but 1) have the default health be 150
# and 2) add a new method called pet, which when invoked, increase the health by 5.
#
# Have the Dog walk() three times, run() twice, pet() once, and have it displayHealth().

class Dog(Animal):
    def __init__(self, name, health=150):
        super(Dog, self).__init__(name, health)
        # self.health = 150
    def pet(self):
        self.health += 5
        return self

dog = Dog('dog')
dog.walk().walk().walk().run().run().pet().displayHealth()


# Now, create another class called Dragon that also inherits everything from Animal,
# but 1) have the default health be 170
# and 2) add a new method called fly, which when invoked, decreased the health by 10.
#
# Have the Dragon walk() three times, run() twice, fly() twice, and have it displayHealth().
# When the Dragon's displayHealth function is called, have it say 'this is a dragon!'
# before it displays the default information (by calling the parent's displayHealth function).

class Dragon(Animal):
    def __init__(self, name, health=170):
        super(Dragon, self).__init__(name, health)
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        print "This is a dragon."
        super(Dragon, self).displayHealth()

dragon = Dragon('dragon')
dragon.walk().walk().walk().run().run().fly().fly().displayHealth()


# Now for the first instance of the animal (instance called 'animal'),
# try calling fly() or pet() and make sure this doesn't work.  (-:

# animal.fly().displayHealth() ---does not work:
# AttributeError: 'Animal' object has no attribute 'fly'
#
# animal.pet().displayHealth() ---does not work:
# AttributeError: 'Animal' object has no attribute 'pet'
