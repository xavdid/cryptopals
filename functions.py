import string
import urllib2
from collections import namedtuple

from numpy import array as narray, exp
from numpy.linalg import norm

Result = namedtuple('Result', 'message score')
SINGLE_BITS = map(chr, range(256))
# from https://en.wikipedia.org/wiki/Letter_frequency
LETTER_FREQUENCIES = narray([.08167, .01492, .02782, .04253, .02702, .02228, .02015, .06094, .06966, .00153, .00772, .04025, .02406, .06749, .07507, .01929, .00095, .05987, .06327, .09056, .02758, .00978, .02360, .00150, .01974, .0007])


# challenge 1.1
def hex_to_b64(s):
    return s.decode("hex").encode("base64").strip()  # has a trailing newline

def xor(a, b):
    return chr(ord(a) ^ ord(b))

# challenge 1.2
def fixed_xor(a, b):
    return ''.join([xor(i, j) for i, j in zip(a, b)])


def score_english(s):
    s = s.lower()  # compare everything case insensitive
    test_values = narray(relative_frequency(s))
    score = norm(LETTER_FREQUENCIES - test_values)
    num_non_english = [x not in string.printable for x in s].count(True)
    return score * exp(num_non_english / float(len(s)))


def relative_frequency(s):
    message_length = float(len(s))
    result = []
    for letter in string.letters[:26]:
        result.append(s.count(letter) / message_length)

    return result


# challenge 1.3
def decode_cipher(s):
    """
    returns tuple of (message, score)
    """
    message = s.strip().decode('hex')
    res = []

    for bit in SINGLE_BITS:
        decoded_message = fixed_xor(message, bit * len(message))
        res.append(Result(decoded_message, score_english(decoded_message)))

    return best_result(res)


# challenge 1.4
def get_strings_from_web(url):
    return [line for line in urllib2.urlopen(url)]


def decode_multi_xor(ciphertexts):
    return best_result([decode_cipher(s) for s in ciphertexts])

def best_result(arr):
    # lower score is better
    return sorted(arr, key=lambda x: x.score)[0]

# challenge 1.5
def encrypt_multi_xor(plaintext, key):
    res = []
    c = 0

    for bit in plaintext:
        res.append(xor(bit, key[c % len(key)]))
        c += 1

    return ''.join(res)

if __name__ == 'main':
    pass
