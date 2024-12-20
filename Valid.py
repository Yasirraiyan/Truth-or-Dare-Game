choose = random.randint(1, 6)
def valid(choose):
  if choose== 1 <= chooseplayer <= 6:
    print("Valid")
else:
    print("Invalid!")

chooseplayer2 = random.choice(choose_array)  # Use random.choice()

if chooseplayer2 in choose_array:
    print("Valid choose")
else:
    print("Invalid Choose!")
