# Number Chain Game
import random
starting_number = random.randint(-50, 50)
print(f"Starting number is: {starting_number}")
list_of_ops = ["+", "-", "*"]
list_of_sec_num = [1, 2, 3, 4, 5]
target = random.randint(-50, 50)
print(f"Your target number is {target}")
current = starting_number
moves = 0
attempts = 10
operation = None

while current!= target and attempts > 0:
	if operation is None:
		operation = input("Choose operation to do('+', '-', '*'): ")
		
		if operation not in list_of_ops:
			print("\nChoose a valid operation, please")
			operation = None
			continue
            
	second_number = int(input("Choose the second number(1-5): "))
	if second_number in list_of_sec_num:
		moves += 1
		if operation == "+":
			current = current + second_number
		elif operation == "-":
			current = current - second_number
		else:
			current = current * second_number
			
		print(f"\nCurrent result is {current}")
		attempts -= 1
		print(f"\nAttempts remaining: {attempts} attempt(s)")
		operation = None
	else:
		print("\nChoose a number between 1 and 5, please")


if attempts == 0:
	print("You reached the attempts limit!")
else:
	print(f"\nYou got the target number which is {target} in {moves} move(s)")
		
