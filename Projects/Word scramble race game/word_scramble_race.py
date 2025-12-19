# Word Scramble Race
import random
from english_words import get_english_words_set

words = list(get_english_words_set(['web2']))
word = random.choice(words).upper()
#print(word)
x = "".join(random.sample(word, len(word)))
print(f"The scrambled word is: {x}")

player_1_guess = ""
player_2_guess = ""

player_1_num_att = 5
player_2_num_att = 5

while player_1_num_att > 0 and player_2_num_att > 0 and player_1_guess!= word and player_2_guess!= word:
	
	print(f"Player 1 has {player_1_num_att} attempts left")
	player_1_guess = input("Player 1 guess is: ").upper()
	player_1_num_att -= 1
	if player_1_guess != word and player_1_guess.isalpha()== True:
		print("Wrong guess!")
	elif player_1_guess != word and player_1_guess.isalpha()== False:
		print("Wrong guess! Please enter only letters")
	
	print(f"Player 2 has {player_2_num_att} attempts left")
	player_2_guess = input("Player 2 guess is: ").upper()
	player_2_num_att -= 1
	if player_2_guess != word and player_2_guess.isalpha()== True:
		print("Wrong guess!")
	elif player_2_guess != word and player_2_guess.isalpha()== False:
		print("Wrong guess! Please enter only letters")
	
if player_1_guess == word and player_2_guess == word and player_1_num_att < player_2_num_att:
	print(f"\nPlayer 1 wins, the word is indeed {word}")

elif player_1_guess == word and player_2_guess == word and player_2_num_att < player_1_num_att:
	print(f"\nPlayer 2 wins, the word is indeed {word}")
	
elif player_1_guess == word and player_2_guess != word:
	print(f"\nPlayer 1 wins, the word is indeed {word}")	

elif player_1_guess != word and player_2_guess == word:
	print(f"\nPlayer 2 wins, the word is indeed {word}")	
	
elif player_1_guess == word and player_2_guess == word and player_2_num_att == player_1_num_att:
	print("\nDraw it is!!")

else:
	print(f"\nNo one guessed the word, the word is: {word}")
