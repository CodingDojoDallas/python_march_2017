class Bike(object):
    def __init__(self, price, max_speed, miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayInfo(self):
        print self.price, self.max_speed, self.miles
    def ride(self):
        print "riding"
        self.miles = self.miles + 10
        return self
    def reverse(self):
        print "reversing"
        if self.miles - 5 < 0:
            self.miles = 0
        else:
            self.miles = self.miles - 5
        return self

bike1 = Bike(200, "25mph")
bike2 = Bike(150, "20mph")
bike3 = Bike(1000, "75mph")

bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()
