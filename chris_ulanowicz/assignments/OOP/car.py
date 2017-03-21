class Car(object):
	def __init__(self,price,speed,fuel,mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if self.price > 10000:
			self.tax = 0.15
		else:
			self.tax = 0.12
		self.display_all()
	def display_all(self):
		print "Price: " + str(self.price)
		print "Speed: " + str(self.speed) + "mph"
		print "Fuel: " + self.fuel
		print "Mileage: " + str(self.mileage) + "mpg"
		print "Tax: " + str(self.tax)

fiat = Car(2000,35,"Full",15)
mini = Car(2500,5,"3/4",105)
citroen = Car(5000,15,"1/2",95)
tata = Car(1000,2,"7/8", 150)
dodge = Car(69995,220,"1/4", 8)
