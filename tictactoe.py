# draw a game board
import random

def boarddrawing(size):
	count = 0
	while True:
		print('-----' * int(size))
		print('|    ' * (int(size) + 1))
		count = count + 1
		if count == int(size):
			print('-----' * int(size))
			break

def checkwinner3():
	row1 = []
	row2 = []
	row3 = []
	matrix = []
	for times in range(0,3):
		row1.append(random.randint(0,2))
		row2.append(random.randint(0,2))
		row3.append(random.randint(0,2))
	matrix.append([row1] +  [row2] + [row3])
	matrix = matrix[0]
	print(matrix)

	for i in range(3):
		if (matrix[i][0] == matrix[i][1] == matrix[i][2]) and (matrix[i][0] != 0):
			print('1. The winner is player ' + str(matrix[i][0]))
	for i in range(3):
		if (matrix[0][i] == matrix[1][i] == matrix[2][i]) and (matrix[0][i] != 0):
			print('2. The winner is player ' + str(matrix[0][i]))
	if (matrix[0][0] == matrix[1][1] == matrix[2][2]) and (matrix[0][0] != 0):
			print('3. The winner is player ' + str(matrix[0][0]))
	if (matrix[2][0] == matrix[1][1] == matrix[0][2]) and (matrix[1][1] != 0):
			print('4. The winner is player ' + str(matrix[1][1]))

def play():
	game = [[0,0,0], [0,0,0], [0,0,0]]
	x = int(input('Player 1 please enter your x: '))
	y = int(input('Player 1 please enter your y: '))
	game[x][y] = 1
	print(game)


def main():
	size = input('enter size of game board: ')
	boarddrawing(size)

play()


