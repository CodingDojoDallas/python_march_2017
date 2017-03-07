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
        return self
    def reverse(self):
        print "Reversing..."
        if (self.miles >= 5):   # Will not deduct 5 if it will be negative
            self.miles -= 5
        return self

bike1 = Bike(200, "25mph")
bike1.ride().ride().ride().reverse().displayInfo()      # Chain together methods

bike2 = Bike(100, "20mph");
bike2.ride().ride().reverse().reverse().displayInfo()

bike3 = Bike(500, "50mph");
bike3.reverse().reverse().reverse().displayInfo()
