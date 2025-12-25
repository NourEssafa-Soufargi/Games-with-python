# Memory Sequence Game
import random
import string
import time
import os

combination = "".join(random.choice(string.ascii_uppercase) for _ in range(3))
print(f"The combination is {combination}", end="\r")
time.sleep(3)
seq_length = 3
answer = input("Enter your answer please: ").upper()
os.system("cls")

while answer == combination: 
	combination = combination + "".join(random.choice(string.ascii_uppercase))
	print(f"The new combination is {combination}", end="\r")
	time.sleep(3)
	seq_length +=1
	answer = input("Enter your answer please: ").upper()
	os.system("cls")
	"""
	os.system("cls" if os.name == "nt" else "clear")
	"cls" is the Windows command to clear the screen.
	"clear" is the Linux/Mac command to clear the screen.
	
	OS	     os.name
	Windows	 'nt'
	Linux	 'posix'
	MacOS	 'posix'
	
	Here since we are using the windows OS,we simply put: os.system("cls")
	"""
	
print("You lost the game!!")
print(f"Your score is {seq_length}")
