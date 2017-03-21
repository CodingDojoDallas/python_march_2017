class Bike(object):
	def __init__(self,price,max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayInfo(self):
		print "Bike has a max speed of " + str(self.max_speed) + ", costs $" + str(self.price) + " and has " + str(self.miles) + " miles on it."
		return self
	def ride(self):
		print "Riding"
		self.miles += 10
		return self
	def reverse(self):
		print "Reversing"
		self.miles -= 5
		return self

suzuki = Bike(10000, 220)
kawasaki = Bike(8000, 200)
yamaha = Bike(9000, 210)

print suzuki
print kawasaki
print yamaha

print suzuki.price
print kawasaki.max_speed
print yamaha.miles

print suzuki.__dict__
print kawasaki

suzuki.ride().ride().ride().reverse().displayInfo()