with open("../../res/p059_cipher.txt") as f:
    CIPHER = [int(c) for c in f.read().split(",")]


def decrypt_cipher(key):
    message = []
    for i, c in enumerate(CIPHER):
        k = ord(key[i % len(key)])
        message.append(chr(c ^ k))
    return "".join(message)


def find_key_and_ascii_vsum():
    for x in range(97, 123):
        for y in range(97, 123):
            for z in range(97, 123):
                key = chr(x) + chr(y) + chr(z)
                message = decrypt_cipher(key)
                if " is " in message and " the " in message:
                    input(key + " : " + message)
                    return sum(ord(m) for m in message)
    return None


print(find_key_and_ascii_vsum())
