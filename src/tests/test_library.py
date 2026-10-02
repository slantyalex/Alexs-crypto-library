from mathcrypto import NumberTheory, AffineCipher, DiffieHellman, RSACipher

def test_number_theory():
    assert NumberTheory.order(3, 13) == 3
    assert NumberTheory.is_primitive_root(13, 19) is True
    assert NumberTheory.discrete_log_bsgs(13, 6, 19) == 10

def test_affine_cipher():
    cipher = AffineCipher.break_known_plaintext('a', 'i', 'b', 'n')
    assert cipher.k1 == 5
    assert cipher.k2 == 8
    assert cipher.encrypt("ab") == "in"

def test_diffie_hellman():
    alice = DiffieHellman(p=23, g=5, private_key=6)
    bob = DiffieHellman(p=23, g=5, private_key=15)
    assert alice.compute_shared_secret(bob.public_key) == bob.compute_shared_secret(alice.public_key)

def test_rsa():
    rsa = RSACipher(p=61, q=53, e=17)
    msg = 42
    assert rsa.decrypt(rsa.encrypt(msg)) == msg