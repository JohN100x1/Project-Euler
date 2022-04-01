from config import path_res


def load_cipher() -> list[int]:
    """Load a list of integers from /res/p059_cipher.txt."""
    with open(path_res / "p059_cipher.txt") as f:
        return [int(c) for c in f.read().split(",")]


def decrypt_cipher(cipher: list[int], key: str) -> str:
    """Get the decrypted message from cipher using key."""
    message = [chr(c ^ ord(key[i % len(key)])) for i, c in enumerate(cipher)]
    return "".join(message)


def sum_decrypted_ascii_values(cipher: list[int]) -> int:
    """Get the sum of the ASCII values of the decryption key."""
    for x in range(97, 123):
        for y in range(97, 123):
            for z in range(97, 123):
                key = chr(x) + chr(y) + chr(z)
                message = decrypt_cipher(cipher, key)
                if " the " in message:
                    return sum(ord(m) for m in message)
