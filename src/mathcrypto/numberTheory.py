import math
from typing import Tuple, Optional, Dict

class NumberTheory:

    @staticmethod
    def egcd(a: int, b: int) -> Tuple[int, int, int]:
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = NumberTheory.egcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    @staticmethod
    def mod_inverse(a: int, m: int) -> int:
        gcd, x, _ = NumberTheory.egcd(a, m)
        if gcd != 1:
            raise ValueError(f"No inverse exists for {a} mod {m} (gcd = {gcd} != 1).")
        return x % m

    @staticmethod
    def totient(n: int) -> int:
        result = n
        p = 2
        temp_n = n
        while p * p <= temp_n:
            if temp_n % p == 0:
                while temp_n % p == 0:
                    temp_n //= p
                result -= result // p
            p += 1
        if temp_n > 1:
            result -= result // temp_n
        return result

    @staticmethod
    def order(a: int, n: int) -> int:
        if math.gcd(a, n) != 1:
            raise ValueError(f"{a} and {n} are not relatively prime.")
        
        phi = NumberTheory.totient(n)
        divisors = []
        for i in range(1, int(math.isqrt(phi)) + 1):
            if phi % i == 0:
                divisors.append(i)
                if i * i != phi:
                    divisors.append(phi // i)
        divisors.sort()

        for d in divisors:
            if pow(a, d, n) == 1:
                return d
        return phi

    @staticmethod
    def is_primitive_root(g: int, p: int) -> bool:
        return NumberTheory.order(g, p) == p - 1

    @staticmethod
    def discrete_log_bsgs(g: int, h: int, p: int) -> Optional[int]:
        m = math.isqrt(p - 1) + 1
        table: Dict[int, int] = {}
        cur = 1
        for j in range(m):
            table[cur] = j
            cur = (cur * g) % p
            
        g_m_inv = pow(NumberTheory.mod_inverse(g, p), m, p)
        cur = h
        for i in range(m):
            if cur in table:
                return i * m + table[cur]
            cur = (cur * g_m_inv) % p
            
        return None