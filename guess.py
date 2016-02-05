print "Please think of a number between 0 and 100000!"
guess = 50000
numGuesses = 0
low = 0
high = 100000
gotIt = "x"
while (gotIt != "c"):
	numGuesses += 1
	print "Is your secret number " + str(guess) + "?"
	print "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low.",
	print "Enter 'c' to indicate I guessed correctly.",
	gotIt = raw_input("")
	if gotIt == "c":
		print "Game over. Your secret number was: " + str(guess)
		break
	elif gotIt == "h":
		high = guess
		guess = low + int((high - low)/2)
	elif gotIt == "l":
		low = guess
		guess = low + int((high - low)/2)
	else:
		print "Sorry, I did not understand your input."
print "Number of guesses: " + str(numGuesses) + "!"