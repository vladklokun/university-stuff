import argparse

def main(args):
	if args.printall:
		printall('address-book')
		
	if args.insert:
		insert('address-book', args.surname, args.name, args.telephone)
		
	print('Done.')
	
def insert(f, surn, name, tel):
	s = surn + name + tel + '\n'
	with open(f, 'a') as address_book:
		address_book.write(s)

def printall(f):
	while True:
		try:
			with open(f, 'r') as address_book:
				for line in address_book:
					print(line)
		except Exception as err:
			print("OS error: {0}".format(err))
			return
			
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	
	# Parse modes
	parser.add_argument('--insert', '-i', action='store_true')
	parser.add_argument('--printall', '-p', action='store_true')
	parser.add_argument('--delete', '-d', action='store_true')
	parser.add_argument('--edit', '-e', action='store_true')
	
	# Parse address book record fields
	parser.add_argument('--name', '-n')
	parser.add_argument('--surname', '-s')
	parser.add_argument('--telephone', '-t')
	
	args = parser.parse_args()
	
	main(args)