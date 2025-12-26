# Dice Battle
import random
player_HP = 30
computer_HP = 30
list11 = ["ATTACK", "DEFEND"]

while player_HP > 0 and computer_HP > 0:
	print("Players's turn: ")
	dice1 = random.randint(1,6)
	print(f"Dice 1 gives {dice1}")
	dice2 = random.randint(1,6)
	print(f"Dice 2 gives {dice2}")
	result1 = dice1 + dice2
	print(f"Total for player is {result1}\n")

	print("Computer's turn: ")
	dice11 = random.randint(1,6)
	print(f"Dice 1 gives {dice11}")
	dice22 = random.randint(1,6)
	print(f"Dice 2 gives {dice22}")
	result11 = dice11 + dice22
	print(f"Total for computer is {result11}\n")

	computer_choice = random.choice(list11)
	print(f"Computer chooses to {computer_choice}")
	
	player_choice = input("Choose attack or defend: ").upper()
	while player_choice not in list11:
		player_choice = input("Enter a valid input (attack or defend):  ").upper()
	
	if player_choice == "ATTACK":
		player_HP = player_HP - result11
		print(f"Total damage for player is {result11}")
	elif player_choice == "DEFEND":
		player_HP = player_HP - (result11//2)
		print(f"Total damage for player is {result11//2}")
	print(f"HP for player becomes {player_HP if player_HP>= 0 else 0}\n")
	
	if computer_choice == "ATTACK":
		computer_HP = computer_HP - result1
		print(f"Total damage for computer is {result1}")
	else:
		computer_HP = computer_HP - (result1//2)
		print(f"Total damage for computer is {result1//2}")
	print(f"HP for computer becomes {computer_HP if computer_HP>= 0 else 0}")

if player_HP > computer_HP:
	print("Player wins!!")
elif player_HP < computer_HP:
	print("Computer wins!!")
else:
	print("Draw it is")
