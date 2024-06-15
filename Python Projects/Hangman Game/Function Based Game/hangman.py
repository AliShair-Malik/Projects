import random

def choose_words():
    Fruits = ['watermelon', 'grapes', 'melon', 'apple', 'banana']
    Languages = ['python', 'c++', 'c#', 'javascript', 'java']
    Games = ['pubg', 'minecarft', 'free fire', 'among us']

    Items_list = [Fruits, Languages, Games]

    words = random.choice(Items_list)

    return random.choice(words)

def display_hangman(teris):
    stages = [
       """
         ------
         |    |
         |    O
         |   \|/
         |    |
         |   / \\
         -
        """,
       """
         ------
         |    |
         |    O
         |   \|/
         |    |
         |   / 
         -
        """,
       """
         ------
         |    |
         |    O
         |   \|/
         |    |
         |  
         -
        """,
       """
         ------
         |    |
         |    O
         |   \|
         |    |
         |
         -
        """,
        """
         ------
         |    |
         |    O
         |    |
         |    |
         |
         -
        """,
        """
         ------
         |    |
         |    O
         |
         |
         |
         -
        """,
        """
         ------
         |    |
         |   
         |
         |
         |
         -
        """
    ]

    return stages[teris]

def play_hangman():
    word = choose_words()
    word_letters = set(word)
    guessed_letters = set()
    teris = 6

    print("Welcome to Hangman Game\n")

    while teris > 0 and len(word_letters) > 0:
        print(display_hangman(teris))
        print(f"You have only {teris} teris")
        print("Guess Letters:", ' '.join(sorted(guessed_letters)))

        letters = [letter if letter in guessed_letters else '_' for letter in word]
        print('Current Word:', ' '.join(letters))

        guess = input("Guess the Letter: ").lower()

        if guess in guessed_letters:
            print(f"You already guessed {guess} ! Try Again")
        elif guess in word_letters:
            guessed_letters.add(guess)
            word_letters.remove(guess)
            print(f"Good Job {guess} added in Word")
        else:
            guessed_letters.add(guess)
            teris -= 1
            print(f"Sorry, {guess} not in the Word")

    if len(word_letters) == 0:
        print("Congratulation You Win the Word is", word)
    else:
        print(display_hangman(teris))
        print("You ran out of Teris, the Word is", word)

play_hangman()