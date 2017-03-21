import unittest
from underscore import Underscore

class UnderscoreTest(unittest.TestCase):
	def setUp(self):
		self._ = Underscore()
		self.test_list = [1,2,3,4,5]

	def testMap(self):
		self.result = self._.map(self.test_list, lambda x: x ** 2)
		return self.assertEqual([1,4,9,16,25], self.result)

	def testReduce(self):
		self.result = self._.reduce(self.test_list, lambda x, y: x + y, 0)
		return self.assertEqual(15, self.result)

	def testFind(self):
		self.result = self._.find(self.test_list, lambda x: x % 2 != 0)
		return self.assertEqual(1, self.result)

	def testFilter(self):
		self.result = self._.filter(self.test_list, lambda x: x % 2 == 0)
		return self.assertEqual([2,4], self.result)
		
	def testReject(self):
		self.result = self._.reject(self.test_list, lambda x: x % 2 == 0)
		return self.assertEqual([1,3,5], self.result)

if __name__ == "__main__":
	unittest.main()