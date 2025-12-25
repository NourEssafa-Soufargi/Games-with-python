# Reaction time tester
import random
import time

time.sleep(random.randint(1,5))
start_time = time.time()

input_ = input("Go")
end_time = time.time() 

elapsed = end_time - start_time

if elapsed <= 0.5:
	print(f"Great your fast, you took {elapsed:.2f} seconds")
else:
	print(f"You took {elapsed:.2f} seconds. You can do faster")
