class Underscore(object):
	def map(self, iterable, function):
		for i in range(len(iterable)):
			iterable[i] = function(iterable[i])
		return iterable

	def reduce(self, iterable, function, memo):
		for num in iterable:
			memo = function(memo,num)
		return memo

	def find(self, iterable, function):
		for num in iterable:
			if function(num):
				return num
		return false

	def filter(self, iterable, function):
		matches = []
		for num in iterable:
			if function(num):
				matches.append(num)
		return matches

	def reject(self, iterable, function):
		rejected = []
		for num in iterable:
			if not function(num):
				rejected.append(num)
		return rejected