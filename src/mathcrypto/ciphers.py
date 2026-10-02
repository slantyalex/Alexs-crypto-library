import math
from .numberTheory import NumberTheory

class CaesarCipher:
    def __init__(self, shift: int):
        self.shift = shift % 26

    def encrypt(self, text: str) -> str:
        res = []
        for char in text:
            if char.isalpha():
                base = ord('a') if char.islower() else ord('A')
                res.append(chr((ord(char) - base + self.shift) % 26 + base))
            else:
                res.append(char)
        return "".join(res)

    def decrypt(self, text: str) -> str:
        return CaesarCipher(-self.shift).encrypt(text)


class AlbamCipher(CaesarCipher):
    def __init__(self):
        super().__init__(13)


class AffineCipher:
    def __init__(self, k1: int, k2: int, alphabet_size: int = 26):
        if math.gcd(k1, alphabet_size) != 1:
            raise ValueError(f"Invalid k1={k1}: gcd({k1}, {alphabet_size}) must be 1.")
        self.k1 = k1
        self.k2 = k2 % alphabet_size
        self.n = alphabet_size
        self.k1_inv = NumberTheory.mod_inverse(k1, alphabet_size)

    def encrypt(self, text: str) -> str:
        res = []
        for char in text:
            if char.isalpha():
                base = ord('a') if char.islower() else ord('A')
                x = ord(char) - base
                enc_x = (self.k1 * x + self.k2) % self.n
                res.append(chr(enc_x + base))
            else:
                res.append(char)
        return "".join(res)

    def decrypt(self, text: str) -> str:
        res = []
        for char in text:
            if char.isalpha():
                base = ord('a') if char.islower() else ord('A')
                y = ord(char) - base
                dec_x = (self.k1_inv * (y - self.k2)) % self.n
                res.append(chr(dec_x + base))
            else:
                res.append(char)
        return "".join(res)

    @classmethod
    def break_known_plaintext(cls, p1: str, c1: str, p2: str, c2: str, alphabet_size: int = 26):
        x1, y1 = ord(p1.lower()) - ord('a'), ord(c1.lower()) - ord('a')
        x2, y2 = ord(p2.lower()) - ord('a'), ord(c2.lower()) - ord('a')

        dx = (x2 - x1) % alphabet_size
        dy = (y2 - y1) % alphabet_size

        dx_inv = NumberTheory.mod_inverse(dx, alphabet_size)
        k1 = (dy * dx_inv) % alphabet_size
        k2 = (y1 - k1 * x1) % alphabet_size

        return cls(k1, k2, alphabet_size)