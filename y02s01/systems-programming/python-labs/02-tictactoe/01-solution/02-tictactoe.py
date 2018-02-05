PLAYER_O = 'O'
PLAYER_X = 'X'

ROWS = 3
COLS = 3

class Error(Exception):
	"""Base class for exceptions"""
	pass
	
class MovementError(Error):
	""" Inherits from Error """
	pass

class Board:
	def __init__(self):
		# Create an empty board.
		self.board = [
			[' ', ' ', ' '],
			[' ', ' ', ' '],
			[' ', ' ', ' ']
		]
		
		self.row_count = ROWS
		self.col_count = COLS
		
	def show(self):
		for line in self.board:
			print(line)
		
	def is_full(self):
		for line in self.board:
			# If there is a space on a board it's not full.
			if ' ' in line:
				return False
				
		return True
		
	def columns(self):
		# Return board "as is"
		return self.board
		
	def rows(self):
		# Return transposed board
		return [list(x) for x in zip(*self.board)]
		
	def main_diagonal(self):
		return [self.board[0][0], self.board[1][1], self.board[2][2]]
		
	def anti_diagonal(self):
		return [self.board[0][2], self.board[1][1], self.board[2][0]]
		
	def set_position(self, pos_x, pos_y, val):
		if not self.position_is_valid(pos_x, pos_y):
			raise MovementError('position not valid')
			
		self.board[pos_x][pos_y] = val
			
	def position_is_valid(self, pos_x, pos_y):
		try:
			curval = self.board[pos_x][pos_y] != ' '
		except Exception as e:
			print('Cannot retrieve board value: {}'.format(e))
			return False
				
		if self.board[pos_x][pos_y] != ' ':
			return False
			
		if pos_x > self.col_count or pos_y > self.row_count:
			return False
			
		return True

class TicTacToeGame:
	def __init__(self):
		# Create an empty board
		self.board = Board()
		
	def show_board(self):
		self.board.show()
	
	def move(self, player, pos_x, pos_y):
		try:
			self.board.set_position(pos_x, pos_y, player)
		except Exception as e:
			raise e
			
	def get_winner(self):
		for player in (PLAYER_X, PLAYER_O):
			if line_wins(self.board.main_diagonal(), player):
				return player
				
			if line_wins(self.board.anti_diagonal(), player):
				return player
				
			for line in self.board.rows():
				if line_wins(line, player):
					return player
					
			for line in self.board.columns():
				if line_wins(line, player):
					return player
		
	def is_over(self):
		if self.board.is_full() or self.get_winner():
			return True
		
		return False
		
def player_make_move(game, player):
	while True:
		try:
			x, y = map(int, input('Player ' + player
			+ ', please make a move (x, y): '))
			game.move(player, x, y)
			break
		except Exception as e:
			print('There was an error: {}'.format(e))
		
def main():
	print('This is a tic-tac-toe game.\n'
	      'Cells are 0-indexed as (x, y).\n')
	
	tictactoe = TicTacToeGame()
	
	tictactoe.board.show()
	
	current_player = 0
	while not tictactoe.is_over():
		players = (PLAYER_X, PLAYER_O)
		player_make_move(tictactoe, players[current_player])
		
		current_player = (current_player + 1) % 2
		
		tictactoe.board.show()
		print('\n')
	
	winner = tictactoe.get_winner()
	if winner != None:
		print('Player ' + winner + ' won the game!')
	else:
		print('Game ended in a draw.')
	
# Checks if line wins the game for a player.
def line_wins(line, player):
	return line == list(player * len(line))
	
if __name__ == '__main__':
	main()