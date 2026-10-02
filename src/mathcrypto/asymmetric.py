import math
from .numberTheory import NumberTheory

class DiffieHellman:
    def __init__(self, p: int, g: int, private_key: int):
        if not NumberTheory.is_primitive_root(g, p):
            raise ValueError(f"{g} is not a primitive root mod {p}.")
        self.p = p
        self.g = g
        self.__private_key = private_key
        self.public_key = pow(g, private_key, p)

    def compute_shared_secret(self, peer_public_key: int) -> int:
        return pow(peer_public_key, self.__private_key, self.p)


class RSACipher:
    def __init__(self, p: int, q: int, e: int = 65537):
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        self.e = e
        if math.gcd(e, self.phi) != 1:
            raise ValueError(f"e={e} and phi={self.phi} are not relatively prime.")
        self.d = NumberTheory.mod_inverse(e, self.phi)

    def encrypt(self, m: int) -> int:
        if m >= self.n:
            raise ValueError("Message integer must be less than modulus n.")
        return pow(m, self.e, self.n)

    def decrypt(self, c: int) -> int:
        return pow(c, self.d, self.n)