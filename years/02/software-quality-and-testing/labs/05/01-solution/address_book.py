ADDRESS_BOOK_FILE = 'address-book'

import argparse

class Record:	
	def __init__(self):
		self.name    = ''
		self.surname = ''
		self.tel     = ''
		
	def get_surname(self):
		return self.surname
		
	def set_surname(self, surname):
		self.surname = surname
		
	def get_name(self):
		return self.name
		
	def set_name(self, name):
		self.name = name
		
	def get_tel(self):
		return self.tel
		
	def set_tel(self, tel):
		self.tel = tel
		
	def set_record(self, surname, name, tel):
		self.set_surname(surname)
		self.set_name(name)
		self.set_tel(tel)
		
	def as_string(self):
		return self.get_surname() + '\t' + self.get_name() + '\t' + self.get_tel() + '\n'
		
class AddressBook:
	def __init__(self):
		self.records = []
		
	def add_record(self, surname, name, tel):
		record = Record()
		record.set_record(surname, name, tel)
		self.records.append(record)
	
	def print_all(self):
		for record in self.records:
			print(record.as_string())
			
			
	def read_from_file(self):
		with open(ADDRESS_BOOK_FILE, 'r') as address_book:
			for line in address_book:
				surname, name, tel = line.split(maxsplit = 3)
				self.add_record(surname, name, tel)
				
	def find_person(self, s):
		matches = []
		for record in self.records:
			if s in record.as_string():
				matches.append(record.as_string())
		
		return matches
		
	def write_to_file(self, f):
		with open(f, 'w') as f:
			for record in self.records:
				f.write(record.as_string())
		
def main(args):
	address_book = AddressBook()
	address_book.read_from_file()
	if args.printall:
		address_book.print_all()
		
	if args.find:
		if args.surname:
			print(address_book.find_person(args.surname))
		else:
			print('Surname not specified. Ignoring.')
		
	if args.insert:
		if args.surname and args.name and args.telephone:
			address_book.add_record(args.surname, args.name, args.telephone)
			address_book.write_to_file(ADDRESS_BOOK_FILE)
		else:
			print('Params not specified. Ignoring.')
		
	print('Done.')

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	
	# Parse modes
	parser.add_argument('--insert', '-i', action='store_true')
	parser.add_argument('--printall', '-p', action='store_true')
	parser.add_argument('--delete', '-d', action='store_true')
	parser.add_argument('--edit', '-e', action='store_true')
	parser.add_argument('--find', '-f', action='store_true')
	
	# Parse address book record fields
	parser.add_argument('--name', '-n')
	parser.add_argument('--surname', '-s')
	parser.add_argument('--telephone', '-t')
	
	args = parser.parse_args()
	
	main(args)