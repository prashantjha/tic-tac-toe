#!/usr/bin/python
def winner(board):
	if board[0][0] == board[0][1] == board[0][2] != None:
			return board[0][0]
	elif board[1][0] == board[1][1] == board[1][2] != None:
			return board[1][0]
	elif board[2][0] == board[2][1] == board[2][2] != None:
			return board[2][0]
	elif board[0][0] == board[1][0] == board[2][0] != None:
			return board[0][0]
	elif board[0][1] == board[1][1] == board[2][1] != None:
			return board[0][1]
	elif board[0][2] == board[1][2] == board[2][2] != None:
			return board[0][2]
	elif board[0][0] == board[1][1] == board[2][2] != None:
			return board[0][0]
	else:
			return None

def display_board(board):
	print board[0][0:3]
	print board[1][0:3]
	print board[2][0:3]

def create_board():
	return [[None, None, None], [None, None, None], [None, None, None]]
		
def play():
	board = create_board()
	display_board(board)
	count = 0
	while count < 9:
		pno = count % 2
		pos = int(input("input your position"))
		if pos > 8:
			print "please inter number less than 9"
			continue
		posx = pos/3
		posy = pos%3
		if board[posx][posy] == None:
			board[posx][posy] = pno
		else:
			continue
		count += 1
		display_board(board)
		won = winner(board)
		if won != None:
			break
	who_won = winner(board)
	if who_won is None:
		print "The game was a tie."
	else:
		print "The winning player is", who_won

if __name__ == "__main__":
	play()
