# Dice Battle advanced
import random 

score_player = 0
score_computer = 0
previous = None
previous1 = None

while score_computer < 50 and score_player < 50:
	order = input("Enter 'ROLL' to roll the die or 'EXIT' to exit the game: ").upper()
	
	if order == "ROLL":
		
		die_player = random.randint(1, 6)
		print(f"You roll: {die_player}")
		
		if die_player == 1:
			score_player -= 3
			
		else:
			score_player = score_player + die_player
						
		die_computer = random.randint(1, 6)
		print(f"\nComputer rolls: {die_computer}")			
			
		if die_computer == 1:
			score_computer -= 3			

		else:
			score_computer = score_computer + die_computer


		while die_player == previous:
			rep = random.randint(1, 6)
			print(f"You roll again: {rep}")
			if rep == 1:
				score_player -= 3
			else:
				score_player = score_player + rep
			previous = rep
		
		previous = rep if die_player == previous else die_player
		
		while die_computer == previous1:
			rep1 = random.randint(1, 6)
			print(f"Computer rolls again: {rep1}\n")
			
			if rep1 == 1:
				score_computer -= 3
			else:
				score_computer = score_computer + rep1	
			previous1 = rep1
		
		previous1 = rep1 if die_computer == previous1 else die_computer
		
		print(f"\nYour score: {min(50,score_player)}\nComputer score: {min(50,score_computer)}")
			
	elif order == "EXIT":
		break
	else:
		print("Enter a valid input('ROLL' or 'EXIT') ")

if order == "EXIT":
	print("You left the game")	

if score_computer >= 50 and score_player >= 50:
	print("Draw!!!")

elif score_computer >= 50:
	print("Computer wins!")
	
elif score_player >= 50:
	print("You win!")
