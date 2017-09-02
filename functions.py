# challenge 1.1
def hex_to_b64(h):
    return h.decode("hex").encode("base64").strip()  # has a trailing newline


# challenge 1.2
def fixed_xor(a, b):
    return hex(int(a, 16) ^ int(b, 16))[2:-1]  # has extra characters


if __name__ == 'main':
    pass
