"""
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make
up the word.
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters
before the game is over.
"""

from random import randint
import tkinter as tk
from tkinter import messagebox
from functools import partial

import cfg


class Hangman:
    def __init__(self):
        self.idx = randint(0, len(cfg.words) - 1)
        self.attempts = 7
        self.letter_used = set()
        self.correct_guessed_letters = set()
        self.letter_order = []
        self.end = False

    def restart(self):
        self.idx = randint(0, len(cfg.words) - 1)
        self.attempts = 7
        self.letter_used = set()
        self.correct_guessed_letters = set()
        self.letter_order = []
        self.end = False

    def check_letter(self, letter, gui):
        self.letter_used.add(letter)
        self.letter_order.append(letter)
        if letter in cfg.letters_in_words[self.idx]:
            self.correct_guessed_letters.add(letter)
            for i in cfg.letters_in_words[self.idx][letter]:
                gui.cfg["letter_labels_text"][i].set(cfg.words[self.idx][i])
        else:
            self.attempts -= 1
            gui.cfg["attempts"].set(f"You have {self.attempts - 1} tries left.")

        gui.cfg["button_labels"][ord(letter) - 97]["state"] = "disabled"

        if self.attempts == 0 or len(self.correct_guessed_letters) == len(cfg.letters_in_words[self.idx]):
            self.end = True

    def end_game(self, gui):  # sourcery skip: use-named-expression
        if not self.end:
            return
        self.end = False
        gui.cfg["attempts"].set("")
        for i in range(len(gui.cfg["letter_labels_text"])):
            gui.cfg["letter_labels_text"][i].set(cfg.words[self.idx][i])
        gui.root.update()
        text = "You lose!" if self.attempts == 0 else "You win!"
        answer = messagebox.askyesno(text,
                                     f"Game over\n\
                                     {text}\n\
                                     Guessed word was - '{cfg.words[self.idx]}'\n\
                                     Do you want to restart the game?")
        if answer:
            self.restart()
            gui.restart(self)
        else:
            gui.root.destroy()
            return True


class GUI:
    def __init__(self, hm):
        self.root = tk.Tk()
        self.root.configure(bg='white')
        self.root.title('Hangman')
        self.root.geometry("800x600")
        self.cfg = {"letter_labels_text": [tk.StringVar() for _ in range(len(cfg.words[hm.idx]))],
                    "button_labels": [],
                    "attempts": tk.StringVar(value=f"You have {hm.attempts - 1} tries left.")}

    def restart(self, hm):
        for i in range(len(self.cfg["letter_labels_text"])):
            self.cfg["letter_labels_text"][i].set("")
        for i in range(len(self.cfg["button_labels"])):
            self.cfg["button_labels"][i]["state"] = "normal"
        self.cfg["attempts"].set(f"You have {hm.attempts - 1} tries left.")

    def draw_interface(self, hm):
        # sourcery skip: convert-to-enumerate, use-itertools-product
        letter_frame = tk.Frame(self.root, width=100, height=100, bg='white')
        for i in range(len(cfg.words[hm.idx])):
            letter_label = tk.Label(letter_frame,
                                    textvariable=self.cfg["letter_labels_text"][i],
                                    font=("Arial", 100),
                                    bg="white",
                                    fg="black",
                                    relief="solid",
                                    bd=3,
                                    width=2)
            letter_label.pack(side="left", pady=10, padx=10)
        letter_frame.pack(side='top')

        buttons_frame = tk.Frame(self.root, width=100, height=100, bg='white')
        num = 97
        for i in range(2):
            for j in range(13):
                button = tk.Button(buttons_frame,
                                   text=chr(num),
                                   height=2,
                                   width=2,
                                   command=partial(hm.check_letter,
                                                   chr(num),
                                                   self))
                button.grid(row=i, column=j)
                self.cfg["button_labels"].append(button)
                num += 1
        buttons_frame.pack(side='bottom')

        attempts_label = tk.Label(self.root,
                                  textvariable=self.cfg["attempts"],
                                  font=("Arial", 20),
                                  bg="white",
                                  fg="black")
        attempts_label.pack()


def main():
    hm = Hangman()
    gui = GUI(hm)
    gui.draw_interface(hm)
    while True:
        gui.root.update()
        if hm.end_game(gui):
            break


if __name__ == "__main__":
    main()
