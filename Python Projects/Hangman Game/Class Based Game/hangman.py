import random

class Hangman:
    def __init__(self):
        self.word = self.choose_words()
        self.word_letter = set(self.word)
        self.guessed_letter = set()
        self.treis = 6
        self.stages = [
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

    def choose_words(self):
        with open('word.txt') as file:
            words = file.read().splitlines()
        return random.choice(words).lower()

    def display_hangman(self):
        return self.stages[self.treis]

    def get_guess(self):
        while True:
            guess = input("Guess the Letter: ").lower()
            if len(guess) == 1 and guess.isalpha():
                if guess in self.guessed_letter:
                    print('You have already guessed that letter. Try again: ')
                else:
                    return guess
            else:
                print('Ivalid Input. Please enter a single letter.')

    def play(self):
        print("Welcom to Hangman")

        while self.treis > 0 and len(self.word_letter) > 0:
            print(self.display_hangman())
            print(f"You have {self.treis} tries left.")
            print("Guess letter:", ' '.join(sorted(self.guessed_letter)))
            print("Current Word:", ' '.join([letter if letter in self.guessed_letter else '_' for letter in self.word]))

            guess = self.get_guess()

            if guess in self.word_letter:
                self.guessed_letter.add(guess)
                self.word_letter.remove(guess)
                print(f"Good job! {guess} is not in the word.")
            else:
                self.guessed_letter.add(guess)
                self.treis -= 1
                print(f'Sorry, {guess} is not in the word.')

        if len(self.word_letter) == 0:
            print("Congratulation You Win the Word is", self.word)
        else:
            print(self.display_hangman())
            print("You ran out of Teris, the Word is", self.word)

if __name__ == "__main__":
    game = Hangman()
    game.play()

            
