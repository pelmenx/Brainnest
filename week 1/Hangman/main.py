"""
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make
up the word.
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters
before the game is over.
"""
from random import randint
import cfg
from string import ascii_lowercase


class Hangman:
    def __init__(self):
        self.idx = randint(0, len(cfg.words) - 1)
        self.attempts = 7
        self.letter_used = set()
        self.correct_guessed_letters = set()
        self.letter_order = []
        self.letters = set(ascii_lowercase)

    def game_initialization(self):
        self.idx = randint(0, len(cfg.words) - 1)
        self.attempts = 7
        self.letter_used = set()
        self.correct_guessed_letters = set()
        self.letter_order = []

    def play(self):
        self.game_initialization()
        while self.attempts > 0:
            self.print_interface()
            letter = self.letter_validation(input("Guess a letter: "))
            print()
            self.letter_used.add(letter)
            self.letter_order.append(letter)
            if letter not in cfg.letters_in_words[self.idx]:
                self.attempts -= 1
            else:
                self.correct_guessed_letters.add(letter)
            if len(self.correct_guessed_letters) == len(cfg.letters_in_words[self.idx]):
                print(f"You guessed the word {cfg.words[self.idx]}!")
                print()
                self.reset_game()
                return
        print(f"You lose!, guessed word was {cfg.words[self.idx]}!")
        self.reset_game()

    def reset_game(self):
        reset = input("Do you want to restart the game? (y/n) ")
        if reset == "y":
            return self.play()

    def print_interface(self):
        print(f"You have {self.attempts-1} tries left.")
        print("Used letters:", end=" ")
        for char in self.letter_order:
            print(char, end=" ")
        print()
        print("word:", end=" ")
        for char in cfg.words[self.idx]:
            if char in self.letter_used:
                print(char, end=" ")
            else:
                print("_", end=" ")
        print()

    def letter_validation(self, letter):
        if letter in self.letters and letter not in self.letter_used:
            return letter
        print()
        print("length of letter must be 1")
        print("letter cannot contain digits and special symbols")
        print("letter can contain only lower case symbols")
        print("letter may be is already used")
        print()
        new_letter = input("Guess a letter: ")
        return self.letter_validation(new_letter)


def main():

    hg = Hangman()
    hg.play()


if __name__ == "__main__":
    main()

# Output
'''
You have 6 tries left.                                                                                                                                           
Used letters:                                                                                                                                                    
Word: _ _ _ _                                                                                                                                                    
Guess a letter: a 

You have 6 tries left.                                                                                                                                           
Used letters: a                                                                                                                                                  
Word: _ a _ a                                                                                                                                                    
Guess a letter: j    

You have 6 tries left.                                                                                                                                           
Used letters: j a                                                                                                                                                
Word: j a _ a                                                                                                                                                    
Guess a letter: v                                                                                                                                                
You guessed the word java !
'''
