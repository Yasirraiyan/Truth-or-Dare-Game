# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
 import random
import math
import time

choose = random.randint(1, 6)
life = 50
score1 = 0
score2 = 0
choose_array = ['truth', 'dare']
print(choose)

chooseplayer = int(input("Enter a number:"))  # Convert input to integer
if 1 <= chooseplayer <= 6:
    print("Valid")
else:
    print("Invalid!")

chooseplayer2 = random.choice(choose_array)  # Use random.choice()

if chooseplayer2 in choose_array:
    print("Valid choose")
else:
    print("Invalid Choose!")

if chooseplayer2 == choose_array[0]:
    print("Choose is truth.")
elif chooseplayer2 == choose_array[1]:
    print("Choose is dare.")

# Player 1's turn
if chooseplayer2 == choose_array[0]:  # If the choice is 'truth'
    ask_qn = input("Ask a question:")
    start_time = time.time()  # Record the start time
    while time.time() - start_time <= 10:  # Check if 10 seconds have elapsed
        print("Time exist.")
        time.sleep(0.5)  # Pause for 0.5 seconds
        life -= 5
    score1 += 1
    if life <= 0:
        print("Expire")

# Player 2's turn
if chooseplayer2 == choose_array[0]:  # If the choice is 'truth'
    ask_qn = input("Ask a question:")
    start_time = time.time()  # Record the start time
    while time.time() - start_time <= 10:  # Check if 10 seconds have elapsed
        print("Time exist.")
        time.sleep(0.5)  # Pause for 0.5 seconds
        life -= 5
    score2 += 1
    if life <= 0:
        print("Expire")

if score1 > score2:
    print("Player 1 is win")
elif score1 < score2:
    print("Player 2 is win")
else:
    print("Draw!")
