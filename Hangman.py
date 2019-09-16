import random

def main():
    welcome = ["Welcome to Hangman! A word will be chosen at random and"
               "You must try to guess the word correctly letter by letter"
               "before you run out of attempts. Good Luck!"
               ]

    for line in welcome:
        print(line, sep='\n')

    # Setting up the play again loop

    play_again = True

    while play_again:

        words = ["hangman", "chairs", "backpack", "bodywash", "clothing",
                 "computer", "python", "program", "glasses", "sweatshirt",
                 "sweatpants", "mattress", "friends", "clocks", "biology",
                 "algebra", "suitcase", "knives", "ninjas", "shampoo"
                 ]

        chosen_word = random.choice(words).lower()
        player_guess = None # Will hold the player guess
        guessed_letters = [] # a list of letters guessed so far
        word_guessed = []
        for letter in chosen_word:
            word_guessed.append("-") # create an unguessed, blank version of he word
        joined_word = None # joins the words in the list word_guessed

        HANGMAN = (

""""
-----
|    |
|
|
|
|
|
|
|
--------
""",
"""
------
|     |
|     0
|
|
|
|
|
|
--------
""",
"""
------
|     |
|     0
|    -+-
|
|
|
|
|
--------
""",
"""
-------
|      |
|      0
|    /-+-\
|
|
|
|
|
--------
""",
"""
-------
|      |
|      0
|    /-+-\
|
|
|
|
|
--------
""",
"""
-------
|      |
|      0
|    /-+-\
|      |
|
|
|
|
--------
""",
"""
-------
|      |
|      0
|    /-+-\
|      |
|     |
|
|
|
--------
""",
"""
-------
|      |
|      0
|    /-+-\
|      |
|     |
|     |
|
|
--------
""",
"""
-------
|      |
|      0
|    /-+-\
|      |
|     | |
|     |
|
|
--------
""",
"""
-------
|      |
|      0
|    /-+-\
|      |
|     | |
|     | |
|
|
--------
""")

        print(HANGMAN[0])
        attempts = len(HANGMAN) - 1

        while (attempts != 0 and "-" in word_guessed):
            print(("\nYou have {} attempts remaining").format(attempts))
            joined_word = "".join(word_guessed)
            print(joined_word)

            try:
                player_guess = str(input("\nPlease select a letter between A-Z" + "\n> ")).lower()
            except: # check valid input
                print("That is not valid input. Please try again.")
                continue
            else:
                if not player_guess.isalpha(): #check the input is a letter
                    print("That is not a letter. Please try again.")
                    continue
                elif len(player_guess) > 1: #Check the input is only one letter
                    print("That is more than one letter. Please try again")
                    continue
                elif player_guess in guessed_letters: #check the letter has not been guessed
                    print("You already guessed that letter, please try again.")
                else:
                    pass

        guessed_letters.append(player_guess)

        for idx, letter in enumerate(len(chosen_word)):
            if player_guess == letter:
                word_guessed[idx] = player_guess # replace all letters in the chosen word that match the players guess

        if player_guess not in chosen_word:
            attempts -= 1
            print(HANGMAN[(len(HANGMAN) - 1) - attempts]) #player guessed word not match with chosen word, goes to next stage of Hangman
    if "-" not in word_guessed: #no blanks remaining
        print(("\nCongratulations! {} was the word ").format(chosen_word))
    else: # loop must have ended because attempts reached 0
        print(("\nUnlucky! The word was {}. ").format(chosen_word))

    print("\nWould you like to play again?")

    response = input("> ").lower()
    if response not in ("yes", "y"):
        play_again = False


