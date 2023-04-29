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


class CaesarCipher:
    def __init__(self):
        self.letter_to_pos = {letter: i for i, letter in enumerate(ascii_lowercase)}
        self.pos_to_letter = {i: letter for i, letter in enumerate(ascii_lowercase)}
        self.modulo = 26

    def validate_action(self):
        action = input("Do you want to (e)ncrypt or (d)ecrypt?: ")
        if action == "e":
            return 1
        elif action == "d":
            return -1
        else:
            return self.validate_action()

    def validate_key(self):
        key = input("Please enter the key (0 to 25) to use: ")
        try:
            return int(key)
        except ValueError:
            return self.validate_key()

    def validate_restart(self):
        restart = input("Do you want to restart program (y/n): ")
        if restart == "y":
            return True
        elif restart == "n":
            return False
        else:
            return self.validate_restart()

    def interface(self):
        mul = 1
        mul *= self.validate_action()
        key = self.validate_key()
        action = "encrypt" if mul == 1 else "decrypt"
        message = input(f"Enter the message to {action}: ")
        print(self.encrypt_decrypt(message, key * mul))
        if self.validate_restart():
            return self.interface()

    def encrypt_decrypt(self, message, key):
        return "".join([self.shift(letter, key) for letter in message.lower()]).upper()

    def shift(self, letter, key):
        if letter not in self.letter_to_pos:
            return letter
        return self.pos_to_letter[(self.letter_to_pos[letter] + key) % self.modulo]


def main():
    cc = CaesarCipher()
    cc.interface()


if __name__ == "__main__":
    main()
