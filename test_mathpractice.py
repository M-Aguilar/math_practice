import unittest
from mathpractice import prime

class PrimeTestCase(unittest.TestCase):
	def test_prime(self):
		test_number_1 = prime(10)
		answer1 = [2, 3, 5, 7]
		compare(test_number_1, answer1)
		self.assertEqual(answer1, test_number_1)
		test_number_2 = prime(100)
		answer2 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
		compare(answer2, test_number_2)
		self.assertEqual(test_number_2, answer2)


def compare(answer, result):
	print("The correct answer: \n" + str(result))
	print("Your answer:\n" + str(answer))


unittest.main()