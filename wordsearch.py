#-----------------------------------------------------------------------------------------------------------------------------------------

#                                                  WORD SEARCH GAME PROGRAM (PYTHON)

#-----------------------------------------------------------------------------------------------------------------------------------------

# importing modules
import random, os
from csv import reader

#-----------------------------------------------------------------------------------------------------------------------------------------

# VARIABLES
NUM_PLAYERS = 0               # variable for total number of players (depends on the user)
DIM         = 0               # variable for dimension (depends on the csv file)

board = []                    # list for storing the board
first_row_list = []           # list for storing the first row of csv file
final_correct_guesses=[]      # list for storing the correct words typed by all players
Players = []                  # list for storing players e.g. if 3 players, then ['Player 0', 'Player 1', 'Player 2']
Score = {}                    # dictionary for keeping track of scores and correct words typed by different players 

# list storing all board csv files
csv_board_files = ['board_1.csv', 'board_2.csv', 'board_3.csv', 'board_4.csv', 'board_5.csv', 'board_6.csv', 'board_7.csv',
'board_8.csv', 'board_9.csv', 'board_10.csv', 'board_11.csv', 'board_12.csv']

#-----------------------------------------------------------------------------------------------------------------------------------------

os.system('cls')      # clear screen (windows)
print()
print("+----------------------------------+")
print("| WELCOME TO THE WORD SEARCH GAME! |")
print("+----------------------------------+")
print("  Fun Multiplayer Quarantine Game!")
print("+----------------------------------+")
print()

NUM_PLAYERS = input("Enter the number of players: ")  # getting input from user for number of players
x = NUM_PLAYERS.isdigit()                             # checking if user entered a digit / number, stores TRUE or FALSE
if x == True:
	NUM_PLAYERS = int(NUM_PLAYERS)

	turn = random.randint(0, NUM_PLAYERS-1)                     # generates and stores the turns of the players

	csv_index = random.randint(0, len(csv_board_files)-1)       # getting random board csv file's index value from csv_board_files list

	with open(csv_board_files[csv_index], 'r') as read:         # opening and reading the file
		csv_reader = reader(read)
		first_row_list = next(csv_reader)                       # skipping the first row and storing it in another list 
		list_of_rows = list(csv_reader)                         # for storing the total number of rows

	rowcol = int(first_row_list[0])                             # takes the first element and stores to get the dimension of the list
	del first_row_list[0]                                       # removes the first element i.e. dimension (row digit)
	del first_row_list[0]                                       # removes the second element i.e. dimension (column digit)

	DIM = rowcol                                                # stores the dimension

	# creating the board
	for r in list_of_rows:
		rowList = []
		for c in r:
			rowList.append(c)
		board.append(rowList)

	def join_string(board):
		new_list = []                         
		for sub_list in board:
			word = ''.join(sub_list)           
			new_list.append(word)              
		return new_list

	# function to check words in rows
	def check_row(word,board):
		sub_list = join_string(board)
		j=0
		for i in sub_list:
			if i.find(word) != -1:            # searching for the presence of the word
				sub_list[j] = i.replace(word,word.upper(),1)
			if i.find(word[::-1]) != -1:      # searching for the presence of the word (reversed)
				sub_list[j] = i.replace(word[::-1],word[::-1].upper(),1)
			j+=1
		return sub_list

	# function to check all rows and columns, calling all other functions here
	def check_all_rol_col(word, board):
		check_list = split(check_row(word,board))
		if check_list == board:
			check_sub_1 = split_store_index_char(check_row(word,board))
			check_sub_2 = split(check_row(word,check_sub_1))
			check_list = split_store_index_char(check_sub_2)
		board = check_list
		return board

	def split_store_index_char(board):
		sub_list =[[row[i] for row in board] for i in range(len(board[0]))]     # going over all rows and storing each row's specific index value's characters
		return sub_list

	def split(board):
		sub_list_1 = []       # stores each row of board
		for word in board:  
			sub_list_2 = [char for char in word]
			sub_list_1.append(sub_list_2)
		return sub_list_1

	

	#board
	os.system('cls')
	print()
	print("+----------------------------------+")
	print("| WELCOME TO THE WORD SEARCH GAME! |")
	print("+----------------------------------+")
	print("  Fun Multiplayer Quarantine Game!")
	print("+----------------------------------+")

	# printing the board
	for cols in range(DIM):
		print('   ', end='')

	print("\n +" + "---+" * DIM)

	for row in range(DIM):
		print(' |', end=' ')
		for col in range(DIM):
			print(board[row][col] + ' | ', end='')
		print("\n +"+"---+"*DIM)

	print()

	# depending on the number of players, the Players list will contain that many players
	for i in range(0, NUM_PLAYERS):
		Players.append("Player "+str(i))

	turn = random.randint(0, NUM_PLAYERS-1)

	# loops until players guess all the words i.e. until the length of the first row's correct words is not equal to the length of the list of correct words entered by players
	while len(first_row_list)!=len(final_correct_guesses):
		turn = (turn + 1) % NUM_PLAYERS

		# asking the particular player (according to his turn) to guess the correct word 
		word = input("Player " + str(turn) + ", enter a word (or 'z' to exit): ")
		print()

		# if player enters 'z', then the program exits
		if word == "z":
			print("Thank you for playing :)")
			break

		else:
			
			# after player enters the word, now checking if that word is in the list that contains the correct words i.e. first_row_list
			if word in first_row_list:

				# to avoid repetitive guesses by the players, checking if that word has already been entered and appended in the list
				if word not in final_correct_guesses:

					board = check_all_rol_col(word,board)         # searching through the board for the word by calling the function
					final_correct_guesses.append(word)            # appending the word to the list
					os.system('cls')
					print()
					print("+----------------------------------+")
					print("| WELCOME TO THE WORD SEARCH GAME! |")
					print("+----------------------------------+")
					print("  Fun Multiplayer Quarantine Game!")
					print("+----------------------------------+")

					# printing the board
					for cols in range(DIM):
						print('   ', end='')

					print("\n +" + "---+" * DIM)

					for row in range(DIM):
						print(' |', end=' ')
						for col in range(DIM):
							print(board[row][col] + ' | ', end='')
						print("\n +"+"---+"*DIM)
					
					# keeping track of scores
					if Players[turn] in Score:                 # according to the player's turn, checking if that player's key is already in dictionary
						Score[Players[turn]].append(word)      # adding the correct word as value to that player's key in dictionary
						
					else:
						Score[Players[turn]] = [word]          # if player's key is not present already, then it makes a new key for that player
					print()
					print("Correct Guess! Keep it up, Player " + str(turn) +"!")

					
					print()
					print("SCORE")

					# printing the scores
					for key, value in Score.items():
						print(key, ":", len([item for item in value if item]), [item for item in value if item])
					print()
				else:
					print("Already Guessed and Chance Over!")       # if word is already present in the players' correct words' list 
					print()
			else:
				print("Sorry! Wrong Guess and Chance Over!")        # if player inputs words other than the correct words
				print()
	os.system("cls")
	print()
	print("Thank You for playing :) All words are guessed!")
	print()
	print("FINAL SCORE")
	for key, value in Score.items():
		print(key, ":", len([item for item in value if item]), [item for item in value if item])
	print()
else:
	print("Invalid input! Please enter a number!")