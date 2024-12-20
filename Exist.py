def exist():
  chooseplayer2 == choose_array[0]:
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
