import unittest
from algebra import quad_form

class AlgebraTestCase(unittest.TestCase):
	
	def test_returns_correct_integers(self):
		self.assertTrue(quad_form(1, 3, -4), (-4.0,1))

	def test_returns_correct_float(self):
		self.assertTrue(quad_form(9, 12, 4), (-0.667))

if __name__== '__main__':
	unittest.main()
