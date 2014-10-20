# Indo2SV selection
# Hangman game
# Author: Ardya Dipta Nandaviri
# www.ardyadipta.com
import os
import sys

os.system("clear")
print "----- Initializing Hangman Game------"
secretWord = raw_input("The secret word: ")
guesses = ' '
wrongGuesses =''

numberOfWrongsAllowed = 8
turns = numberOfWrongsAllowed

while turns > 0:         
	failed = 0

	os.system("clear")
	print "-----------------------------------------"

	for i in range(0, len(secretWord)):
		if secretWord[i] in guesses:
			sys.stdout.write(secretWord[i])
		else:
			sys.stdout.write('?')
			failed += 1

	print "\n"
			
	print "Wrong guesses (", + (turns - numberOfWrongsAllowed), "): ", 

	for i in range(0, len(wrongGuesses)):
		sys.stdout.write(wrongGuesses[i]),
		if not (i == len(wrongGuesses)-1):
			sys.stdout.write(", ")

	print "\n"
	if turns == numberOfWrongsAllowed - 1:
		for x in range(1,16):
			print '*'
	
	if turns == numberOfWrongsAllowed -2:
		print '**********'
		for x in range(1,15):
			print '*'

	if turns == numberOfWrongsAllowed -3:
		print '**********'
		print '*        *'
		print '*        * * *'
		print '*        **   *'
		print '*        ***** '
		for x in range(1,11):
			print '*'

	if turns == numberOfWrongsAllowed -4:
		print '**********'
		print '*        *'
		print '*        * * *'
		print '*        **   *'
		print '*        ***** '
		print '*           *   '
		print '*           *    '
		print '*           * '
		print '*           * '
		for x in range(1,7):
			print '*'

	if turns == numberOfWrongsAllowed -5:
		print '**********'
		print '*        *'
		print '*        * * *'
		print '*        **   *'
		print '*        ***** '
		print '*         * *   '
		print '*        *  *    '
		print '*           * '
		print '*           * '
		for x in range(1,7):
			print '*'

	if turns == numberOfWrongsAllowed -6:
		print '**********'
		print '*        *'
		print '*        * * *'
		print '*        **   *'
		print '*        ***** '
		print '*         * * * '
		print '*        *  *  * '
		print '*           * '
		print '*           * '
		for x in range(1,7):
			print '*'


	if turns == numberOfWrongsAllowed -7:
		print '**********'
		print '*        *'
		print '*        * * *'
		print '*        **   *'
		print '*        ***** '
		print '*         * * * '
		print '*        *  *  * '
		print '*           * '
		print '*           * '
		print '*          *'
		print '*         * '
		for x in range(1,5):
			print '*'


	if failed == 0:
		print "\nYou won"
		break

	print "\n"
	guess = raw_input("Your guess (a char): ")
	guesses += guess

	if ((guess not in secretWord) and (guess not in wrongGuesses)):
		for char in guesses:
			if not(char in secretWord) and not (char in wrongGuesses):
				wrongGuesses += char
		turns -= 1

		print "Wrong\n"
		print "You have", + turns, 'more guesses'

		if turns == 0:
			os.system("clear")
			print "-----------------------------------------"
			print "Wrong guesses (", + (turns - numberOfWrongsAllowed), "): " , 
			for i in range(0, len(wrongGuesses)):
				sys.stdout.write(wrongGuesses[i]),
				if not (i == len(wrongGuesses)-1):
					sys.stdout.write(", ")

			print "\n"

			print "YOU LOST\n" 
			print '**********'
			print '*        *'
			print '*        * * *'
			print '*        **   *'
			print '*        ***** '
			print '*         * * * '
			print '*        *  *  * '
			print '*           * '
			print '*           * '
			print '*          * *'
			print '*         *   *'
			for x in range(1,5):
				print '*'

	