import random 

#initialize global variables
COMPUTER_WINS = 1
PLAYER_WINS = 2
TIE = 0
INVALID = 3
ROCK = 1
PAPER = 2
SCISSORS = 3


#define main function
def main():
	player= int(input('Enter 1 for rock, 2 for paper, 3 for scissors: ')) #set variable for player input
	if player <= 3:
		computer= random.randint(1,3)	#set computer choice to a random number
		choice= 1,2,3
		result1= choiceString(player) #call choice function
		result2 = choiceString(computer)
		print("Player chose",result1) #display result
		print("Computer chose",result2)


		if rockPaperScissors(computer,player) == 1: #call rockPaperScissors function to display winner
			print("Computer Wins.")
		elif rockPaperScissors(computer,player) == 2:
			print("Player Wins.")
		elif rockPaperScissors(computer, player)==0:
			print('tie')
			main()
		else:
			print('invalid')
	else:
		print('Something went wrong')
		print("That is not a valid choice. No winner")



	
#define choiceString function
def choiceString(choice):
	if choice == 1: #value-returning function to display choice
		return "Rock"
	elif choice == 2:
		return "Paper"
	elif choice == 3:
		return "Scissors"
	else:
		return "Something went wrong"


#define rockPaperScissors function
def rockPaperScissors(computer, player): #value-returning function to return winning value
		if computer==1 and player==2:
			return COMPUTER_WINS
		elif computer==1 and player==3:
			return COMPUTER_WINS
		elif computer==2 and player==1:
			return COMPUTER_WINS
		elif computer==2 and player==3:
			return PLAYER_WINS
		elif computer==3 and player==1:
			return PLAYER_WINS
		elif computer==3 and player==2:
			return COMPUTER_WINS
		elif player==1 and computer==2:
			return COMPUTER_WINS
		elif player==1 and computer==3:
			return PLAYER_WINS
		elif player==2 and computer==1:
			return PLAYER_WINS
		elif player==2 and computer==3:
			return COMPUTER_WINS
		elif player==3 and computer==1:
			return COMPUTER_WINS
		elif player==3 and computer==2:
			return COMPUTER_WINS
		elif player==computer:
			return TIE
		else:
			return INVALID


main()




