import random

def display_hangman(attempts):
    hangman_graphics = [
        '''
         ------
         |    |
              |
              |
              |
              |
              |
        =========
        ''',
        '''
         ------
         |    |
         O    |
              |
              |
              |
              |
        =========
        ''',
        '''
         ------
         |    |
         O    |
         |    |
              |
              |
              |
        =========
        ''',
        '''
         ------
         |    |
         O    |
        /|    |
              |
              |
              |
        =========
        ''',
        '''
         ------
         |    |
         O    |
        /|\\   |
              |
              |
              |
        =========
        ''',
        '''
         ------
         |    |
         O    |
        /|\\   |
        /     |
              |
              |
        =========
        ''',
        '''
         ------
         |    |
         O    |
        /|\\   |
        / \\   |
              |
              |
        =========
        '''
    ]
    print(hangman_graphics[attempts])

def play_hangman():
    word_list = [ 
        'kenya',
        'america',
        'china', 
        'india', 
        'ethiopia',
        'pakistan',
        'tanzania',
        'congo',
        'somalia'
    ]
    
    word_ = random.choice(word_list)
    guessed_words = []
    high_attempts = 7
    attempted = 0
    done = False

    while not done:
        print("\n" + " ".join([letter if letter in guessed_words else "_" for letter in word_]))
        
        # Display hangman graphic
        display_hangman(attempted)

        guess = input("Guess a letter: ").lower()
        if guess in guessed_words:
            print("You already guessed that letter.")
        elif guess in word_:
            print("That's correct!")
            guessed_words.append(guess)
        else:
            print("Nah, my guy!")
            attempted += 1
            guessed_words.append(guess)

        if attempted >= high_attempts:
            done = True
            display_hangman(attempted)  # Show final hangman graphic
            print(f"Sorry, you've used all your attempts. The word was: {word_}")
        elif set(word_) == set(guessed_words):
            done = True
            print("Be proud! You are good at this. You've guessed the word:", word_)

play_hangman()
