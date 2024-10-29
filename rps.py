import random
count = 0
userwin = 0
compwin = 0
listname = ["rock", "paper", "scissor"]
while True:
	b = input("Enter rock, paper, or scissor (or 'quit' or 'stop' to stop): ")
	b.lower()
	if b == "quit" or b == "stop":
		break
	a = random.choice(listname)
	print("You chose:", b)
	print("Computer chose:", a)
	count += 1
	if a == b:
		print("Draw")
		print("Count:", count)
		print("Your wins:", userwin)
		print("Computer wins:", compwin)
	elif (a == "rock" and b == "scissor") or (a == "scissor" and b == "paper") or (a == "paper" and b == "rock"):
		print("Computer wins")
		compwin += 1 
		print("Count:", count)
		print("Your wins:", userwin)
		print("Computer wins:", compwin)
	elif b in listname:
		print("You win")
		userwin += 1
		print("Count:", count)
		print("Your wins:", userwin)
		print("Computer wins:", compwin)
	else:
		print("Invalid input")