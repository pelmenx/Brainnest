'''
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It
encrypts letters by shifting them over by a
certain number of places in the alphabet. We
call the length of shift the key. For example, if the
key is 3, then A becomes D, B becomes E, C becomes
F, and so on. To decrypt the message, you must shift
the encrypted letters in the opposite direction. This
program lets the user encrypt and decrypt messages
according to this algorithm.

When you run the code, the output will look like this:

Do you want to (e)ncrypt or (d)ecrypt?
> e
Please enter the key (0 to 25) to use.
> 4
Enter the message to encrypt.
> Meet me by the rose bushes tonight.
QIIX QI FC XLI VSWI FYWLIW XSRMKLX.


Do you want to (e)ncrypt or (d)ecrypt?
> d
Please enter the key (0 to 26) to use.
> 4
Enter the message to decrypt.
> QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
MEET ME BY THE ROSE BUSHES TONIGHT.
'''
from string import ascii_lowercase
import tkinter as tk


class CaesarCipher:
    def __init__(self):
        self.letter_to_pos = {letter: i for i, letter in enumerate(ascii_lowercase)}
        self.pos_to_letter = {i: letter for i, letter in enumerate(ascii_lowercase)}
        self.modulo = 26

    @staticmethod
    def validate_key(key):
        try:
            return int(key)
        except ValueError:
            return

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
        self.root.geometry("700x450")

    def draw_interface(self, cc):
        def take_input(mul):
            output_text.delete('1.0', "end")
            s = input_text.get("1.0", "end-1c")
            k = cc.validate_key(key_text.get("1.0", "end-1c"))
            if not k:
                return
            out = cc.encrypt_decrypt(s, k * mul)
            output_text.insert("end", out)

        input_grid = tk.Frame(self.root, width=100, height=100, bg='white', pady=5)
        input_name = tk.Label(input_grid, text="Input", bg="white", fg="black")
        input_text = tk.Text(input_grid, height=10, bg="white", fg="black")
        input_name.grid(row=0, column=0)
        input_text.grid(row=0, column=1)

        key_grid = tk.Frame(self.root, width=100, height=100, bg='white', pady=5)
        key_name = tk.Label(key_grid, text="Key", bg="white", fg="black")
        key_text = tk.Text(key_grid, width=3, height=1, bg="white", fg="black",font=("Arial", 40),)
        key_name.grid(row=0, column=0)
        key_text.grid(row=0, column=1)

        action_grid = tk.Frame(self.root, width=100, height=100, bg='white', pady=5)
        encrypt = tk.Button(action_grid, height=2,
                            width=20,
                            text="Encrypt",
                            command=lambda: take_input(1))
        decrypt = tk.Button(action_grid, height=2,
                            width=20,
                            text="Decrypt",
                            command=lambda: take_input(-1))
        encrypt.grid(row=0, column=0)
        decrypt.grid(row=0, column=1)

        output_grid = tk.Frame(self.root, width=100, height=100, bg='white', pady=5)
        output_name = tk.Label(output_grid, text="Output", bg="white", fg="black")
        output_text = tk.Text(output_grid, height=10, bg="white", fg="black")
        output_name.grid(row=0, column=0)
        output_text.grid(row=0, column=1)

        input_grid.pack()
        key_grid.pack()
        action_grid.pack()
        output_grid.pack()


def main():
    cc = CaesarCipher()
    gui = GUI()
    gui.draw_interface(cc)
    gui.root.mainloop()


if __name__ == "__main__":
    main()
