#!usr/bin/env python

import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):

	def test_numero_comum(self):
		self.assertEqual(FizzBuzz(1),1)
		self.assertEqual(FizzBuzz(2),2)
		self.assertEqual(FizzBuzz(4),4)
		self.assertEqual(FizzBuzz(7),7)

	def test_retorna_fizz(self):
		self.assertEqual(FizzBuzz(3), 'fizz')
		self.assertEqual(FizzBuzz(6), 'fizz')
		self.assertEqual(FizzBuzz(9), 'fizz')
		self.assertEqual(FizzBuzz(12), 'fizz')

	def test_retorna_buzz(self):
		self.assertEqual(FizzBuzz(5), 'buzz')
		self.assertEqual(FizzBuzz(10), 'buzz')
		self.assertEqual(FizzBuzz(20), 'buzz')
		self.assertEqual(FizzBuzz(25), 'buzz')

	def test_retorn_fizzbuzz(self):
		self.assertEqual(FizzBuzz(15), 'fizzbuzz')
		self.assertEqual(FizzBuzz(30), 'fizzbuzz')
		self.assertEqual(FizzBuzz(45), 'fizzbuzz')

if __name__ == '__main__':
	unittest.main()