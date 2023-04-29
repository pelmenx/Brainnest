'''
This program can hack messages encrypted 
with the Caesar cipher from the previous project, even 
if you don’t know the key. There are only 26 
possible keys for the Caesar cipher, so a computer can easily try all possible decryptions and display the results to the user. In cryptography, we call 
this technique a brute-force attack.
'''

from string import ascii_lowercase


class CaesarCipher:
    def __init__(self):
        self.letter_to_pos = {letter: i for i, letter in enumerate(ascii_lowercase)}
        self.pos_to_letter = {i: letter for i, letter in enumerate(ascii_lowercase)}
        self.modulo = 26

    def brute_force(self, message):
        for i in range(self.modulo):
            print(i, self.encrypt_decrypt(message, -i))

    def encrypt_decrypt(self, message, key):
        return "".join([self.shift(letter, key) for letter in message.lower()]).upper()

    def shift(self, letter, key):
        if letter not in self.letter_to_pos:
            return letter
        return self.pos_to_letter[(self.letter_to_pos[letter] + key) % self.modulo]


def main():
    cc = CaesarCipher()
    cc.brute_force("QIIX QI FC XLI VSWI FYWLIW XSRMKLX")


if __name__ == "__main__":
    main()