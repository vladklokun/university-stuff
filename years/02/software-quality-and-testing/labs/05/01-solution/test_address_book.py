import unittest
import address_book

class TestRecordMethods(unittest.TestCase):
	"""Test Record class methods"""
	
	def test_name_setter(self):
		a = address_book.Record()
		a.set_name('Vasya')
		self.assertEqual(a.name, 'Vasya')
	
	def test_name_getter(self):
		a = address_book.Record()
		a.set_name('Vasya')
		self.assertEqual(a.get_name(), 'Vasya')
		
	def test_surname_setter(self):
		a = address_book.Record()
		a.set_surname('Pupkin')
		self.assertEqual(a.surname, 'Pupkin')
		
	def test_surname_getter(self):
		a = address_book.Record()
		a.set_surname('Pupkin')
		self.assertEqual(a.get_surname(), 'Pupkin')
		
if __name__ == '__main__':
	unittest.main()