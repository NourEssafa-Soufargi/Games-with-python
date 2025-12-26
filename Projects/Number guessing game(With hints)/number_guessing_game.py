# Number guessing game(With hints)
import random

num_of_tries = 10
score = 100
secret_number = random.randint(0, 100)
#print(secret_number) #Used for debugging

def ask_guess(message):
	guess = int(input(message))
	while guess < 0 or guess > 100:
		guess = int(input("Please enter a valid number(0–100): "))
	return guess

while num_of_tries > 0 and score > 0:
	guess = ask_guess(f"You have {num_of_tries} tries left\nGuess the number(0-100): ")
	num_of_tries -= 1

	if guess == secret_number:
		print(f"Great job! The number is indeed {guess}")
		print(f"Score: {score}")
		break

	diff = abs(secret_number - guess)

	if diff <= 3:
		score = score - 2
		print(f"Very close!\nScore: {max(score,0)}")
        
	elif diff <= 5:
		score = score - 5
		print(f"Hot!\nScore: {max(score,0)}")
        
	elif 6<= diff <= 12:
		score = score - 10
		print(f"Warm!\nScore: {max(score,0)}")
        
	else:
		score = score - 15
		print(f"Cold!\nScore: {max(score,0)}")

	score = max(score,0)

else:
	print(f"You lost! The number was {secret_number}")
