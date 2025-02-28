from solutions.p059 import load_cipher, sum_decrypted_ascii_values


def test_sum_decrypted_ascii_values() -> None:
    cipher = load_cipher()
    assert sum_decrypted_ascii_values(cipher) == 129448
