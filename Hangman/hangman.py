import string
from words import choose_word
from images import IMAGES
def is_word_guessed(secret_word,letters_guessed):
   
    # secret_word: string, the secret word to guess.

    # Hangman game yeh start karta hai:

    # * Game ki shuruaat mei hi, user ko bata dete hai ki
    #   secret_word mei kitne letters hai

    # * Har round mei user se ek letter guess karne ko bolte hai

    # * Har guess ke baad user ko feedback dete hai ki woh guess uss
    #   word mei hai ya nahi

    # * Har round ke baar, user ko uska guess kiya hua partial word
    #   display karta hai, aur underscore use kar kar woh letters bhi dikha deta hai
    #   jo user ne abhi tak guess nahi kiye hai

    # '''

    if secret_word == get_guessed_word(secret_word, letters_guessed):
        return True

    return False
    
    if secret_word == get_guessed_word(secret_word, letters_guessed):
        return True

    return False


def ifValid(user_input):
    if len(user_input) != 1:
        return False

    if not user_input.isalpha():
        return False

    # True humne tab hi return kiya hai jab
    # user_input ki length 1 hai aur woh character hai
    return True




def get_hint(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess karna hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: ek character jo abhi tak guess nahi hua hai
    '''

    import random
    letters_not_guessed = []
    
    index = 0
    while (index < len(secret_word)):
        letter = secret_word[index]
        if letter not in letters_guessed:
            if letter not in letters_not_guessed:
                letters_not_guessed.append(letter)

        index += 1

    return random.choice(letters_not_guessed)


def get_guessed_word(secret_word,letters_guessed):

	index=0
	guessed_word=""
	while (index<len(secret_word)):
		if secret_word[index] in letters_guessed:
			guessed_word+=secret_word[index]
		else:
			guessed_word+="_"
		index+=1
	return guessed_word

def get_available_letters(letters_guessed):

	import string
	letters_left=string.ascii_lowercase
	return letters_left

def hangman(secret_word):

    print ("                 ::  Welcome to the game, Hangman! ::     ")
    print()
   
    print ()


    user_difficulty_choice = input("""At what label you wants to play this game?
    	\na)\tEasy\nb)\tMedium\nc)\tHard\n\nChoose options from a, b, and c: \n \n""")
    print()
    print("You choosed option: ",user_difficulty_choice)
    print()
    print("Now, enjoy the Game:")
    print()
    print ("I am thinking of a word that is " + str(len(secret_word))  +" letters long.")
    print()

    total_lives = remaining_lives = 8
    # images_selection_list_indices mei hum woh images ke indices
    # store kar rahe hai, jo hume display karni hai, kyuki jab
    # total_lives 8 se kam hogi toh hum kuch hi images dikha sakte hai

    images_selection_list_indices = [0, 1, 2, 3, 4, 5, 6, 7]
    if user_difficulty_choice == "b":
    	total_lives = remaining_lives = 6
    	images_selection_list_indices = [0, 2, 3, 5, 6, 7]

    elif user_difficulty_choice == "c":
    	total_lives = remaining_lives = 4
    	images_selection_list_indices = [1, 3, 5, 7]

    else:
    	if user_difficulty_choice != "a":
    		print ("Sorry! your choice is invalid.\nGame is going to start with easy mode.")


    letters_guessed = []

    while (remaining_lives>0):
        available_letters = get_available_letters(letters_guessed)
        print ("Available letters: " + available_letters)
        print()

        guess = input("If you wants to take hint type (hint)\nOtherwise guess a letter: ")
        print()
        if guess == "hint":
            letter = get_hint(secret_word, letters_guessed)
        else:
        	letter = guess.lower()
        	if (not ifValid(letter)):
        		continue

        if letter in secret_word:
            letters_guessed.append(letter)
            print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
            print()

            if is_word_guessed(secret_word, letters_guessed) == True:
            	print (" * * Congratulations, you won! * * ")
            	print()
            	break

        else:
        	print()
        	print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
        	print()
        	print (IMAGES[images_selection_list_indices[total_lives-remaining_lives]])
        	print()
        	print()
        	print("Remaining_lives:"+str(remaining_lives))
        	print()
        	letters_guessed.append(letter)
        	print()
        	remaining_lives -= 1
        	print()
    
    else:
    	print ("Sorry, you ran out of guesses. The word was " + str(secret_word) + ".")
    	print()
    	print("Better luck next time!")
    	print()
secret_word=choose_word()
hangman(secret_word)




