class Bike(object):
    def __init__(self, price, max_speed):
        print "New bike purchased."
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print "Bike Info\n- Price: {}\n- Maximum Speed: {}\n- Total Miles: {}".format(self.price, self.max_speed, self.miles)
    def ride(self):
        print "Riding..."
        self.miles += 10
    def reverse(self):
        print "Reversing..."
        if (self.miles >= 5):   # Will not deduct 5 if it will be negative
            self.miles -= 5

bike1 = Bike(200, "25mph")
for i in range(3):
    bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2 = Bike(100, "20mph");
for i in range(2):
    bike2.ride()
    bike2.reverse()
bike2.displayInfo()

bike3 = Bike(500, "50mph");
for i in range(3):
    bike3.reverse()
bike3.displayInfo()
