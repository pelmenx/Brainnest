'''
This program can hack messages encrypted
with the Caesar cipher from the previous project, even
if you don’t know the key. There are only 26
possible keys for the Caesar cipher, so a computer can easily try all possible decryptions and display the results to the user. In cryptography, we call
this technique a brute-force attack.
'''


import _tkinter
from string import ascii_lowercase
import tkinter as tk


class CaesarCipher:
    def __init__(self):
        self.letter_to_pos = {letter: i for i, letter in enumerate(ascii_lowercase)}
        self.pos_to_letter = {i: letter for i, letter in enumerate(ascii_lowercase)}
        self.modulo = 26

    def encrypt_decrypt(self, message, key):
        return "".join([self.shift(letter, key) for letter in message.lower()]).upper()

    def shift(self, letter, key):
        if letter not in self.letter_to_pos:
            return letter
        return self.pos_to_letter[(self.letter_to_pos[letter] + key) % self.modulo]


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg='white')
        self.root.title('Caesar Cipher')
        self.root.geometry("1300x900")
        self.outputs = []
        self.input = None

    def brute_force(self, cc):
        s = self.input.get("1.0", "end-1c")
        for x, item in enumerate(self.outputs):
            item.configure(state="normal")
            item.delete('1.0', "end")
            out = cc.encrypt_decrypt(s, -x)
            item.insert("end", out)
            item.configure(state="disabled")

    def draw_interface(self):  # sourcery skip: use-itertools-product
        input_grid = tk.Frame(self.root, bg='white', pady=5)
        input_name = tk.Label(input_grid, text="Input", bg="white", fg="black")
        self.input = tk.Text(input_grid,width=140, height=3, bg="white", fg="black")
        input_name.grid(row=0, column=0)
        self.input.grid(row=0, column=1)
        output_grid = tk.Frame(self.root, bg='white', pady=5)
        for i in range(2):
            for j in range(13):
                output_name = tk.Label(output_grid, text=f"key {i * 13 + j}", bg="white", fg="black")
                output = tk.Text(output_grid,
                                 width=65,
                                 height=3,
                                 bg="white",
                                 fg="black",
                                 borderwidth=1)
                output.configure(state="disabled")
                self.outputs.append(output)
                output_name.grid(row=j, column=i * 2)
                output.grid(row=j, column=i * 2 + 1)

        input_grid.pack()
        output_grid.pack()


def main():
    cc = CaesarCipher()
    gui = GUI()
    gui.draw_interface()
    while True:
        try:
            gui.root.update()
            gui.brute_force(cc)
        except _tkinter.TclError:
            return


if __name__ == "__main__":
    main()
