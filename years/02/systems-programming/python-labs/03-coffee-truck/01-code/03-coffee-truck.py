from random import randrange

MAX_COFFEE_PRICE  = 500
MAX_CRATE_WEIGHT  = 100
MAX_TRUCK_SIZE    = 1000
COFFEE_TYPES      = ['Arusha', 'Mocha', 'Mundo']

class Coffee:
	def __init__(self, name = '', price = 0):
		if name == '':
			name = COFFEE_TYPES[randrange(len(COFFEE_TYPES))]
		if price == 0:
			price = randrange(MAX_COFFEE_PRICE)
			
		self.name = name
		self.price_per_kilo = price
	
	def get_price(self):
		return self.price_per_kilo
		
class Crate:
	def __init__(self, contents, weight = 0):
		if weight == 0:
			weight = randrange(MAX_CRATE_WEIGHT)
			
		self.weight = weight
		self.contents = contents
		
	def get_price(self):
		return self.weight * self.contents.get_price()
		
class Truck:
	# It's better to do contents as dictionary
	# since there can be multiple crates with
	# one type of coffee. WONTFIX
	def __init__(self, contents = [], size = 0):
		self.size = size
		self.contents = contents
		
	def get_price(self):
		# Sum all crate prices in truck instance contents
		return sum(crate.get_price() for crate in self.contents)
		
	def add_crate(self, crate):
		self.contents.append(crate)
		self.size += 1
		
def main():
	
	truck = Truck()
	
	coffee_types = [Coffee(), Coffee(), Coffee()]
	
	# Add a random quantity of crates with
	# random types of coffee. Class constructors
	# take care of the rest.
	for i in xrange(randrange(MAX_TRUCK_SIZE)):
		truck.add_crate(Crate(coffee_types[randrange(len(coffee_types))]))

	
	print('The price of goods in the truck: ' + str(truck.get_price()))
	
if __name__ == '__main__':
	main()
	