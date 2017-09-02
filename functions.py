words = set(line.strip() for line in open('/usr/share/dict/words'))

# challenge 1.1
def hex_to_b64(s):
    return s.decode("hex").encode("base64").strip()  # has a trailing newline


# challenge 1.2
def fixed_xor(a, b):
    return hex(int(a, 16) ^ int(b, 16))[2:-1]  # has extra characters

def score_english(s):
    """
    takes a string of english text and returns a score for how likely it is to have english words on them (purely based on letter frequency)
    """
    score = 0
    message = s.lower()

    for word in words:
        if word in message:
            score += len(word)

    return score


# https://stackoverflow.com/a/40949538/1825390
def string2bits(s):
    return [bin(ord(x))[2:].zfill(8) for x in s]


def bits2string(b):
    return ''.join([chr(int(x, 2)) for x in b])


def xor_bytestr(a, b):
    return bin(int(a, 2) ^ int(b, 2))[2:]

# challenge 1.3
def decode_cipher(s):
    message_bits = string2bits(s.decode('hex'))
    res = {
        'max': 0,
        'message': None
    }

    for char in 'abcdefghijklmnopqrstuvwxyz':
        xor = string2bits(char)[0]
        message = bits2string([xor_bytestr(b, xor) for b in message_bits])
        # print message
        score = score_english(message)
        if score > res['max']:
            res['max'] = score
            res['message'] = message

    # print 'messsage is probably {} (with score of {})'.format(res['message'], res['max'])
    return res['message']


if __name__ == 'main':
    pass
