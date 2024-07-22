from itertools import product

from requests import get

from utils.exceptions import SolutionNotFoundError


def load_cipher() -> list[int]:
    """Load a list of integers from p059_cipher.txt."""
    url = "https://projecteuler.net/project/resources/p059_cipher.txt"
    content = get(url).content.decode("utf-8")
    return [int(num) for num in content.split(",")]


def decrypt_cipher(cipher: list[int], key: str) -> str:
    """Get the decrypted message from cipher using key."""
    message = [chr(c ^ ord(key[i % len(key)])) for i, c in enumerate(cipher)]
    return "".join(message)


def sum_decrypted_ascii_values(cipher: list[int]) -> int:
    """Get the sum of the ASCII values of the decryption key."""
    for key_tuple in product([chr(i) for i in range(97, 123)], repeat=3):
        key = "".join(key_tuple)
        message = decrypt_cipher(cipher, key)
        if " the " in message:
            return sum(ord(m) for m in message)
    raise SolutionNotFoundError("Cannot decrypt message.")
