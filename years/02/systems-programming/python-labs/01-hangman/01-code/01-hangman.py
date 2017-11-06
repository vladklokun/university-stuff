from random import randrange

DEFAULT_ATTEMPTS = 6
WORDLIST         = ['time', 'year', 'people', 'way', 'day', 'man', 'thing', 'woman']

class HangmanGame:
	def __init__(self, word = [], attempts = DEFAULT_ATTEMPTS):
		if word == []:
			word = WORDLIST[randrange(len(WORDLIST))]
			
		self.word     = word
		self.attempts = attempts
		self.current_progress = ['_'] * len(self.word)
		
	def get_word(self):
		return self.word
		
	def decrease_attempts(self):
		self.attempts -= 1
		
	def is_over(self):
		return self.attempts == 0 or self.word_is_guessed()
	
	def word_is_guessed(self):
		return '_' not in self.get_current_progress()
	
	def get_current_progress(self):
		return self.current_progress
		
	def word_contains(self, letter):
		return letter in self.get_word()
	
	def update_progress(self, letter):
		word = self.get_word()
		for i, c in enumerate(word):
			if letter == word[i]:
				self.current_progress[i] = letter
		
	def make_guess(self, letter):
		if self.word_contains(letter):
			self.update_progress(letter)
		else:
			self.decrease_attempts()
			
	def take_input(self):
		self.print_hangman()
		print(self.get_current_progress())
		#while True:
		try:
			s = str(input("Please enter a letter: ")).lower()
		#        break
		except:
			print('Something went wrong. Please try again.')
				
		self.make_guess(s)
			
	def print_hangman(self):
		if self.attempts == 6:
			print("________      ")
			print("|      |      ")
			print("|             ")
			print("|             ")
			print("|             ")
			print("|             ")
		elif self.attempts == 5:
			print("________      ")
			print("|      |      ")
			print("|      0      ")
			print("|             ")
			print("|             ")
			print("|             ")
		elif self.attempts == 4:
			print("________      ")
			print("|      |      ")
			print("|      0      ")
			print("|     /       ")
			print("|             ")
			print("|             ")
		elif self.attempts == 3:
			print("________      ")
			print("|      |      ")
			print("|      0      ")
			print("|     /|      ")
			print("|             ")
			print("|             ")
		elif self.attempts == 2:
			print("________      ")
			print("|      |      ")
			print("|      0      ")
			print("|     /|\     ")
			print("|             ")
			print("|             ")
		elif self.attempts == 1:
			print("________      ")
			print("|      |      ")
			print("|      0      ")
			print("|     /|\     ")
			print("|     /       ")
			print("|             ")
		else:
			print("________      ")
			print("|      |      ")
			print("|      0      ")
			print("|     /|\     ")
			print("|     / \     ")
			print("|             ")
	
def main():
	print('This is a game of Hangman')
	
	game = HangmanGame()
	print(game.get_word())
	while not game.is_over():
		game.take_input()
	print(game.is_over())
	
if __name__ == '__main__':
	main()